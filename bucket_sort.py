import math
import insertion_sort

class bucket_sort:

    def insertion_sort(self, custom_list):
        for i in range(1,len(custom_list)):
            key = custom_list[i]
            j = i-1
            while j >= 0 and key < custom_list[j]:
                custom_list[j+1] = custom_list[j]
                j -= 1;
            custom_list[j+1] = key
        return custom_list

    def bucket_sorter(self, custom_list):
        number_of_buckets = round(math.sqrt(len(custom_list)))
        max_number = max(custom_list)
        arr = []

        for i in range(number_of_buckets):
            arr.append([])

        for j in custom_list:
            index_b = math.ceil(j*number_of_buckets/max_number)
            arr[index_b-1].append(j)

        for i in range(number_of_buckets):
            arr[i] = self.insertion_sort(arr[i]) # after dividing buckets, you can use any sorting method, i used insertion sort.
        return arr


custom_list = bucket_sort()
print(custom_list.bucket_sorter([1,9,2,8,3,7,4,6,5]))