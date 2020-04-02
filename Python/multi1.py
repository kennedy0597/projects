import multiprocessing as mp

print(mp.cpu_count())

def worker(num):
    print('worker: ',num)
    return

if __name__=='__main__':
    jobs=[]
    for i in range(4):
        p = mp.Process(target=worker, args=(1,))
        jobs.append(p)
        p.start()
    for job in jobs:
        print(job.name)
        print(job.pid)