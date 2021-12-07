def zigzag(list):
    max = 0
    tmp_count = 0
    z_status = 0
    for i in range(len(list)):
        if z_status == 0:
            if list[i] > list[i+1]:
               z_status = 1
               tmp_count += 1
            else:
                if tmp_count > max:
                    max = tmp_count
                    tmp_count = 0
                else:
                    tmp_count = 0
        elif z_status == 1:
            if list[i] < list[i+1]:
               z_status = 0
               tmp_count += 1
            else:
                if tmp_count > max:
                    max = tmp_count
                    tmp_count = 0
                else:
                    tmp_count = 0
    return max
my_list = [4,3,6,2,7,8,3,5,9,9,5]
print(zigzag(my_list))





