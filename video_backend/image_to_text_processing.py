import torch
from lavis.models import load_model_and_preprocess
import cv2
from PIL import Image


def processing_video(video_path, scenes):
    # setup device to use
    device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

    # we associate a model with its preprocessors to make it easier for inference.
    # with torch.cuda.amp.autocast(dtype=torch.float16):
    model, vis_processors, _ = load_model_and_preprocess(
        name="blip2_t5", model_type="pretrain_flant5xl", is_eval=True, device=device
    )
    vis_processors.keys()

    current_scene_index = 0
    current_scene = scenes[current_scene_index]
    image_to_texts_for_scene = []
    image_to_texts = []
    cap = cv2.VideoCapture(video_path)
    frame_index = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            # image_to_texts.append('. '.join(image_to_texts_for_scene))
            break

        if frame_index >= current_scene.end_frame:
            current_scene_index += 1
            if current_scene_index < len(scenes):
                current_scene = scenes[current_scene_index]
            # image_to_texts.append('. '.join(image_to_texts_for_scene))
            image_to_texts.append(image_to_texts_for_scene)
            image_to_texts_for_scene = []
        if frame_index % 5 == 0:
            image_to_text = predict_step_frame(frame, device, model, vis_processors)
            image_to_texts_for_scene.append({'frame': frame_index, 'text': image_to_text[0]})
        frame_index += 1
    cap.release()
    return image_to_texts


def predict_step_frame(raw_image, device, model, vis_processors):
    img = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(img)
    image = vis_processors["eval"](im_pil).unsqueeze(0).to(device)
    preds = model.generate({"image": image})
    return preds
