import socket

HOST = ''
PORT = 9009

def runServer():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock: #소켓 객체 생성
        sock.bind((HOST,PORT)) #서버ip 및 포트와 바인드
        sock.listen(1) #처리 가능한 연결 수 설정
        print('클라이언트 연결을 기다리는 중..')
        conn, addr = sock.accept() #클라이언트 요청을 기다리고 연결 요청이 오면 수락, tcp 소켓과 클라이언트 주소 리턴
        with conn:
            print('[%s]와 연결됨'%addr[0])
            while True:
                data = conn.recv(1024) #클라이언트 요청메시지 수신
                if not data:
                    break
                print('메시지 수신[%s]'%data.decode())
                conn.sendall(data) #클라이언트로 응답데이터 송신

runServer()