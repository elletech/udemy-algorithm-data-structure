import heapq
from collections import Counter
from typing import List


def top_n_with_head(words: List[str], n: int) -> List[str]:
    # d = {}
    # for word in words:
    #     d[word] = d.get(word, 0) + 1
    counter_word= Counter(words)
    data = [(-counter_word[word], word) for word in counter_word]
    heapq.heapify(data)
    return [heapq.heappop(data)[1] for _ in range(n)]


if __name__ == '__main__':
    w = ['python', 'c', 'java', 'go', 'python', 'c', 'go', 'python']
    print(top_n_with_head(w, 3))
