#CAR GAME
command=""
started=False
while True:
    command=input (">").lower()
    if command=="start":
        if started:
            print("Car already started")
        else started=True
            print("Car Started...")
    elif command=="stop":
        if not started
            print ("Car already stopped")
        else
        print("Car Stopped")
        started=False
    elif command=="help":
        print("""
Start -  To Start the car
Stop -To Stop the car
Quit - To Quit""")
    elif command == "quit":
        break

else:
    print("Sorry! I don't understand that")