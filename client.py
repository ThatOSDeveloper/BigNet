import socket
import re
from os import system, name

# Define our clear function
def clear():
    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For mac and Linux (here, os.name is 'posix')
    else:
        _ = system('clear')

def fetch_page(ip, port=8080):
    # Create a socket object and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    
    # No HTTP request needed, just receive the raw text
    response = client_socket.recv(4096).decode()
    
    # Close the connection
    client_socket.close()
    
    return response

if __name__ == "__main__":
    ip = input("Enter the server IP address: ")
    
    while True:
        # Fetch and display the page data
        body = fetch_page(ip)
        clear()
        # Print the page content directly
        print(body)
        
        # Prompt user for next action
        action = input("\nEnter 'exit' to quit, Enter 'change' to change server IP, press Enter to fetch the page again: ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'change':
            ip = input("Enter the new server IP address: ")
