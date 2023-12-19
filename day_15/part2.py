import re


def get_hash(a_str):
    val = 0
    for c in a_str:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def do_step(boxes, step):
    lab = re.match(r"[a-zA-Z]+", step).group(0)
    box_n = get_hash(lab)
    oprt = re.search(r"[\-=0-9]+", step).group(0)
    if oprt[0] == '-':
        if lab in boxes[box_n]:
            boxes[box_n].pop(lab)
    elif oprt[0] == '=':
        boxes[box_n][lab] = int(oprt[1])


file = open("input.txt", "r")
steps = file.read().replace("\n", "").split(",")

boxes = []
for i in range(256):
    boxes.append({})
for step in steps:
    do_step(boxes, step)

fpows = [box_i * slot * fl for box_i, box in enumerate(boxes, 1) for slot, (lab, fl) in enumerate(box.items(), 1)]

print(sum(fpows))

file.close()
