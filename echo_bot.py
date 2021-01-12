import os, sys
import random
import string
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
from weather_data import weatherget
from config import client_id,client_secret,album_id,line_channel_access_token,line_channel_secret
from imgurpython import ImgurClient
from advice import advice


app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET',line_channel_secret)


channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', line_channel_access_token)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

# authenticate
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# process the HTTP request POST from LINE API
@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    handler.handle(body, signature)
    return 0

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    if event.message.text == '003':
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你好我是003\n我可以做到:\n1 天氣預報(左)\n2 給你建議(中)\n3 幫你把照片放到電腦(右)')
        )


    if event.message.text == '天氣如何阿?':



        cloud_description,current_temp,feels_like_temp,temp_min,temp_max,humidity,wind_speed = weatherget()
        
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='天氣狀況 = '+cloud_description+'\n'+
        '體感溫度 = '+feels_like_temp+'度\n'+
        '溫度 = '+temp_min+'~'+temp_max+'度\n'+
        '降雨機率 = '+humidity+'%\n'+        
        '風速 = '+wind_speed+'級')
        )
        x=float(feels_like_temp)
        y=float(temp_min)
        z=float(temp_max)
        a=float(humidity)
        b=float(wind_speed)
        c=float(current_temp)

    elif event.message.text == '給我個建議':
        
        cloud_description,current_temp,feels_like_temp,temp_min,temp_max,humidity,wind_speed = weatherget() 
        y=float(temp_min)
        z=float(temp_max)
        a=float(humidity)
        b=float(wind_speed)
        c=float(current_temp)
        reply_arr=[]
        
        if a>=50:
            reply_arr.append(TextSendMessage(text='帶個傘可能會下雨喔~'))

            
            
        if c<=20:
            reply_arr.append(TextSendMessage(text='有點冷喔帶個外套~'))

            
            
        elif c>=25:
            reply_arr.append(TextSendMessage(text='好熱別穿太厚喔~'))

            

        if (z - y) >= 5:
            reply_arr.append(TextSendMessage(text='現在有點熱但晚上會冷喔，記得外套~'))
 
            

        if b>=5:
            reply_arr.append(TextSendMessage(text='吹阿吹啊我的驕傲放縱，帶個風衣啦'))
            
        line_bot_api.reply_message(
        event.reply_token,
        reply_arr
        ) 
        
    elif event.message.text == '幫我存照片':       
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='給003看看!!!')
        ) 
    


    else :
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
        )
    return 0

@handler.add(MessageEvent, message=ImageMessage)
def message_image(event):
    image_name = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(4))
    image_content = line_bot_api.get_message_content(event.message.id)
    image_name = image_name.upper()+'.jpg'
    path='./static/'+image_name
    with open(path, 'wb') as fd:
        for chunk in image_content.iter_content():
            fd.write(chunk)
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text='好漂亮的照片幫你存起來喔')
    ) 
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')