#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for i in range(0, len(name)):
        if name[i][0] != "_" and name[i][1] != "_":
            print("{}".format(name[i]))
