import traceback
import time


def foo():
    f = open('test/testfile2', 'w')
    f.write('Test write this')
    print("Content written successfully")
    f.close()


try:
    foo()
except FileNotFoundError as err:
    print('...')
except OSError as err:
    # This will only check for an IOError exception and then execute this print statement
    print(f"Error: {err} Could not find file or read data")
    print(traceback.format_exc())


