import os

def initialize():
    path = f'{os.getcwd() + "/.pit"}'

    try:
        os.makedirs(path, exist_ok=True)
        return (True, f"Initialized empty Pit repository in {os.getcwd()}/.pit/")
    except Exception as e:
        return (False, f"Reinitialized existing Git repository in {os.getcwd()}/.pit/")