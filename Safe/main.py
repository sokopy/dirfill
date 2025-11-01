import os, time, random

os.system("title Dirfill Safe v1")

while True:
    os.system("color 7 & cls")
    conf = input("Welcome to Dirfill Safe . Do you want to execute the safe version of Dirfill? (y/n)\n> ")
    if conf.lower() == "y": break;
    elif conf.lower() == "n": exit()
    else:
        print(f"'{conf}' is not a valid option. Type 'y' to execute or 'n' to exit")
        time.sleep(3)
 
def get_random_unicode(l):
    include_ranges = [(0x00AE,0x00FF),(0x0100,0x017F),(0x0180,0x024F),(0x2C60,0x2C7F),(0x16A0,0x16F0),(0x0370,0x0377),(0x037A,0x037E),(0x0384,0x038A),(0x038C,0x038C)]
    ab = [chr(code_point) for current_range in include_ranges for code_point in range(current_range[0], current_range[1])]
    return ''.join(random.choice(ab) for _ in range(l))

for i in range(50):
    open(f"{get_random_unicode(15)}", "x", encoding="utf-8").write(str(get_random_unicode(100)))