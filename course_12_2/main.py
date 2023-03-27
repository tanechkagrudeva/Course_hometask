import json
from general_formuls import sort, final_information


filename = "operations.json"

def do_info_():
    with open(filename, "r", encoding='utf-8') as file:
        data = json.load(file)

    data = sort(data)

    for item in range(5):
       print(final_information(data[item]))
       print()

if __name__ == '__main__':
    do_info_()