
def 길이 (text):
    result = 0
    if len(text) <= 20:
        result = 50
    elif len(text) > 20:
        result = 100
    return result

var = 길이("asdsadsadasdasasdasdasdsadasdasdasdas")
print(var)