
# coding: utf-8

# In[3]:


def speak(x):
    import speech_recognition as sr
    import pyttsx3
    import pyaudio
    engine=pyttsx3.init()
    engine.say(x)
    engine.runAndWait()


# In[4]:


def recog():
    import speech_recognition as sr
    import pyttsx3
    import pyaudio
    mic=sr.Microphone()
    rec=sr.Recognizer()
    with mic as source:
        print("say:")
        audio=rec.listen(source)
        text=rec.recognize_google(audio)
        return(text)


# In[5]:


#cmd=recog()
def send(cmd):
    import subprocess as sp
    import socket
    s=socket.socket()
    s.connect(("192.168.43.112",1235))
    speak('enter your command')
    speak(cmd)
    cmd=cmd.encode()
    s.send(cmd)
    text=s.recv(100).decode()
    return(text)


# In[7]:


import time
print("                    welcome to crontab                     ")
speak('welcome to crontab')
print("you can either login by password , or by your face image")
speak("you can either login by password , or by your face image")
print("tell system how you want to login")
speak("tell system how you want to login")
passwd='hello'
a=recog()
print(a)
i=3
check=0
while i>0:
    i=i-1
    if 'password' in a:
        speak("enter your password")
        in_pass=input('')
        if in_pass==passwd:
            speak('Hello anand how may i help you')
            check==1
        else:
            if i==0 : 
                print("shutting down .....")
                speak("you are not allowed to login")
                send('init 0')
            if i!=0 :
                print("please try again , you have only {} chance left".format(i))
                speak("please try again , you have only {} chance left".format(i))
    if 'face' or 'camera' or 'web camera' :
        print("After 3 sec please come in front of webcam for face detection")
        speak("After 3 sec please come in front of webcam for face detection")
        
        time.sleep(3)
        print("hello")
                    
            
    


# In[ ]:


if i!=0:
                print("please write correct password you have only {} chances left".format(i)
            
            


# In[ ]:




