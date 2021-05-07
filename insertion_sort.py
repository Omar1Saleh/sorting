class insertion_sort:

    def ins_sort(self, custom_list):
        for i in range(1,len(custom_list)):
            key = custom_list[i]
            j = i-1
            while j >= 0 and key < custom_list[j]:
                custom_list[j+1] = custom_list[j]
                j -= 1;
            custom_list[j+1] = key
        return custom_list

new_list = insertion_sort()
print(new_list.ins_sort([3,1,6,2,7,4]))