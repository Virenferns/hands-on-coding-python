def find_maxvalue(list, k):
    output = []
    for i in range(0, (len(list) - k)+1):
        total_value = sum(list[i:k])
        k += 1
        output.append(total_value)
    return max(output)

# print(find_maxvalue([-3,4,3,-2,2,5], 4))