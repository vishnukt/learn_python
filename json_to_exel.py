import tablib
import requests
r = requests.get('https://5f717a7064a3720016e60748.mockapi.io/students/students')
students = tablib.Dataset()
students.headers = ['Sl_No', 'Marks', 'Subject', 'Age', 'Name']
if r.status_code == 200:
    s = r.json()
    for i in s:
        # Sl_No, Marks, Subject, Age, Name = i[0],i[1],[2],i[3],i[4]
        # print(i)
        students.append([i['id'], i['marks'], i['subject'], i['age'], i['name']])
    # students.export('xlsx')
    with open('output.xlsx', 'wb') as f:
        f.write(students.export('xlsx'))
