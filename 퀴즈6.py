# num = [100,200,300]
def 부가세 (num):
    result = []
    for nums in num:
        sum = int(nums + (nums * 0.1))
        result.append(sum)
    return result

var = [100,200,300]
print(부가세(var))