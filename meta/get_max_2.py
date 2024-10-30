
def get_max_two(l):

    cur_max = l[0]
    cur_max_sum = 0

    for i in range(1, len(l) - 1):
        cur_max_sum = max(cur_max_sum, cur_max + l[i + 1])
        cur_max = max(cur_max, l[i])
        print(cur_max_sum, cur_max)

    return cur_max_sum


l = [200, 300, 105, 10, 6]

res = get_max_two(l)
print(res)
