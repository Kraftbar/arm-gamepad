#!/bin/bash
# TODO: check if eval is blocking
# TODO:   

command_to_spawn1="python3 ~/arm-gamepad/xarm-remote.py"
function start_xarm() {
      eval "$command_to_spawn1"
}
function check_xarm_ps_running(){
  nc_pid=$(pgrep -f "$command_to_spawn1")
  echo "$nc_pid"
}

while true; do
  arm_ps=$(check_xarm_ps_running)
  if [ -e "/dev/input/js0" ] && [ -z "$arm_ps" ]; then

    start_xarm
  fi

  sleep 1
done

# test