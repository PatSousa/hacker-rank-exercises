def number_needed(a, b):
    # Difference of characters from a to b is already counted
    to_change_a = 0
    to_change_b = 0
    # Go char by char and check occurences in other string
    for char in ''.join(set(a)):
        num_occur_a = a.count(char)
        num_occur_b = b.count(char)
        if (num_occur_a - num_occur_b) > 0:
            to_change_a += num_occur_a - num_occur_b

    for char in ''.join(set(b)):
        num_occur_a = a.count(char)
        num_occur_b = b.count(char)
        if (num_occur_b - num_occur_a) > 0:    
            to_change_b += num_occur_b - num_occur_a

    total_changes = to_change_a + to_change_b
    return total_changes

print number_needed(a, b)
