from __future__ import print_function

import os
import sys


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self,root=None):
        self.root = Node(root)
    def insert(self,data):
        if data <= self.root.data:
            if self.root.left == None:
                self.root.left = Tree(data)
            else:
                self.root.left.insert(data)
        else:
            if self.root.right == None:
                self.root.right = Tree(data)
            else:
                self.root.right.insert(data)

    def insert_new(self,root_data,child_data,child_orientation):
        # print("I",self.root.data,root_data,child_data,child_orientation)
        # if self.root.data == root_data:
        #     if child_orientation == 'L':
        #         self.root.left = Tree(child_data)
        #     if child_orientation == 'R':
        #         self.root.right = Tree(child_data)
        #     return True
        # else:
        #     print("L",self.root.data,self.root.left,self.root.right)
        #     if self.root.left:
        #         self.root.left.insert_new(root_data,child_data,child_orientation)
        #     if self.root.right:
        #         self.root.right.insert_new(root_data,child_data,child_orientation)
        if self.root.data == root_data:
            if child_orientation == 'L':
                self.root.left = Tree(child_data)
            if child_orientation == 'R':
                self.root.right = Tree(child_data)
            # print("Done:",root_data,child_data)
            return True
        else:
            f1 = f2 = False
            if self.root.left:
                f1 = self.root.left.insert_new(root_data,child_data,child_orientation)
            if self.root.right:
                f2 = self.root.right.insert_new(root_data,child_data,child_orientation)
            return f1 or f2
        # if self.root.left == None or self.root.right == None:
        #     if self.root.data == root_data:
        #         if child_orientation == 'L':
        #             self.root.left = Tree(child_data)
        #         if child_orientation == 'R':
        #             self.root.right = Tree(child_data)
        #         # print("Done:",root_data,child_data)
        #         return True
        #     else:
        #         f1 = f2 = False
        #         if self.root.left:
        #             f1 = self.root.left.insert_new(root_data,child_data,child_orientation)
        #         if self.root.right:
        #             f2 = self.root.right.insert_new(root_data,child_data,child_orientation)
        #         return f1 or f2
        # else:
        #     f1 = f2 = False
        #     if self.root.left:
        #         f1 = self.root.left.insert_new(root_data,child_data,child_orientation)
        #     if self.root.right:
        #         f2 = self.root.right.insert_new(root_data,child_data,child_orientation)
        #     return f1 or f2
                # return False



    def buildTreeFromString(self,txt):
        # print(txt,len(txt))
        if len(txt) >= 3:
            subTxt = txt[0:3]
            # print("Here",txt,subTxt)
            root_data,child_data,child_orientation = int(subTxt[0]),int(subTxt[1]),subTxt[2]
            # print(subTxt,root_data,child_data,child_orientation)
            # print(self.root.data)
            if self.insert_new(root_data,child_data,child_orientation):
                self.buildTreeFromString(txt[3:])
            else:
                # print("F",root_data,child_data,child_orientation)
                return False
        else:
            return True

    def mirror(self):
        if self.root.left == None and self.root.right == None:
            return self
        if self.root.left:
            self.root.left.mirror()
        if self.root.right:
            self.root.right.mirror()
        tmp = self.root.left
        self.root.left = self.root.right
        self.root.right = tmp
        return self

    def inOrderTraversal(self):
        if self.root.left:
            self.root.left.inOrderTraversal()
        print(self.root.data,end=' ')
        if self.root.right:
            self.root.right.inOrderTraversal()


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        no_of_edges = int(input())
        txt = input().split(' ')
        # print(txt)
        t = Tree(int(txt[0]))
        # t.insert(5)
        # t.insert(12)
        # t.insert(2)
        # t.insert(4)
        # t.insert(7)
        # t.insert(18)
        # t.insert(11)
        # print(t.root.data)
        # if t.buildTreeFromString(txt):
        #     t.inOrderTraversal()
        #     print()
        #     t.mirror()
        #     t.inOrderTraversal()
        #     print()
        # else:
        #     print("Tree building failed")
        t.buildTreeFromString(txt)
        t.mirror()
        t.inOrderTraversal()
        print()
