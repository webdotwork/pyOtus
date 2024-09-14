import socket
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs


# Функция для получения сообщения статуса HTTP
def get_http_status_message(status_code):
    try:
        status = HTTPStatus(status_code)
        return f"{status.value} {status.phrase}"
    except ValueError:
        return "200 OK"


def handle_client(client_socket):
    # Получаем запрос от клиента
    request_data = client_socket.recv(1024).decode('utf-8')

    # Разбираем строку запроса (Request-Line)
    request_lines = request_data.splitlines()
    if len(request_lines) > 0:
        request_line = request_lines[0]
    else:
        return

    # Разбираем метод, путь и HTTP-версию
    method, path, _ = request_line.split()

    # Парсим путь и параметры запроса
    parsed_url = urlparse(path)
    query_params = parse_qs(parsed_url.query)

    # Получаем статус из параметра status
    status_code = query_params.get('status', ['200'])[0]
    try:
        status_code = int(status_code)
    except ValueError:
        status_code = 200

    # Получаем сообщение для статуса
    status_message = get_http_status_message(status_code)

    # Формируем тело ответа
    response_body = [
        f"Request Method: {method}",
        f"Request Source: {client_socket.getpeername()}",
        f"Response Status: {status_message}",
    ]

    # Добавляем заголовки запроса в тело ответа
    for header in request_lines[1:]:
        if header:
            response_body.append(header)

    # Создаем тело ответа в виде строки
    response_body_text = "\r\n".join(response_body)

    # Формируем HTTP ответ
    response = (
            f"HTTP/1.1 {status_message}\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {len(response_body_text)}\r\n"
            "Connection: close\r\n\r\n"
            + response_body_text
    )

    # Отправляем ответ клиенту
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()


def start_server(host='127.0.0.1', port=5000):
    # Создаем серверный сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server running on http://{host}:{port}")

    while True:
        # Принимаем входящее соединение
        client_socket, addr = server_socket.accept()
        handle_client(client_socket)


if __name__ == "__main__":
    start_server()
