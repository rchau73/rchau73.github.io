#!/bin/bash
# frame.sh <video dir> <frame index>: renders one frame at 30 fps
V="$1"; i="$2"; t=$(python3 -c "print($i/30)")
w=$(( i % 8 ))
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1080,1080 --user-data-dir="$V/prof-$w" --screenshot="$V/frames/f$(printf %05d "$i").png" "file://$V/scene.html#$t" >/dev/null 2>&1
