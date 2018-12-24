# import bleach
import re
import html
# import json

json_data = '{"name": "abc", "role": "manager", "code":"abcdefg,!awea<"}'
json_data1 = '{"name": "abc", "role": "manager", "code":"<script>Some random script</script>"}'

'''
    Input data must be of type string or json
'''


class JsonDataInvalid(Exception):
    pass


def func1(data):
    '''text = '<h1>This will be our heading</h1>'
    print("before bleach applied: " + text)
    text = bleach.clean(text)
    print("after bleach applied: " + text)'''

    '''bleached_json = bleach.clean(data)
    print(bleached_json)
    invalidChars = set({'&', '<', '>'})
    if any(char in invalidChars for char in bleached_json):
        # your condition goes here
        print("Invalid data")
    else:
        print("Valid data")
    '''
    print(data)
    try:
        substring = '<.*>'
        result = re.search(substring, data)
        if result:
            raise JsonDataInvalid
        else:
            print("Data OK!!!")
            print(html.escape(data))
    except JsonDataInvalid:
        print("Data contains some invalid input!!!")


func1(json_data)
func1(json_data1)
