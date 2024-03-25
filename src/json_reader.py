import json


def json_reader(json_file_path: str) -> []:

    out = list()
    with open(json_file_path, "r") as f:
        users = json.loads(f.read())

    for u in users:
        out.append(u)

    return out
