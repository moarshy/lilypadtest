#!/bin/bash

echo "Hello World"

param1=$1
param2=$2
param3=$3

echo "param1: $param1"
echo "param2: $param2"
echo "param3: $param3"

# add param1, param2, param3
sum=$(($param1+$param2+$param3))

echo "sum: $sum"