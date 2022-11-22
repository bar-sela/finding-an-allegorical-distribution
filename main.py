# This is a sample Python script.
import copy


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import random

import search


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list = []
    print("enter the number of different stuff: ")
    numberOfstuffFromUser = input()
    numberOfstuffFromUser = int(numberOfstuffFromUser)
    for i in range(0, numberOfstuffFromUser):
        print("enter stuff number " + str(i) + " value:")
        stuffValue = input()
        list.append(int(stuffValue))
    root = search.Node()
    print("enter : 1 -for Section A :"
          + "2 -for Section B ")
    input = input()
    print("the division's are: ")
    if int(input) == 1:
        listAns = search.dfs(list, numberOfstuffFromUser, root, 0)
    elif int(input) == 2:
        listAns = search.dfs2(list, numberOfstuffFromUser, root, 0, [])
    print("***********")
    print("The egalitarian division is:")
    print(listAns)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
