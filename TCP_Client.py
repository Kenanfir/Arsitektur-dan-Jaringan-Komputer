import socket
import sys

# Membuat TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect ke server pada saat server listen
server_address = ('localhost', 10010)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Mengirim data ke server
    message = 'New Message'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Mencari respon dari server
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv()
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
