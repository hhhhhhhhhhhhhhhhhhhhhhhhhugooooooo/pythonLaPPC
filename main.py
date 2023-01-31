import threading
import random
import multiprocessing
import time
import signal
import os
import socket
import sysv_ipc
class DataEchange():
    def __init__(self, pid, quantite,message):
        self.pid=pid
        self.quantite =quantite 
        self.message=message
# Create a Python script that simulates an energy-producing and consuming home

def Home(production_rate, consumption_rate, trade_policy,socket_number,queue,surplus,a,b,c):
    surplus=calculate_surplus(production_rate,consumption_rate)
    time.sleep(1)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 10000))
    data = f"{a} {b} {c}"
    client.sendall(data.encode())
    print(f"Sent: {data}")
    client.close()
    trade_energy(trade_policy,surplus)

def trade_energy(trade_policy,surplus):
    if(surplus>10):
        print(trade_policy)
    pass

        
def calculate_surplus(production_rate,consumption_rate):
    return production_rate - consumption_rate
         
         
def Market(initial_price, temperature,ensoleillement,temp_change,duration,upDown):
    signal.signal(signal.SIGINT, HiverVolcanique)
    signal.signal(signal.SIGUSR1, GulfWar)
    signal.signal(signal.SIGUSR2, Siberia)
    signal.signal(signal.SIGALRM, RetourNormal)
    print('salut')
    t=External()
    threadh1=threading.Thread(target=communicate_with_h1)
    threadh2=threading.Thread(target=communicate_with_h2)
    threadh3=threading.Thread(target=communicate_with_h3)
    threadh1.start()
    threadh2.start()
    threadh3.start()
    threadh1.join()
    threadh2.join()
    threadh3.join()
    while True:
        t.run()
         



def HiverVolcanique():
    print("Hiver Volcanique")
    exit(0)
    
def GulfWar():
    print("Received SIGUSR1. Outputting data to output1.txt...")
    update_price(50)
    #print(self.price)
    with open('output1.txt', 'w') as f:
        f.write('Data outputted by SIGUSR1')

def Siberia():
    #temp.duration =20
        #temp.temp_change = 3
        #temp.upDown = -1
        #temp.ensoleillement = 0.01
    print("Received SIGUSR2. Outputting data to output2.txt...")

def RetourNormal():
    #temp.duration =5
        #temp.temp_change = 2
        #temp.ensoleillement = 0.5
        #temp.temperature = 22
    print("Received SIGUSR2. Outputting data to output2.txt...")        

def update_price( transaction_amount, lock):
    # acquire lock to prevent multiple transactions from happening simultaneously
    lock.acquire()
    price += transaction_amount
    lock.release()
        
        
    
def communicate_with_h1():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 10000))
    server.listen()
    client, address = server.accept()
    print(f"Connected to {address}")
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        a, b, c = map(int, data.split())
        print(f"Received: {a=} {b=} {c=}")    
    client.close()    
def communicate_with_h2():
    print('test')
    pass
def communicate_with_h3():
    print('test')
    pass


def Weather(temperature,ensoleillement,temp_change,duration,upDown):
    while True:
        update_temperature(duration,temperature,upDown,temp_change)
        update_ensoleillement(ensoleillement)  
        #print(self.temperature.value)
        #print(self.ensoleillement.value)
        time.sleep(1)  

def update_temperature(duration,temperature,upDown,temp_change):
    if duration.value>=0:
        duration.value-=1
        temperature.value += upDown.value*int(temp_change.value*random.randrange(0,10)/10)
    else:
        upDown.value=random.choice([-1, 1])
        duration.value = random.randrange(3,7)
        temperature.value+= upDown.value*int(temp_change.value*random.randrange(0,10)/10)
def update_ensoleillement(ensoleillement):
    a= random.randrange(-10,10)/100
    if a+ensoleillement.value >=1:
        ensoleillement.value=1
    elif a+ensoleillement.value <=0:
        ensoleillement.value=0   
    else:
        ensoleillement.value+=a     


def External():
    time.sleep(1)
    r=random.randrange(0,1000)
    if r<1:
        os.kill(os.getppid(), signal.SIGINT)
    elif r<31:
        os.kill(os.getppid(), signal.SIGUSR2)
    elif r<81:
        os.kill(os.getppid(), signal.SIGALRM)
    elif r<901:
        os.kill(os.getppid(), signal.SIGUSR1)
    else:
        pass    
               
if __name__=='__main__':
    temperature = multiprocessing.Value('i', 22)
    ensoleillement = multiprocessing.Value('d', 0.5)
    temp_change = multiprocessing.Value('i', 2)
    duration = multiprocessing.Value('i', 4)
    upDown = multiprocessing.Value('i', -1)
    time.sleep(1)
    queue=sysv_ipc.MessageQueue()
    m = multiprocessing.Process(target=Market, args=(10,temperature,ensoleillement,temp_change,duration,upDown))
    p=multiprocessing.Process(target=Weather,args=(temperature,ensoleillement,temp_change,duration,upDown))
    h1=multiprocessing.Process(target=Home,args=(10,8,"always give",10000,queue,0,1,2,3))
    h1.start()
    m.start()
    p.start()
    m.join()
    p.join()
    h1.join()
    
