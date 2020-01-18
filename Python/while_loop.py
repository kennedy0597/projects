command = ""
is_car_started = False

while True:
    command=input("> ").lower()
    if command == "start":
        if is_car_started:
           print("car is already started")
        else:
             is_car_started = True
             print("car started")
    elif command == "stop":
        if not is_car_started:
         print("Car is already stopped")
        else:
            print("car stopped")
            is_car_started = False
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("sorry i don't understand")