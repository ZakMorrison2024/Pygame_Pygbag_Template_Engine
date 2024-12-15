import socket
import threading
import random

# Function to handle each client
def handle_client(client_socket, client_address, client_choices):
    try:
        # Receive choice from the client
        choice = client_socket.recv(1024).decode()
        print(f"Player {client_address} chose {choice}")
        #client_choices[client_address] = choice

        if len(client_choices) == 2:
            # Determine the result after both players have made their choice
            player1_choice = client_choices[list(client_choices.keys())[0]]
            player2_choice = client_choices[list(client_choices.keys())[1]]

            # Determine the winner
            result = get_winner(player1_choice, player2_choice)

            # Send result back to both players
            for client in client_choices.keys():
                client_socket.send(result.encode())

            # Reset game state for the next round
            client_choices.clear()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

# Setting up the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(2)
    print("Server listening on port 5555...")

    client_choices = {}

    while True:
        client_socket, client_address = server.accept()
        print(f"Player connected from {client_address}")
        threading.Thread(target=handle_client, args=(client_socket, client_address, client_choices)).start()

if __name__ == "__main__":
    start_server()

################## client

# Function to send choice to server
def send_choice(choice):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 5555))
            s.send(choice.encode())
            result = s.recv(1024).decode()
            return result
    except Exception as e:
        return "Error: Unable to connect to server."

        if result:
            result_text = FONT.render(result, True, RED)

if __name__ == "__main__":
    game_loop()
