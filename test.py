import csv
from collections import defaultdict
from pprint import pprint


user_id_list = []
with open('users.csv', 'r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)
    while True:
        row = next(csv_dict_reader, 'end')
        if row == 'end': break
        if row['is_active'] == 'True':
            user_id_list.append(row['user_id'])

_dict = defaultdict(dict)
with open('transactions.csv', 'r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)
    while True:
        row = next(csv_dict_reader, 'end')
        if row == 'end': break
        if row['user_id'] in user_id_list:
            if row['is_blocked'] == 'False':
                cat_id = int(row['transaction_category_id'])
                if cat_id not in _dict: _dict[cat_id] = {'users': set()}
                _dict[cat_id]['users'].add(row['user_id'])
                _dict[cat_id]['amount'] = _dict[cat_id].get('amount', 0) \
                    + float(row['transaction_amount'])

result_list = [
	(id, stat['amount'], len(stat['users'])) for id, stat in _dict.items()
]
result_list.sort(key=lambda a: a[1], reverse=True)
pprint(result_list)