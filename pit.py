import sys
from commands import helper, add,init

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
        status, messege = init.initialize()
        
        if not status:
            return messege
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    print(main(), end="")
