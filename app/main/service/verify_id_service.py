"""verify_id_service.py: Functions called by the route (/client/cle/verification) in id_controller.py"""
__author__ = "Girard Alexandre"

import re # To use regular expressions


# Call a function to verify the ID and generate a JSON feedback
def check_id(id):
    response_object = {
            'status': None,
            'request': id,
            'result': None,
        }
    try:
        if(is_id_valid(id)):
            response_object["status"] = 'successfully finished'
            response_object["result"] = 1
        else:
            response_object["status"] = 'successfully finished - but input not valid format (1 maj letter and 9 numbers expected)'
            response_object["result"] = 0
    except:
        response_object["status"] = 'unsuccessfully finished - an error occured'
        response_object["result"] = 0
    return response_object


def is_id_valid(id):
    if(type(id) != str):
        return False

    regex = re.compile('^([A-P]||Z)[0-9]{9}$')
    if(not regex.match(id)):
        return False

    numbers = id[1:10]
    if(int(numbers) < 10000000):
        total = -1
    else:
        total = 100
        while(total > 15):
            total = 0
            for number in numbers:
                total += int(number)
            numbers = str(total)

    if(alpha_corresponds_to_total(id[0], total+1)):
        return True
    else:
        return False


def alpha_corresponds_to_total(alpha, total):
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
