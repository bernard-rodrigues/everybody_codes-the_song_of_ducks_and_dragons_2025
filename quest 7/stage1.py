data = """Azral,Siljorath,Vanral,Vanjorath,Silthel,Silral,Azjorath,Azthel,Vanthel

o > r
A > z
V > a
a > t,l,b
z > j,b
l > t,j,r
S > i
n > t,j,r
j > o
r > a
i > b
h > e
t > h
e > l""".split("\n")

def check_graph(name: str, index: int, available_letters: list[str], instructions_dict: dict[str, str]) -> str | None:
    if name[index] not in available_letters:
        return None
    else:
        if index == len(name) - 1:
            return name
        else:
            new_available_letters = list(instructions_dict[name[index]])
            return check_graph(name, index + 1, new_available_letters, instructions_dict)
    
names = data[0].split(",")
instructions = data[2:]

instructions_dict = {}

output = []

for instruction in instructions:
    inst = instruction.replace(" ","").split(">")
    instructions_dict[inst[0]] = inst[1]

available_letters = [letter for letter in instructions_dict.keys() if letter.isupper()]

for name in names:
    new_name = check_graph(name, 0, available_letters, instructions_dict)
    if new_name:
        output.append(new_name) 

# Output must be Azjorath
print(output)