import sys
from commands import helper, add, init
from helpers import flags

def main():
    if len(sys.argv) < 2:
        print("Usage: pit <command> [<args>]")
        return

    command = sys.argv[1]
    
    if command == '--help' or command == 'help':
        helper.run()
    elif command == 'add':
        add.run()
    elif command == 'init':
        messege = init.initialize()
        
        return messege
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    print(main())
