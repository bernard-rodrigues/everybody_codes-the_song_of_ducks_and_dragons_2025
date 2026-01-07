name_list = "Lirgonn,Lazirzorin,Yndxelor,Mavzral,Glaurxel,Nythgarath,Irynlon,Orydaros,Kynralis,Mavquor,Talkryth,Malithlith,Mornkael,Helfal,Jaertal,Rahrilor,Aelithox,Daltaril,Orahorath,Draithrax,Urorath,Thazisis,Phyragrath,Harnnarel,Drethgryph,Galfeth,Selsyron,Krynnrex,Braemal,Aerrovan".split(",")

instructions = "L9,R36,L48,R46,L31,R40,L7,R35,L48,R40,L26,R12,L36,R9,L33,R33,L44,R14,L37,R38,L5,R28,L5,R32,L5,R29,L5,R9,L5,R20,L5,R33,L5,R41,L5,R31,L5,R26,L5,R35,L33,R24,L9,R20,L20,R30,L23,R33,L8,R12,L14,R7,L45,R44,L20,R26,L11,R27,L9".split(",")

list_len = len(name_list)

def swap_with_zero(name_list: list[str], position: int) -> list[str]:
    aux = name_list[position]
    name_list[position] = name_list[0]
    name_list[0] = aux

    return name_list

for instruction in instructions:
    # Reset the cursor to index 0
    position = 0
    
    # Read first character to check the current direction
    direction = -1 if instruction[0] == "L" else 1

    # Move the current index based on remaining characters
    position += direction*int(instruction[1:])
    
    # Adjust the index to the circular list
    position = position % list_len
    
    # Swaps the current index element with index 0 element
    name_list = swap_with_zero(name_list, position)

# Print the name in index 0
print(name_list[0])