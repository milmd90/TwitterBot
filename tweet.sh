#!/bin/bash
# usage: tweet.sh <your_command> <sleep_duration>

a=0
while [ $a -lt $1 ]
  do
  a=`expr $a + 1`
  python tweet.py
  sleep $2
done
