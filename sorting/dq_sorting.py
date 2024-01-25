class MergeSort:
    @classmethod
    def merge_sort(self, a_list):
        # O(nlogn)
        # print("Splitting", a_list)
        if len(a_list) > 1:
            mid = len(a_list) // 2
            left_half = a_list[:mid]
            right_half = a_list[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i,j,k = 0,0,0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    a_list[k] = left_half[i]
                    i = i + 1
                else:
                    a_list[k] = right_half[j]
                    j = j + 1
                k = k + 1
            while i < len(left_half):
                a_list[k] = left_half[i]
                i = i + 1
                k = k + 1
            while j < len(right_half):
                a_list[k] = right_half[j]
                j = j + 1
                k = k + 1
        # print("Merging", a_list)

class QuickSort:
    @classmethod
    def quick_sort(self, a_list):
        self.quick_sort_helper(a_list, 0, len(a_list) - 1)

    @classmethod
    def quick_sort_helper(self, a_list, first, last):
        if first < last:
            split = self.partition(a_list, first, last)
            self.quick_sort_helper(a_list, first, split-1)
            self.quick_sort_helper(a_list, split+1, last)
    
    @classmethod
    def partition(self, a_list, first, last):
        pivot = a_list[first]
        left_mark = first + 1
        right_mark  = last
        done = False

        while not done:
            while left_mark <= right_mark and a_list[left_mark] <= pivot:
                left_mark += 1
            while left_mark <= right_mark and a_list[right_mark] >= pivot:
                right_mark -= 1
            
            if right_mark < left_mark:
                done = True
            else:
                a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
            
        a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

        return right_mark



if __name__ == "__main__":
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(a_list)
    MergeSort.merge_sort(a_list=a_list)
    print("merge sort: ", a_list)
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    QuickSort.quick_sort(a_list=a_list)
    print("QuickSort: ", a_list)