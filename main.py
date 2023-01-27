import threading
import random
import multiprocessing
import time
import signal
import os
import socket
import pickle
# Create a Python script that simulates an energy-producing and consuming home
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
		receiveData()
		production_rate=a*(2*ensoleillement)
		pass
		
	def calculate_consumption_rate(self):
		receiveData()
		consuption_rate=consumption_rate+(22-temperature)*0.5
        
    def trade_energy(self):
        if self.trade_policy == "always_give":
            # give away surplus energy to other homes
            # give consumption_rate/10
            self.queue.put("Anyone in need ?")
            time.sleep(1)
            if (self.queue.get()=="Anyone in need ?" and self.surplus<production_rate/10):
				self.queue.put("I am in need, my pid is "+self.getpid())
			time.sleep(1)
			if ((self.queue.get())==str.startswith("I am in need, my pid is ") and self.surplus>self.consumption_rate/5):
				num_string=(self.queue.get()).split("is ")[-1].strip()   #get pid of the process that sent the message
				num=int(num_string)
				self.queue.put(num+", here is some energy, "+consumption_rate/10)				#mutex lock à mettre ici pour protéger le changement de la valeur surplus
				self.surplus=self.surplus-consumption_rate/10
            # calls queue to listen for givers (if surplus<production_rate/10)
				#if no givers use socket to buy
            pass
        elif self.trade_policy == "always_sell":
            # sell surplus energy to the market
            # sell consumption_rate/10
            if (self.surplus>consumption_rate/5):
				sellToMarket(consumption_rate/10)
            if (self.queue.get()=="Anyone in need ?" and self.surplus<production_rate/10):
				self.queue.put("I am in need, my pid is "+self.getpid())
            # does not call queue for takers (as it always sells)
				#therefore sell using socket
            # calls queue to listen for givers(if surplus<prodution_rate/10)
				#if no givers use socket to buy
            pass
        else:  self.trade_policy == "sell_if_no_takers"
            # check if other homes want surplus energy
            self.queue.put("Anyone in need ?")
            time.sleep(1)
            if (self.queue.get()=="Anyone in need ?" and self.surplus<production_rate/10):
				self.queue.put("I am in need, my pid is "+self.getpid())
			time.sleep(1)
			if ((self.queue.get())==str.startswith("I am in need, my pid is ") and self.surplus>self.consumption_rate/5):
				num_string=(self.queue.get()).split("is ")[-1].strip()   #get pid of the process that sent the message
				num=int(num_string)
				self.queue.put(num+", here is some energy, "+consumption_rate/10)
			else :
				sellToMarket(consumption_rate/10)
            # if not, sell to the market
            # trade consumption_rate/10
            # calls queue to ask for takers (if no takers sell)
				#therefore sell using socket
            # calls queue to listen for givers (if surplus<production_rate/10)
				#if no givers use socket to buy
            pass
            
	def sellToMarket(amountSold):
		#sells some energy to the market
		
		pass
    
	def run:
		while True : 
			if (surplus > consumption_rate/5 or surplus<production_rate/10):
				trade_energy()
			calculate_surplus()
			
		


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

    def update_critical_data(self, transaction_amount, energy_sold,internal_factors,externall_factors):
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
        t.run()
        threadh1.join()
        threadh2.join()
        threadh3.join()
        while True:
            time.sleep(1)
            pass
	def communicate_with_h1(self):
		self.sock1.send(pickle.dumps(price), pickle.dumps(ensoleillement),pickle.dumps(temperature))
		self.sock1.recv(pickle.loads)
	def communicate_with_h2(self):
		self.sock2.send(pickle.dumps(price), pickle.dumps(ensoleillement),pickle.dumps(temperature))
		self.sock2.recv(pickle.loads)
	def communicate_with_h3(self):
		self.sock3.send(pickle.dumps(price), pickle.dumps(ensoleillement),pickle.dumps(temperature))
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
	
	
	sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(('localhost', 10000))
    _, port1 = sock1.getsockname()
    sock1.listen()
    conn1, _ = sock1.accept()
    
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock2.bind(('localhost', 20000))
    _, port2 = sock2.getsockname()
    sock2.listen()
    conn2, _ = sock2.accept()
    
    
    sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock3.bind(('localhost', 30000))
    _, port3 = sock3.getsockname()
    sock3listen()
    conn3, _ = sock3.accept()
	
	queue=multiprocessing.Queue()
	
	
    m = Market(10,temperature,temp_change,ensoleillement,upDown,duration,sconn1,conn2,conn3)
    p=Weather(temperature,temp_change,ensoleillement,upDown,duration)
    h1=Home(10,8,"always give",conn1,queue)
    h2=Home(10,8,"always sell",conn2,queue)
    h3=Home(10,9, "sell if no takers",conn3,queue)
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
    

