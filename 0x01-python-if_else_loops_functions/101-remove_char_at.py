def remove_char_at(str, n):
    new_str = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            new_str += str[i]
    return new_str
