#!/bin/bash

# TODO: Handle arm is truned off. 

command_to_spawn1="nc -l -u -k 12345" 
command_to_spawn2="python3 ~/arm-gamepad/xarm-local.py"
host="192.168.1.158"  



while true; do
  ping -c 1 "$host" > /dev/null

  if [ $? -eq 0 ]; then
    pid1=$(pgrep -f "$command_to_spawn1")
    pid2=$(pgrep -f "$command_to_spawn2")
    echo "Host is reachable. Spawning command..."
    if [ -z "$pid1" ]; then
        eval "$command_to_spawn1 | $command_to_spawn2 &"
    else
        kill "$pid1"
        kill "$pid2"
    fi
  fi


  sleep 1  
done
