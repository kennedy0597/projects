import subprocess

#p = subprocess.Popen('date', stdout=subprocess.PIPE, shell=True)
#(output, err) = p.communicate()
#p.status = p.wait()
#print('today is ', output)
#print('Error is', err)
#print('Exit status is ', p.status)

fileobj = open('test.txt', 'w')
fileobj.write("hello world!")
fileobj.close

subprocess.Popen(["start", "test.txt"], shell=True)