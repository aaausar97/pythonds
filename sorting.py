def bubble_sort(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                temp = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j+1] = temp
            
def bubble_sort_short(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        exchanges = False
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                exchange = True
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
        if not exchange:
            break
    
def selection_sort(a_list):
    for i, item in enumerate(a_list):
        min_ = len(a_list) - 1
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_]:
                min_ = j
        if min_ != i:
            a_list[min_], a_list[i] = a_list[i], a_list[min_]

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i

        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos = cur_pos - 1
        
        a_list[cur_pos] = cur_val