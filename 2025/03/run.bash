#!/bin/bash
export OMP_NUM_THREADS=$1
time ./part2 ${@:2}