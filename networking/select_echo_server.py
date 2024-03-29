import select
import socket
import sys
import queue

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address), file=sys.stderr)
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

# Sockets from which we expect to read
inputs = [server]

# Socket to which we expect to write
outputs = []

# Outgoing message queues (socket:Queue)
message_queue = {}

while inputs:
    # Wait for at least one of the sockets to be
    # ready for processing
    print('waiting for the next event', file=sys.stderr)
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    # Handle inputs
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print('connection from', client_address, file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            # Give the connection a queue for data
            # we want to send
            message_queue[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data
                print('received {!r} from {}'.format(
                    data,s.getpeername()),file=sys.stderr)
                message_queue[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpret empty result as closed connection
                print('closing', client_address, file=sys.stderr)
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # Remove message queue
                del message_queue[s]

    # Handle outputs
    for s in writeable:
        try:
            next_msg = message_queue[s].get_nowait()
        except queue.Empty:
            # No message waiting, so stop checking
            # for writability
            print('',s.getpeername(),'queue empty',
                file=sys.stderr)
            outputs.remove(s)
        else:
            print('sending {!r} to {}'.format(next_msg, s.getpeername()), file=sys.stderr)
            s.send(next_msg)
        # Handle "exceptional condititions"
        for s in exceptional:
            print('exception condition on', s.getpeername(), file=sys.stderr)
            # Stop listening for input on the connection
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            # Remove message queue
            del message_queue[s]
