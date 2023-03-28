from scenedetect import detect, ContentDetector


def detect_scenes(video_path):
    scene_list = detect(video_path, ContentDetector())
    return scene_list
