#快速排序
# list=[6,3,2,5,8,1]
#①基本思想。实现思想是每步从排序记录中选出排序码最小（最大）的记录，放在已排序记录序列的最后（前）；
# ②算法特点。直接选择排序算法n个记录的文件的直接选择排序可经过n-1趟直接选择排序得到有序结果。
# for i in range(len(list)-1):
#     min=list[i]
#     for j in range(i+1,len(list)):
#         if list[j]<min:
#             list[i]=list[j]
#             list[j]=min
#             min=list[i]
# print(list)
#函数调用
# def select(list):
#     for i in range(len(list)-1):
#         min=list[i]
#         for j in range(i+1,len(list)):
#             if list[j]<min:
#                 min=list[j]
#
#                 list[i],list[j]=list[j],list[i]
# list=[6,3,2,5,8,1]
# select(list)
# print(list)

#冒泡排序
#冒泡排序就是把小的元素往前调或者把大的元素往后调。比较是相邻的两个元素比较，交换也发生在这两个元素之间。所以，如果两个元素相等，是不会再交换的；如果两个相等的元素没有相邻，那么即使通过前面的两两交换把两个相邻起来，这时候也不会交换，所以相同元素的前后顺序并没有改变，所以冒泡排序是一种稳定排序算法。
def bubble(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    #return list
list=[6,3,2,5,8,1]
bubble(list)
#函数y=f(X),print(list)相当于输出X，而print（bubble（list））则是输出f(x),需要return，才有值
print(list)
print(bubble(list))

# def bubble_sort(nums):
#     for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
#         for j in range(len(nums) - i - 1):  # j为列表下标
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     return nums
#
#
# print(bubble_sort([45, 32, 8, 33, 12, 22, 19, 97]))
