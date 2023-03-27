
def sort(data):
    user_info = []
    for item in data:
        if item.get('state') == "EXECUTED":
            user_info.append(item)
    user_info.sort(key=lambda x: x.get('date'), reverse=True)
    return user_info


def correct_date(new_date):
    corr_date = new_date[0:10].split('-')
    return corr_date[2] + " " + corr_date[1] + " " + corr_date[0]


def final_information(point):
    new_date = correct_date(point.get('date'))
    description = point.get('description')
    from_user = user_card(point.get('from'))
    to_user = user_card(point.get('to'))
    user_operation = point.get('operationAmount').get('amount')
    user_currency = point.get('operationAmount').get('currency').get('name')

    if from_user:
        return f'{new_date} {description}\n{from_user} -> {to_user}\n{user_operation} {user_currency}'
    else:
        return f'{new_date} {description}\n{to_user}\n{user_operation} {user_currency}'


def user_card(user_card):
    if not user_card:
        return ''
    card = user_card.split(' ')
    if card[0] == "Счет":
        return f'Счет **{card[1][16:]}'
    return f'{" ".join(card[:-1])} {card[-1][:4]} {card[-1][4:6]}** **** {card[-1][12:]}'


