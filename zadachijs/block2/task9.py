import time, random, os

def c0d3():
    l0ad = "Loading..."
    for _ in range(180):
        print(f"\033[38;5;{random.randint(0, 255)}m{l0ad}\033[0m", end='\r')
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    msg = ''.join([chr(x) for x in [112, 101, 110, 105, 115]])
    r3s = ''.join([f"\033[38;5;{random.randint(0, 255)}m{char}\033[0m" for char in msg])
    print(r3s)

if __name__ == "__main__":
    c0d3()