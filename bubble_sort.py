class bubble_sort:

    def sort(self, custome_list):
        for i in range(len(custome_list)-1):
            for j in range (len(custome_list)-i-1):
                if custome_list[j] > custome_list[j+1]:
                    custome_list[j], custome_list[j + 1] = custome_list[j + 1], custome_list[j]
        return custome_list


new_custome_list = bubble_sort()
print(new_custome_list.sort([3,2,6,1,9,4]))
