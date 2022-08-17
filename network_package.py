from sys import stdin


class Processor(list):

    def __init__(self, size):
        self.size = size

        
    def push(self, arrival, duration):
        if not self:
            self.append(arrival + duration)
            return arrival
        m = max(self[-1], arrival)
        if len(self) < self.size or len(self) == self.size and self[0] <= arrival:
            self.append(m + duration)
            if len(self) > self.size:
                self.pop(0)
            return m
        return -1


def main():
    size, n = map(int, input().split())
    S = Processor(size)
    for line in stdin:
        arrival, duration = map(int, line.split())
        print(S.push(arrival, duration))


if __name__ == '__main__':
    main()
