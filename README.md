
## IOT Coat Hanger - Helper003

An IoT coat hanger.

Which is pairs with your smartphone to deliver information such as weather 
forecasts and reminds you to take essential items, like your keys, before you head out.

### Why I Want to made This Project

To address the common frustration of modern individuals who are often in a rush to leave but 
cannot decide what items to bring, our shelf features blinking LED lights to suggest items to carry. This is a great boon for those with decision fatigue.

Additionally, it comes with an automatic photo storage feature and a weather forecast function, 
providing references for when you occasionally want to make the decision on your own.

### Architecture

The system is implement using `Python3` and operated through a `Line chatbot` interface, with a `Raspberry Pi 3` performing the
computations, connecting to a clothes hanger that uses LED lights to recommend items to take for the day. Following table is
the fountion I made and their explaination.

| File Name    | Purpose                                                   |
| ------------ | --------------------------------------------------------- |
| `weather_data` | OpenWeather API                                           |
| `advice.py`    | Suggests items to carry based on data from weather_data   |
| `config.py`   | Stores various keys                                       |
| `echo_bot.py`  | LineBot                                                   |
| `led.py`       | Test LED lights                                           |

### GUI

The rich menu is depicted with three main options, illustrated in an image hosted on Imgur (Helper003 rich menu).
The features include:

| ![](https://i.imgur.com/Tc2szcp.png) |
|:-----------------------------------:|
| **GUI** |

### Necessary material 

| Material Name | Quantity | Purpose |
| ------------- | -------- | ------- |
| Raspberry Pi 3 | 1 | Running code |
| LED Lights | 3 | Indicating items to carry |
| Sturdy Hanger | 1 | Hanging items |
| Female-to-Female Dupont Wire | 4 | Connecting Raspberry Pi to LEDs |
| Male-to-Male Dupont Wire | 7 | Connecting Raspberry Pi to LEDs |


### Circuit Design and Physical Photographs

<font color=#FF0000> Actually, I use Rasberry pi 3 instead of arduno </font>

![](https://i.imgur.com/VjEgrMd.png)

![](https://i.imgur.com/45c1pLi.png)

![](https://i.imgur.com/YXfZ3YA.png)

### Additional Explanation in Chinese
<h2> 8. 可以改進或其他發想</h2>

- [ ] 將Ngrok替代為heroku，開發搭配鬧鐘功能
- [ ] 自動上傳照片功能，希望可以自動上傳到網路平台
- [ ] 氣象API的資料處理要更有效、準確
- [ ] 實體衣架並未完成

<h2> 9.參考資料</h2>

[六小時AIoT專題實作：樹莓派管家](https://medium.com/%E5%8D%81%E7%99%BE%E5%8D%83%E5%AF%A6%E9%A9%97%E5%AE%A4/%E5%85%AD%E5%B0%8F%E6%99%82aiot%E5%B0%88%E9%A1%8C%E5%AF%A6%E4%BD%9C-%E6%A8%B9%E8%8E%93%E6%B4%BE%E7%AE%A1%E5%AE%B6-39fddf4b949c)

[Python: 透過Open Weather Map API抓取天氣資料](http://www.ducala.org/1899/python-%E9%80%8F%E9%81%8Eopen-weather-map-api%E6%8A%93%E5%8F%96%E5%A4%A9%E6%B0%A3%E8%B3%87%E6%96%99/)

<h2> 10.安裝教學</h2>

### Weather API

* 1.在Open weather map 中註冊帳號，然後按紅圈處

    ![](https://i.imgur.com/kNzt7xq.png)

* 2.複製圖中的KEY

    ![](https://i.imgur.com/NjevHWi.png)

* 3.將KEY貼到 `weather_data`的APPID
<font color=#FF0000> 注意 ' ' 也要刪掉。 </font>

    ![](https://i.imgur.com/Rb0UXHg.png)

    ![](https://i.imgur.com/JvfsZCL.png)

* 4.如果成功輸出結果如下

    ![](https://i.imgur.com/48ZFGeB.png)

### flask

* 1.首先請下載flask 

        pip3 install Flask 
        

* 2.執行 `web_app.py`

        python3 web_app.py

* 3.測試
    從筆電瀏覽器
    http://raspberrypi.local:5000
    <font color=#FF0000> or </font>
    http://rasberry的IP:5000

### ngrok<font color=#FF0000> (ps:如果其他裝置想訪問ngrok的flask需要在相同區域網路下) </font>

* 1.首先請下載ngrok
    
    https://ngrok.com/

* 2.註冊後下載<font color=#FF0000>Linux</font>版

* 3.打開 cmd 解壓縮

* 4.生成驗證檔，裡面有authtoken

* 5.`./ngrok http 5000` （Flask 預設在 port 5000）

### LineChat Bot

* 1.註冊然後登入
https://developers.line.biz/en/

        Create new provider > Create new Messaging API channel > App name 是新增的LINE帳號名稱 > QR code

* 2.登入
https://manager.line.biz/
可以找到剛剛新增的Bot

* 3.掃描 QR code 或者 搜尋 ID 以便後續測試

    ![](https://i.imgur.com/zLAUdkd.png)


* 4.關閉自動回復並開啟Web hook

    ![](https://i.imgur.com/10EDeTe.png)

    ![](https://i.imgur.com/nYMSkBT.png)
    
* 5.編輯`echo_bot.py`

* 6.中斷`web_app.py`

* 7.安裝 LINE Bot 開發套件

        pip3 install line-bot-sdk
        
* 8.設定環境變數
    * CHANNEL ACCESS TOKEN 按ISSUE

    ![](https://i.imgur.com/I7VNf1Z.png)
    
    * 將產生的CHANNEL ACCESS TOKEN填入`config.py`

            export LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET
            export LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN

* 9.執行`echo_bot.py`

### 裝置實作

* 1.先利用`led.py`測試led燈是否連接妥當

* 2.根據上文的線路設計製作

### 圖文選單

* 1.進入 https://manager.line.biz/
    
    點選你要的linebot > 圖文選單 > 依照圖片中輸入    <font color=#FF0000>(ps:儲存後需等待一下)</font>
    
    ![](https://i.imgur.com/sSW9NGr.png)
    
    ![](https://i.imgur.com/B1DC1JG.png)
    
<font size=30 color=#FF0000> 然後執行echo_bot.py就完成 </font>

    






