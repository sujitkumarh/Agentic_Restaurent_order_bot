import json

def check_dietary_constraints(items, dietary):
    # Dummy check: always returns True
    return True

def filter_menu_by_dietary(dietary):
    with open("data/menu.json") as f:
        menu = json.load(f)["menu"]
    filtered = [item for item in menu if dietary in item.get("dietary", [])]
    return filtered
