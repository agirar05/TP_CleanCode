def checkID(id):
    if(isIDValid(id)):
        response_object = {
            'status': 'success',
            'request': id,
            'result': 1
        }
    else:
        response_object = {
            'status': 'success',
            'request': id,
            'result': 0
        }
    return response_object, 201

def isIDValid(id):
    if(len(id) != 10):
        return False

    if(not isGoodAlphaChar(id[0])):
        return False

    numbers = id[1:10]
    if(not numbers.isnumeric()):
        return False
    
    if(int(numbers) < 10000000):
        total = -1
    else:
        total = 100
        while(total > 15):
            total = 0
            for number in numbers:
                total += int(number)
            numbers = str(total)
    
    if(alphaCorrespondsToTotal(id[0], total+1)):
        return True
    else:
        return False

def isGoodAlphaChar(char):
    goodAlphas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                    "L", "M", "N", "O", "P", "Z"]
    return char in goodAlphas

def alphaCorrespondsToTotal(alpha, total):
    switcher = {
        0: "Z",
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P"
    }
    if(alpha == switcher.get(total, "Invalid number")):
        return True
    else:
        return False