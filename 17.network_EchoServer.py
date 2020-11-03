import socketserver
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('클라이언트 접속 : {0}'.format(self.client_address[0]))
        sock = self.request
        
        # 데이터를 수신하고 그 결과를 rbuff에 담습니다.rbuff는 bytes형식임
        rbuff  = sock.recv(1024)
        received = str(rbuff, encoding="utf-8")
        print('수신 : {0}'.format(received))
        
        # 수신한 데이터를 그대로 클라이언트에게 다시 송신함.
        sock.send(rbuff)
        print('송신 : {0}'.format(received))
        sock.close()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('{0} <Bind IP>'.format(sys.argv[0]))
        sys.exit()
        
    bindIP = sys.argv[1]
    bindPort = 5425 #에코서버는 5425포트
    
    # IP, Port 번호를 담은 튜플과 baseRequestHandler의 파생 클래스인 
    # 클래스를 매개변수로 넘깁니다.
    server = socketserver.TCPServer((bindIP, bindPort), MyTCPHandler)
    
    print('메아리 서버 시작...')
    # 클라이언트로부터 접속 요청을 받아들일 준비를 합니다.
    server.serve_forever()