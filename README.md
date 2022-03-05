# broken_news

## Setup

---

1. Generate API key and secret: https://uberduck.ai/account/manage
2. Set those as env. vars:
    * UBERDUCK_Key
    * UBERDUCK_Secret

3. Install 7zip: https://www.7-zip.org/download.html
4. Install FFMPEG: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
    * Will need to restart any IDE you are using for env var update to be recognized
5. Install VLC: https://www.videolan.org/
    * This is for playing test .wav files, Windows defaulted to Grove Music for me which made the files sound really distorted and made me think something was wrong.

6. `pip install opencv-python`


https://github.com/DanielSWolf/rhubarb-lip-sync
https://github.com/DanielSWolf/rhubarb-lip-sync/releases

"C:\bv\s\Rhubarb-Lip-Sync-1.11.0-Windows\rhubarb.exe" -o C:\bv\p\broken_news\src\output.json "C:\bv\p\broken_news\src\fish.wav" -f json


