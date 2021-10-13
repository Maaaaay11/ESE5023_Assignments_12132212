# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:06:48 2021

@author: thoudd0701
"""
#5.1 find expression
def Find_expression(var):
# 建立运算符的LIST
    operator = ['+','-','']
# sep是用于后续join操作的空值
    sep = ''
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        for n in range(3):
                            for o in range(3):
                                for p in range(3):
                                    # 建立string类型的数字数组
                                    num = ["1","2","3","4","5","6","7","8","9"]
                                    # 在num数组各数字间插入运算符
                                    num.insert(1,operator[i])
                                    num.insert(3,operator[j])
                                    num.insert(5,operator[k])
                                    num.insert(7,operator[l])
                                    num.insert(9,operator[m])
                                    num.insert(11,operator[n])
                                    num.insert(13,operator[o])
                                    num.insert(15,operator[p])
                                    # join函数，利用sep将num数组中的元素连接为字符串
                                    expression = sep.join(num)
                                    # 利用eval函数计算字符串运行结果
                                    res = eval(expression)
                                    if res == var:
                                    #输出表达式
                                        print(str(expression) + "=" + str(res))
                                        continue    

Find_expression(100)                  
                                    

#5.2Total solution
def Find_expression(var):
# 建立运算符的LIST
    operator = ['+','-','']
# sep是用于后续join操作的空值
    sep = ''
    count = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    for m in range(3):
                        for n in range(3):
                            for o in range(3):
                                for p in range(3):
                                    # 建立string类型的数字数组
                                    num = ["1","2","3","4","5","6","7","8","9"]
                                    # 在num数组各数字间插入运算符
                                    num.insert(1,operator[i])
                                    num.insert(3,operator[j])
                                    num.insert(5,operator[k])
                                    num.insert(7,operator[l])
                                    num.insert(9,operator[m])
                                    num.insert(11,operator[n])
                                    num.insert(13,operator[o])
                                    num.insert(15,operator[p])
                                    # join函数，利用sep将num数组中的元素连接为字符串
                                    expression = sep.join(num)
                                    # 利用eval函数计算字符串运行结果
                                    res = eval(expression)
                                    if res == var:
                                        # 计算解的个数
                                        count += 1
                                        continue    
    return count

import matplotlib.pyplot as plt

# 生成一个长度为101的数组
Total_solutions = [0 for i in range(101)] 
for i in range(101):
    Total_solutions[i]=Find_expression(i)
number = range(0,101)

# 画图
plt.plot(number, Total_solutions)

plt.xlabel("Number")
plt.ylabel("Total_solutions")

plt.title("The total solutions of each number")
# 画出每个数字的解的个数的图像
plt.show

# 找到解的个数的最大值/最小值
solution_max = max(Total_solutions)
solution_min = min(Total_solutions)

# 获取解的个数的最大值对应的数字
arr_max = []
for i in range(101):
    if Total_solutions[i] == solution_max:
        arr_max.append(i) 

# 获取解的个数的最小值对应的数字
arr_min = []
for i in range(101):
    if Total_solutions[i] == solution_min:
        arr_min.append(i)  
        

print("The lowest number of solutions is  "+str(arr_max) +", and the number of solution is "+str(solution_min))
print("The largest number of solutions is  "+str(arr_min) +", and the number of solution is "+str(solution_max))


            
            