import sys

def main(argv):
    """
    the main function of my rip project
    :type argv: list
    :rtype : int
    :param argv : list of arguments
    :return: 1 for success, otherwise 0
    """
    if sys.platform.startswith("linux"):
        print(argv)
    ## set the flag for using fake data
    elif sys.platform.startswith("darwin"):
        print("use fake data")
    return 1


if __name__ == "__main__":
    quit(main(sys.argv))