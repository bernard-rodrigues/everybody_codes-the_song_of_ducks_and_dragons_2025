data = """Xaryt

X > a,o
a > r,t
r > y,e,a
h > a,e,v
t > h
v > e
y > p,t""".split("\n")

def check_graph(name: str, index: int, available_letters: list[str], instructions_dict: dict[str, str]) -> str | None:
    if name[index] not in available_letters:
        return None
    else:
        if index == len(name) - 1:
            return name
        else:
            new_available_letters = list(instructions_dict[name[index]])
            return check_graph(name, index + 1, new_available_letters, instructions_dict)
        
def find_names(name: str, available_letters: list[str], letter_index: int, graph: dict[str, str], name_list: list[str] = []):
    # Nome atual com a próxima letra disponível
    current_name = name + available_letters[letter_index]
    
    # Se a última letra do nome atual não estiver no grafo
    # Ou o tamanho do nome ultrapassou 11
    if current_name[-1] not in graph.keys():
        # Se houver mais letras disponíveis para checar no nó atual
        if letter_index < len(available_letters) - 1:
            
            # Chamada com o mesmo nome e a próxima letra do nó atual
            return find_names(name, available_letters, letter_index + 1, graph, name_list)
        else:
            return name_list
    elif len(current_name) > 11:
        return name_list
    # Se o tamanho do nome atual é inferior a 7
    elif len(current_name) < 7:
        
        # Se houver mais letras disponíveis para checar no nó atual
        if letter_index < len(available_letters) - 1:
            
            # Chamada com o mesmo nome e a próxima letra do nó atual
            return find_names(name, available_letters, letter_index + 1, graph, name_list)
        else:
            # Caso contrário
            # Chamada com o nome atualizado e o nó da nova letra adicionada
            return find_names(current_name, list(graph[current_name[-1]]), 0, graph, name_list)
    
    # Se o número de letras estiver entre 7 e 11
    elif 7 <= len(current_name) <= 11:
        # Adiciona o nome válido à lista
        name_list.append(current_name)
        
        # Se houver mais letras disponíveis para checar no nó atual
        if letter_index < len(available_letters) - 1:
            
            # Chamada com o mesmo nome e a próxima letra do nó atual
            return find_names(name, available_letters, letter_index + 1, graph, name_list)
        else:
            # Caso contrário
            # Chamada com o nome atualizado e o nó da nova letra adicionada
            return find_names(current_name, list(graph[current_name[-1]]), 0, graph, name_list)

    
    
names = data[0].split(",")
instructions = data[2:]

instructions_dict = {}

output = []

for instruction in instructions:
    inst = instruction.replace(" ","").split(">")
    instructions_dict[inst[0]] = inst[1]

available_letters = [letter for letter in instructions_dict.keys() if letter.isupper()]

total = 0
name_list = []

for name in names:
    if check_graph(name, 0, available_letters, instructions_dict):
        name_list = find_names(name, list(instructions_dict[name[-1]]), 0, instructions_dict, name_list)


print(name_list)