personal_dict = {'name': {'first_name': 'Scott', 'last_name': 'Smajor',
                          'nickname': "Dangthat'salongname"}, 'favourite creatures': {'irl': 'owl', 'fictional': 'elves'},
                 'favourite animals': {'irl': 'owl', 'fictional': 'elves'}}
personal_dict_result = {}
for key, value in personal_dict.items():
    if value not in personal_dict_result.values():
        personal_dict_result[key] = value
print(personal_dict_result)
