class selection_sort:
    def sel_sort(self, custom_list):
        for i in range(len(custom_list)):
            min_index = i
            for j in range(i+1, len(custom_list)):
                if custom_list[min_index] > custom_list[j]:
                    min_index = j
            custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]
        return custom_list

new_list = selection_sort()
print(new_list.sel_sort([3,1,5,7,2,9,4]))

