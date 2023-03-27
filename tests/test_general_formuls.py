from course_12_2.general_formuls import correct_date, user_card, final_information, sort
import pytest

def test_correct_date():
    assert correct_date('2018-03-23T10:45:06.972075') == '23 03 2018'
    assert correct_date('2019-03-23T01:09:46.296404') == '23 03 2019'
    assert correct_date('2019-07-12T20:41:47.882230') == '12 07 2019'
    assert correct_date('2018-04-04T17:33:34.701093') == '04 04 2018'


def test_user_card():
    assert user_card('Счет 10848359769870775355') == 'Счет **5355'
    assert user_card('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
    assert user_card('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'

def test_final_information():
    dr = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
    }

    final= '26 08 2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.'

    assert final_information(dr) == final

def test_1_user_card():
    assert user_card('') == ''

def test_1_final_information():
    dr_1 = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2018-03-23T10:50:58.294041",
    "operationAmount": {
        "amount": "48223.05",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Открытие вклада",
    "to": "Счет 64686473678894779589"
    }

    final_1 = '23 03 2018 Открытие вклада\nСчет **9589\n48223.05 руб.'

    assert final_information(dr_1) == final_1

def test_sort():
    dict =[
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075"
    },
    {
        "id": 214024827,
        "state": "Open",
        "date": "2018-12-20T16:43:26.929246"
    },
    {
        "id": 863064926,
        "state": "Open",
        "date": "2019-12-08T22:46:21.935582"
    }
    ]

    sort_dict = [
         {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075"
         },
    ]

    assert sort(dict) == sort_dict


