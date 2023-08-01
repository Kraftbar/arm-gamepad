#!/bin/bash

# TODO: Handle arm is truned off. 
# ps -aux | grep -e "xarm" -e "nc -l"
command_to_spawn1="nc -l -u -k 12345" 
command_to_spawn2="python3 ~/arm-gamepad/xarm-local.py"

function start_xarm() {
nohup sh -c " $command_to_spawn1 | $command_to_spawn2 " &>/dev/null &
}
function check_xarm_status() {
  response=$(./gotest/getstate)
  echo "$response"
}
function check_xarm_ps_running(){
  nc_pid=$(pgrep -f "$command_to_spawn1")
  echo "$nc_pid"
}

#test 

# spawing and getting the parent prosses, so we can kill both


pattern="(0001|0002)"

while true; do
  arm_status=$(check_xarm_status)
  arm_ps=$(check_xarm_ps_running)
  # if it is up and no ps -> start
  if [[  "$arm_status" =~ $pattern && -z "$arm_ps" ]]; then
    start_xarm
    echo "it is up and no ps -> start"
  fi
  # if it is not up and   ps -> kill 
  echo "--" $arm_ps "--"
  if [[ ! "$arm_status" =~ $pattern && -n "$arm_ps" ]]; then
    echo $arm_ps
    kill $arm_ps
    echo "it is not up and   ps -> kill"
  fi



  sleep 1  
done


# 1:In motion
# 2:Sleep
# 3:Suspend
# 4:Stop
# 5:System reset

 