import socket
import threading

# قائمة لتخزين الرسائل المستلمة
logs = []

def start_syslog_server(host='0.0.0.0', port=515):
    # إنشاء سوكت جديد للاستماع على TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Listening for syslog messages on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8').strip()
            if message:
                print(f"Received message: {message}")
                logs.append(message)  # تخزين الرسالة في القائمة
        except:
            break
    client_socket.close()
