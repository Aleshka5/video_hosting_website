from transformers import FSMTForConditionalGeneration, FSMTTokenizer


def translate(text_list):
    mname = "facebook/wmt19-en-ru"
    tokenizer = FSMTTokenizer.from_pretrained(mname)
    model = FSMTForConditionalGeneration.from_pretrained(mname)
    translated_list = []
    # for key, value in result_dict.items():
    for text_frame_text in text_list:
        frame = text_frame_text['frame']
        text = text_frame_text['text'] + '.'
        input_ids = tokenizer.encode(text, return_tensors="pt")
        outputs = model.generate(input_ids)
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # translated_dict[key] = decoded
        translated_list.append({'frame': frame, 'text': decoded})
    return translated_list
