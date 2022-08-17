from sys import stdin
from itertools import combinations


def dist_2(p_1, p_2):
    return (p_1[0] - p_2[0])**2 + (p_1[1] - p_2[1])**2


def merge(points_1, points_2):
    points = []
    i, j = 0, 0
    while i < len(points_1) and j < len(points_2):
        if points_1[i][1] <= points_2[j][1]:
            points.append(points_1[i])
            i += 1
        else:
            points.append(points_2[j])
            j += 1
    points.extend(points_1[i:])
    points.extend(points_2[j:])
    return points


def min_dist(points):
    if len(points) <= 3:
        dist = 10**20
        for p_1, p_2 in combinations(points, 2):
            dist = min(dist, dist_2(p_1, p_2))
        return dist, sorted(points, key=lambda point: point[1])
    m = len(points) // 2
    x = points[m][0]
    h, points_1 = min_dist(points[:m])
    h_2, points_2 = min_dist(points[m:])
    if h > h_2:
        h = h_2
    points, h_sq = merge(points_1, points_2), h**0.5
    stripe = [point for point in points if abs(point[0] - x) < h_sq]
    for i, p_1 in enumerate(stripe):
        for j in range(max(i - 7, 0), i):
            dist = dist_2(p_1, stripe[j])
            if h > dist:
                h = dist
    return h, points


def main():
    n = int(input())
    points = []
    for line in stdin:
        x, y = map(int, line.split())
        points.append((x, y))
    points.sort()
    print(min_dist(points)[0]**0.5)


if __name__ == '__main__':
    main()
