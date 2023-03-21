#!/usr/bin/env python3

from itertools import combinations
from string import ascii_lowercase
import sys

def dfs(current_node):
    if visited[current_node]:
        return
    visited[current_node] = True
    for next_node in adj_graph.get(current_node, []):
        if not visited[next_node]:
            dfs(next_node)
    order.append(current_node)


if __name__ == '__main__':
    for _ in range(int(input())):
        words = [sys.stdin.readline().strip() for _ in range(int(input()))]
        # Make Graph
        adj_graph = {}
        for word_left, word_right in zip(words, words[1:]):
            for char_left, char_right in zip(word_left, word_right):
                if char_left != char_right:
                    adj_graph.setdefault(char_right, set()).add(char_left)
                    break
        # Topological Sort
        visited = {char: False for char in ascii_lowercase}
        order = []
        for char in ascii_lowercase:
            dfs(char)
        # Print Order
        if any(char_left in adj_graph and char_right in adj_graph[char_left]
               for char_left, char_right in combinations(order, 2)):
            print('INVALID HYPOTHESIS')
        else:
            print(''.join(order))
