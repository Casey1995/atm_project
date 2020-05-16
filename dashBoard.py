import db
import getpass as p

def dashBoard(username,password):
    #print('X'*20, 'THIS IS WONDER BANK', 'X'*20)
    #print('#',' '*57,'#')
    #print('X'*61)
    #account_number, balance, fullname, _ = db.query_db(db.customer_info_query,'username','password')
    account_number, balance, fullname = db.query_db(db.display_customer_data_query,username,password)[0]
    print('WELCOME TO WONDER BANK'.center(60))
    print()
    print('Name:',fullname)
    print('Account number:',account_number,'\t\t Balance:',balance)
    print()
    print('..............'.center(60))
    print()
    print('BELOW ARE OPTION FOR YOUR SERVICE'.center(60))
    print()
    print('Cash deposit: \t',1,'\t\t\tTransfer:',3)
    print('Cash withdrawal:',2,'\t\t\tExit    :',4)
    print('#',' '*57,'#')
    print('X'*61)
    return (account_number, balance)

