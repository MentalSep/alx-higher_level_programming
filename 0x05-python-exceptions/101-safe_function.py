#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as ErrorMessage:
        import sys
        print("Exception: {}".format(ErrorMessage), file=sys.stderr)
        result = None
    return result
