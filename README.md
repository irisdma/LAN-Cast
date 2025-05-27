# 💻 LAN-Cast

Fast Screen Sharing Over LAN built for Gamers 💻→💻
LAN Cast lets you mirror your PC screen to another device (like a laptop) over your local network - with **super low latency and up to 240 FPS**.

## ⚡ Features

- 🖥️ **Real time screen sharing** over LAN
- 🧠 **Low latency (< 50ms)** using raw sockets + TurboJPEG
- 🎮 **High frame rate** (up to 240 FPS on good hardware)
- ☁️ Lightweight - no bloat, no browser overhead
- 🔌 Completely offline (P2P only)

## 🛠️ How It Works

- Your **main PC** (server) captures the screen and encodes it using TurboJPEG.
- It streams the frames directly to your **laptop** (client) over TCP.
- The laptop displays the stream in real-time using OpenCV.

## 🚀 Setup Instructions

### ⚙ 1. Requirements (on required devices)
- LANClient to Viewing PC, LANStreamer to Main PC
- **Python 3.9+** (Tested on 3.11)
- All Inluded Install Packages (Python Libraries + libjpeg-turbo-3.1.0-gcc64)

### 🎇 2. Essential Setup

### 💻 Host PC
1. After installing the packages on each required device, run host.py on main PC
2. On main PC, open a CMD prompt and run "ipconfig"
3. Copy the IPv4 and edit client.py, and replace the host with the new client ip
### 💻 2nd PC
1. Transfer client.py to 2nd PC
2. Now set any other settings you would like and run client.py

**If all followed correclty, you should now have a full screenshare on your 2nd PC over LAN**

# 🎯 Performance Tips
Use Ethernet instead of Wi-Fi for better latency

Lower resolution in server.py for faster encode:
EX:) RESOLUTION = (960, 540)

Reduce JPEG quality to 70 for better speed:
EX:) encoded = jpeg.encode(frame, quality=70)
