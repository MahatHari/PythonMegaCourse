import json

with open('file3.txt') as json_file:
    data = json.load(json_file)
print('DATA', data)

data["metals"]["gold"] = {

    "conductivity": 33.5,

    "density": 0.255,

    "heat": 0.129,

    "melting point": 2171,

    "thermal expansion": 4.7,

    "yield strength": 288,

    "tensile strength": 441,

    "minimum impact energy": 22,

}

with open('file3.txt', 'w') as file:
    json.dump(data, file)


# loading file and multiplying by 2
