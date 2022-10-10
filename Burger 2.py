import turtle #Base for importing pictures and using as buttons
import platform #Library for checking OS system for importing sound
import pathlib #library for importing path for file (important for windows)
import os #library for managing system properties
import imp #
import threading #library for background worker and managing side processes
import time #library for background workers to count time
import random #library for random values
from datetime import datetime #library for checking the system time (for extras)
SAVEFILE=[0,0,0] #list which reads the file and store info as backup
#initializing main globals:
clicks=0
actual_clicks=0
grandmas=0
#reading the data from savefile
def ReadData():
        global SAVEFILE
        global clicks
        global actual_clicks
        global grandmas
        clicks=SAVEFILE[0]
        grandmas=SAVEFILE[1]
        actual_clicks=SAVEFILE[2]
#Reading the data from file and saving to SAVEFILE
def ReadFile():
        global SAVEFILE
        f=open("SaveFile.csv","r+")
        SAVEFILE[0]=int(f.readline())
        SAVEFILE[1]=int(f.readline())
        SAVEFILE[2]=int(f.readline())
        f.close()
        ReadData()
ReadFile()
#Importing and positioning all pictures
wn=turtle.Screen()
wn.title('Burger Clicker')#game title
wn.bgcolor("black")#background color
wn.register_shape("basic-burger.gif")
wn.register_shape('GOLDEN.gif')
wn.register_shape("cheese-burger.gif")
wn.register_shape("advanced-burger.gif")
wn.register_shape("quarterpunder-burger.gif")
wn.register_shape("heartattack.gif")
wn.register_shape("tripple-burger.gif")
wn.register_shape('workerINACTION.gif')
wn.register_shape("RESET.gif")
reset=turtle.Turtle()
reset.shape('RESET.gif')
reset.goto(-300,300)
reset.speed(0)
burger=turtle.Turtle()
wn.register_shape("worker.gif")
worker=turtle.Turtle()
golden=turtle.Turtle()
worker.shape("worker.gif")
worker.goto(0,-350)
worker.speed(0)
burger.speed(0)#speed of gif animation

#Burger changes its form with clicks 
def BurgerSize():
	if clicks<=100:
		burger.shape('basic-burger.gif')
	elif clicks>100 and clicks<=250:
		burger.shape('cheese-burger.gif')
	elif clicks>250 and clicks<=550:
		burger.shape('advanced-burger.gif')
	elif clicks>550 and clicks<=850:
		burger.shape('quarterpunder-burger.gif')
	elif clicks>850 and clicks<=1050:
		burger.shape('tripple-burger.gif')
	elif clicks>1050:
		burger.shape('heartattack.gif')
current_clicks=0 #variable calculating number of clicks per user for achievement
timeforgoldenbutton='NULL' #time when golden button disappear
GOLDENHOURTILL='NULL' #time when golden hour featuring doubled values dissappears
def GoldenButtonTime():
        while 1:
                now=datetime.now()#check current time
                time2=now.strftime("%H:%M:%S")#store data as string
                if(time2==timeforgoldenbutton):
                        golden.goto(4000,4000)#when the time comes go to impossible to click place
def goldenclick(x,y): #function adds random bonus to number of clicks after clicking golden burger
        global clicks
        a=random.randrange(100,400)
        clicks+=a
        golden.goto(4000,4000)
def BabushkaDoClick(): #function of workers
        global clicks
        global current_clicks
        global grandmas
        global GOLDENHOURTILL
        while 1:
                now=datetime.now()
                time1=now.strftime("%H:%M:%S")
                if(GOLDENHOURTILL==time1):#check if goldenhour expires
                        time.sleep(1)
                        grandmas-=20
                        a=random.randrange(0,400)
                b=random.randrange(0,400)#draw number and decide if this time the bonus will be added
                if(b==0):#adding golden burger bonus in random location and starting background worker to keep the time. After the time expires, the burger will dissapear
                        time.sleep(100)
                        golden.shape('GOLDEN.gif')
                        c=random.randrange(0,400)
                        d=random.randrange(0,400)
                        golden.goto(c,d)
                        timeforgoldenbutton=time1
                        g1=threading.Thread(target=GoldenButtonTime)
                        g1=setDaemon(True)
                        g1.start()
                        golden.onclick(goldenclick)#derive possibility to click object
                elif(b==1):#rare golden hour system
                        time.sleep(3600)
                        GOLDENHOURTILL=time1
                        grandmas+=20
                        print('GoldenHOUR!!!111')
                if(grandmas>0):#grandmas boost for hired worker autoclicks the burger every second
                        time.sleep(1)
                        print('Diners ready darling')
                        clicked(270,270)
def ForceSave():#used for saving data to .csv file
        global grandmas
        global actual_clicks
        global clicks
        try:
                open('SaveFile.csv', 'w').close()
                with open('SaveFile.csv', 'a') as f:
                        f.write(str(clicks)+'\n'+str(grandmas)+'\n'+str(actual_clicks)+'\n')
                        f.close()
        except OSError:
                print('Failed to save')
        else:
                print('GAME SAVED')
def AutoSave():#background worker used for saving data every 60 seconds
        while 1:
                time.sleep(60)
                now=datetime.now()
                time1=now.strftime("%H:%M:%S")
                ForceSave()
def RestartApp():#system security for application used for restarting system after major application changes
        ForceSave()
        os.system('python "Burger.py"')
        sys.exit(0)
def ResetGame(x,y):#resets the game and delete save
        global clicks
        global grandmas
        global actual_clicks
        clicks=0
        grandmas=0
        actual_clicks=0
        ForceSave()
        RestartApp()

BurgerSize()#initialize the burger development
#set pen and write information on screen
pen=turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,250)
pen2=turtle.Turtle()
pen2.hideturtle()
pen2.color('white')
pen2.penup()
pen2.goto(0,200)
pen2.write(f"{grandmas} Clicks/sec",align="center",font=("Courier New",12,"bold"))
#Set background workers for clicking and saving
diner=threading.Thread(target=BabushkaDoClick)#set what function will be called
diner.setDaemon(True)#terminate the worker after the main thread ends
diner.start()#Start the background worker
t2=threading.Thread(target=AutoSave)
t2.setDaemon(True)
t2.start()
pen.write(f"Clicks: {clicks}",align="center",font=("Courier New",32,"bold"))
def CheckForAchievement():#Function showing milestones on console
        global clicks
        global grandmas
        if(clicks==1500):
                print('Achievement get: Burgerdaise')
        if(clicks==3000):
                print('Achievement get: Maniac')
        if(grandmas==10):
                print('Achievement get: HardWorkers')
def clicked(x,y):#function for clicking the burger, adds the number of clicks and refreshes the page
    global clicks
    global actual_clicks
    if platform.system()=='Windows':#for windows use different method of playing sound
        import winsound#library available only on windows
        winsound.PlaySound(str(pathlib.Path(__file__).parent.absolute())+'\consumption.wav',winsound.SND_ASYNC)
    else:
        os.system("afplay consumption.wav&")#after clicking play sound of eating
    clicks+=1
    actual_clicks+=1
    CheckForAchievement()#Check if achievement has been unlocked
    BurgerSize()#Check if burger needs to be updated
    pen.clear()#Refresh number of clicks
    pen.write(f"Clicks: {clicks}",align="center",font=("Courier New",32,"bold"))
    print('+1')
     
def hire(x,y):#function used for hiring employees who add extra clicks per second
        worker.shape('workerINACTION.gif')
        global clicks
        if(clicks>=500):
                print("Grandma hired!")
                global grandmas
                global current_clicks
                current_clicks+=5
                clicks-=500
                grandmas+=1
                RestartApp()
        else:
                print('No money')
        time.sleep(1)
        worker.shape('worker.gif')
burger.onclick(clicked)
worker.onclick(hire)
reset.onclick(ResetGame)
wn.mainloop()#MainOpen
