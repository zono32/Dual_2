docker build -t front-telegram .

docker tag front-telegram zono32/front-telegram:latest

docker push zono32/front-telegram:latest
