import socket
import msvcrt
import select
import errno
import random
import rsa
import keyboard
import sys
HEADER_LENGTH = 15

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")
# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
client_socket.setblocking(False)
#client_socket.settimeout(2)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
usernam = my_username
li= rsa.rsa1()
publickey = str(li[2]) + str(0) + str(li[1])
#print(publickey)
username = (publickey + " " + usernam).encode('utf-8')
#pub = publickey.encode('utf-8')
#pub_header = f"{len(pub):<{HEADER_LENGTH}}".encode('utf-8')
#n case anyone else is wondering what the ":<5" syntax is for. It apparently pads the 
#string with spaces so the length is equal to the number on the right (5 in my example).
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')

client_socket.send(username_header + username)
#client_socket.send(pub_header + pub)
messa=None

while True:

 try:
        # Now we want to loop over received messages (there might be more than one) and print them
        

            # Receive our "header" containing username length, it's size is defined and constant
            username_header = client_socket.recv(HEADER_LENGTH)
            #pub_header = client_socket.recv(HEADER_LENGTH)
            # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            # Convert header to int value
            username_length = int(username_header.decode('utf-8').strip())

            # Receive and decode username
            username = client_socket.recv(username_length).decode('utf-8')
            publ = username.split(" ",1)[0]
           
            conne=None
            # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
            
            #dec_message= 
            # Print message
            
           # print()
             # Wait for user to input a message
            while True:
                try:
                    print("here")
                    #if keyboard.is_pressed('e'):
                    #    sys.stdout.flush()
                    messa = input(f'{my_username} > ')
                    
                    if conne == "exchanged":
                        messa = rsa.encrypt(publ,messa)
                    #print(f'{username} > {messa}')
                    if messa:

                # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
                            messa = messa.encode('utf-8')
                            message_header = f"{len(messa):<{HEADER_LENGTH}}".encode('utf-8')
                #print(message_header)
                            client_socket.send(message_header + messa)
                           #messa = None
           # messag = rsa.encrypt(li[1],li[2],messa)
                    message_header = client_socket.recv(HEADER_LENGTH)
                    if not len(message_header):
                        continue
                    message_length = int(message_header.decode('utf-8').strip())
                    message = (client_socket.recv(message_length).decode('utf-8')).strip()
                    messag = message.split(" " , 1)
                    if(len(messag)==2):
                      if ord(messag[1][0])>=65:
                        if ord(messag[0][1])<=57 and  ord(messag[0][2])<=57:
                        
                            if messag[1] != my_username:
                             username = messag[1]
                             publ=messag[0]
                    if conne == "exchanged":
                       # mes = ""
                        #for i in messag:
                         #   mes =  mes + " " + i
                        if(ord(message[0])<=57 and ord(message[len(message)-1])<=57):
                            me=message.split(" ")
                            messaa= rsa.decrypt(li[0],li[1],me)
                            print(f'{username} > {messaa}')
                    conne= "exchanged"

                except IOError as e:
                    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                        print('Reading error: {}'.format(str(e)))
                        sys.exit()

        # We just did not receive anything
                    continue
    # If message is not empty - send it
            
 except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

 except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: {}'.format(str(e)))
        sys.exit()