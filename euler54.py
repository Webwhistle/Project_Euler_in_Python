import sys, os
from collections import Counter

#Open the txt file as a matrix
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname('euler54.txt')))

with open(os.path.join(__location__, 'euler54.txt')) as f:
    data = [line.split(' ') for line in f.readlines()]

def counter(five_cards):
    occurence_count = Counter(five_cards)
    value = occurence_count.most_common(1)[0][0]
    counter = 0
    for i in five_cards:
        if i == value:
            counter+=1
    return counter, value

def hand_detection(five_cards):
    suits = [card[1] for card in five_cards]
    values = [card[0] for card in five_cards]
    values = [item.replace("T","10") for item in values]
    values = [item.replace("J","11") for item in values]
    values = [item.replace("Q","12") for item in values]
    values = [item.replace("K","13") for item in values]
    if len(list(set(suits))) == 1:
        values.sort()
        if values == ["2","3","4","5","A"]:
            "Straight flush, Ace low"
            return [9, (max(values))]
        else:
            values = [item.replace("A","14") for item in values]
            values = [int(value) for value in values]
            if max(values) - min(values) == 4:
                "Straight flush, Ace high"
                return [9, (max(values))]
            else:
                "Flush"
                return [6, max(values)]
    elif len(list(set(values))) == 5:
        values1 = [item.replace("A","1") for item in values]
        values1 = [int(value) for value in values1]
        if max(values1) - min(values1) == 4:
            "Straight, Ace low"
            return [5, max(values1)]
        values2 = [item.replace("A","14") for item in values]
        values2 = [int(value) for value in values2]
        if max(values2) - min(values2) == 4:
            "Straight, Ace high"
            return [5, max(values2)]
        else:
            "High card"
            return [1, max(values2)]
    elif len(list(set(values))) == 4:
        values = [item.replace("A","14") for item in values]
        values = [int(value) for value in values]
        "Pair"
        return [2, int(counter(values)[1])]
    elif len(list(set(values))) == 3:
        values = [item.replace("A","14") for item in values]
        values = [int(value) for value in values]
        if counter(values)[0] == 3:
            "Three of a kind"
            return [4, counter(values)[1]]
        else:
            least_common = Counter(values).most_common()[-1][0]
            values.remove(least_common)
            "Two pair"
            return [3, max(values)]
    elif len(list(set(values))) == 2:
        if Counter(values).most_common()[-1][1] == 1:
            "Four of a kind"
            return [8, max(values)]
        else:
            "Full house"
            return [7, max(values)]

def hand_comparison(ten_cards):
    hand_one, hand_two = ten_cards[0:5], ten_cards[5:10]
    if hand_detection(hand_one)[0] == hand_detection(hand_two)[0]:
        if hand_detection(hand_one)[1] > hand_detection(hand_two)[1]:
            return 1
        else:
            return 2
    else:
        if hand_detection(hand_one)[0] > hand_detection(hand_two)[0]:
            return 1
        else:
            return 2

player_one = 0
player_two = 0
for i in range(1000):
    if hand_comparison(data[i]) == 1:
        player_one +=1
    if hand_comparison(data[i]) == 2:
        player_two +=1

print(player_one, player_two)
