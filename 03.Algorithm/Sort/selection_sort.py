
class Sort:
    def select_sort(self, array, direction):
        for i in range(len(array)-1):
            if (direction == True):
                min_index = i
                for j in range(i+1, len(array)):
                    if array[min_index] > array[j]:
                        min_index = j
                array[i], array[min_index] = array[min_index], array[i]
            elif (direction == False):
                max_index = i
                for j in range(i+1, len(array)):
                    if array[max_index] < array[j]:
                        max_index = j
                array[i], array[max_index] = array[max_index], array[i]

li = [2, 3, 1, 5, 4]
sort = Sort()
sort.select_sort(li, True)
print(li)
sort.select_sort(li, False)
print(li)



