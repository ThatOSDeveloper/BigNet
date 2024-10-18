#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 4096

void clear_console() {
    printf("\033[H\033[J"); // ANSI escape code for clearing console
}

void fetch_page(char *server_ip) {
    int sock = 0;
    struct sockaddr_in serv_addr;
    char buffer[BUFFER_SIZE] = {0};

    // Create socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("Socket creation error\n");
        return;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert server IP to binary form and connect
    if (inet_pton(AF_INET, server_ip, &serv_addr.sin_addr) <= 0) {
        printf("Invalid address / Address not supported\n");
        return;
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        printf("Connection failed\n");
        return;
    }

    // Receive the page content
    int valread = read(sock, buffer, BUFFER_SIZE);
    printf("Received content:\n%s\n", buffer);

    close(sock);
}

int main() {
    char server_ip[100];
    char action[10];

    printf("Enter the server IP address: ");
    scanf("%s", server_ip);

    while (1) {
        clear_console();

        // Fetch and display the page content
        fetch_page(server_ip);

        // Prompt user for the next action
        printf("\nEnter 'exit' to quit, 'change' to change server IP, or press Enter to fetch the page again: ");
        fgets(action, sizeof(action), stdin);  // Consume the newline
        fgets(action, sizeof(action), stdin);

        if (strcmp(action, "exit\n") == 0) {
            break;
        } else if (strcmp(action, "change\n") == 0) {
            printf("Enter the new server IP address: ");
            scanf("%s", server_ip);
        }
    }

    return 0;
}
