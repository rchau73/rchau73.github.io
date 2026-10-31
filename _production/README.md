# Video sources

Each video is an HTML page whose state is a function of the time in its URL hash (`videoC.html#12.5`).
`frame.sh <dir> <video> <frame>` renders one 1080×1080 frame with headless Chrome; ffmpeg joins them at 30 fps:

    D=$(grep -o 'const D=[0-9]*' videos/videoC.html | cut -d= -f2)
    mkdir -p videos/framesC && seq 0 $((D*30-1)) | xargs -P 8 -I{} videos/frame.sh "$PWD/videos" C {}
    ffmpeg -framerate 30 -i videos/framesC/f%05d.png -c:v libx264 -pix_fmt yuv420p -crf 18 -preset slow -movflags +faststart ../media/videoC-product.mp4

Screenshots are in `shots/`. GitHub Pages (Jekyll) does not serve folders starting with `_`.
Video 1 is `video1/scene.html` (its own styles, no common.css).
