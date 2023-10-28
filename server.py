# I am blackout drunk Alex B
# 10/26/23
# Get Fucked You Useless Clowns

import http.server
import socket
from _thread import *
import ssl

server = "192.168.0.108"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Khorne demands blood for the blood god
try:
    s.bind((server,port))

except socket.error as e:
    str(e)

s.listen(4)

print("Waiting for other Users...Server Started.")

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""

    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected.")
                break
            else :
                print("Recieved: ", reply)
                print("Sending : ", reply)
            conn.sendall(str.encode(reply))
        except :
            break

        print("Lost Connection.")
        conn.close()


while True:
    # accept incoming connections and record address
    conn, addr = s.accept()
    print("connected to:", addr)

    start_new_thread(threaded_client, (conn,))

#
# server_address = ("0.0.0.0", 80)
# httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
# httpd.socket = ssl.wrap_socket(httpd.socket,
#                                server_side=True,
#                                certfile="certificate.crt",
#                                keyfile="private.key",
#                                ssl_version=ssl.PROTOCOL_TLS)
# httpd.serve_forever()