from itertools import permutations

data = [int(x) for x in input().split()]
N = data[0]
M = data[1]
x = int((N-1)/2)

numbers = []

def swaps_to_first(list, swaps):

    if(len(list) != 1):

        wished_positions = sorted(list)

        real_i_position = list.index(wished_positions[0])
        swaps =  swaps + abs(0-real_i_position)
        
        swaps_to_first(list[1:], swaps)
    else:
        return int(swaps)



for i in range(1, N+1):
    numbers.append(i)

permutations = list(permutations(numbers))

for i in range(len(permutations)):
    permutations[i] = list(permutations[i])

total_swaps = 0

def count_to_succes(list):
    swaps = 0
    max_position = list.index(N)
    swaps = swaps + int((abs(x-max_position)))

    swaps = swaps + swaps_to_first(list[:x], 0)
    swaps = swaps + swaps_to_first(list[x +1 :], 0)

    


    return int(swaps)





for numbers_iteration in permutations:
    total_swaps = total_swaps + count_to_succes(numbers_iteration)

print(total_swaps % M)