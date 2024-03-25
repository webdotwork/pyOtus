import json


def json_writer(user_data: []) -> []:

    out = list()
    for user in user_data:
        data = dict(
            name=user["name"],
            gender=user["gender"],
            address=user["address"],
            age=user["age"],
            books=[],
        )
        out.append(data)

    with open("result.json", "w") as f:
        s = json.dumps(out, indent=4)
        f.write(s)

    return out
