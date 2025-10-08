#openssl req -x509 -out localhost.crt -keyout localhost.key -newkey rsa:2048 -nodes -sha256 -subj /CN=localhost
# it will create a certificate and a key file
# add them in a folder where client and server code is and run the server code first and then the client code
# Web Security with SSL/TLS: Server Code
import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="localhost.crt", keyfile="localhost.key")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("", 4434))
    server.listen(5)
    print("Server ready and listening for connections")

    # Wait for new connections in a loop
    while True:
        sock, address = server.accept()
        print("New connection from", f"{address[0]}:{address[1]}")

        # Wrap socket with ssl
        ssl_sock = context.wrap_socket(sock, server_side=True)

        while True:
            data = ssl_sock.recv(1024)
            # Decode byte array to utf-8 string
            decoded = data.decode('utf-8')
        
            # Close the socket if the sock sends empty bytes
            if decoded == "":
                break
            # Log what the sock sends
            print(f"[{address[0]}:{address[1]}] {decoded}")
            
            # Echo the data back to the sock
            ssl_sock.sendall(data)
        
        # Gracefully close the connection and wait for next one
        print("Closing connection with", f"{address[0]}:{address[1]}")
        ssl_sock.close()