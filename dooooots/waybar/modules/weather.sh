#!/bin/bash
#
# weather script for waybar, copyed from  movsxd @ https://github.com/movsxd/dotfiles
# may go more complex and add icons down the track
resp=$(curl -s en.wttr.in?format=%t 2>/dev/null | cut -d+ -f2)
echo -e "{\"text\":\""$resp"\"}"
