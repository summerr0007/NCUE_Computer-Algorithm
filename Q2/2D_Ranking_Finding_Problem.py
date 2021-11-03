import logging
import sys

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

points = []
buffer = []
ranks = []


class filereader:
    def __init__(self, path) -> None:
        self.path = path

    def __call__(self):
        try:
            self.testfile = open(self.path, "r")
            lines = self.testfile.readlines()
            lines = [line.strip().split(' ') for line in lines]
            return self.topoint(lines)
        except Exception as e:
            logger.critical(e)
            exit()

    def topoint(self, a):
        return [point(val[0], val[1], idx) for idx, val in enumerate(a)]


class point:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y > other.y

    def __str__(self) -> str:
        return f"point ({self.x},{self.y}) at {self.index} "


def heapsort(lst):
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst


def Rank2D(lower, upper):
    if upper - lower <= 1:
        return
    middle = (int)((upper+lower)/2)

    counts = 0
    i = lower
    j = middle
    k = lower
    Rank2D(lower, middle)
    Rank2D(middle, upper)
    while(i < middle or j < upper):
        if i == middle:
            buffer[k] = points[j]
            ranks[buffer[k].index] += counts
            j += 1
            k += 1
        elif j == upper:
            buffer[k] = points[i]
            i += 1
            k += 1
        elif points[i].y < points[j].y:
            buffer[k] = points[i]
            counts += 1
            i += 1
            k += 1
        else:
            buffer[k] = points[j]
            ranks[buffer[k].index] += counts
            j += 1
            k += 1

    for q in range(lower, upper):
        points[q] = buffer[q]


if __name__ == "__main__":
    points = filereader("test2.txt")()
    o_points = points.copy()
    buffer = [point(0, 0, 0) for i in range(0, len(points))]
    ranks = [0 for i in range(0, len(points))]
    # for a in points:
    #     print(a)

    # print("*******************************************************************")
    Rank2D(0, len(points))
    for a in zip(o_points, ranks):
        print(a[0], "rank is ", a[1])

    print(f"total = {len(points)} \n")
    print(f"max rank = {max(ranks)}\n")
    print(f"min rank = {min(ranks)}\n")
    print(f"average rank = {round(sum(ranks)/len(ranks)):.2f}\n")

# for a in buffer:
#     print(a)
# print(ranks)
