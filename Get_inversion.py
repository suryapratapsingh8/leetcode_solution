from typing import List
def numberOfInversions(a : List[int], n : int) -> int:
    # Count the number of pairs:
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                cnt += 1
    return cnt

if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    n = 5
    cnt = numberOfInversions(a, n)
    print("The number of inversions is:", cnt)