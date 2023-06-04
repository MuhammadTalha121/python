import time

def jump_training(num_jumps):
    """
    This function simulates a jump training session by prompting the user to jump a certain number of times.
    """
    print("Get ready to jump!")
    time.sleep(1)
    print("Jump as high as you can!")
    time.sleep(1)
    for i in range(num_jumps):
        print("Jump!")
        time.sleep(1)

if __name__ == "__main__":
    num_jumps = int(input("How many jumps would you like to do? "))
    jump_training(num_jumps)
