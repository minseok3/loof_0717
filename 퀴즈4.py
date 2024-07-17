


def 평균 (num_list):
    result = 0
    for i in num_list:

        result = result + i
        avg = result/len(num_list)
    return avg

var = list(range(1,100))
print(평균(var))