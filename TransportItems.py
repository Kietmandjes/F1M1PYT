import time 
from os  import system, name

def clear():
    if name == "nt":
        _ = system ("cls")
    else: 
        _=system ("clear")
def start(): 
    clear() 
    print("Factory: [fiets]\nDistributor: []\nShop:[]")
    time.sleep(2)
    clear()
    print("Factory: []\nDistributor: [fiets]\nShop:[]")
    time.sleep(2)
    clear()
    print("Factory: []\nDistributor: []\nShop:[fiets]")
    time.sleep(2)
    clear()
    print("Factory: []\nDistributor: []\nShop:[]")
    time.sleep(2)
    clear()
    restart2()
    
def restart2():
    restart=input("Restart Y/N:")
    restart1=restart.upper()
    if restart1=='N':
        ()
    elif restart1=='Y':
        start()
    else:
        print("Incorrect input.")
        restart2()
start()