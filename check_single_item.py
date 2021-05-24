import json
from item import item
from requests import request
from tele_conf import *

intersted_items = {}
magic_sold_out = r'disabled">Sold Out</button>'
item_list = []

def main():
    with open(r"conf.json","r") as f:
        intersted_items = json.load(f)
    
    for name,link in intersted_items.items():
        item_list.append(item(name,link,is_available(link)))
    
    _debug_pretty_print()

def _debug_pretty_print():
    for it in item_list:
        print(str(it))

def is_available(link):
    resp = request(r"GET",link)
    if magic_sold_out in resp.text:
        return False
    return True

def tele_reply(reply,chat_id):
    url = GENERIC_TELEGRAM_API + TELEGRAM_BOT_TOKEN + "/sendMessage"
    data = {"chat_id" : chat_id,
            "text" : reply}
    print("=============The message that sent:" + reply) #DEBUG
    sent = request("POST",url,data=data)
    print(sent.text) #DEBUG

if_name__ == '__main__':
    main()
