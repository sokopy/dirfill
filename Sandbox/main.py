import random, os

def random_unicode(l):
    include_ranges = [(0x00AE,0x00FF),(0x0100,0x017F),(0x0180,0x024F),(0x2C60,0x2C7F),(0x16A0,0x16F0),(0x0370,0x0377),(0x037A,0x037E),(0x0384,0x038A),(0x038C,0x038C)]
    ab = [chr(code_point) for current_range in include_ranges for code_point in range(current_range[0], current_range[1])]
    return ''.join(random.choice(ab) for _ in range(l))

for i in range(10):
    open(f"{random_unicode(10)}", "x", encoding="utf-8").write(str(random_unicode(100)))