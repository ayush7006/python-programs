user_input1 = int(input('enter your number 1 -->'))
user_input2 = int(input('enter your number 2 -->'))
print("1 for + \n, 2 for - \n, 3 for * \n, 4 for % ")
opr = int(input("enter your opr -->"))
if opr is 1 :
    sum = user_input1+user_input2
elif opr is 2 :
    sum = user_input1-user_input2
elif opr is 3 :
    sum = user_input1*user_input2
elif opr is 4 :
    sum = user_input1/user_input2
else:
    print('error')
print(sum)                    