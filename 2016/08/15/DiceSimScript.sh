#!/bin/bash
gcc -o DiceSimulator.o DiceSimulator.c


for j in `seq 2 8`; do 
	i=1
	while [ $i -le 1000000 ]; do
	./DiceSimulator.o $i $j
	let i=(i+i);
	sleep 1
done
done
