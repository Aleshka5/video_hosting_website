import os

from flask import Flask, jsonify, request
from flask_executor import Executor
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from sqlalchemy.orm import joinedload
import time
from datetime import datetime
import pickle
import operator

from image_to_text_processing import processing_video
from opencv_utils import get_duration_and_fps, create_preview
from scene_detector_processing import detect_scenes
from summorization_processing import summorization
from translation_processing import translate
from video_downloader import download_from_youtube
from text_to_audio_processing import Speaker

db = SQLAlchemy()
# create the app
app = Flask(__name__, static_folder='app', static_url_path="/app")
cors = CORS(app)
executor = Executor(app)
UPLOAD_FOLDER = './app/videos'
ALLOWED_EXTENSIONS = {'mp4'}
# configure the Postgres database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://bvideo:f67Uc98KG5jc3KENrLXD@91.185.84.99:5432/bvideo"
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# initialize the app with the extension
db.init_app(app)

# create the extension
from models import User, Video, Scene, Process, Subtitle

with app.app_context():
    db.create_all()

# login
@app.route('/api/login', methods=['POST'])
@cross_origin()
def login():
    data = request.json
    user = User.query.filter_by(telegram=data['login']).first()
    if user:
        if user.password == data['password']:
            return jsonify(user.as_dict())
        else:
            return 'wrong password', 500
    else:
        return 'user not found', 500

@app.route('/api/register', methods=['POST'])
@cross_origin()
def register():
    data = request.json
    user = User.query.filter_by(telegram=data['login']).first()
    if user:
        return 'user already exists', 500
    else:
        name = data['name']
        telegram = data['login']
        password = data['password']
        loyalty = 0
        user = User(name, telegram, password, loyalty)

        try:
            db.session.add(user)
            db.session.commit()
            return jsonify(user.as_dict())
        except Exception as e:
            db.session.rollback()
            return str(e), 400

# read all users api
@app.route('/api/users', methods=['GET'])
@cross_origin()
def read_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.as_dict())

    speaker = Speaker()
    subtitles = speaker.text2speech([{'frame': 0, 'text': 'Мужчина держит в руке нож'}, {'frame': 0, 'text': 'Женшина у стонка'}], True, file_name='./app/audio/output_' + str(0) + '_')

    return jsonify(result)

# read single user api
@app.route('/api/users/<int:user_id>', methods=['GET'])
@cross_origin()
def read_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        return jsonify(user.as_dict())
    else:
        return '', 404

# create user api
@app.route('/api/users', methods=['POST'])
@cross_origin()
def create_user():
    data = request.json
    name = data['name']
    telegram = data['telegram']
    password = data['password']
    loyalty = data['loyalty']
    user = User(name, telegram, password, loyalty)

    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(user.as_dict())
    except Exception as e:
        db.session.rollback()
        return str(e), 400

# update user api
@app.route('/api/users/<int:user_id>', methods=['PUT'])
@cross_origin()
def update_user(user_id):
    data = request.json
    user = User.query.filter_by(id=user_id).first()
    if user:
        user.name = data['name']
        user.telegram = data['telegram']
        user.password = data['password']
        user.loyalty = data['loyalty']

        try:
            db.session.commit()
            return jsonify(user.as_dict())
        except Exception as e:
            db.session.rollback()
            return str(e), 400
    else:
        return '', 404

@app.route('/api/videos', methods=['GET'])
@cross_origin()
def read_videos():
    videos = Video.query.all()
    result = []
    for video in videos:
        result.append(video.as_dict())
    return jsonify(result)

@app.route('/api/videos/<int:video_id>', methods=['GET'])
@cross_origin()
def read_video(video_id):
    video = Video.query.filter_by(id=video_id).first()
    if video:
        return jsonify(video.as_dict())
    else:
        return '', 404

@app.route('/api/simple/upload', methods=['POST'])
def upload_simple_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part', 400
    type = request.form['type']

    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return 'No selected file', 400

    # filename = secure_filename(file.filename)
    if type == 'video':
        ts = str(time.time())
        video_file_name = ts + '.mp4'
        video_file_path_app = './app/videos/' + video_file_name
        file.save(video_file_path_app)
        return jsonify(video_file_name)

    if type == 'image':
        ts = str(time.time())
        image_file_name = ts + '.jpg'
        image_file_path_app = './app/images/' + image_file_name
        file.save(image_file_path_app)
        return jsonify(image_file_name)

    if type == 'audio':
        audio_file_path_app = './app/audio/' + file.filename
        file.save(audio_file_path_app)
        return jsonify(file.filename)


@app.route('/api/videos/upload', methods=['POST'])
def upload_video():
    # check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part', 400
    name = request.form['name']
    description = request.form['description']
    category = request.form['category']

    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        # filename = secure_filename(file.filename)
        ts = str(time.time())
        video_file_name = ts + '.mp4'
        video_file_path_app = './app/videos/' + video_file_name
        file.save(video_file_path_app)
        duration, fps = get_duration_and_fps(video_file_path_app)
        img_name = ts + '.jpg'
        create_preview(img_name, video_file_path_app)
        video = Video(name, description, category, 'images/' + img_name, 'videos/' + video_file_name, duration, fps)
        # process = Process(1, video.id, datetime.now(), None, datetime.now(), False, None)
        try:
            db.session.add(video)
            # db.session.add(process)
            db.session.commit()
            return jsonify(video.as_dict())
        except Exception as e:
            db.session.rollback()
            return str(e), 400

@app.route('/api/videos/download', methods=['POST'])
@cross_origin()
def download_video():
    data = request.json
    url = data['url']
    name = data['name']
    description = data['description']
    category = data['category']
    ts = str(time.time())
    video_file_name = ts + '.mp4'
    video_file_path_app = './app/videos/' + video_file_name
    download_path = download_from_youtube(url, video_file_name)

    if download_path != None:
        duration, fps = get_duration_and_fps(video_file_path_app)
        img_name = ts + '.jpg'
        create_preview(img_name, video_file_path_app)
        video = Video(name, description, category, 'images/' + img_name, 'videos/' + video_file_name, duration, fps)
        # process = Process(1, video.id, datetime.now(), None, datetime.now(), False, None)
        try:
            db.session.add(video)
            # db.session.add(process)
            db.session.commit()
            return jsonify(video.as_dict())
        except Exception as e:
            db.session.rollback()
            return str(e), 400
    else:
        return 'Error download', 400

@app.route('/api/process/start', methods=['POST'])
@cross_origin()
def video_processing_start():
    data = request.json
    process = Process.query.filter_by(id=data['id']).first()
    video = Video.query.filter_by(id=data['videoId']).first()
    if video:
        if not process:
            process = Process(1, video.id, datetime.now(), None, datetime.now(), False, None)
            try:
                db.session.add(process)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return str(e), 400

        executor.submit(process_pipeline, process.id)
        return jsonify(process.as_dict())
    else:
        return False, 404

def process_pipeline(processId):
    process = Process.query.filter_by(id=processId).first()
    video = Video.query.filter_by(id=process.video_id).first()

    try:
        update_process_status(process, 1)
        video_file_name = video.video_file_path.split('/')[-1]
        video_file_path = './app/videos/' + video_file_name
        detected_scenes = detect_scenes(video_file_path)
        scenes = save_scenes(detected_scenes, video.id)
        update_process_status(process, 2)

        image_to_text_list = processing_video(video_file_path, scenes)
        # with open('parrot.pkl', 'wb') as f:
        #     pickle.dump(image_to_text_list, f)
        # with open('parrot.pkl', 'rb') as f:
        #     image_to_text_list = pickle.load(f)
        update_process_status(process, 3)


        # summary_texts = summorization(image_to_text_list)
        best_image_to_texts = simple_summarization(image_to_text_list)
        update_process_status(process, 4)

        translations = translate(best_image_to_texts)

        # db.session.add(scenes[0])
        # db.session.commit()

        update_process_status(process, 5)
        speaker = Speaker()
        subtitles = speaker.text2speech(translations, True, file_name='./app/audio/output_' + str(video.id) + '_')

        save_subtitles(scenes, subtitles)

        update_process_status(process, 6, True)
    except Exception as e:
        process.is_success = False
        process.date_end = datetime.now()
        process.error_message = 'Unknown error' if len(str(e)) == 0 else str(e)
        process.updated_at = datetime.now()
        db.session.commit()

def simple_summarization(image_to_text_list):
    best_image_to_texts = []
    for image_to_text_for_scene in image_to_text_list:
        best_text = ''
        dict_for_scene = {}
        for image_to_text in image_to_text_for_scene:
            text = image_to_text['text']
            if text in dict_for_scene:
                dict_for_scene[text] += 1
            else:
                dict_for_scene[text] = 1
        max_key = max(dict_for_scene.items(), key=operator.itemgetter(1))[0]
        for image_to_text in image_to_text_for_scene:
            if image_to_text['text'] == max_key:
                best_image_to_texts.append(image_to_text)
                break

    return best_image_to_texts


def save_subtitles(scenes, subtitles):
    scene_index = 0
    for subtitle in subtitles:
        cur_scene = scenes[scene_index]
        subtitleModel = Subtitle(scenes[0].id, subtitle['text'], subtitle['audio'], subtitle['frame_start'], subtitle['frame_end'])
        scene_index += 1
        db.session.add(subtitleModel)
    db.session.commit()


def save_scenes(scene_list, video_id):
    scenes = []
    for i, scene in enumerate(scene_list):
        scene = Scene(video_id, scene[0].get_frames(), scene[1].get_frames())
        if i == 0:
            try:
                db.session.add(scene)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return str(e), 400
        # TODO: save to database
        scenes.append(scene)

    return scenes


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/process/status/<int:process_id>', methods=['GET'])
@cross_origin()
def process_status(process_id):
    process = Process.query.filter_by(id=process_id).first()
    if process:
        return jsonify(process.as_dict())
    else:
        return False, 404


@app.route('/api/subtitles/<int:video_id>', methods=['GET'])
@cross_origin()
def read_subtitles_by_video(video_id):
    scenes = Scene.query.filter_by(video_id=video_id).options(joinedload(Scene.subtitles)).all()
    result = []
    for scene in scenes:
        for subtitle in scene.subtitles:
            result.append(subtitle.as_dict())
    return jsonify(result)

# @app.route('/')
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # return send_from_directory("static", "index.html")
    if '.' in path:
        return app.send_static_file(path)
    else:
        return app.send_static_file('index.html')

def update_process_status(process, status, is_success=False):
    try:
        if is_success:
            process.is_success = True
            process.date_end = datetime.now()

        process.status = status
        process.updated_at = datetime.now()
        db.session.commit()
    except Exception as e:
        db.session.rollback()


if __name__ == '__main__':
    app.run()
