import websocket
from threading import Thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print('### closed ###')

def on_open(ws): 
    def run(*args): 
        for i in range(3): 
            time.sleep(1) 
            ws.send("Hello {}".format(i)) 
        time.sleep(1) 
        ws.close() 
        print("thread terminating...") 
    
    Thread(target=run).start()

if __name__=='__main__':
    ws = websocket.WebSocketApp('ws://localhost:8080/start/echo',
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
    
    ws.run_forever()    # 이벤트 처리 루프 -close되면 리턴
