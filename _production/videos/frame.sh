#!/bin/bash
# frame.sh <dir> <video n> <frame index>: renders one 1080x1080 frame at 30 fps
# each Chrome gets 60 s (a headless Chrome sometimes never exits after the screenshot), one retry
V="$1"; n="$2"; i="$3"; t=$(python3 -c "print($i/30)")
out="$V/frames$n/f$(printf %05d "$i").png"
for _ in 1 2; do
  perl -e 'alarm 60; exec @ARGV' "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1080,1080 --allow-file-access-from-files --user-data-dir="$V/prof-$n-$((i % 8))" --screenshot="$out" "file://$V/video$n.html#$t" >/dev/null 2>&1
  [ -s "$out" ] && exit 0
done
