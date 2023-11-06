# Pixi Demo

Minimal image (153 MB) for starting a Jupyter server in a Pixi-defined environment, with python and C dependencies.

## Local

`pixi run start`

## Docker

```
# inside project folder: build image and start container (<15 sec)
docker buildx build . --tag pixidemo
docker run -it -p 8888:8888 -d pixidemo /bin/bash
docker attach <container-id>

# inside container: install environment and start jupyter server (<15 sec)
pixi run jn
```
