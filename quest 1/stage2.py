name_list = "Vanidris,Mornnyn,Gorathulrix,Hyravash,Ulkzyph,Sarzeth,Thazketh,Voraxxaril,Zaloryx,Ozankynar,Qalfarin,Iskarnylor,Phyrloris,Oryhynd,Paldselor,Vyrldaros,Vaelzal,Tazmal,Rythzyph,Tirphor".split(",")

instructions = "L18,R11,L17,R14,L16,R10,L19,R8,L17,R7,L5,R13,L5,R12,L5,R10,L5,R5,L5,R16,L17,R11,L12,R18,L19,R10,L8,R9,L12".split(",")

position = 0
list_len = len(name_list)

for instruction in instructions:
    # Read first character to check the current direction
    direction = -1 if instruction[0] == "L" else 1

    # Move the current index based on remaining characters
    position += direction*int(instruction[1:])
    
    # Adjust the index to the circular list
    position = position % list_len

print(name_list[position])