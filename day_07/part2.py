
def eval_hand(hand):
    c_dict = {}
    for c in "abcdefghijklm":
        c_dict[c] = 0
    for c in hand:
        if c != "a":
            c_dict[c] += 1
    c_dict = dict(sorted(c_dict.items(), key=lambda item: item[1], reverse=True))
    for c in hand:
        if c == "a":
            c_dict[next(iter(c_dict))] += 1
    n_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for c, n in c_dict.items():
        n_dict[n] += 1
    n_dict.pop(0)
    n_dict = dict(sorted(n_dict.items(), key=lambda item: item[0], reverse=True))
    ns = list(n_dict.values())
    ns = "".join(str(n) for n in ns)
    return ns


file = open("input.txt", "r")
lines = file.read().splitlines()
hands_w_b = [line.split() for line in lines]

cards_src = "J23456789TQKA"
cards_dst = "abcdefghijklm"
cards_trans_tab = str.maketrans(cards_src, cards_dst)
hands_w_b = [(hand[0].translate(cards_trans_tab), int(hand[1])) for hand in hands_w_b]

hands_sorted = sorted(hands_w_b, key=lambda x: eval_hand(x[0]) + x[0])
hands_sorted = [(hands_sorted[i][0], hands_sorted[i][1], i+1) for i in range(len(hands_sorted))]
wins = [hands_sorted[i][1] * hands_sorted[i][2] for i in range(len(hands_sorted))]

print(sum(wins))

file.close()
