# Agentic Voice Ordering System for Restaurants

## Overview
This project demonstrates an agentic AI-powered voice ordering system for restaurants, supporting multiple languages, dietary needs, and channels (kiosk, phone, web, mobile). It features modular agents for voice recognition, menu intelligence, recommendations, dietary filtering, and POS integration.

## Folder Structure
- `app/` - Frontend web app (HTML/CSS/JS, kiosk/mobile friendly)
- `backend/` - FastAPI backend with agent endpoints
- `agents/` - Modular agent logic (voice, menu, recommendation, dietary, stock)
- `integrations/` - POS and other system integrations
- `data/` - Sample menu, stock, and order data
- `utils/` - Utility functions (future use)

## Features
- Voice-based and multi-language ordering (English, Spanish)
- Menu ingestion with combos, modifiers, allergens, promotions
- Personalized recommendations
- Dietary/allergen filtering
- POS integration and stock updates
- Real-time menu and order status
- Accessible UI for kiosk, web, and mobile

## How to Run
1. **Install Python dependencies**
   - `pip install fastapi uvicorn`
2. **Start the backend**
   - `cd backend`
   - `uvicorn main:app --reload`
3. **Open the frontend**
   - Open `app/index.html` in your browser (kiosk/mobile compatible)
   - For full cross-origin support, use a local web server (e.g., `python -m http.server` in `app/`)
4. **Try the flow**
   - Click "Start Voice Order" (simulated)
   - View menu, place order, see status

## SME
- Rohit Goel, Ravi Pol

---
This is a prototype. For production, add real voice/NLU, authentication, and robust integrations.
