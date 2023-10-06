#!/usr/bin/python3

"""
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes
"""

def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited[current_box] = True

    for key in boxes[current_box]:
        if key >= 0 and key < n and not visited[key]:
            stack.append(key)

    return all(visited)
