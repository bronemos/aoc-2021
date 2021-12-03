#!/usr/bin/bash

for i in {1..25}
do
    mkdir day${i}
    >day${i}/day${i}.py
    >day${i}/input.txt
done