#!/usr/bin/python3
def magic_calculation(a, b):
    import sys
    try:
        result = fct(*args)
        return result
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return(None)
    except TypeError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return(None)
    except NameError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return(None)
    except ZeroDivisionError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return(None)
    except IndexError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return(None)
