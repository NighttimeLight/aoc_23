
def get_hash(a_str):
    val = 0
    for c in a_str:
        val += ord(c)
        val *= 17
        val %= 256
    return val


file = open("input.txt", "r")
steps = file.read().replace("\n", "").split(",")

hashes = [get_hash(step) for step in steps]

print(sum(hashes))

file.close()
