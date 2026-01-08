data = """Jaerzor,Helvor,Ardencyth,Zarathirin,Helaxis,Ardenacris,Ilmarfyr,Ilmarzor,Zarathketh,Tharilvor,Helgnar,Dorgnar,Ardencalyx,Cyndfyr,Zarathgnar,Tharilgnar,Zarathaxis,Dorcyth,Jaergnar,Dorvor,Tharilcalyx,Helcalyx,Ardenfyr,Tharilketh,Helketh,Jaeracris,Cyndacris,Ardenvor,Zarathacris,Helvor,Ilmarketh,Helfyr,Tharilfyr,Ilmaririn,Helketh,Ardenzor,Tharilzor,Zarathcyth,Zarathgnar,Ardengnar,Cyndvor,Helacris,Cyndcyth,Ardenaxis,Doracris,Cyndirin,Helgnar,Zarathketh,Dorzor,Zarathfyr,Jaercyth,Doraxis,Dorfyr,Zarathcalyx,Helaxis,Zarathvor,Dorketh,Helzor,Zarathzor,Helirin,Helcyth,Jaerfyr,Dorcalyx,Zarathfyr,Ilmarvor,Doririn,Ardenirin,Jaercalyx,Cyndzor,Helacris,Zarathzor,Ilmarcyth,Ardenketh,Tharilacris,Helcalyx,Helcyth,Jaeririn,Jaeraxis,Tharilirin,Jaervor,Cyndaxis,Jaerketh,Ilmarcalyx,Tharilcyth,Ilmargnar,Zarathcyth,Cyndketh,Helzor,Zarathaxis,Zarathcalyx,Ilmaraxis,Cyndcalyx,Helirin,Helfyr,Zarathirin,Ilmaracris,Cyndgnar,Zarathvor,Zarathacris,Tharilaxis

y > r,t,x,v
h > i,v,a,k,z,g,f,c
J > a
k > e
z > o
i > r,n,s,l
f > y
v > o
l > m,y,i,v,a,k,z,g,f,c
a > r,c,x,l,v,t
A > r
n > i,v,a,k,z,g,f,c,d
I > l
g > n
Z > a
r > f,v,i,a,k,z,g,c
D > o
C > y
o > r,v
T > h
e > n,t,v,r
d > e,i,v,a,k,z,g,f,c
m > a
t > h
x > i
H > e
c > r,y,a""".split("\n")

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

total = 0
for i, name in enumerate(names):
    if check_graph(name, 0, available_letters, instructions_dict):
        total += (i + 1)

# Output must be 2595
print(total)