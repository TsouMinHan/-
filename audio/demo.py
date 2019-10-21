import random

# 亂數出題
signs_ls = ['+', '-', '*', '/'] # 顯示及判斷時使用
signs2_ls = ['加', '減', '乘', '除'] # 文字轉語音使用

# 產生隨機數字與運算符號
num1 = random.randint(1, 20)
num2 = random.randint(1, 20)

question_num = random.randint(0, 3)

sign1 = signs_ls[question_num]
sign2 = signs2_ls[question_num]

# 題目文字 - 轉語音檔時使用
question = '%d %s %d = ' % (num1, sign2, num2)

# 透過運算符號，產生答案
if sign1 == '+':
    ans = num1 + num2
elif sign1 == '-':
    ans = num1 - num2
elif sign1 == '*':
    ans = num1 * num2
elif sign1 == '/':
    ans = round(num1 / num2, 2)

print('題目: %d %s %d = ' % (num1, sign1, num2))
print(ans)

# 轉語音
from gtts import gTTS
from pygame import mixer
import time
import tempfile

with tempfile.NamedTemporaryFile(delete=True) as fp:
    tts=gTTS(text=question, lang='zh-TW')
    tts.save('%s.mp3' % (fp.name))
    mixer.init()
    mixer.music.load('%s.mp3' % (fp.name))
    mixer.music.play()
    time.sleep(3)

# 對答案
input_ans = eval(input('請輸入答案: '))

if input_ans == ans:
    txt = '恭喜答對了，答案是%d' % ans
else:
    txt = '答錯了，答案是%d' % ans

with tempfile.NamedTemporaryFile(delete=True) as fp:
    tts=gTTS(text=txt, lang='zh-TW')
    tts.save('%s.mp3' % (fp.name))
    mixer.init()
    mixer.music.load('%s.mp3' %  (fp.name))
    mixer.music.play()
    time.sleep(3)