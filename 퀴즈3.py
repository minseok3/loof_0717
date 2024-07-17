def 학점 (text):
    result = ""
    if 0 <= text <= 20:
        result = "E"
    elif 21 <= text <= 40:
        result = "D"
    elif 41 <= text <= 60:
        result = "C"
    elif 61 <= text <= 80:
        result = "B"
    elif 81 <= text <= 100:
        result = "A"
    return result
var = 학점(int(input("학점을 입력하시오:")))
print(var)