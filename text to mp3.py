from pydub import AudioSegment
from gtts import gTTS

def text_to_speech(text):
    language = 'en'
    my_obj = gTTS(text=text, lang=language, slow=False)
    my_obj.save("readed_text.mp3")
    sound = AudioSegment.from_file("readed_text.mp3", format="mp3")
    sound.export("readed_text.mp3")

if __name__ == '__main__':
    text_to_speech(text="CodeCrunch!")
