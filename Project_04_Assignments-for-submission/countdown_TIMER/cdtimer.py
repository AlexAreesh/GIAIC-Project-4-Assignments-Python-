import time

seconds = int(input("Enter time in seconds: "))
while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1

print("Time's up dudeeeeee")
