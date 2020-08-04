import keyboard
from threading import Semaphore, Timer
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from string import ascii_lowercase
import sys
import os
from datetime import datetime

class Keylogs:
    def __init__(self):
        self.log={}
        self.fig=plt.figure()
        self.noLog={}
        self.lastKey='0'

    def onPress(self, event):
        key=event.name
        #print('running')
        #print(key)
        if len(key)==1:
            if key not in self.log:
                self.log[key]=1
            else:
                self.log[key]=self.log.get(key)+1
        else:
            if key=="esc" and (self.lastKey=="1" or self.lastKey=="2"):
                # Close the plot and write the analysis
                self.analyse()
                plt.close(self.fig)
                sys.exit(0)
            if key not in self.noLog:
                self.noLog[key]=1
            else:
                self.noLog[key]=self.noLog.get(key)+1
        self.lastKey=key


    def showData(self, i):
        # Update the figure here with the updated log data
        groups=list(self.log.keys())
        values=list(self.log.values())
        #print('running')
        plt.cla()
        plt.bar(groups,values)
        #$plt.title('Key strokes')
        #plt.tight_layout()
        #plt.show()
        #pass

        #Timer(interval=self.interval,function=self.showData).start()

 #   def animate(i):
  #      plt.bar(groups,values)

    def analyse(self):
        pass
        # Print some basic analysis
        if self.lastKey=="1":
            self.gameAnalyse()
        elif self.lastKey=="2":
            self.wordAnalyse()

    def gameAnalyse(self):
        dir=os.path.join("C:\\","Logs")
        if not os.path.exists(dir):
            os.mkdir(dir)
        dir=os.path.join("C:\\","Logs","Games")
        if not os.path.exists(dir):
            os.mkdir(dir)
        
        f=open(dir+"\\"+datetime.now().strftime("%m%d%Y-%Hx%Mx%S")+".txt",'w+')
        qs=str(self.log.get('q'))
        ws=str(self.log.get('w'))
        es=str(self.log.get('e'))
        rs=str(self.log.get('r'))
        f.write("Buttons Pressed:\nQ: "+qs+"\nW: "+ws+"\nE: "+es+"\nR: "+rs)
        f.write("\n\nTotal Key Strokes: " + str(sum(list(self.log.values()))))
        f.close()

    def wordAnalyse(self):
        pass

    def start(self):
        keyboard.on_release(callback=self.onPress)
        #print("started")
        ani=animation.FuncAnimation(self.fig,self.showData,interval=1000)
        plt.show()
        
if __name__=="__main__":
    logger=Keylogs()
    logger.start()

    # Print analytics
    logger.analyse()