import time


# we import time module and a cool function sleep.
my_time = int(input("Enter the time in seconds:  "))

# we will loop throw it.
for t in reversed(range(0, my_time)):
    seconds = t % 60
    minutes = int(t / 60) % 60
    hours = int(t / 3600)
    print(f"{hours}:{minutes}:{seconds}")
    time.sleep(1)

print("It's ,Over!")
