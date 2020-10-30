black_list=['卖面膜','卖茶叶','卖手机','卖衣服','卖牛奶']
# list列表是可变的
# for循环是index+1
# for i in black_list:
#     black_list.remove(i)
#复制数组
new_black_list=black_list[:]
for i in new_black_list:
    black_list.remove(i)

print(black_list)
