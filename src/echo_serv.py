import socket
import sys
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs


def get_http_status_message(status_code):
    try:
        status = HTTPStatus(status_code)
        return f"{status.value} {status.phrase}"
    except ValueError:
        return "200 OK"


def handle_client_connection(client_socket):
    request = client_socket.recv(1024).decode()
    headers = request.split("\r\n")

    if len(headers) > 0:
        # Get the request line
        request_line = headers[0]
        method, path, _ = request_line.split()

        # Parse URL parameters
        parsed_url = urlparse(path)
        query_params = parse_qs(parsed_url.query)
        status_code = query_params.get('status', ['200'])[0]

        try:
            status_code = int(status_code)
        except ValueError:
            status_code = 200

        response_status = get_http_status_message(status_code)

        # Build response headers and body
        response_headers = [
            "HTTP/1.1 " + response_status,
            "Content-Type: text/plain",
            "Content-Length: " + str(len(request)),
            "Connection: close",
        ]

        response_body = [
            f"Request Method: {method}",
            f"Request Source: {client_socket.getpeername()}",
            f"Response Status: {response_status}",
        ]

        for header in headers:
            if header and not header.startswith('GET') and not header.startswith('HTTP'):
                response_body.append(header)

        response = "\r\n".join(response_headers) + "\r\n\r\n" + "\n".join(response_body)

        client_socket.sendall(response.encode())
    client_socket.close()


def start_server(host='127.0.0.1', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server running on http://{host}:{port}/")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            handle_client_connection(client_socket)
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()
