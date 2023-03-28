import cv2


def get_duration_and_fps(file_path):
    video = cv2.VideoCapture(file_path)

    totalNoFrames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    duration = round(totalNoFrames / fps)

    return duration, fps


def create_preview(img_name, file_path):
    cap = cv2.VideoCapture(file_path)

    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        count = count + 1
        if count > 50:
            cv2.imwrite('./app/images/' + img_name, frame)
            break

    cap.release()
