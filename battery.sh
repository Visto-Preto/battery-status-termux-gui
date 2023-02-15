#!/data/data/com.termux/files/usr/bin/bash
echo "Battery info"
termux-battery-status | bat --color=always --pager=never --decorations=never --language=json
read ENTER

