#!/bin/bash

DOMINIOPROD=kev2110/pythonprod:v1.0
DOMINIOQA=kev2110/pybinver:v1.0
VOLUMEN=v1:/var/
RUTA=/var/lib/docker/volumes/v1/_data/

docker run --rm -v $VOLUMEN $DOMINIOPROD
docker run --rm -v $VOLUMEN $DOMINIOQA

echo "Log version" > /home/binaps_version/`date +%Y%m%d`_logversion.txt

cd $RUTA && cat prodlog.txt qalog.txt > /home/binaps_version/`date +%Y%m%d`_logversion.txt
