# import json

# a = {
#     'name':'Elchin',
#     'surname':'Bayramli',
#     'age':21,
#     'married':False,
#     'children':('Ali','Vali'),
#     'data':{
#         'data1':{
#             'name':'Elchin'
#         }
#     }
#     }
# print(a)
# a_json = json.dumps(a, indent=2, sort_keys=True)
# print(a_json)

# a_json = '{"name": "Elchin", "surname": "Bayramli", "age": 21, "married": false, "children": ["Ali", "Vali"]}'
# a_load = json.loads(a_json)
# print(type(a_load))

# with open('my_file1.json','w+', encoding='utf-8') as f:
#     json.dump({"name": "Elçin", "surname": "Bayramli", "age": 21, "married": False, "children": ["Ali", "Vali"]},
#                f, ensure_ascii=False, indent=4)


# with open('my_file1.json','r+') as f:
#    a =  json.load(f)
#    print(a)
