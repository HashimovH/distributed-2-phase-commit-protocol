import socket
import subprocess
import os


def send_message(message, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.settimeout(1)
        try:
            sc.connect(('127.0.0.1', port))
        except:
            return ''

        sc.send(message.encode('utf-8'))
        r_msg = sc.recv(2048).decode('utf-8')
        return r_msg


def create(id_, is_coordinator, port, value):
    python_run_command = 'py Process.py --id {} --port {} --isCoordinator {} --value {}'.format(
        id_, port, is_coordinator, value)
    subprocess.Popen(python_run_command, shell=True, stdout=subprocess.PIPE)
