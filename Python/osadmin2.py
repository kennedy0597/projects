import subprocess

subprocess.call('dir', shell=True)
subprocess.run('dir', shell=True)
subprocess.check_call('dir', shell=True)
print(subprocess.check_output(["echo", "Hello World!"], shell=True))

p = subprocess.Popen(["echo", "Hello World!"], stdout=subprocess.PIPE, shell=True)
# once communicated, the current pipe will be closed
print(p.communicate())

proc = subprocess.Popen(["echo","to stdout"], stdout=subprocess.PIPE, shell=True)
stdout_v = proc.communicate()[0]
repr(stdout_v)
print(stdout_v)
print(repr(stdout_v))

# open a calculator
#subprocess.Popen("C:\\Windows\\System32\\calc.exe")
#p = subprocess.Popen("C:\\Windows\\System32\\calc.exe")
#print(p.communicate())

# open a word doc
#subprocess.Popen(["start", "test1.txt"], shell=True)

process_result = {}
p = subprocess.Popen(["echo", "Testing123"], stdout=subprocess.PIPE, shell=True)
process_result[1] = p.communicate()
p1 = subprocess.Popen("dir", stdout=subprocess.PIPE, shell=True,stderr=subprocess.PIPE)
process_result[2] = p1.communicate()
print(process_result[1])
print(process_result[2])

#process_result3 = [[],[]]
#for i in process_result:
#    process_result3[0].append(i)

#for i in process_result1:
#    process_result3[1].append(i)

#print(process_result3[0])
#print(process_result3[1])







