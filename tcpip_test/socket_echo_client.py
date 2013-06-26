import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    for i in range(0,3):
            nameList = [' ',' ',' ']
            nameList[i] = str(i)
            print >>sys.stderr, 'sending "%s"' % nameList[i]
            sock.sendall(nameList[i])

            # Look for the response
            amount_received = 0
            amount_expected = len(nameList[i])
    
            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
