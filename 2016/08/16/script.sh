#!/bin/bash
make -f makefile
numIterations=$1
i=1
num=1
while [ $i -le $numIterations ]; do
./a.out $num
let num=(num*10);
let i=i+1;
sleep 1
done
