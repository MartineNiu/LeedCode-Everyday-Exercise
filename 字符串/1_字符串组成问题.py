def a_b():
    a = input()
    b = input()
    len_a = len(a)
    len_b = len(b)  

    if len_b % len_a != 0:
        return 'No'

    while len_b >0:
        if a != b[:len_a]:
            return 'No'
        else:
            b = b[len_a:]
            len_b = len(b)
    return 'Yes'

result = a_b()
print(result)
        


