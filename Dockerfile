FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl # --no-install-recommends

RUN curl -fsSL https://pixi.sh/install.sh | bash

WORKDIR /code

COPY . /code/

EXPOSE 8888
