import csv
import json
import requests
idtoken_list = list()
idtoken_list.append(['id', 'token'])
dict_list = list()
def csv2script():
    url = 'http://localhost:8000/register'
    #taking data from a csv file
    with open("Book2.csv", "r") as csv_obj:
        csv_reader = csv.reader(csv_obj)
        csv_list = list(csv_reader)
        #changing header for json
        headers = ["first_name", "last_name", "password", "email_address", "phone", "eth_password"]
        for line in csv_list[1:]:
            i = 0
            list1 = list()
            data_dict = dict()
            print("Data to be entered: ")
            print(line)
            for str1 in headers:
                data_dict[str1] = line[i]
                i += 1
            dict_list.append(data_dict.copy()) #shallowcopy
            response = requests.post(url, json=data_dict)
            resp = response.json()
            print("Response from server: ")
            print(resp)
            #getting auth token for users and saving it in a list with id
            token = auth(data_dict['password'], data_dict['email_address'])
            id = resp.get('payload').get('id')
            list1 = [id, token]
            idtoken_list.append(list1.copy())
        #writing id and token to a csv file
        with open('Book3.csv', 'w') as csv_write_obj:
            csv_writer = csv.writer(csv_write_obj, delimiter = ',')
            csv_writer.writerows(idtoken_list)
        print("End of script!!!")
        for i in idtoken_list:
            print(i)

def auth(password, email_address):
    url = 'http://127.0.0.1:8000/auth'

    response = requests.post(url, json={
        "password": password,
        "email_address": email_address
    })
    auth_key = response.json()
    print((auth_key))
    #token_list.append(auth_key.get('access_token'))
    return auth_key.get('access_token')
    #return response.json()

def csv2personalinfoapi():
    #url = 'http://127.0.0.1:8000/users/{}/personal_info_details'.format(id_list[0])
    url = 'http://127.0.0.1:8000/users/f7cba7a233214282a300df17da6cbb80/personal_info_details'
    json_data = {
        'info_name':'driving license',
        'identification_number':'dir1'
    }
    token = auth('atmecs@123456', "ceo5@atmecs.com")
    response = requests.post(
        url=url,
        json=json_data,
        headers={"Authorization": "JWT " + token}
    )
    resp = response.json()
    print(resp)

def csv2educationalinfoapi():
    #url = 'http://127.0.0.1:8000/users/{}/personal_info_details'.format(id_list[0])
    url = 'http://127.0.0.1:8000/users/f7cba7a233214282a300df17da6cbb80/education_details'
    json_data = {
        'school':'DPS Hyderabad',
        'degree':'JNTU hyderabad'
    }
    token = auth('atmecs@123456', "ceo5@atmecs.com")
    response = requests.post(
        url=url,
        json=json_data,
        headers={"Authorization": "JWT " + token}
    )
    resp = response.json()
    print(resp)

for i in dict_list:
    print(i)

for i in idtoken_list:
    print(i)
