#!/bin/bash

#echo 'Hello'

SCHRO_PY=${SCHRODINGER}'run'

FPATH=$(pwd)/$1

COMMAND="${SCHRO_PY} ${FPATH}"

bash -c "${COMMAND}"
