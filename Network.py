from Process import Process
from helper import create, send_message
from random import randint
from random import choice
import socket


class Network:
    current_port = randint(10000, 60000)
    node_list = []
    coordinator = None
    consistency_history = []

    def __init__(self, nodes, history):
        self.consistency_history = history
        for node in nodes:
            self.handleCreation(node[0], node[1])
            self.current_port += 1

    def handleCreation(self, id_, is_coordinator):
        # add each node to the network with Node class
        node_id = int(id_.replace("P", ""))
        # Create Node obj to store in the node_list
        node_obj = Process(node_id, is_coordinator, self.current_port)
        create(node_obj.id_, node_obj.is_coordinator, node_obj.port)

        reply = send_message("here?", node_obj.port)

        if reply == "yes":
            self.node_list.append(node_obj)
            if node_obj.is_coordinator:
                self.coordinator = node_obj

            print(
                f"Node {node_obj.label} has been created on PORT {self.current_port}")

    def process_command(self, command):
        message = ""
        return message
