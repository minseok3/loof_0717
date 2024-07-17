
def 홀짝 (num):
    result = ""
    if num % 2 == 0:
        result = "짝수"
    else:
        result = "홀수"
    return result
var = int(input("숫자를 입력하세요:"))
print(홀짝(var))