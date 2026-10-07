"""실습 과제 1: O(n^2) 기초 정렬 알고리즘 3개를 구현한다."""

 

 

def bubble_sort(array):

    """인접한 두 원소를 비교하며 큰 값을 오른쪽으로 보낸다."""

    # TODO: 버블 정렬을 구현한다.

    # 함수는 새 리스트를 만들지 않고, 전달받은 array를 직접 정렬해야 한다.
    list = array
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    pass

 

 

def selection_sort(array):

    """정렬되지 않은 구간의 최솟값을 찾아 왼쪽에 놓는다."""

    # TODO: 선택 정렬을 구현한다.

    # 함수는 새 리스트를 만들지 않고, 전달받은 array를 직접 정렬해야 한다.
    list = array
    for i in range(len(list)):
        min =i
        for j in range(i+1,len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]

    pass

  

def insertion_sort(array):

    """왼쪽의 정렬된 구간에 다음 원소를 알맞은 위치로 삽입한다."""

    # TODO: 삽입 정렬을 구현한다.

    # 함수는 새 리스트를 만들지 않고, 전달받은 array를 직접 정렬해야 한다.
    list = array
    for i in range(1,len(list)):
        key =list[i]
        j=i-1
        while j>=0 and list[j]>key:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    pass

 

 

if __name__ == "__main__":

    data = [11, 46, 33, 1, 6, 37, 8, 33, 10, 33, 17, 27, 15, 24]

 

    bubble_data = list(data)

    print("Bubble Sort")

    print("정렬 전:", bubble_data)

    bubble_sort(bubble_data)

    print("정렬 후:", bubble_data)

    print()

 

    selection_data = list(data)

    print("Selection Sort")

    print("정렬 전:", selection_data)

    selection_sort(selection_data)

    print("정렬 후:", selection_data)

    print()

 

    insertion_data = list(data)

    print("Insertion Sort")

    print("정렬 전:", insertion_data)

    insertion_sort(insertion_data)

    print("정렬 후:", insertion_data)
