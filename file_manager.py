import csv
import pandas as pd


def get_URL_data():
    headers = ['URL', 'Price', 'Mail']
    df = pd.read_csv("data/watched_products.csv", names=headers)
    URL = df['URL']

    return URL


def get_Price_data():
    headers = ['URL', 'Price', 'Mail']
    df = pd.read_csv("data/watched_products.csv", names=headers)
    Price = df['Price']

    return Price


def get_Mail_data():
    headers = ['URL', 'Price', 'Mail']
    df = pd.read_csv("data/watched_products.csv", names=headers)
    Mail = df['Mail']

    return Mail

def add_product_follower(URL,Price,Mail):
    dataFile = open("data/watched_products.csv", "a")

    CsvWriter = csv.writer(dataFile, delimiter=",")

    data = ["\n"+URL, Price, Mail]

    CsvWriter.writerow(data)

    dataFile.close()
