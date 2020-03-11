# 重量单位转换
# import math
# def Weight_Convert():
#     gram = float(input('Enter gram: '))
#     kilogram = gram / 1000
#     return print('kiloGram is {}'.format(kilogram))
#
# KiloGram = Weight_Convert()
#
# 计算直角三角形斜边长
# def Triangle_Caculator():
#     lengthA = float(input('Enter triangle first side length: '))
#     lengthB = float(input('Enter triangle first second length: '))
#     lengthC = math.sqrt(math.pow(lengthA, 2)+math.pow(lengthB, 2))
#     return print('The right triangle third side is {}'.format(lengthC))
#
# ThirdSide = Triangle_Caculator()
#
# 创建文件夹，写内容
# def create_file(textname, msg):
#     desktop_path = 'C://Users/FANG/Desktop/'
#     full_path = desktop_path + textname + '.txt'
#     file = open(full_path, 'w')
#     file.write(msg)
#     file.close()
#
# 替换文本
# def text_filter(ori_word, censored_word = 'lame', replace_word = 'Awesome'):
#     return ori_word.replace(censored_word, replace_word)
#
# def censored_text_create(name, msg):
#     censored_msg = text_filter(msg)
#     create_file(name, censored_msg)
#
# censored_text_create('Try', 'lame!lame!lame!')


# 循环练习 -- 按输入数量，创建文件夹，名称与数量相同
# for i in range(1, 10):
#     for j in range(1, 10):
#         print('{} * {} = {}'.format(i, j, i*j))

# def create_txt():
#     desktop_path = 'C://Users/FANG/Desktop/'
#     createnum = input('input file num u want: ')
#     for i in range(1, int(createnum)+1):
#         full_path = desktop_path + str(i) + '.txt'
#         file = open(full_path, 'w')
#         file.close()
#
# create_txt()

# 循环练习--复利
# 复利计算公式 S = p*(1+rate)^year
# def invest():
#     amount = input('Enter ur amount: ')
#     rate = input('Enter ur rate: ')
#     time = input('Enter ur time(year): ')
#     print('principle amount is: ' + amount)
#     for time in range(1, int(time)+1):
#         amount1 = int(amount) * pow(1 + float(rate), int(time))
#         print('year ' + str(time) + 's amount is： ' + str(amount1))
#
# invest()

# 循环练习--打印XX以内偶数
#


#数据结构-list
# fruit = ['pineapple','pear']
# print('original fruit: ', fruit)
# fruit.insert(1,'grape')
# print('insert fruit: ', fruit)
# fruit[0:0] = ['orange']
# print('insert again: ', fruit)
# fruit.remove('grape')
# print('delete fruit: ', fruit)
# fruit[0] = 'apple'
# print('modify fruit: ', fruit)
# del fruit[0:1]
# print('delete again: ', fruit)

#数据结构-list
# num_list = [6, 10, 100, 3.0, 777, 32]
# print(sorted(num_list, reverse=True))

#list
#定义list
invitName = ['A','B','C']

#删除list中元素
notCome = invitName.pop(2)

#list中新增加一个元素
invitName.insert(2,'D')

print(invitName)

#用pop的信息，显示删除的元素
print('Player '+notCome+ ' not come!')

for i in range(0, len(invitName)):
    print('Send mail to ' + invitName[i] + ' successfully')
    print('hi')



