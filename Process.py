import socket
import argparse
import time


class Process:
    HOST = '127.0.0.1'
    is_coordinator = False

    def __init__(self, id_, is_coordinator, port):
        self.id_ = id_
        self.label = f"P{id_}"
        self.is_coordinator = is_coordinator
        self.port = port

    def make_coordinator(self):
        self.is_coordinator = True

    def undo_coordinator(self):
        self.is_coordinator = False

    def processMessages(self, message):
        if message == "here?":
            return "yes"

    def join(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _socket:
            _socket.bind((Process.HOST, self.port))
            _socket.listen()
            print(f'Node {self.id_} has been created on PORT {self.port}')
            while True:
                con, _ = _socket.accept()
                with con:
                    message = con.recv(2048).decode('utf-8').rstrip('\n')

                    if message == 'bye':
                        print(f'Node {self.id_}: I am going out..')
                        break
                    response = self.processMessages(message)

                    con.send(response.encode('utf-8'))


if __name__ == '__main__':
    print("Process file is running")
    parser = argparse.ArgumentParser(description="Create a new process")
    parser.add_argument('--id', type=int, help='Id of the node')
    parser.add_argument('--port', type=int, help='Port of the node')
    parser.add_argument('--isCoordinator', type=str, help='Is it coordinator?')
    args = parser.parse_args()
    node = Process(
        args.id, args.isCoordinator, args.port)
    node.join()
