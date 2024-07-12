import os

def initialize():
    """Creates .pit/ directory and initializes a basic repository structure."""
    base_path = os.path.join(os.getcwd(), ".pit")

    dir_paths = [
        "objects",
        "logs",
        "info",
        "branches",
        "hooks",
        "refs",
    ]

    file_paths = [
        "config",
        "description.txt",
        "HEAD.txt",
        "index.txt",
        "packed-refs.txt",
    ]

    try:
        os.makedirs(base_path, exist_ok=True)

        for dir_name in dir_paths:
            os.makedirs(os.path.join(base_path, dir_name), exist_ok=True)
        
        for file_name in file_paths:
            file_path = os.path.join(base_path, file_name)
            open(file_path, 'w').close()

        return f"Initialized empty Pit repository in {base_path}"
    except FileExistsError:
        return f"Reinitialized existing Pit repository in {base_path}"
    except Exception as e:
        return f"Failed to initialize Pit repository: {str(e)}"
