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