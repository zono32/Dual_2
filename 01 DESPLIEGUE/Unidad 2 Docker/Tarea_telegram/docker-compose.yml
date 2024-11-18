version: '3'
services:
  backend:
    build:
      context: ./back
    ports:
      - "8001:8001"
    environment:
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
      - TELEGRAM_CHAT_ID=${TELEGRAM_CHAT_ID}

  frontend:
    build:
      context: ./front
    ports:
      - "8080:80"
