import json
from item import item
from requests import request

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

if __name__ == '__main__':
    main()
