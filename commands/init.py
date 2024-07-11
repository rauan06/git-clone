import os

def initialize():
    path = ".pit/"
    if not os.path.exists(path):
        os.mkdir(".pit/")
    else:
        return (False, "You already have initialized pit in this directory.")
    
