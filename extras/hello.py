#!/usr/bin/env python
import getpass

USERNAME = getpass.getuser()

def main():
    print('hello', USERNAME)

if __name__ == '__main__':
    main()
