from utils import Fishbone

# number list removing the identifier
number_list = "69:4,2,7,7,5,4,2,3,9,9,5,6,3,1,5,3,2,7,9,4,6,1,1,7,4,2,9,2,7,1".split(":")[1].split(",")
converted_number_list = [int(i) for i in number_list]

fishbone = Fishbone(converted_number_list[0])

for i in range(1, len(converted_number_list)):
    fishbone.add_element_to_fishbone(converted_number_list[i])

result = ""
for fishbone_line in fishbone.get_lines():
    result += str(fishbone_line.get_center())
print(result)