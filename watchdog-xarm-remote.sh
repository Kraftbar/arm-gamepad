#!/bin/bash

command_to_spawn="python3 ~/arm-gamepad/xarm-remote.py"


while true; do
  # Check if controller is plugged
  if [ -e "/dev/input/js0" ]; then

    pid=$(pgrep -f "$command_to_spawn")
    # Check if it has crashed
    if [ -z "$pid" ]; then
      eval "$command_to_spawn"
    fi

  else
    echo "Device '/dev/input/js0' not found. Terminating script..."

  fi

  sleep 1
done

# test