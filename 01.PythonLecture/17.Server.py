import socketserver
import sys
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("client addr : {0}".format(self.client_address[0]))
        sock = self.request
        #수신
        rbuff = sock.recv(1024).strip()
        receive = str(rbuff,encoding='utf-8')
        print("수신 메세지 : {}".format(receive))

        #송신
        receive = receive + " OK!"
        sbuff = bytes(receive, encoding='utf-8') #스트림
        sock.send(sbuff)
        print("송신 메세지 : {}".format(receive))
        sock.close()

if __name__ == "__main__":
    bindIp, bindPort = "localhost", 9999

    with socketserver.TCPServer((bindIp, bindPort), MyTCPHandler) as server:
        print("Server Start!!")
        server.serve_forever()

#실행방법
#python .\17.Server.py
