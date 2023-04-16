command = ""
started = False
while True:
    command = input(">").lower()

    if command == "help":
        print("""Type - 
        Start = To Start The Car
        Stop = To Stop The Car
        End = To Finish Game""")

    elif command == "start":
        if started:
            print("Engine Already Started!!!")
        else:
            started = True
            print("Engine Started...")

    elif command == "stop":
        if not started:
            print("Engine Already Stopped!!!")
        else:
            started = False
            print("Engine Stopped...")

    elif command == "end":
        print("Thanks For Playing")
        break

    else:
        print("I Didn't Understand")

