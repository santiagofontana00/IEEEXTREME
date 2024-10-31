data = [int(x) for x in input().split()]
L = data[0]
A = data[1]

def maximize_number(n, k):
    # Convert N to a list of characters for easier manipulation
    n = list(str(n))
    max_number = int(''.join(n))  # Start with the initial number

    # Recursive helper function to perform swaps
    def backtrack(s, swaps_left):
        nonlocal max_number

        # Update max_number with current configuration if it's larger
        max_number = max(max_number, int(''.join(s)))

        # Stop recursion if no swaps are left
        if swaps_left == 0:
            return

        length = len(s)
        # Attempt to maximize the current configuration by swapping
        for i in range(length - 1):
            for j in range(i + 1, length):
                # Only swap if it creates a larger number or we are still searching
                if s[j] > s[i]:
                    # Swap characters at i and j
                    s[i], s[j] = s[j], s[i]

                    # Recursive call after the swap
                    backtrack(s, swaps_left - 1)

                    # Undo swap (backtrack)
                    s[i], s[j] = s[j], s[i]

    # Start backtracking with the initial number as a list and k swaps
    backtrack(n, k)
    return max_number

print(maximize_number(L, A))