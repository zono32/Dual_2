version: '3'
services:
  backend:
    image: zono32/back-telegram:latest
    ports:
      - "8001:8001"
    environment:
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
      - TELEGRAM_CHAT_ID=${TELEGRAM_CHAT_ID}

  frontend:
   image: zono32/front-telegram:latest
    ports:
      - "8080:80"
