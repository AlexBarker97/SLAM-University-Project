import threading, random, time

def infiniteloop1():
    while True:
        global value
        value = random.randint(35,100)
        print(value,"(Value)")
        time.sleep(0.1)

def infiniteloop2():
    r=[]
    global theta
    theta = []
    duty = 50
    while True:
        duty -= 1        
        print(duty, "Duty")
        if duty >= 10:
            r.append(value)
            theta.append(duty)
            time.sleep(0.1)
        else:
            print(r,theta)
            break
            

thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()
