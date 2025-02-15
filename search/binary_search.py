"""
* bianry search (이진 탐색)
- 정렬된 배열에서 특정한 값의 위치를 찾는 알고리즘
- 배열의 중간 값과 찾으려는 값을 비교하여, 중간 값이 찾으려는 값보다 크면 왼쪽을, 작으면 오른쪽을 탐색
- 시간 복잡도: O(logN)
- return: 찾으려는 값의 인덱스 (없으면 None)
- python library: bisect
    - https://dduniverse.tistory.com/entry/python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-bisect-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
"""
def bianry_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) -1
    mid = (low + high) // 2
    if high >= low:
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            return bianry_search(arr, target, low, mid-1)
        if arr[mid] < target:
            return bianry_search(arr, target, mid+1, high)
    return None

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(bianry_search(arr, 7)) # 3
    print(bianry_search(arr, 13)) # 6
    print(bianry_search(arr, 20)) # None