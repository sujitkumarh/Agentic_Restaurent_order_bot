import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agents.voice_agent import process_voice_order
from agents.menu_agent import get_menu, get_recommendations
from agents.stock_agent import check_stock
from agents.dietary_agent import filter_menu_by_dietary
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/menu")
def menu():
    return get_menu()

@app.post("/order")
async def order(request: Request):
    data = await request.json()
    return process_voice_order(data)

@app.get("/recommendations")
def recommendations(customer_id: str = None):
    return get_recommendations(customer_id)

@app.get("/stock")
def stock():
    return check_stock()

@app.get("/menu/dietary")
def menu_dietary(dietary: str):
    return filter_menu_by_dietary(dietary)
