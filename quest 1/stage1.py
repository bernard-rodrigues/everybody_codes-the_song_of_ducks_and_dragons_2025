name_list = "Zyrdin,Fersar,Havverax,Lazrax,Valtaril,Morngnaris,Fyrsor,Zyrjorath,Eryquor,Cragrex".split(",")

instructions = "L6,R8,L2,R8,L1,R9,L1,R9,L8,R4,L4".split(",")

position = 0
list_len = len(name_list)

for instruction in instructions:
    # Read first character to check the current direction
    direction = -1 if instruction[0] == "L" else 1
    # Move the current index
    position += direction*int(instruction[1])
    
    # Limit left to index 0
    if position < 0: position = 0
    # Limit right to index equals list length
    elif position >= list_len: position = list_len - 1

print(name_list[position])