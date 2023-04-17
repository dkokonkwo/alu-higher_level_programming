#!/usr/bin/python3
"""
Python script to send request to given URL
and display body of response, decoded
also handles urllib.error.HTTPError exception
"""


if __name__ == "__main__":
    from urllib import request, error
    from sys import argv
    try:
        with request.urlopen(argv[1]) as requested:
            content = requested.read()
            print(content.decode("UTF-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
