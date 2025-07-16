import json

def get_menu():
    with open("data/menu.json") as f:
        return json.load(f)

def get_recommendations(customer_id=None):
    # Dummy recommendations
    return [
        {"id": 1, "name": "Veggie Burger Combo"},
        {"id": 3, "name": "Gluten-Free Salad"}
    ]
