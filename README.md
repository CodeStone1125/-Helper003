<h1>智能掛勾-Helper003</h1>
<h2> 1. 關於專案</h2>

利用Linechat bot作為操作介面， Rasberry pi 3 進行運算的操作，連接衣架利用LED燈推薦今天攜帶物品

<h2> 2. 專案導言</h2>

為了解決現代人常常趕著出門卻無法決定攜帶物品的煩惱，直接在架子閃爍led燈提示建議攜帶物品，絕對是選擇障礙者的一大福音。

順便附贈自動存取相片功能，和氣象預報功能。讓你偶爾想自己決定時也有參考依據。

<h2> 3. 專案構想</h2>

此處利用LineBot的特色->圖文選單，讓你連打字都免了。
* 使用者介面
    * ![](https://i.imgur.com/Tc2szcp.png)
( "https://imgur.com/a/fIo1Uc0" , "Helper003 圖文選單")

* 有以下功能


    * 1. 預報天氣(左)
    * 2. 建議攜帶物品(中)
    * 3. 上傳照片到電腦(Rasberry Pi 3)(右)

<h2> 4. 專案所需實體材料</h2>


材料名稱| 數量 |  用途  
:-: | :-: | :-: 
Rasberry Pi 3 | 1 | 運算程式碼 |
Led燈 | 3 | 提示攜帶物品 |
堅固衣架 | 1 | 吊掛物品 |
母對母杜邦線 | 4 | 連接Rasberry Pi與LED |
公對公杜邦線 | 7 | 連接Rasberry Pi與LED |

<h2> 5. 線路設計,指令表與實體照片</h2>

![](https://i.imgur.com/VjEgrMd.png)

<h2> 6. 程式設計</h2>

<table>
    <tr>
        <td bgcolor=#7FFFD4>
        背景顏色
        </td>
    </tr>
</table>

static
advice.py
config.py
echo_bot.ipynb
echo_bot.py
led.py

<h2> 7. 影片呈現連結</h2>




<h2> 8. 可以改進或其他發想</h2>

* 將Ngrok替代為heroku，開發搭配鬧鐘功能
* 自動上傳照片功能，希望可以自動上傳到網路平台
* 氣象API的資料處理要更有效、準確
* 實體衣架並未完成

<h2> 9.參考資料</h2>

[六小時AIoT專題實作：樹莓派管家](https://medium.com/%E5%8D%81%E7%99%BE%E5%8D%83%E5%AF%A6%E9%A9%97%E5%AE%A4/%E5%85%AD%E5%B0%8F%E6%99%82aiot%E5%B0%88%E9%A1%8C%E5%AF%A6%E4%BD%9C-%E6%A8%B9%E8%8E%93%E6%B4%BE%E7%AE%A1%E5%AE%B6-39fddf4b949c)
[Python: 透過Open Weather Map API抓取天氣資料](http://www.ducala.org/1899/python-%E9%80%8F%E9%81%8Eopen-weather-map-api%E6%8A%93%E5%8F%96%E5%A4%A9%E6%B0%A3%E8%B3%87%E6%96%99/)
