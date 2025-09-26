# import socket module
from socket import *
# In order to terminate the program
import sys

FORMAT = "UTF-8"

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen() #1
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #2
    
    try:
      message = connectionSocket.recv(1024).decode(FORMAT)
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "rb") #4
      
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
      outputdata = b"HTTP/1.1 200 OK\r\n"        
      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
      outputdata += b"Connection: close\r\n"
      outputdata += b"Server: webserver\r\n"
      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      outputdata += b"\r\n"

      #Fill in end
               
      for i in f: #for line in file - append your html file contents to output data
        #Fill in start 
        outputdata += i
        #Fill in end 
      
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start
      connectionSocket.sendall(outputdata)
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      body = b"<html><body><h1>404 Not Found</h1><body></html>" #Declare body because we are not reading file

      status404 = b"HTTP/1.1 404 Not Found\r\n"
      conType = b"Content Type: text/html; charset=UTF-8\r\n"
      conLength = b"Content Length: " + str(len(body)).encode(FORMAT) + b"\r\n" #no need for content length in 200 ok. 
      connectionEnd = b"Connection: close\r\n"
      serverName = b"Server: webserver\r\n"

      response = status404 + conType + conLength + connectionEnd + serverName + b"\r\n" + body 

      connectionSocket.sendall(response)


      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
