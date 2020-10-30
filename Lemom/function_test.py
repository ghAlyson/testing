#定义函数：将用户输入的所有数字相乘之后对20取余数
#用户输入的 数字个数不确定
# def function(number):
#     start_number = 1
#     for i in number:
#
#         start_number*=int(i)
#     return start_number % 20
# number=input("请输入一组数字：")
# new_number=number.split(",")
# print(function(new_number))
####
# list=[2,3,4,7]
# a=1
# for i in list:
#
#     a=a*i
# result=a%20
# print(result)
##编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度内容，并将新内容输出
# def list_len(list):
#     if len(list)>2:
#         return list[:2]
#     return list
# list=input("输入列表：")
# new_list=list.split(",")
# #list=[1,2]
# print(list_len(new_list))

##列表去重
# def remove_list(list):
##set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据
#     return set(list)
# print(remove_list([2,3,4,5,6,2,3,4]))

##第2种，for循环
def remove_lement(m_list):
    new_list=[]
    for i in m_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(remove_lement([2,4,5,3,4,6,5,7]))