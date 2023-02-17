# python3

from collections import namedtuple
import os

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"


def main():
    choice = input()
    if choice in "F":
        os.chdir('/Users/Ricis/github-classroom/DA-testa/steks-un-iekavas-RitvarsZuns/test')
        file_names = ["0", "1", "2", "3", "4", "5",]
        for file_name in file_names:
            with open(file_name, 'r') as f:
                text = f.readline().strip()
                mismatch = find_mismatch(text)
                print(mismatch)
    elif choice in "I":
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch)
    else:
        print("Invalid choice, please try again.")



if __name__ == "__main__":
    main()
