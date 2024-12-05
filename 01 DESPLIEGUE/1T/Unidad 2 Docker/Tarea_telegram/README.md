
services:

  backend:

   image: zono32/back-telegram

   container_name: back

   ports:

    - "8001:8001"

   environment:

    - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}

    - TELEGRAM_CHAT_ID=${TELEGRAM_CHAT_ID}

  frontend:

   image: zono32/front-telegram

   container_name: front

   depends_on:

    - backend

   ports:

    - 8080:80
