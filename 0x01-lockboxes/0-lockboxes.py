#!/usr/bin/env python3

"""
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes
"""

def canUnlockAll(boxes):
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))

    while len(unseen_boxes) > 0:
        index = unseen_boxes.pop()

        if not index or index >= n or index < 0:
            continue
        if index not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[index])
            seen_boxes.add(index)
    return n == len(seen_boxes)
