import socket
import cv2
import numpy as np

HOST = 'MAIN PC IPv4 Address HERE' 
PORT = 9999

def receive_stream():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print(f"[+] Connected to server {HOST}:{PORT}")

    while True:
        size_bytes = sock.recv(4)
        if not size_bytes:
            break
        size = int.from_bytes(size_bytes, byteorder='big')
        buffer = b''
        while len(buffer) < size:
            data = sock.recv(size - len(buffer))
            if not data:
                return
            buffer += data

        np_arr = np.frombuffer(buffer, dtype=np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        cv2.imshow("LAN Stream", frame)
        if cv2.waitKey(1) == 27:
            break

    sock.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    receive_stream()
