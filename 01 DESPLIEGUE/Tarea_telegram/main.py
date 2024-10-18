from fastapi import FastAPI
from pydantic import BaseModel
import telegram

app = FastAPI()
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'
bot = telegram.Bot(token=TOKEN)

class Message(BaseModel):
    message: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to my API REST"}

@app.post("/message")
async def send_message(msg: Message):
    bot.send_message(chat_id=CHAT_ID, text=msg.message)
    return {"status": "Message sent"}
