from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
import telegram
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()


class TelegramDTO(BaseModel):
    message: str


app = FastAPI()
router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to my API REST"}


@router.post("/message")
async def send_message(data_bot: TelegramDTO):
    try:
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")

        if not token or not chat_id:
            raise ValueError("Token or chat ID not found in environment variables.")  # noqa: E501

        bot = telegram.Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=data_bot.message)
        return {"message": "Message sent successfully"}
    except telegram.error.TelegramError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred: " + str(e))  # noqa: E501

app.include_router(router)
# fastapi dev main.py --port 8001
# Para ejecutar el servidor: uvicorn main:app --host 0.0.0.0 --port 8001 --reload  # noqa: E501
