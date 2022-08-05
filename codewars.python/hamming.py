from heapq import heappush, heappop
from itertools import islice


# https://www.codewars.com/kata/526d84b98f428f14a60008da/python
def generate_hamming_numbers():
    heap = [1]
    while True:
        h = heappop(heap)
        while heap and h == heap[0]:
            heappop(heap)
        for m in [2, 3, 5]:
            heappush(heap, m * h)
        yield h


def hamming(n):
    return list(islice(generate_hamming_numbers(), n))[-1]
