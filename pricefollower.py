import requests
from bs4 import BeautifulSoup
from send_mail import sendMail
import constants as keys

stores = ["amazon", "hepsiburada", "trendyol"]

headers = keys.headers

def pricefollow(URL, expected_price, mail):

    print("")

    for i in range(0, len(stores)):
        whc_store = str(URL).find(stores[i])

        if (whc_store > 0 and i == 0):
            whc_store = "amazon"
            amazon_follower(URL, expected_price, mail)
            break

        elif (whc_store > 0 and i == 1):
            whc_store = "hepsiburada"
            hepsiburada_follower(URL, expected_price, mail)
            break

        elif (whc_store > 0 and i == 2):
            whc_store = "trendyol"
            trendyol_follower(URL, expected_price, mail)
            break

        else:
            continue



def amazon_follower(URL, expected_price, mailaddr):

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()

    raw_price = soup.find("span", "a-price-whole").get_text()

    converted_price = raw_price.replace(
        ",", "").replace(".", "").replace(" TL", "")
    last_two_index = len(converted_price)

    price = int(converted_price[0:last_two_index])

    print("Ürün Adı : "+title)
    print("Ürünün Güncel Fiyatı : "+str(price))

    if(price <= expected_price):
        print("Amazonda takip ettiğin ürünün fiyatı düştü !!!")
        content = title+" Amazonda takip ettiğin ürünün fiyatı düştü !!! \nGüncel Fiyat : " + \
            str(price)+" TL"+"\nÜrün linki : \n"+URL
        subject = "Ürünün Fiyatı Düştü 😍🔥🔥🔥"
        sendMail(mailaddr, subject, content=content)
    
    print("\n-----------------------------------------\n")


def hepsiburada_follower(URL, expected_price, mailaddr):

    page=requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("span", "product-name").get_text().strip()

    raw_price = soup.select_one(
        '#offering-price span:first-child').get_text()

    converted_price = raw_price.replace(
        ",", "").replace(".", "").replace(" TL", "")
    last_two_index = len(converted_price)

    price = int(converted_price[0:last_two_index])

    print("Ürün Adı : "+title)
    print("Ürünün Güncel Fiyatı : "+str(price))

    if(price <= expected_price):
        print("Hepsiburada da takip ettiğin ürünün fiyatı düştü !!!")
        content = title+" Hepsiburada da takip ettiğin ürünün fiyatı düştü !!! \nGüncel Fiyat : " + \
            str(price)+" TL"+"\nÜrün linki : \n"+URL
        subject = "Ürünün Fiyatı Düştü 😍🔥🔥🔥"
        sendMail(mailaddr, subject, content=content)

    print("\n-----------------------------------------\n")


def trendyol_follower(URL, expected_price, mailaddr):

    page=requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1", "pr-new-br").get_text().strip()

    try:
        raw_price = soup.find("div", "pr-bx-nm with-org-prc").get_text()
        converted_price = raw_price.replace(
            ",", "").replace(".", "").replace(" TL", "")
        last_two_index = len(converted_price)
    except:
        raw_price = soup.find("span", class_="prc-dsc").get_text()
        converted_price = raw_price.replace(
            ",", "").replace(".", "").replace(" TL", "")
        last_two_index = len(converted_price)-2


    price = int(converted_price[0:last_two_index])

    print("Ürün Adı : "+title)
    print("Ürünün Güncel Fiyatı : "+str(price))

    if(price <= expected_price):
        print("Trendyol da takip ettiğin ürünün fiyatı düştü !!!")
        content = title+" Trendyol da takip ettiğin ürünün fiyatı düştü !!! \nGüncel Fiyat : " + \
            str(price)+" TL"+"\nÜrün linki : \n"+URL
        subject = "Ürünün Fiyatı Düştü 😍🔥🔥🔥"
        sendMail(mailaddr, subject,content=content)

    print("\n-----------------------------------------\n")
    
