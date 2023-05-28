#!/bin/bash
# Add this script to ~/.profile with an "&"

command_to_spawn="nc -l -u 12345 | python3 joystick_reader.py"

check_and_spawn_command() {
  if [ -e "/dev/input/js0" ]; then
    echo "Device '/dev/input/js0' found. Spawning command..."
    $command_to_spawn
  else
    echo "Device '/dev/input/js0' not found. Terminating script..."
    exit 1
  fi
}

# Initial check and command spawn
check_and_spawn_command

while true; do
  if [ -e "/dev/input/js0" ]; then
    # File exists, check if command is running
    pid=$(pgrep -f "$command_to_spawn")
    if [ -z "$pid" ]; then
      echo "Device '/dev/input/js0' found. Spawning command..."
      $command_to_spawn
    fi
  else
    echo "Device '/dev/input/js0' not found. Terminating script..."
    exit 1
  fi

  sleep 1  # Sleep for 1 second before the next check
done