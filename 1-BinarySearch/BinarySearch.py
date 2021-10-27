#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binarysearch(array, findelement, arraysize):
    left = 0
    right = len(array)
    middle = int((left + right)/2)
    index = -1
    while (left < right-1 and array[middle] != findelement):
        if array[middle] > findelement:
            right = middle
        else:
            left = middle
        middle = int((left + right)/2)
    if array[middle] == findelement:
        index = middle
    return index


# In[5]:


# считали размер массива
arraysize = int(input())

# считывание данных в массив
array = []
line = input()
for x in line.split():
    array.append(int(x))

vsego = int(input())
current = 0
#проходимся по нужному числу элементов
while current < vsego:
    # считываем строку
    line = input()
    # производим бинарный поиск и записываем в файл
    print(str(binarysearch(array, int(line), arraysize)))
    current+=1


# In[ ]:





# In[62]:





# In[ ]:





# In[ ]:




