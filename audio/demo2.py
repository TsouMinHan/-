from gtts import gTTS
from pygame import mixer
import time
import tempfile

# 程式說出選項
with tempfile.NamedTemporaryFile(delete=True) as fp:
    tts=gTTS(text='請問您想要吃飯還是麵呢?', lang='zh-TW')
    tts.save('%s.mp3' % (fp.name))
    mixer.init()
    mixer.music.load('%s.mp3' % (fp.name))
    mixer.music.play()
    time.sleep(3)

# 依照選項回答
import speech_recognition

r = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:

    print("校準麥克風...")
    r.adjust_for_ambient_noise(source, duration=3)

    print("說些什麼吧!")
    audio = r.listen(source)

ans = '' # 預設值，避免在辨識出現錯誤時沒有宣告變數
try:
    print("Google Speech Recognition 認為你說:")
    ans = r.recognize_google(audio, language="zh-TW")
    print(ans)

except speech_recognition.UnknownValueError:
    print("Google Speech Recognition 無法理解你說什麼")

except speech_recognition.RequestError as e:
    print("沒有回應 Google Speech Recognition service: {0}".format(e))

# 產生回覆答案，並說出答案
import random

rice_ls = ['小南', '阿松',]
noodle_ls = ['小江南', '大吉祥',]

if '飯' in ans:
    response_txt = '你可以吃' + rice_ls[random.randint(0, len(rice_ls)-1)]

elif '麵' in ans:
    response_txt = '你可以吃' + noodle_ls[random.randint(0, len(noodle_ls)-1)]

else:
    response_txt = '抱歉，我不清楚你說什麼'

with tempfile.NamedTemporaryFile(delete=True) as fp:
    tts=gTTS(text=response_txt, lang='zh-TW')
    tts.save('%s.mp3' % (fp.name))
    mixer.init()
    mixer.music.load('%s.mp3' % (fp.name))
    mixer.music.play()
    time.sleep(3)
