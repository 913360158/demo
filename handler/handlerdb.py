debian = {
    "project": "successful ：model is running"
}


def produce(action_name):
    global debian
    try:
        handler = debian.get(action_name)
    except KeyError as e:
        print(str(e))
        handler = "NotFindModel"
    return handler
