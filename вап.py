import random

N = int(input())

arr = [random.randint(0, 5) for _ in range(N)]

print(" ".join(map(str, arr)))

index_dict = {}

for i, num in enumerate(arr):
    if num not in index_dict:
        index_dict[num] = [i]
    else:
        index_dict[num].append(i)
        duplicates_found = True

if 'duplicates_found' in locals():
    print("YES")

else:
    print("NO")
