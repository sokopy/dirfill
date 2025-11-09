import random, os

def ru(l):
    ir = [(0x00AE,0x00FF),(0x0100,0x017F),(0x0180,0x024F),(0x2C60,0x2C7F),(0x16A0,0x16F0),(0x0370,0x0377),(0x037A,0x037E),(0x0384,0x038A),(0x038C,0x038C)]
    a = [chr(cp) for cr in ir for cp in range(cr[0], cr[1])]
    return ''.join(random.choice(a) for _ in range(l))

for i in range(5):
    open(f"{ru(15)}", "x", encoding="utf-8").write(ru(50))