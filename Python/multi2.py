import multiprocessing as mp

def powerOf(num):
    return num**2

def my_func(x):
    print("the square of", x, "is", x**2, "done by", mp.current_process().name)

def main():
    print("cpu count: ", mp.cpu_count())

    numbers = list(range(10,20))
    print("numbers in list", numbers)

    pool = mp.Pool(mp.cpu_count())
    result = pool.map(powerOf, numbers)
    result.append(mp.current_process())
    print(result)

    first_list = [2, 3, 4, 5, 5, 6]
    print("first_list")
    result1 = pool.map(my_func, first_list)
    print(result1)
    print("second list")
    second_list = [11, 12, 15, 16, 18, 25]
    result2 = pool.map(my_func, second_list)
    print(result2)

if __name__ == "__main__":
    main()