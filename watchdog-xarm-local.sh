#!/bin/bash

# TODO: Handle arm is truned off. 
# ps -aux | grep -e "xarm" -e "nc -l"
command_to_spawn1="nc -l -u -k 12345" 
command_to_spawn2="python3 ~/arm-gamepad/xarm-local.py"

function start_xarm() {
nohup sh -c " $command_to_spawn1 | $command_to_spawn2 " &>/dev/null &
}
function check_xarm_status() {
  response=$(~/arm-gamepad/gotest/getstate)
  echo "$response"
}
function set_xarm_status() {
  response=$(~/arm-gamepad/gotest/setstate)
  echo "$response"
}
function check_xarm_ps_running(){
  nc_pid=$(pgrep -f "$command_to_spawn1")
  echo "$nc_pid"
}

#test 

# spawing and getting the parent prosses, so we can kill both

### TODO::: KILL PS ON STARTUP!!!
### TODO::: KILL PS ON STARTUP!!!
### TODO::: KILL PS ON STARTUP!!!
### TODO::: KILL PS ON STARTUP!!!
### TODO::: KILL PS ON STARTUP!!!
pattern="(0001|0002)"
pattern2='5004'
while true; do
  arm_status=$(check_xarm_status)
  arm_ps=$(check_xarm_ps_running)
  # if it is up and no ps -> start
  if [[  "$arm_status" =~ $pattern && -z "$arm_ps" ]]; then
    start_xarm
    echo "it is up and no ps -> start"
  elif [[  "$arm_status" =~ $pattern2  ]]; then
    set_xarm_status
    echo "error button detected -> reset"
  fi
  # if it is not up and   ps -> kill 
  echo "--" $arm_status "--"
  echo "--" $arm_ps "--"
  if   [[ ! "$arm_status" =~ $pattern && -n "$arm_ps" ]]; then
    echo $arm_ps
    kill $arm_ps
    echo "it is not up and   ps -> kill"

  fi



  sleep 1  
done

# Motion state setting (SET)
# 3: Suspend the current motion
# 4: Stop all current motion (restart the system)
# 0: Enter the motion mode

Get the motion state (GET)
# 1:In motion
# 2:Sleep
# 3:Suspend
# 4:Stop
# 5:System reset

 
