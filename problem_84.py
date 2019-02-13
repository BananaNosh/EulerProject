import random
import numpy as np
from collections import deque


# problem 84
def monopoly_moves(n, dice_faces=6):
    cc_cards = deque(range(1, 17))
    ch_cards = deque(range(1, 17))
    random.shuffle(cc_cards)
    random.shuffle(ch_cards)

    def change_pos_if_necessary(pos):
        cc_fields = [2, 17, 33]
        ch_fields = [7, 22, 36]
        if pos in cc_fields:
            card = cc_cards.popleft()
            cc_cards.append(card)
            if card == 1:
                pos = 0
            elif card == 2:
                pos = 10
        elif pos in ch_fields:
            card = ch_cards.popleft()
            ch_cards.append(card)
            if card == 1:
                pos = 0
            elif card == 2:
                pos = 10
            elif card == 3:
                pos = 11
            elif card == 4:
                pos = 24
            elif card == 5:
                pos = 39
            elif card == 6:
                pos = 5
            elif card == 7 or card == 8:
                pos = (((pos + 5) % 40) // 10 + 1) * 10 - 5  # railway
            elif card == 9:
                pos = 28 if pos == 22 else 12
            elif card == 10:
                pos = pos - 3
                pos = change_pos_if_necessary(pos)
        elif pos == 30:
            pos = 10
        return pos

    count = dict([(pos, 0) for pos in range(40)])
    count[-1] = 0
    pos = 0
    doubles_count = 0
    for i in range(n):
        if i % 1000 == 0:
            print(i)
        count[pos] += 1
        count[-1] += 1
        dice_1 = random.randint(1, dice_faces)
        dice_2 = random.randint(1, dice_faces)
        if dice_1 == dice_2:
            doubles_count += 1
            if doubles_count == 3:
                doubles_count = 0
                pos = 10
                continue
        else:
            doubles_count = 0
        number = dice_1 + dice_2
        pos = (pos + number) % 40
        pos = change_pos_if_necessary(pos)
    return count


if __name__ == '__main__':
    counts = monopoly_moves(10000000, 4)
    print(counts)
    for pos, count in counts.items():
        print(f"pos {pos}\t-\t{count / counts[-1]}")
    sorted_counts = sorted(counts, key=lambda x: counts[x], reverse=True)
    print([(key, counts[key] / counts[-1]) for key in sorted_counts])

