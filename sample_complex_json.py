#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json


class Customer:
    def __init__(self, name, grade, age, home, office):
        self.name = name
        self.grade = grade
        self.age = age
        self.address = Address(home, office)

    def __repr__(self):
        return repr((self.name, self.grade, self.age, self.address.home, self.address.office))


class Address:
    def __init__(self, home, office):
        self.home = home
        self.office = office

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


customers = [
    Customer('john', 'A', 15, '111', 'aaa'),
    Customer('jane', 'B', 12, '222', 'bbb'),
    Customer('dave', 'B', 10, '333', 'ccc'),
]
json_str = json.dumps(customers, default=lambda o: o.__dict__, sort_keys=True, indent=4)
print json_str

oo = json.loads(json_str)
customer_list = []
for c in oo:
    customer_list.append(c)
    print c

customer_list_json = json.dumps(customer_list, default=lambda o: o.__dict__, sort_keys=True, indent=4)
print customer_list_json
