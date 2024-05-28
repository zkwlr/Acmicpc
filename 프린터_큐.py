# S3
import sys
from collections import deque

input = sys.stdin.readline

test_cases = int(input())

for _ in range(test_cases):
    print_order = 0
    num_docs, target_index = map(int, input().split())
    documents = [[int(x), 0] for x in input().split()]
    documents[target_index][1] = 1  # Mark the target document
    documents = deque(documents)
    while True:
        priorities = [doc[0] for doc in documents]  # Extract the priorities
        if documents[0][0] == max(
            priorities
        ):  # If the first document is the highest priority
            print_order += 1
            if documents[0][1] == 1:  # If the first document is the target
                print(print_order)
                break

            documents.popleft()  # Remove the printed document
        else:
            documents.rotate(-1)  # Move the first document to the end
