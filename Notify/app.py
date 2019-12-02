from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from Notify import LineNotify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
bootstrap=Bootstrap(app)
notify = LineNotify()

notification_ls = list()
warring_ls = list()

class MsgForm(FlaskForm):
   name = StringField('輸入訊息內容', validators=[DataRequired()])
   select = SelectField('選擇訊息種類', choices=[('1', '通知'), ('2', '警告')])
   submit = SubmitField('送出')

class KeyForm(FlaskForm):
   name = StringField('輸入權杖碼', validators=[DataRequired()])
   select = SelectField('選擇註冊訊息種類', choices=[('1', '通知'), ('2', '警告')])
   submit = SubmitField('註冊')

@app.route('/', methods=['GET', 'POST'])
def index():

   msg_form = MsgForm()
   key_form = KeyForm()

   if msg_form.validate_on_submit():
      msg = msg_form.name.data
      mode = msg_form.select.data      

      if mode == '1':
         for ele in notification_ls:
            notify.send_msg(msg, ele)

      else:
         for ele in warring_ls:
            notify.send_msg(msg, ele)

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