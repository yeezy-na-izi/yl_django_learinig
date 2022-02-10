import requests


def dwarf_pest(port, host, **kwargs):
    data = requests.get(f"http://{host}:{port}").json()
    if kwargs["place"] not in data:
        data[kwargs["place"]] = [dict(list(kwargs.items()))]
    else:
        data[kwargs["place"]].append(dict(list(kwargs.items())))
    return data
