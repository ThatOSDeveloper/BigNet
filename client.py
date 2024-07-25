import socket
import re
from os import system, name
# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def fetch_page(ip, path, port=8080):
    # Create a socket object and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    
    # Send an HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {ip}\r\n\r\n"
    client_socket.sendall(request.encode())
    
    # Receive the response from the server
    response = client_socket.recv(4096).decode()
    
    # Extract the plain text from the HTTP response
    headers, body = response.split("\r\n\r\n", 1)
    
    # Close the connection
    client_socket.close()
    
    return body

def extract_links(text):
    # Simple link extraction from plain text
    links = re.findall(r'http://[^\s]+', text)
    return links

if __name__ == "__main__":
    ip = input("Enter the server IP address: ")
    
    while True:
        # Fetch and display the page data
        body = fetch_page(ip, '/')
        clear()
        # Print the page content directly
        print(body)
        
        # Extract and display links
        links = extract_links(body)
        if links:
            print("\nExtracted links:")
            for link in links:
                print(link)
        
        # Prompt user for next action
        action = input("\nEnter 'exit' to quit or press Enter to fetch the page again: ")
        if action.lower() == 'exit':
            break
