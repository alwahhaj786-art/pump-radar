import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

def check_and_send(symbol, entry, target, stop_loss, block_percent, market_cap, liquidity):
    profit_percent = ((target - entry) / entry) * 100
    if profit_percent < 50:
        return False
    message = f"""🚨 توصية البمب من القاع
🪙 العملة: {symbol}
🧮 نسبة الكتلة: {block_percent}%
💸 نسبة الربح المتوقع: {profit_percent:.0f}%
💰 الماركت كاب: ${market_cap}
📊 السيولة: ${liquidity}
🎯 الدخول: {entry}
📈 الهدف النهائي: {target}
🛑 وقف الخسارة: {stop_loss}"""
    send_telegram(message)
    return True

if __name__ == "__main__":
    check_and_send("BTC/USDT", 5433, 8688, 1234, 70, "91K", "33K")
