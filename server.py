import socket
import sys
import time

s = socket.socket()
host = socket.gethostname() #Seab hosti nime milleks on arvuti nimi
print("server will start on host:", host) # Prindib teksti, mis hostil server alustab
port = 8080 # Seab pordiks 8080
s.bind((host, port)) # Host ja port määratud
print("")
print("Server done binding to host and port successfully") # Prindib teksti
print("")
print("Server is waiting for incoming connections")#Prindib teksti
print("")
s.listen(1)# listenib
conn, addr = s.accept() #connection seatakse socketile
print(addr, "Has connected to the server and is now online") # prindib teksti, et on connectitud
print("")
while 1:
    message = input(str(">> ")) # Tekitab sõnumi kirjutamise inputi
    message = message.encode() # encodeb sõnumi
    conn.send(message) # saadab sõnumi
    print("message has been sent") # prindib teksti, et sõnum on saadetud
    print("")
    incoming_message = conn.recv(1024) # Checkib sissetulevaid sõnumeid
    incoming_message = incoming_message.decode() # decodeb sissetuleva sõnumi
    print(" Client :", incoming_message) # näitab sõnumit ekraanil
    print("")