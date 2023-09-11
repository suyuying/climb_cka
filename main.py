
import requests
from bs4 import BeautifulSoup
from tg import tool
from config import Setting
import re
# 定義目標URL
url = "https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/"

# 發送HTTP GET請求
response = requests.get(url)

# 檢查是否成功獲取頁面
if response.status_code == 200:
    # 解析HTML內容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到目標元素
    target_element = soup.find("div", class_="lf_pdp_fundamentals-buy-body-card-info-price")

    # 檢查是否找到目標元素
    if target_element:
        # 提取元素的文本內容
        price = target_element.text.strip()
        tg_obj=tool.TelegramBot(token=Setting.tg_token,chat_id=Setting.chat_id,)
        # 列印價格
        print("今日價格:", price)
        pattern=r"\w+"
        price_int=re.search(pattern,price).group()
        tg_obj=tool.TelegramBot(token=Setting.tg_token,chat_id=Setting.chat_id,)
        tg_obj.send_message(f"今日價格{price}")
        if int(price_int) < 395:
            print(f"今日有特惠價:{price}")
            tg_obj.send_message(f"今日有特惠價:{price}")
    else:
        print("找不到目標元素")
else:
    print("無法獲取網頁內容")
