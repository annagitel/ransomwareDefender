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


def extantion_test(filename):
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
            print("it was not a ascii-encoded unicode string")
            return False
    print("ascii test passed")


def caesar_test():
    print("testing caesar encryption")
    return True


def frequency_test():
    print("testing frequency encryption")
    return True


def last_modified_test():
    print("testing last modification")
    return True


if __name__ == '__main__':

    # dir_str = input("please enter the directory you want to check: ")
    dir_str = "/home/asandler/PycharmProjects/ransomwareDefender/files"
    directory = os.fsencode(dir_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print("-------------------------")
        print(filename)
        print("-------------------------")
        lock_test(dir_str + '/' + filename)
        print("\n")
        extantion_test(filename)
        print("\n")
        ascii_test(dir_str + '/' + filename)
        print("\n")
        caesar_test()
        print("\n")
        frequency_test()
        print("\n")
        last_modified_test()
        print("\n")
