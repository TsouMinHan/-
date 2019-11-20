## Html 基本介紹
* [Html - 基本範例](https://www.w3schools.com/html/html_basic.asp)

* [Html - table](https://www.w3schools.com/html/html_tables.asp)

* [Html - class](https://www.w3schools.com/html/html_classes.asp)

* [Html - id](https://www.w3schools.com/html/html_id.asp)

## 作品介紹 - 顯示學校公告資訊
透過程式爬取學校網站的公告內容，並透過語音播放

## 使用套件
`pygame`
`gTTS`
`requests`
`BeautifulSoup`

## 程式架構
* 爬取網頁內容
* 整理資料格式
* 語音撥放

## 安裝套件
pygame
開啟 Anaconda prompt 輸入:
```bash
pip install pygame
```
py檔輸入:
```python
import pygame
```
https://pypi.org/project/pygame/

-----------

gTTS
開啟 Anaconda prompt 輸入:
```bash
pip install gTTS
```
py檔輸入:
```python
from gtts import gTTS
```
https://pypi.org/project/gTTS/

-----------

## 取得網頁資料
```python
base_url = "https://www.nfu.edu.tw/zh/"    # 設定網址

res = requests.get(base_url)    # 對網頁發出請求
# print(res.status_code)    # 顯示伺服器回應狀態碼
html = res.text    # 取得網頁Html原始碼
# print(html)
```

## 解析資料
```python
soup = BeautifulSoup(html, 'html.parser')    # 解析Html程式碼
# print(soup.prettify())    # 輸出排版後的Html程式碼
```

## 取得區塊標籤
```python
div_soup = soup.find('div', class_='tab-content')    # 搜尋第一個符合條件的內容，("標籤", class_="class名稱")
# print(div_soup.prettify())
div_soup = div_soup.find_all('div', id="行政公告")    # 搜尋所有符合條件的內容，("標籤", id="id名稱")，結果會是陣列
# div_soup = div_soup.find_all('div', class_='tab-pane')
# print(div_soup)

# 從div內找出所有的a
for ele in div_soup:                      
    a_soup = ele.find_all('a')    # title是陣列
```

## 取得資料
```python
ls = []    # 儲存資料
for ele in a_soup:
    txt = ele.text.strip()    # 從超連結中取出文字部分，並除去空白字符
    if txt:    # 判斷是否為空字串
        ls.append(txt)
#     print(txt)
# print(60*'-')
# print(ls)
```

## 整理資料
```python
# print(len(ls))
ls = ls[1:]    # 取位址1到最後的資料
# ls.pop(0)
# print(len(ls))
```

## 播放語音
```python
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
```
