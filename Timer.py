import time


time.sleep(1)
print('Welcome, user')
time.sleep(1)
name = input('What is your name?\n\n')
print('\n\nWelcome to the timer,')
time.sleep(2)
print(name)
time.sleep(2)
while True:
    try:
        timeset = int(input('\n\nENTER SECONDS:\n\n'))
        break
    except ValueError:
        print('\n\n\nYou stupid freaking crazy idiot! THAT IS NOT A FREAKING NUMBER!!')
print(timeset)
for i in range(timeset):
    time.sleep(1)
    timeset = timeset - 1
    print(timeset)
for i in range(3):
    print(name,', TIMER COMPLETE!!!')

    
