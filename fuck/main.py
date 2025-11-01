import random

def ru(l):
    ir = [(0x00AE,0x00FF),(0x0100,0x017F),(0x0180,0x024F),(0x2C60,0x2C7F),(0x16A0,0x16F0),(0x0370,0x0377),(0x037A,0x037E),(0x0384,0x038A),(0x038C,0x038C)]
    ab = [chr(cp) for cr in ir for cp in range(cr[0], cr[1])]
    return ''.join(random.choice(ab) for _ in range(l))

x=2

while 1:
    open(f"{ru(250)}", "x", encoding="utf-8").write(str(ru(x)))
    x*=x