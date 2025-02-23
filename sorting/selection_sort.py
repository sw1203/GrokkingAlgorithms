"""
* Selection Sort (선택 정렬)
- 가장 작은 값을 찾아 가장 앞에 값과 비교하여 교환해 나가는 방식
- 상세 과정
    - 주어진 리스트에서 가장 작은 값을 찾는다.
    - 그 값을 맨 앞에 위치한 값과 교환한다.
    - 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교환한다.
- 시간 복잡도: O(N^2)
- return: 오름차순된 리스트
"""

def selection_sort(arr: list):
    for idx, item in enumerate(arr):
        min_idx = idx
        for j in range(idx+1, len(arr)):
            if arr[j] < item:
                min_idx = j
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
    return arr

if __name__ == "__main__":
    arr = [3, 4, 2, 1, 5]
    print(selection_sort(arr)) # [1, 2, 3, 4, 5]
    arr = [1, 1, 0, 0, 1]
    print(selection_sort(arr)) # [0, 0, 1, 1, 1]
