def is_bit_set(x, pos):
    mask = 1 << pos
    return ( x & mask ) != 0


print("Bit 0: 1011 1100 set?", is_bit_set(0b10111100, 0))
print("Bit 1: 1011 1100 set?", is_bit_set(0b10111100, 1))
print("Bit 2: 1011 1100 set?", is_bit_set(0b10111100, 2))
print("Bit 3: 1011 1100 set?", is_bit_set(0b10111100, 3))
print("Bit 4: 1011 1100 set?", is_bit_set(0b10111100, 4))
print("Bit 5: 1011 1100 set?", is_bit_set(0b10111100, 5))
print("Bit 6: 1011 1100 set?", is_bit_set(0b10111100, 6))
print("Bit 7: 1011 1100 set?", is_bit_set(0b10111100, 7))
