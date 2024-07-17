# def 구구단 (number):
#     num = number
#     count = 0
#     while count < 9:
#         count = count + 1
#         r = num * count
#         print(num, "X",count ,"=", r)
#
# 구구단(2)

def 구구단2 (a=input("숫자를 입력하세요:")):
    for e in range(1,10):
        print(a, "X",e ,"=", int(a)*e)

구구단2
