## 作品介紹 - LineNotify通知系統
建立網頁表單，透過LineNotify傳送訊息

## 使用套件
`Flask` `requests`

## 程式架構
 * 網頁表單
 * 伺服器資料處理
 * LineNotify傳送訊息

## 安裝套件
`Flask`
開啟 Anaconda prompt 輸入:
```bash
conda install -c anaconda flask
# pip install Flask
```

`Flask-Bootstrap`
開啟 Anaconda prompt 輸入:
```bash
conda install -c conda-forge flask-bootstrap 
# pip install Flask-Bootstrap   # 課堂上使用這個
```

`Flask-wtf`
開啟 Anaconda prompt 輸入:
```bash
conda install -c anaconda flask-wtf  # 課堂上使用這個
# pip install flask-wtf
```


## 建立伺服器
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h>'
    
if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)
   # app.run(host='127.0.0.1', port=8080)
```

## 建立網頁

```python
# -------------here-------------
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# -------------here-------------
bootstrap=Bootstrap(app)

@app.route('/')
def index():
# -------------here-------------    
    p = 'Hello, World!'
    title = 'Notify'
    return render_template('index.html', title=title, p=p)
    
if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)
   # app.run(host='127.0.0.1', port=8080)
```

建立 templates/index.html
```html
{% extends "bootstrap/base.html" %}

{% block title %} {{ title }} {% endblock %} 

{% block content %}
{{ p }}
{% endblock %}
```

## 建立表單

```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# -------------here-------------
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
# -------------here-------------
app.config['SECRET_KEY'] = 'secret_key'
bootstrap=Bootstrap(app)

# -------------here-------------
class MsgForm(FlaskForm):
   name = StringField('輸入訊息內容', validators=[DataRequired()])
   select = SelectField('選擇訊息種類', choices=[('1', '通知'), ('2', '警告')])
   submit = SubmitField('送出')

class KeyForm(FlaskForm):
   name = StringField('輸入權杖碼', validators=[DataRequired()])
   select = SelectField('選擇註冊訊息種類', choices=[('1', '通知'), ('2', '警告')])
   submit = SubmitField('註冊')

# -------------here-------------
@app.route('/', methods=['GET', 'POST'])
def index():
    msg_form = MsgForm()
    key_form = KeyForm()

    return render_template('index.html', msg_form=msg_form, key_form=key_form)
    
if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)
   # app.run(host='127.0.0.1', port=8080)
```

```html
{% extends "bootstrap/base.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %} Notify {% endblock %} 

{% block content %}
<div class="container ">
    <div class="row">
        <br>
        <br>
        <div class="col-sm-4">
                
        </div>
        <div class="col-sm-4">
                {{ wtf.quick_form(msg_form) }}
        </div>
    </div>

    <div class="row">
        <br>
        <br>
        <div class="col-sm-4">
                
        </div>
        <div class="col-sm-4">
                {{ wtf.quick_form(key_form) }}
        </div>
    </div>

</div>
{% endblock %}
```

## 表單資料處理

```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bootstrap=Bootstrap(app)

# -------------here-------------
notification_ls = list()
warring_ls = list()

#class MsgForm(FlaskForm):...

#class KeyForm(FlaskForm):...

@app.route('/', methods=['GET', 'POST'])
def index():
    msg_form = MsgForm()
    key_form = KeyForm()

# -------------here-------------
    if msg_form.validate_on_submit():
      msg = msg_form.name.data
      mode = msg_form.select.data      

      if mode == '1':
        pass
      else:
        pass

      msg_form.name.data = ''

   if key_form.validate_on_submit():
      key = key_form.name.data
      mode = key_form.select.data

      if mode == '1':
        notification_ls.append(key)
      else:
        warring_ls.append(key)

      key_form.name.data = ''

    return render_template('index.html', msg_form=msg_form, key_form=key_form)
    
if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)
   # app.run(host='127.0.0.1', port=8080)
```

## 建立Notify.py`

```python
import requests

class LineNotify:
    def __init__(self,):
        pass
    
    def lineNotifyMessage(self, token, msg):
        headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
        }        
        payload = {'message': msg}

        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        return r.status_code

    def send_msg(self, msg, token):
    # 修改為你要傳送的訊息內容
        message = msg
        self.lineNotifyMessage(token, message)
```

## 導入檔案並改寫程式碼

```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
# -------------here-------------
from Notify import LineNotify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bootstrap=Bootstrap(app)
# -------------here-------------
notify = LineNotify()

notification_ls = list()
warring_ls = list()

#class MsgForm(FlaskForm):...

#class KeyForm(FlaskForm):...

@app.route('/', methods=['GET', 'POST'])
def index():
    msg_form = MsgForm()
    key_form = KeyForm()

    if msg_form.validate_on_submit():
      msg = msg_form.name.data
      mode = msg_form.select.data      

# -------------here-------------
      if mode == '1':
        for ele in notification_ls:
            notify.send_msg(msg, ele)
      else:
        for ele in warring_ls:
            notify.send_msg(msg, ele)

      msg_form.name.data = ''

#   if key_form.validate_on_submit():
#       ...

    return render_template('index.html', msg_form=msg_form, key_form=key_form)
    
if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)
   # app.run(host='127.0.0.1', port=8080)
```

## 連結LineNotify
https://bustlec.github.io/note/2018/07/10/line-notify-using-python/
