import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from pygame import mixer
import tempfile
import time

base_url = "https://www.nfu.edu.tw/zh/"    # 設定網址

res = requests.get(base_url)    # 對網頁發出請求
# print(res.status_code)    # 顯示伺服器回應狀態碼
html = res.text    # 取得網頁Html原始碼
# print(html)



soup = BeautifulSoup(html, 'html.parser')    # 解析Html程式碼
# print(soup.prettify())    # 輸出排版後的Html程式碼



div_soup = soup.find('div', class_='tab-content')    # 搜尋第一個符合條件的內容，("標籤", class_="class名稱")
# print(div_soup.prettify())
div_soup = div_soup.find_all('div', id="行政公告")    # 搜尋所有符合條件的內容，("標籤", id="id名稱")，結果會是陣列
# div_soup = div_soup.find_all('div', class_='tab-pane')
# print(div_soup)

# 從div內找出所有的a
for ele in div_soup:                      
    a_soup = ele.find_all('a')    # title是陣列



ls = []    # 儲存資料
for ele in a_soup:
    txt = ele.text.strip()    # 從超連結中取出文字部分，並除去空白字符
    if txt:    # 判斷是否為空字串
        ls.append(txt)
#     print(txt)
# print(60*'-')
# print(ls)


# print(len(ls))
ls = ls[1:]    # 取位址1到最後的資料
# ls.pop(0)
# print(len(ls))


pro_txt = '請輸入選擇(數字)\n'
for num, i in enumerate(ls):    # 處理提示字
    # print(num, i)
    pro_txt += '{}.  {}\n'.format(num+1, i)

num = int(input(pro_txt + '\n')) -1    # 為了用於陣列位址，因此-1

with tempfile.NamedTemporaryFile(delete=True) as fp:
    tts=gTTS(text=ls[num], lang='zh-TW')
    tts.save('%s.mp3' % (fp.name))
    mixer.init()
    mixer.music.load('%s.mp3' % (fp.name))
    mixer.music.play()
    time.sleep(10)