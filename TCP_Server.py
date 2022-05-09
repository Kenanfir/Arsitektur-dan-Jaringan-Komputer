import socket
import sys

# Membuat TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Menggabungkan socket dengan address
server_address = ('localhost', 10010)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Mencari Client dengan address yang sama
sock.listen(1)

while True:
    # Menunggu koneksi dari Client
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Menerima data dari Client
        while True:
            data = connection.recv()
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Memberhentikan koneksi
        connection.close()
