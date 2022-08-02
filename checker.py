from asyncio.windows_events import NULL
from contextlib import nullcontext
import time
from pricefollower import pricefollow
from file_manager import add_product_follower
from file_manager import get_URL_data
from file_manager import get_Price_data
from file_manager import get_Mail_data



list_of_product = [[0 for x in range(3)] for y in range(10)]

for i in range (0,len(list_of_product)):

    reply = input("Ürün girmek istiyormusunuz (Y/N) : ")
    if reply=='Y' or reply == 'y':
        tempURL = list_of_product[i][0] = input("Ürünün URL linkini giriniz : ")
        tempPrice = list_of_product[i][1] = input("Bildirim Fiyatını Giriniz : ")
        tempMail = list_of_product[i][2] = input("Mail Adresinizi Giriniz : ")
        add_product_follower(tempURL, tempPrice, tempMail)

    elif reply == 'N' or reply == 'n':
        print("Daha fazla ürün girilmeyecektir.")
        break
    else :
        print("Yanlış giriş yaptınız lütfen tekrar giriniz !!!")
        i = i-1

URL_data = get_URL_data()
Price_data = get_Price_data()
Mail_data = get_Mail_data()

while True:

    for i in range(0, len(URL_data)):

        if(URL_data[i] != NULL and Price_data[i] != NULL and Mail_data[i] != NULL):
            pricefollow(URL_data[i], Price_data[i], Mail_data[i])

        else:
            continue

    time.sleep(60)
    
    

    


