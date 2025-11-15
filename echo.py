#tcp server in a process that handles multiple clients
#echos back the data the client sent

import logging
import multiprocessing
import select
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)

#server
def chatserver(ip, sort):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #adressfamilyIPV4, TCP socketstream
    logging.info(f'Binding to [{ip}, {port}]')
    server.bind((ip, port))
    server.setblocking(False)
    server.listen(100)
    logging.info(f'Listening to {ip}:{port}')

    readers = [server]

    while True:
        readable, writable, errored = select.select(readers, [], [], 0.5) #select a list to read from, write to, list of errors
        #for every run readable, loop
        for s in readable: #for socket in readable
            try:
                if s == server: #s is server socket
                    client.address = s.accept() #incoming connection
                    client.setblocking(False)
                    readers.append(client)
                    logging.info(f'Connection: {address}')
                else:
                    data = s.recv(1024) #receive data from client
                    if data: #no data
                        logging.info(f'Echo: {data}')
                        s.send(data) #see the data received
                    else:
                        logging.info(f'Remove: {s}')
                        s.close() #close socket
                        readers.remove(s) #remove from readers list
                        

            except Exception as ex:
                logging.warning(ex.args)


def main():
    #run server
    svr = multiprocessing.Process(target=chatserver, args=['localhost', 2067], daemon=True, name='Server') #daemon true means it will close when main process closes


    
if __name__ == "__main__":
    main()

            

