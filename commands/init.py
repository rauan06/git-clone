import os

def initialize():
    """Creates .pit/ directory
    in: None
    return: Message with a state of the program. 
            - Initialized empty Pit repository, if Pit was successfully inittialize
            - Reinitialized existing Git repository, if Pit was already initialized
    """
    path = f'{os.getcwd() + "/.pit"}'

    try:
        os.makedirs(path, exist_ok=True)
        return f"Initialized empty Pit repository in {path}"
    except Exception as e:
        return f"Reinitialized existing Git repository in {path}"