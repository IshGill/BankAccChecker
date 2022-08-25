def cleaned_acc(acc_num):
    acc_num_list = [i for i in acc_num if i != '-' and i != " " and i.isdigit()]
    if len(acc_num_list) >= 2:
        print(acc_num_list)
        acc_num_list.insert(2, '-')
        print(acc_num_list)
    if len(acc_num_list) >= 7:
        acc_num_list.insert(7, '-')
    if len(acc_num_list) >= 15:
        acc_num_list.insert(15, '-')
    last_index_dash = len(acc_num_list) - acc_num_list[::-1].index('-') - 1
    if len(acc_num_list[last_index_dash + 1:]) == 3 and len(acc_num_list) >= 16:
        acc_num_list.pop(last_index_dash+1)
    return "".join(acc_num_list)



