first_dict = {'id1':
                  {'name': 'Ruslan', 'class': 1, 'subjects' :
                      {'Math', 'Algorithms', 'English'}
                   },
              'id2':
                  {'name': 'Mark','class': 2,'subjects' :
                      {'Geometry', 'Java', 'Cooking'}
                   },
              'id3':
                  {'name': 'Ruslan','class': 1, 'subjects' :
                      {'Math', 'Algorithms', 'English'}
                   }
              }
result_dict = {}
print(type(result_dict))
for key, value in first_dict.items():
    if value not in result_dict.values():
        result_dict[key] = value
print(result_dict)