import keyboard 
flag=0 # using module keyboard
while True:
	  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            flag=0
        if flag==0:      # finishing the loop
        	print("you didnt press anything")
        	flag=1
    except:
        break  # if us