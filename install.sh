#!/bin/bash

CMD=$1
TAG=$2
if [[ $CMD = "build" ]]
then
  # if you add new python modules,please build this first
  #docker build -t registry.hxquant.com:5000/hxquant/hxquantmgm:base -f Dockerfile-base .
  docker rmi registry.hxquant.com:5000/hxquant/hxquantmgm:$TAG
  docker build -t registry.hxquant.com:5000/hxquant/hxquantmgm:$TAG -f Dockerfile ..
elif [[ $CMD = "run" ]]
then
  docker run -d --net=host \
    -v /dev/shm:/dev/shm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /home/quant/backtest-data:/home/jovyan/backtest-data \
    -v /home/quant/dataapi-data:/home/jovyan/dataapi-data \
    -v /home/quant/jupyter-data:/home/jovyan/jupyter-data \
    --env BACKTEST_ENV=dev \
    --name hxquantmgm registry.hxquant.com:5000/hxquant/hxquantmgm:$TAG sleep infinity
elif [[ $CMD = "rm" ]]
then
  docker stop hxquantmgm
  docker rm hxquantmgm
  docker rmi registry.hxquant.com:5000/hxquant/hxquantmgm:$TAG
elif [[ $CMD = "push" ]]
then
  docker push registry.hxquant.com:5000/hxquant/hxquantmgm:$TAG
else
  echo "please input the action."
fi
