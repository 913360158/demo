debian = {
    "project": "None"
}

def produce(action_name):
    global factory
    try:
        handler = debian[action_name]
        handler.action = action_name
    except KeyError as e:
        print(str(e))
        handler = "KeyError"
    return handler