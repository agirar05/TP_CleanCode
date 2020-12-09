"""create_id_service.py: Functions called by the route (/client/cle/creation) in id_controller.py"""
__author__ = "Girard Alexandre"

import re  # To use regular expressions


# Call a function to create an ID and generate a JSON feedback
def create_id(id):
    response_object = {
            'status': None,
            'request': id,
            'result': None,
        }
    try:
        if(input_is_valid(id)):
            complete_id = create_complete_id(id)
            response_object["status"] = 'successfully finished'
            response_object["result"] = complete_id
        else:
            response_object["status"] = 'successfully finished - but input not valid format (9 numbers expected)'
            response_object["result"] = 'null'
    except:
        response_object["status"] = 'unsuccessfully finished - an error occured'
        response_object["result"] = 'null'
    return response_object


def input_is_valid(id_to_check):
    if(type(id_to_check) != str):
        return False

    regex = re.compile('^[0-9]{9}$')
    if(regex.match(id_to_check)):
        return True
    else:
        return False


def create_complete_id(id):
    numbers = id
    if(int(numbers) < 10000000):
        total = -1
    else:
        total = 100
        while(total > 15):
            total = 0
            for number in numbers:
                total += int(number)
            numbers = str(total)

    letter = get_letter_by_total(total+1)
    return letter + id


def get_letter_by_total(total):
    letter_by_total = {
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
    return letter_by_total[total]
