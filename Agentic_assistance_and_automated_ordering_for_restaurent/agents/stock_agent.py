import json

def check_stock():
    with open("data/stock.json") as f:
        return json.load(f)
