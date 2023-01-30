import threading
import random
import multiprocessing
import time
import signal
import os
import socket
import pickle
# Create a Python script that simulates an energy-producing and consuming home
class DataEchange():
    def __init__(self, pid, quantite,message):
        self.pid=pid
        self.quantite =quantite 
        self.message=message



class Home(multiprocessing.Process):
    def __init__(self, production_rate, consumption_rate, trade_policy,socket_number, queue):
        self.a=production_rate
        self.production_rate = production_rate
        self.consumption_rate = consumption_rate
        self.trade_policy = trade_policy
        self.achat=0
        self.surplus = 0
        self.socket_number=socket_number
        self.queue=queue
        
    def receiveData(self):
        self.socket_number.recv(pickle.loads)
    def calculate_surplus(self):
        self.surplus = self.surplus+self.production_rate - self.consumption_rate
        
    def calculate_production_rate(self):
        self.receiveData()
        self.production_rate=self.a*(2*ensoleillement)
        pass
		
        
    def calculate_consumption_rate(self):
        self.receiveData()
        self.consuption_rate=self.consumption_rate+(22-temperature)*0.5
        
    def trade_energy(self):
        objettemp2=self.queue.recv()

        if self.trade_policy == "always give":
            # give away surplus energy to other homes
            # give consumption_rate/10
            echangetemp=DataEchange(0,0,"Anyone in need ?")
            self.queue.send(echangetemp)
            time.sleep(1)
            if (objettemp2.message=="Anyone in need ?" and self.surplus<self.production_rate/10):
                echangetemp=DataEchange(os.getpid(),0,"")
                self.queue.send(echangetemp)
                time.sleep(1)
                if ( self.surplus>self.consumption_rate/5):
                 #get pid of the process that sent the message
                    echangetemp=DataEchange(objettemp2,self.consumption_rate/10,"")
                    self.queue.send(echangetemp)				#mutex lock à mettre ici pour protéger le changement de la valeur surplus
                    self.surplus=self.surplus-self.consumption_rate/10
            # calls queue to listen for givers (if surplus<production_rate/10)
                time.sleep(1)
                if(type(objettemp2)==DataEchange):
                    if(objettemp2.pid==self.getpid()):
                        self.cunsumption_rate+=objettemp2.quantite
				#if no givers use socket to buy
                time.sleep(1)
        elif self.trade_policy == "always sell":
            # sell surplus energy to the market
            # sell consumption_rate/10
            self.sellToMarket(self.consumption_rate/10)
            if (objettemp2.message=="Anyone in need ?" and self.surplus<self.production_rate/10):
                echangetemp=DataEchange(os.getpid(),0,"")
                self.queue.send(echangetemp)
            time.sleep(1)
            if(type(objettemp2)==DataEchange):
                if(objettemp2.pid==self.getpid()):
                    self.cunsumption_rate+=objettemp2.quantite
				#if no givers use socket to buy
            time.sleep(1)
            # does not call queue for takers (as it always sells)
				#therefore sell using socket
            # calls queue to listen for givers(if surplus<prodution_rate/10)
				#if no givers use socket to buy
        elif(self.trade_policy=="sell if no takers"):
            echangetemp=DataEchange(0,0,"Anyone in need ?")
            self.queue.send(echangetemp)
            time.sleep(1)
            if (objettemp2.message=="Anyone in need ?" and self.surplus<self.production_rate/10):
                echangetemp=DataEchange(os.getpid(),0,"")
                self.queue.send(echangetemp)
                time.sleep(1)
                if ( self.surplus>self.consumption_rate/5):
                 #get pid of the process that sent the message
                    echangetemp=DataEchange(objettemp2,self.consumption_rate/10,"")
                    self.queue.send(echangetemp)				#mutex lock à mettre ici pour protéger le changement de la valeur surplus
                    self.surplus=self.surplus-self.consumption_rate/10
            # calls queue to listen for givers (if surplus<production_rate/10)
                time.sleep(1)
                if(type(objettemp2)==DataEchange):
                    if(objettemp2.pid==self.getpid()):
                        self.cunsumption_rate+=objettemp2.quantite
				#if no givers use socket to buy
                time.sleep(1)
            else:
                self.sellToMarket(self.consumption_rate/10) 

            # if not, sell to the market
            # trade consumption_rate/10
            # calls queue to ask for takers (if no takers sell)
				#therefore sell using socket
            # calls queue to listen for givers (if surplus<production_rate/10)
				#if no givers use socket to boy
            
    def sellToMarket(amountSold):
		#sells some energy to the market
        print(amountSold)
        pass

    def run(self):
        while True : 
            if (self.surplus > self.consumption_rate/5 or self.surplus<self.production_rate/10):
                self.trade_energy()
            self.calculate_surplus()
			
		


class Market(multiprocessing.Process):
    def __init__(self, initial_price,temperature,temp_change,ensoleillement,upDown, duration,sock1,sock2,sock3):
        super().__init__()
        self.stock=10
        self.price = initial_price
        self.temperature = multiprocessing.Value('d', 0.0)
        self.ensoleillement = multiprocessing.Value('i', 0)
        signal.signal(signal.SIGINT, self.HiverVolcanique)
        signal.signal(signal.SIGUSR1, self.GulfWar)
        signal.signal(signal.SIGUSR2, self.Siberia)
        signal.signal(signal.SIGALRM, self.RetourNormal)
        self.sock1=sock1
        self.sock2=sock2
        self.sock3=sock3

    def HiverVolcanique(self, signum, frame):
        print("cheh")
        exit(0)
    
    def GulfWar(self, signum, frame):
        print("Received SIGUSR1. Outputting data to output1.txt...")
        self.update_critical_data(0,0,0,50)
        with open('output1.txt', 'w') as f:
            f.write('Data outputted by SIGUSR1')

    def Siberia(self, signum, frame):
        #temp.duration =20
            #temp.temp_change = 3
            #temp.upDown = -1
            #temp.ensoleillement = 0.01
        print("Received SIGUSR2. Outputting data to output2.txt...")

    def RetourNormal(self, signum, frame):
        #temp.duration =5
            #temp.temp_change = 2
            #temp.ensoleillement = 0.5
            #temp.temperature = 22
        print("Received SIGUSR2. Outputting data to output2.txt...")        

    def update_critical_data(self, transaction_amount, energy_sold,internal_factors,external_factors):
        # acquire lock to prevent multiple transactions from happening simultaneously
        self.transactions_lock.acquire()
        self.stock=self.stock-energy_sold
        self.price=0.99*self.price+internal_factors+external_factors
        self.transactions_lock.release()
        
    def run(self):
        threadh1=threading.Thread(target=self.communicate_with_h1)
        threadh2=threading.Thread(target=self.communicate_with_h2)
        threadh3=threading.Thread(target=self.communicate_with_h3)
        threadh1.start()
        threadh2.start()
        threadh3.start()
		
        print('salut')
        t=External()
        t.start()
        threadh1.join()
        threadh2.join()
        threadh3.join()
        t.join()
        print("wesha laure")
        while True:
            time.sleep(1)
            pass
    def communicate_with_h1(self):
        self.sock1.send(pickle.dumps(self.price,self.ensoleillement,self.temperature))   #bonne syntaxe à utiliser, même si je ne sais pas pourquoi il y a un problème à la ligne 162
        (price_given,ensol_given,temp_given)=pickle.loads(self.sock1.recv(10000))
    def communicate_with_h2(self):
        self.sock2.send(pickle.dumps(self.price), pickle.dumps(ensoleillement),pickle.dumps(temperature))
        self.sock2.recv(pickle.loads)
    def communicate_with_h3(self):
        self.sock3.send(pickle.dumps(self.price), pickle.dumps(ensoleillement),pickle.dumps(temperature))
        self.sock3.recv(pickle.loads)
	


class Weather(multiprocessing.Process):
    def __init__(self, temperature,temp_change,ensoleillement,upDown,duration):
        super().__init__()
        self.temperature = temperature
        self.temp_change = temp_change
        self.upDown = upDown
        self.duration = duration
        self.ensoleillement = ensoleillement
        
    def update_temperature(self):
        
        if self.duration>=0:
            self.duration-=1
            self.temperature += self.upDown*int(self.temp_change*random.randrange(0,10)/10)
        else:
            self.upDown=random.choice([-1, 1])
            self.duration = random.randrange(3,7)
            self.temperature += self.upDown*float(self.temp_change*random.randrange(0,10)/10)    
    def update_ensoleillement(self):
        a= random.randrange(-10,10)/100
        if a+self.ensoleillement >=1:
            self.ensoleillement=1
        elif a+self.ensoleillement <=0:
            self.ensoleillement=0   
        else:
            self.ensoleillement+=a     
    def run(self):
        while True:
            self.update_temperature()
            self.update_ensoleillement()
            #print(self.temperature)
            #print(self.ensoleillement)
            time.sleep(1)     





class External(multiprocessing.Process):
        def __init__(self):
            super().__init__() 
        def run(self):
            while True:
                time.sleep(1)
                r=random.randrange(0,1000)
                if r<1:
                    os.kill(os.getppid(), signal.SIGINT)
                elif r<31:
                    os.kill(os.getppid(), signal.SIGUSR2)
                elif r<81:
                    os.kill(os.getppid(), signal.SIGALRM)
                elif r<91:
                    os.kill(os.getppid(), signal.SIGUSR1)
                else:
                    pass    

 
 
 
 
 
 
 
 
 
               
if __name__=='__main__':
    temperature=multiprocessing.Value('d',22)
    temp_change=multiprocessing.Value('i',2)
    ensoleillement=multiprocessing.Value('d',0.5)
    upDown=multiprocessing.Value('i',-1)
    duration=multiprocessing.Value('i',5)
    transactions_lock=threading.Lock()

	
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    sock1.bind(('localhost', 10000))
    _, port1 = sock1.getsockname()
    sock1.listen()
    conn1, _ = sock1.accept()
    
    sock2.bind(('localhost', 20000))
    _, port2 = sock2.getsockname()
    sock2.listen()
    conn2, _ = sock2.accept()
    
    
    sock3.bind(('localhost', 30000))
    _, port3 = sock3.getsockname()
    sock3.listen()
    conn3, _ = sock3.accept()


    
    queue=multiprocessing.Queue()



	
	
    m = Market(10,temperature,temp_change,ensoleillement,upDown,duration,sock1,sock2,sock3)
    p=Weather(temperature,temp_change,ensoleillement,upDown,duration)
    h1=Home(10,8,"always give",sock1,queue)
    h2=Home(10,8,"always sell",sock2,queue)
    h3=Home(10,9,"sell if no takers",sock3,queue)
    m.start()
    p.start()
    h1.start()
    h2.start()
    h3.start()
    m.join()
    p.join()
    h1.join()
    h2.join()
    h3.join()
