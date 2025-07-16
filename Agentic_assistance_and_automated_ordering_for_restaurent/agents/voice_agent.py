import random
from .menu_agent import get_menu
from .recommendation_agent import get_recommendations
from .dietary_agent import check_dietary_constraints
from integrations.pos import send_order_to_pos

def process_voice_order(order_data):
    # Simulate voice-to-text and NLU
    items = order_data.get("items", [])
    dietary = order_data.get("dietary", [])
    language = order_data.get("language", "en")
    # Check dietary constraints
    if not check_dietary_constraints(items, dietary):
        return {"status": "error", "message": "Dietary constraint not met."}
    # Simulate stock check and POS integration
    pos_response = send_order_to_pos(order_data)
    return {"status": "success", "pos_response": pos_response}
