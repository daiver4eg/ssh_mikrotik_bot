import paramiko
import clear_data
from config import USER
from config import SECRET


def mikrotik_request(host, ssh_command_to_device):
    wifi_key = ""
    #user = ''
    #secret = ''

    port = 22
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Подключение
    print("connecting...")
    try:
        client.connect(hostname=host, username=USER, password=SECRET, port=port)
    except Exception as e:
        # Обработка ошибки
        print("Произошла ошибка:", e)
        return "Произошла ошибка, не могу установить соединение" + "\n"
    # Выполнение команды
    print("receive data")
    stdin, stdout, stderr = client.exec_command(ssh_command_to_device)
    # Читаем результат
    data = stdout.read() + stderr.read()
    client.close()

    print("что мы получили от роутера:", data)
    #Если строка условно пустая, то будем считать успех
    try:
        if data == b'\r\n\r\n\r\n' or data== b'\r\n' or data == b'':
            print("test")
            return "Success" + "\n"

    except Exception as e:
        # Обработка ошибки
        print("Произошла ошибка:", e)
        return "Произошла ошибка" + "\n"
    return "Command was send to device" + "\n"




