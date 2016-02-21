#!/bin/bash

UNAME=$(uname)

if [ ${UNAME} == 'Darwin' ]
then
    XARGS="xargs -0 -J % pep8 %"
else
    XARGS="xargs -0 -t pep8"
fi

find ./openpyscad/ -name '*.py' -print0 | ${XARGS} --ignore=E501
