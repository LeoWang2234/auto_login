#!/bin/bash
# new mac id generated randomly
new_mac=$(openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//')
echo $new_mac

# alter mac id
sudo ifconfig en0 ether $new_mac

# get mac id now is in use ,if alteration success ,it should be the 
# same with new_mac
mac_now_in_use=$(ifconfig en0 | grep ether)
echo $mac_now_in_use


