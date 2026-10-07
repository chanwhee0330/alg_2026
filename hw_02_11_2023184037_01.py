"""실습 과제 1: O(n^2) 기초 정렬 알고리즘 3개를 구현한다."""
def heap_sort(array):
    n = len(array)

    def heapify(size, root):
        largest = root
        left = root*2+1
        right = root*2 +2

        if left <size and array[left]>array[largest]:
            largest = left
        if right < size and array[right]>array[largest]:
            largest = right

        if largest != root:
            array[root],array[largest] = array[largest],array[root]

            heapify(size,largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for end in range(n - 1, 0, -1):
        array[0], array[end] = array[end], array[0]
        heapify(end, 0)


    return array

def count_sort(array):
    arr = array
    count = [0] * 47
    for i in arr:
        count[i] += 1

    index = 0

    for number in range(len(count)):
        for _ in range(count[number]):
            array[index]=number
            index += 1
    return array
 

if __name__ == "__main__":

    data = [11, 46, 33, 1, 6, 37, 8, 33, 10, 33, 17, 27, 15, 24]

 

    heap_data = list(data)

    print("Heap Sort")

    print("정렬 전:", heap_data)

    heap_sort(heap_data)

    print("정렬 후:", heap_data)

    print()

 

    count_data = list(data)

    print("Count Sort")

    print("정렬 전:", count_data)

    count_sort(count_data)

    print("정렬 후:", count_data)

    print()

 
