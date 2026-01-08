data = "ABCaBBCAACbACaCbaAAbcbaCbbbcbcACBcBCbCaCCccaBCccCBCcbaaBBcAAABaBbcAAAaBbABBCBBaBCAAaaBbBbbBaAACaAaab"

chars_to_remove = "BbCc"

knight_pairs = "".join(char for char in data if char not in chars_to_remove)

total = 0
for i in range(len(knight_pairs)):
    if knight_pairs[i] == "A":
        total += knight_pairs[i:].count("a")

# Output must be 184
print(total)