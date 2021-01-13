import socket
import sys

if __name__ == "__main__":
    serverIp, serverPort = "localhost", 9999 #Server
    clientIp, clinetPort = "localhost", 9998
    message = "hello world"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((clientIp,clinetPort)) #Client
        sock.connect((serverIp,serverPort)) #연결 요청

        #송신
        sbuff = bytes(message, encoding='utf-8') #스트림
        sock.send(sbuff) #송신
        print("송신 메세지 : {}".format(message))
        #수신
        rbuff = sock.recv(1024)
        receive = str(rbuff,encoding='utf-8')
        print("수신 메세지 : {}".format(receive))

#실행방법
#python .\17.Client.py
