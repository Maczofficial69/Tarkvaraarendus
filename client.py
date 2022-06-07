import socket

s = socket.socket()
host = input(str("Please enter the hostname of the server : ")) # prindib teksti kuhu pead sisestama serveri nime
port = 8080 # seab pordi
s.connect((host,port)) # connectib hosti ja portiga
print("Connected to chat server") # connectib chati serveriga
while 1:

    message = input(str(">> ")) # Tekitab sõnumi kirjutamise inputi
    message = message.encode() # encodeb sõnumi
    s.send(message) # saadab sõnumi
    print("message has been sent") # prindib teksti, et sõnum on saadetud
    print("")
    incoming_message = s.recv(1024) # Checkib sissetulevaid sõnumeid
    incoming_message = incoming_message.decode() # decodeb sissetuleva sõnumi
    print(" Client :", incoming_message) # näitab sõnumit ekraanil
    print("")
