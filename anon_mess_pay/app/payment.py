
import requests
from data.config import TBANK_API_KEY, TBANK_MERCHANT_ID

def create_payment(amount: float = None, description: str = "Оплата подписки"):
    if amount is None:
        return None, None
    """Создание платежа через Т-Банк"""
    try:
        response = requests.post(
            "https://api.tbank.ru/v1/invoice/create",
            headers={
                "Authorization": TBANK_API_KEY,
                "Content-Type": "application/json"
            },
            json={
                "terminal": TBANK_MERCHANT_ID,
                "amount": amount,
                "description": description,
                "notification_url": "https://your-bot-domain.com/webhook/payment",
                "success_url": "https://t.me/your_bot",
                "fail_url": "https://t.me/your_bot"
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            return data.get("id", ""), data.get("url", "")
        return None, None
    except Exception as e:
        print(f"Error creating payment: {e}")
        return None, None

def check_payment(payment_id: str) -> bool:
    """Проверка статуса платежа"""
    try:
        response = requests.get(
            f"https://api.tbank.ru/v1/invoice/status/{payment_id}",
            headers={
                "Authorization": TBANK_API_KEY
            }
        )
        if response.status_code == 200:
            data = response.json()
            return data["status"] == "CONFIRMED"
        return False
    except Exception as e:
        print(f"Error checking payment: {e}")
        return False
