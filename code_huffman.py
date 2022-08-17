class Huffman(list):

    def insert(self, v):
        self.append(v)
        self.sort()

        
    def extract_min(self, D):
        self.insert([self[0][0] + self[1][0], self[0][1] + self[1][1]])
        self[0][0] = '0'
        D.append(self[0])
        self[1][0] = '1'
        D.append(self[1])
        self.remove(self[0])
        self.remove(self[0])


def main():
    s = input()
    frecs = {}
    D = []
    code = {}
    for char in s:
        frecs[char] = frecs.get(char, 0) + 1
    lst = Huffman()
    for char, frec in frecs.items():
        lst.insert([frec, char])
    if len(frecs) == 1:
        for char in frecs.keys():
            D.append(['0', char])
    else:
        for i in range(len(frecs) - 1):
            lst.extract_min(D)
    D.reverse()
    for char in frecs.keys():
        for el in D:
            if char in el[1]:
                code[char] = code.get(char, '') + el[0]
    st = ''
    for char in s:
        st += code[char]
    print(len(frecs), len(st))
    for char, ch_code in code.items():
        print(f'{char}: {ch_code}')
    print(st)


if __name__ == '__main__':
    main()
