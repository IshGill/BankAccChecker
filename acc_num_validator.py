from ast import main
from clean_account import cleaned_acc

def validate_acc_nums():
    your_num = input("Enter the account number provided to you: ")
    pymnt_num = input("Enter the account number you've entered for payment: ")
    check_your_num = cleaned_acc(your_num)
    check_pymnt_num = cleaned_acc(pymnt_num)
    if check_your_num != check_pymnt_num:
        index_err_record = []
        for i in range(len(check_pymnt_num)):
            if i < len(check_your_num):
                if check_your_num[i] != check_pymnt_num[i]:
                    index_err_record.append(i)
        print(f"ERROR: THE BANK ACCOUNT NUMBER WHICH YOU HAVE ENTERED AND THE ACTUAL PAYMENT NUMBER DO NOT MATCH.\n" 
              f"Real payment number: {check_pymnt_num}\n"
              f"Your payment number: {check_your_num}")
        prev = 0
        print("Numbers differ here: ", end="")
        for i in index_err_record:
            print(f"{' '*(i - prev)}^", end="")
            prev = i + 1
    else:
        print(f"SUCCESS: BOTH ACCOUNT NUMBERS MATCH.\n"
              f"Real payment number: {check_pymnt_num}\n"
              f"Your payment number: {check_your_num}")

validate_acc_nums()


    

