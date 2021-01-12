from weather_data import weatherget
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
def advice():

    cloud_description,current_temp,feels_like_temp,temp_min,temp_max,humidity,wind_speed = weatherget()
                
    x=float(feels_like_temp)
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
    return 0   