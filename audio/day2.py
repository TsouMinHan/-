# 轉語音
from gtts import gTTS
from pygame import mixer
import time
import tempfile

with tempfile.NamedTemporaryFile(delete=True) as fp:
    tts=gTTS(text='你好，我是google小姐', lang='zh-TW')
    tts.save('%s.mp3' % (fp.name))
    mixer.init()
    mixer.music.load('%s.mp3' % (fp.name))
    mixer.music.play()
    time.sleep(3)