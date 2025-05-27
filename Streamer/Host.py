import socket
import cv2
import numpy as np
import mss
import time
from turbojpeg import TurboJPEG

jpeg = TurboJPEG(lib_path=r"C:\libjpeg-turbo-gcc64\bin\libturbojpeg.dll")

HOST = '0.0.0.0'
PORT = 9999
RESOLUTION = (1920, 1080)
FPS = 60

def capture_and_stream():
    sct = mss.mss()
    monitor = sct.monitors[1]

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[*] Waiting for client on {HOST}:{PORT}...")
    conn, addr = server.accept()
    print(f"[+] Connected to {addr}")

    frame_delay = 1 / FPS
    while True:
        start = time.time()
        img = sct.grab(monitor)
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        frame = cv2.resize(frame, RESOLUTION)
        encoded = jpeg.encode(frame, quality=80)

        size = len(encoded).to_bytes(4, byteorder='big')
        try:
            conn.sendall(size + encoded)
        except:
            break

        elapsed = time.time() - start
        sleep = frame_delay - elapsed
        if sleep > 0:
            time.sleep(sleep)

if __name__ == "__main__":
    capture_and_stream()
