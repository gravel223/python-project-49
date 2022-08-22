#!/usr/bin/env python3
import sys
from cli import welcome_user

def welcome(hello):
    print(hello)

def main():
    welcome("Welcome to the Brain Games!")
    welcome_user

if __name__ == '__main__':
    main()


