# arm-gamepad

```sh
cd
git clone https://github.com/Kraftbar/arm-gamepad
echo "~/arm-gamepad/watchdog-xarm-local.sh &" >> ~/.bashrc
# Reload the bash profile
source ~/.bashrc
cd gamepad


cd
git clone https://github.com/Kraftbar/arm-gamepad
echo "~/arm-gamepad/watchdog-xarm-remote.sh &" >> ~/.bashrc
# Reload the bash profile
source ~/.bashrc
cd gamepad


go build -o gotest/getstate gotest/getstate.go && ./gotest/getstate









nohup sh -c "nc -l -u -k 12345 | python3 ~/arm-gamepad/xarm-local.py" &

nybo@nybo-Latitude-7480:~$ pstree -p  | grep -C10 "sh"

nybo@nybo-Latitude-7480:~$ lsof -p 5397 | grep -E '([0-9]+[wu])|([0-9]+[wu].+[2,1]u)'
python3 5397 nybo    1w   REG    8,2        0 10356710 /home/nybo/nohup.out
python3 5397 nybo    2w   REG    8,2        0 10356710 /home/nybo/nohup.out
python3 5397 nybo    3u  IPv4  71662      0t0      TCP nybo-Latitude-7480.lan:56226->192.168.1.158:502 (ESTABLISHED)
python3 5397 nybo    4u  IPv4  71663      0t0      TCP nybo-Latitude-7480.lan:46624->192.168.1.158:30002 (ESTABLISHED)
nybo@nybo-Latitude-7480:~$ lsof -p 5396 | grep -E '([0-9]+[wu])|([0-9]+[wu].+[2,1]u)'
nc      5396 nybo    0w   CHR    1,3      0t0        6 /dev/null
nc      5396 nybo    1w  FIFO   0,13      0t0    73154 pipe
nc      5396 nybo    2w   REG    8,2        0 10356710 /home/nybo/nohup.out
nc      5396 nybo    3u  IPv4  72605      0t0      UDP *:12345 
nybo@nybo-Latitude-7480:~$ lsof -p 5395 | grep -E '([0-9]+[wu])|([0-9]+[wu].+[2,1]u)'
sh      5395 nybo    0w   CHR    1,3      0t0        6 /dev/null
sh      5395 nybo    1w   REG    8,2        0 10356710 /home/nybo/nohup.out
sh      5395 nybo    2w   REG    8,2        0 10356710 /home/nybo/nohup.out






# test 
nohup sh -c "nc -l -u -k 12345 | python3 ~/arm-gamepad/xarm-local.py &>/dev/null" &
nohup sh -c "nc -l -u -k 12345 | python3 ~/arm-gamepad/xarm-local.py " &>/dev/null &

pstree -p  | grep -C10 "sh"


```
