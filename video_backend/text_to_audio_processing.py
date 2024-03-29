import torch
from IPython.display import Audio
from pydub import AudioSegment
from pydub.effects import speedup
# import audiosegment
import wave
# import pyaudio


class Speaker():
    def __init__(self, language='ru'):
        language = language
        model_id = 'v3_1_ru'
        device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

        self.model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                  model='silero_tts',
                                                  language=language,
                                                  speaker=model_id)
        self.model.to(device)

        self.gen_rate = 48000
        self.speaker = 'aidar'  # ['aidar', 'baya', 'kseniya', 'xenia', 'eugene', 'random']
        self.put_accent = True
        self.put_yo = True

    def text2speech(self, full_text, markup=None, speaker=None, file_name='output', fps=24):
        result = []
        if not speaker:
            speaker = self.speaker
        # if type(full_text) == dict:
        id = 0
        # device = torch.device("cuda") if torch.cuda.is_available() else "cpu"
        for frame_and_text in full_text:
            frame_start = frame_and_text['frame']
            text = frame_and_text['text']
            audio = self.model.apply_tts(text=text,
                                         speaker=speaker,
                                         sample_rate=self.gen_rate,
                                         put_accent=self.put_accent,
                                         put_yo=self.put_yo)

            if markup:
                gen_length = int(audio.shape[0] / self.gen_rate)
                # print(markup['voice_markup'][int(id)])
                # markup_length = int((markup['voice_markup'][int(id)]['end_frame'] - markup['voice_markup'][int(id)][
                #     'start_frame']) / fps)
                # speed_coef = markup_length / gen_length
                # if speed_coef > 1:
                #     speed_coef = 1
                # elif speed_coef < 0.5:
                #     speed_coef = 0.5
                # print(f'Коэффициент темпа речи: {speed_coef}')
                file_path = file_name + str(id) + '.wav'
                with open(file_path, 'wb') as f:
                    f.write(Audio(audio, rate=48000).data)
                audio = AudioSegment.from_wav(file_path)
                # new_file = speedup(audio, 1.5, 150)
                duration_frame = int(audio.duration_seconds * fps)
                frame_end = frame_start + duration_frame
                result.append({'frame_start': frame_start, 'frame_end': frame_end, 'text': text, 'audio': file_path})
                # new_file.export(file_path, format="wav")

                # np_audio = audiosegment.from_file(file_name + str(id) + '.wav').resample(
                #     sample_rate_Hz=48000 * speed_coef, sample_width=2,
                #     channels=1).to_numpy_array()
                # print(np_audio.shape)
                # print('Старт записи аудио сопровождения')
                # with wave.open(f'output{id}.wav', 'wb') as wf:
                #     p = pyaudio.PyAudio()
                #     wf.setnchannels(1)
                #     wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
                #     wf.setframerate(44000)
                #     print('Recording...')
                #     for i in range(0, len(np_audio), 4000):
                #         wf.writeframes(np_audio[i:i + 4000])
                #     print('Done')
                #     p.terminate()
            # else:
                # with open('class_' + id + '.wav', 'wb') as f:
                #     f.write(Audio(np_audio, rate=44000).data)
            id += 1

        return result
