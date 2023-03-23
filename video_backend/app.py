from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from sqlalchemy.orm import joinedload

db = SQLAlchemy()
# create the app
app = Flask(__name__, static_folder='app', static_url_path="/app")
cors = CORS(app)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:f67Uc98KG5jc3KENrLXD@containers-us-west-167.railway.app:5517/railway"
app.config['CORS_HEADERS'] = 'Content-Type'
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

# create the extension
from models import User, Video, Scene

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

if __name__ == '__main__':
    app.run()
