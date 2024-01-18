#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1
    args = sys.argv[1:]

    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_args, "" if num_args == 1 else "s"))

    for i in range(num_args):
        print("{}: {}".format(i + 1, args[i]))
