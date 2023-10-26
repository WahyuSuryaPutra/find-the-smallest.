def smallest(n):
    n_str = str(n)
    smallest_num = n
    i, j = 0, 0

    for index_i in range(len(n_str)):
        digit_i = n_str[index_i]
        temp_str = n_str[:index_i] + n_str[index_i + 1:]

        for index_j in range(len(temp_str) + 1):
            new_str = temp_str[:index_j] + digit_i + temp_str[index_j:]
            new_num = int(new_str)

            if new_num < smallest_num:
                smallest_num = new_num
                i, j = index_i, index_j

    return [smallest_num, i, j]

# Test cases
print(smallest(261235))  # Output: [126235, 2, 0]
print(smallest(209917))  # Output: [29917, 0, 1]
print(smallest(1000000))  # Output: [1, 0, 6]