# from time import sleep
# from threading import *
#
# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)
#
#
#
# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")
#             sleep(1)
#
# t1=Hello()
# t2=Hi()
#
# t1.start()
# sleep(0.2)
# t2.start()
#
# t1.join()
# t2.join()
#
# print("Bye")
import threading
#----------------------------------------------------------------------------
# from threading import *
# from time import sleep
#
# class Demo(Thread):
#     def double(self):
#         for i in range(5):
#             print("Python")
#             sleep(1)
#
#     def square(self):
#         for i in range(5):
#             print("SQL")
#             sleep(1)
#
# obj=Demo()
#
#
# t1=Thread(target=obj.double)
# t2=Thread(target=obj.square)
#
# t1.start()
# sleep(0.2)
# t2.start()
#
# t1.join()
# t2.join()

#-------------------------------------------------------------
# from threading import *
# from time import sleep
#
# def alphagen():
#     for i in range(65,91):
#         print(current_thread().name, chr(i))
#         sleep(1)
#
# t1=Thread(target=alphagen, name="ABC")  #For identification purpose we gave thread names.
# t2=Thread(target=alphagen, name="XYZ")
#
# t1.start()
# sleep(0.2)
# t2.start()
#
# t1.join()
# t2.join()

#-----------------------------------------------------------------------------------------------------------
# from threading import *
# from time import sleep
#
# class NumThread(Thread):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         for num in range(5):
#             print(self.name,num)
#             sleep(1)
#
# t1=NumThread()
# t2=NumThread()
# t1.name="Surya"
# t2.name="Harsh"
#
# t1.start()
# sleep(0.2)
# t2.start()
#
# t1.join()
# t2.join()

#-----------------------------------------------------------------------------------
# from threading import *
# from time import sleep
#
# class TableGen(Thread):
#     def __init__(self,n):
#         super().__init__()
#         self.__name=n
#
#     def run(self):
#         for i in range(1,11):
#             print(f"{self.__name}x{i}={self.__name*i}")
#             sleep(1)
#
#
# t1=TableGen(4)
# t2=TableGen(6)
#
# t1.start()
# sleep(0.2)
# t2.start()
#
# print(t1.is_alive())
# print(t2.is_alive())
#
# t1.join()
# t2.join()

#-----------------------------------------------------------------------------------------------
from threading import *

class Bus:
    def __init__(self):
        self.__seats=40
        self.mylock=threading.Lock()

    def reserve(self,name,n):
         self.mylock.acquire()
         for i in range(n):
             self.__seats=self.__seats-1
             print(f'{name} your seat is reserved.')
         print(f'{self.__seats} seats are available.')
         self.mylock.release()

class reservethread(Thread):
    def __init__(self,b,name,n):
        super().__init__()
        self.bus=b
        self.name=name
        self.n=n

    def run(self):
        self.bus.reserve(self.name,self.n)

businstance=Bus()

t1=reservethread(businstance,'Passenger1',3)
t2=reservethread(businstance,'Passenger2',4)

t1.start()
t2.start()

t1.join()
t2.join()
