#CAR GAME:
#help
#start-to start the car
#stop-to stop the car
#quit-to exit
#asd
#i don't understand
#start
#Car started ... Ready to go !!
#stop
#car stopped
#quit

command = ""
started= False
#while command != "quit":
while True:
    command =input("> ").lower()
    if command == "start":
        if started:
            print("car is already started!!")
        else :
            started = True
            print("car started!!...")
    elif command == "stop":
        if not started:
            print('car is already stopped!!')
        else:
            started=False
            print("car stopped!!..")
    elif command == "help":
        print("""
start-to start the car
stop-to stop the car
quit-to exit
       """ )
    elif command =="quit":
        break
    else:
        print("SORRY, I DON'T UNDERSTAND THAT !!")





