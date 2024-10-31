fridge_1 = [-100, 100]
fridge_2 = [-100, 100]
fridge_in_turn = 1


N = int(input())

substances = []

for substance in range(N):
    substance = [int(x) for x in input().split()]
    substances.append(substance)

def ordered_substances(substances):
    return sorted(substances, key=lambda x: x[0])

ordered_substances_list = ordered_substances(substances)

for substance in ordered_substances_list:
    if fridge_in_turn == 1:
        if substance[0] >= fridge_1[0] and substance[0] <= fridge_1[1]:
            fridge_1[0] = substance[0]
            fridge_1[1] = substance[1]
        else:
            fridge_in_turn = 2
    
    if fridge_in_turn == 2:
        if substance[0] >= fridge_2[0] and substance[0] <= fridge_2[1]:
            fridge_2[0] = substance[0]
            fridge_2[1] = substance[1]
        else:
            fridge_in_turn = 3

if fridge_in_turn == 3:
    print(-1)

else:
    print(f"{fridge_1[0]} {fridge_2[0]}")



    
