#CAR GAME
command=""
while True:
    command=input (">").lower()
    if command=="start":
        print("Car Started...")
    elif command=="stop":
        print("Car Stopped")
    elif command=="help":
        print("""
Start -  To Start the car
Stop -To Stop the car
Quit - To Quit""")
    elif command == "quit":
        break

else:
    print("Sorry! I don't understand that")