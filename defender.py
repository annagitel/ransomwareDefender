import os


def lock_test(filepath):
    print("Testing if file is locked")
    try:
        f = open(filepath, 'r')
    except IOError:
        print("file is locked")
        return False

    print("lock test passed")
    return True


def extention_test(filename):
    print("testing if filename is valid")
    arr = filename.split('.')
    if len(arr) != 2:
        "file name is not OK!"
        return False

    if arr[1] != 'txt':
        "file extantion is not OK!"
        return False

    print("filename test passed")
    return True


def ascii_test(filepath):
    print("testing if file content is ASCII encoded")
    f = open(filepath, 'r')
    lst = f.readlines()
    for line in lst:
        if not line.isascii():
            print("it was not a ascii-encoded unicode string ")
            return False
    print("ascii test passed")


if __name__ == '__main__':
    dir_str = input("please enter the directory you want to check or press ENTER to check in the current directory: ")
    if dir_str == "":
        directory = os.getcwd()
        dir_str = str(directory)
    else:
        directory = os.fsencode(dir_str)

    print(f"going over : {str(directory)}")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename != 'defender.py':
            ans = True
            print("-------------------------")
            print(filename)
            print("-------------------------")
            ans = lock_test(dir_str + '/' + filename)
            print("\n")
            ans = extention_test(filename)
            print("\n")
            ans = ascii_test(dir_str + '/' + filename)

            if not ans:
                print(f"!!! {filename} FILE IS ENCRYPTED !!!!")
