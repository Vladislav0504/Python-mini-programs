from sys import stdin


class Node:

    def __init__(self, key=None):
        self.lt = None
        self.rt = None
        self.key = key
        self.h = 0
        self.sum = key
        self.numb_v = 1


class BinarySearchTree(Node):
    root = None


    def correct(self, v):
        if v:
            v.sum = v.key
            v.numb_v = 1
            v.h = 0
            if v.lt:
                v.h = 1 + v.lt.h
                v.numb_v += v.lt.numb_v
                v.sum += v.lt.sum
            if v.rt:
                v.h = max(v.h, 1 + v.rt.h)
                v.numb_v += v.rt.numb_v
                v.sum += v.rt.sum


    def rotate(self, child, par):
        if child == par.lt:
            par.lt = child.rt
            child.rt = par
        else:
            par.rt = child.lt
            child.lt = par
        self.correct(par)
        self.correct(child)
        if self.root.key == par.key:
            self.root = child
        return child


    def balance(self, v):
        if v:
            self.correct(v)
            if v.lt and (not v.rt and v.lt.rt or v.rt and v.lt.lt and v.lt.h - v.rt.h == 2 and v.lt.h - v.lt.lt.h == 2):
                v.lt = self.rotate(v.lt.rt, v.lt)
            elif v.rt and (not v.lt and v.rt.lt or v.lt and v.rt.rt and v.rt.h - v.lt.h == 2 and v.rt.h - v.rt.rt.h == 2):
                v.rt = self.rotate(v.rt.lt, v.rt)
            if v.lt and v.lt.lt and (not v.rt or v.rt and v.lt.h - v.rt.h == 2 and v.lt.h - v.lt.lt.h == 1):
                v = self.rotate(v.lt, v)
            elif v.rt and v.rt.rt and (not v.lt or v.lt and v.rt.h - v.lt.h == 2 and v.rt.h - v.rt.rt.h == 1):
                v = self.rotate(v.rt, v)
        return v


    def insert(self, v, x):
        if v is None:
            if self.root == v:
                self.root = Node(x)
            return Node(x)
        if x < v.key:
            v.lt = self.insert(v.lt, x)
        elif x > v.key:
            v.rt = self.insert(v.rt, x)
        return self.balance(v)


    def exists(self, v, x):
        if v is None:
            return 'false'
        elif v.key == x:
            return 'true'
        elif x < v.key:
            return self.exists(v.lt, x)
        return self.exists(v.rt, x)


    def min_tree(self, v):
        if v and v.lt:
            return self.min_tree(v.lt)
        return v


    def max_tree(self, v):
        if v and v.rt:
            return self.max_tree(v.rt)
        return v


    def next_tree(self, v, x):
        cur = 'none'
        while v:
            if v.key > x:
                cur = v.key
                v = v.lt
            else:
                v = v.rt
        return cur


    def prev_tree(self, v, x):
        cur = 'none'
        while v:
            if v.key < x:
                cur = v.key
                v = v.rt
            else:
                v = v.lt
        return cur


    def k_max(self, v, k):
        if v is None:
            return None
        s = 0 if v.rt is None else v.rt.numb_v
        if s >= k:
            return self.k_max(v.rt, k)
        elif s + 1 == k:
            return v.key
        return self.k_max(v.lt, k - s - 1)


    def delete(self, v, x):
        if v is None:
            return None
        if v.key == x:
            if v.rt:
                v.key = self.next_tree(v.rt, x)
                v.rt = self.delete(v.rt, v.key)
            elif v.lt:
                if v == self.root:
                    self.root = v.lt
                return v.lt
            else:
                if v == self.root:
                    self.root = None
                return None
        elif x < v.key:
            v.lt = self.delete(v.lt, x)
        else:
            v.rt = self.delete(v.rt, x)
        return self.balance(v)


    def sum_tree(self, v, lt, rt):
        s = 0
        while v:
            if v.key > rt:
                v = v.lt
            elif v.key < lt:
                v = v.rt
            else:
                break
        v_lt, v_rt = v, v
        while v_rt:
            if v_rt.key <= rt:
                s += v_rt.sum
                while v_rt and v_rt.key <= rt:
                    v_rt = v_rt.rt
            else:
                s -= v_rt.sum
                while v_rt and v_rt.key > rt:
                    v_rt = v_rt.lt
        while v_lt and v_lt.key >= lt:
            v_lt = v_lt.lt
        while v_lt:
            if v_lt.key >= lt:
                s += v_lt.sum
                while v_lt and v_lt.key >= lt:
                    v_lt = v_lt.lt
            else:
                s -= v_lt.sum
                while v_lt and v_lt.key < lt:
                    v_lt = v_lt.rt
        return s


def f(x, s):
    return (x + s) % 1000000001


def main():
    #s = 0
    tree = BinarySearchTree()
    n = int(input())
    for line in stdin:
        command, x = line.split()
        if command == '+1' or command == '1':
            tree.insert(tree.root, int(x))
        elif command == '-1':
            tree.delete(tree.root, int(x))
        else:
            print(tree.k_max(tree.root, int(x)))


if __name__ == '__main__':
    main()
