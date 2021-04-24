import socket
import subprocess
import threading
import time

from Constand_Hs import Constand_Hs

class Process_Thread(threading.Thread):
    def __init__(self,Cmd,condition,host,Port):
        threading.Thread.__init__(self)
        self.Cmd=Cmd
        self.condition=condition
        self._host=host
        self._Port=Port
    def run(self):
        while 1:
            try:
                while 1:
                    full_msg=''
                    data=sock.recv(Constand_Hs.HEADERSIZE)
                    if len(data)>0:
                        full_msg+=data.decode('utf-8')
                    if len(data)<=Constand_Hs.HEADERSIZE and len(data)>0:
                        self.condition.acquire()
                        self.Cmd.append(full_msg)
                        self.condition.notify()
                        self.condition.release()
                        pass
                    full_msg=''
                    if len(data)==0:
                        sock.close()
                        time.sleep(2)
                    pass

            except Exception as e:
                try:
                    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    sock.connect_ex((self._host,self._Port))
                    print('Connected')
                except Exception as e:
                    sock.close()
                    pi=subprocess.call(['ping',self._host,'-c1','-W2','-q'])
                    if pi==0:
                        del pi
                        continue
            # finally:
            #     if checkwifi()==False:
            #         print('Rasp Pi Zero W turn off wifi. Pls reset Rasp pi')
            #         restart()
    def __del__(self):
        print('Doi tuong preducer bi xoa')