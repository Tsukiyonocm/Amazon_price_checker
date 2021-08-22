
from sys import float_repr_style
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import config as cfg
from random import randint

test_1 = ["https://www.amazon.com/dp/B06ZZ1MKW8/?coliid=I1S7URDP873KP1&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08G1XNG7J/ref=tmm_kin_swatch_0?_encoding=UTF8&coliid=I15CT0V01VN8S7&colid=35QH7NCHBH01U&qid=&sr=", "https://www.amazon.com/dp/B00I82884W/?coliid=I2NSN362O7FHKI&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it"]

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36", "Referer" : "https://www.google.com", 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'}

price_threshold = {}
batches = [test_1]

def check_all():
    for URL in test_1:
        check_price(URL)
    print(price_threshold)
    send_mail(price_threshold)

def check_price(URL):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="kindle-price").get_text()

    converted_price = float(price[2:])

    if (converted_price <= 3.99):
        dict_index = len(price_threshold)
        dict_title = title.strip()
        dict_price = converted_price
        price_threshold[dict_index] = {"Title": dict_title, "Price": dict_price, "URL": URL}

    time.sleep(randint(5,15))


def send_mail(dict):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # If posting online, make sure to hide the password here
    server.login("craigmenne@gmail.com", str(cfg.gpass))
    subject = "Price Checker is working"
    body = build_email(price_threshold)

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "craigmenne@gmail.com",
        "craigmenne@gmail.com",
        msg
    )

    print("Email has been sent!")

    server.quit()


def build_email(dict):
    """
    Takes the dictionary and creates the body of the email.
    """

    body = ""

    if len(price_threshold) <=  7:
        body = body + "Nothing new to report here, But here are the usuals anyway:" + "\n\n"
    else:
        body = body + "It appears there was a new item addition. Please check carefully!" + "\n\n"

    for id, info in price_threshold.items():
        for key in info:
            body = body + "  " + str(info[key])
        body = body + "\n\n"

    return body

check_all()


"""
What I need to do here: 
check which batch a URL is in:
If price threshold is 0: 
    There was no books below threshold
elif url is in batch 1:
    email subject:
        "Batch 1 Prices checked"
elif url is in batch 2:
        email subject:
        "Batch 2 prices checked"
etc
"""