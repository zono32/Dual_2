from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
import telegram
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Cargar variables de entorno desde el archivo .env
load_dotenv()


class TelegramDTO(BaseModel):
    message: str


app = FastAPI()
router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar "*" por tu dominio en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", summary="Home endpoint", description="Root endpoint to verify API is working")
async def root():
    return {"message": "Welcome to my API REST"}


@router.post("/message", summary="Send a message to Telegram")
async def send_message(data_bot: TelegramDTO):
    try:
        logging.info("Processing message: %s", data_bot.message)

        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")

        if not token or not chat_id:
            logging.error("Missing Telegram credentials in environment variables")
            raise ValueError("Token or chat ID not found in environment variables.")

        bot = telegram.Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=data_bot.message)

        logging.info("Message sent successfully")
        return {"message": "Message sent successfully"}
    except telegram.error.TelegramError as e:
        logging.error("Telegram error: %s", str(e))
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error("An unexpected error occurred: %s", str(e))
        raise HTTPException(status_code=500, detail="An error occurred: " + str(e))


app.include_router(router)