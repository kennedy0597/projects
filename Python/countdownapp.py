import time, subprocess

timeleft = 60
while timeleft>0:
    print("\n", timeleft, end="")
    time.sleep(1)
    if(timeleft==55):
        subprocess.Popen(["start","test.txt"], shell=True)
    if (timeleft==50):
        calcproc = subprocess.Popen(["C:\\Windows\\System32\\calc.exe", "1234"], stdout=subprocess.PIPE)
        print(calcproc.communicate())
    if (timeleft==0):
       wordproc = subprocess.Popen(["start", "Automobile_data.csv"], shell=True)
       print(wordproc.communicate())
    if (timeleft==40):
       music1 = subprocess.Popen("C:\\Program Files (x86)\\Google\\Chrome\\Application", stdout=subprocess.PIPE)
       print(music1.communicate())
    if (timeleft==35):
       csv1 = subprocess.Popen(["start","Automobile_data"], shell=True)
       print(csv1.communicate())
    timeleft = timeleft - 1
Print(x)
