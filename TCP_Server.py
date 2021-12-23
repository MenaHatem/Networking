from socket import socket 
from re import findall
from uuid import getnode
from random import choice


def algorithm_TCP ():

    application_type = ["HTTP" , "FTP" , "SMTP"]

    server = socket()
    host = ""
    port = 12345
    server.bind((host, port))
    server.listen(4)
    print ("Socket server listening...")
    connection , address = server.accept()
    
    while True:
   
        client_mac = ':'.join(findall('..', '%012x' % getnode())).upper()

        print ("IP Address:" , address[0])
        print ("Client's MAC Address:" , client_mac)
        print ("Protocol is TCP")
        print ("Port address:" , address[1])
        print ("Application type:" , choice(application_type))

        connection.close()
        break 