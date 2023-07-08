#!/bin/bash
# Add this script to ~/.profile with an "&"

# TODO: CHEK IF THE COMMAND PROSSES CRASHES IF THE ARM IS UNPLUGGED

command_to_spawn="nc -l -u 12345 | python3 joystick_reader.py"
host="192.168.1.158"  



while true; do
  ping -c 1 "$host" > /dev/null

  if [ $? -eq 0 ]; then
    pid=$(pgrep -f "$command_to_spawn")
    echo "Host is reachable. Spawning command..."
    if [ -z "$pid" ]; then
      $command_to_spawn
    fi
  else

  fi

  sleep 1  
done
