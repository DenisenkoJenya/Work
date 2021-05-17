from functions import students_from_kunger, mans_from_Kungur, mans_rating_from_Kungur, names_not_from_Perm, select_all_sorted

names = students_from_kunger()
for name in names:
    print(name['nameStud'])

names = mans_from_Kungur()
for name in names:
    print(name['nameStud'])

names = mans_rating_from_Kungur()
for name in names:
    print(name['nameStud'], name['rating'])

names = names_not_from_Perm()
for name in names:
    print(name['nameStud'])

names = select_all_sorted()
for name in names:
    print(name['nameStud'])
