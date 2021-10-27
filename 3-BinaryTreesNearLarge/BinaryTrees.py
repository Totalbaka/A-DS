#!/usr/bin/env python
# coding: utf-8

# In[1]:


from binarytree import Node


# In[15]:


def nearlargefind(root, key, nearlarge):
    if root is None:
        return nearlarge
    else:
        if root.value <= key:#если значение меньше относительно искомого
            nearlarge = nearlargefind(root.right, key, nearlarge)#- ищем справа
        else:#если больше 
            nearlarge = nearlargefind(root.left, key, nearlarge)# но пытаемся найти поменьше
            # - он нас удовлетворяет, срваниваем с уже найденным (или если первый подходящий - просто сохраняем)
            if(root.value < nearlarge or nearlarge == -1):
                nearlarge = root.value;
    return nearlarge


# In[16]:


#Вставка нового элемента в бинарное дерево
#т.е. идет проверка вхождения элемента, а затем если этот элемент не нашелся в месте, где должен находиться - 
#добавляется в место где он должен находиться
def insert(root, key):
    parent = None#для хранения предыдущего элемента если упремся в null-
    node = root
    #проход по дереву в поисках элемента
    while node != None and key != node.value:
        if node.value < key:#перемещение в правое поддерево
            leftright = True#если true, то добавляем справа от родителя
            parent = node
            node = node.right
        else:#перемещение в левое поддерево
            leftright = False#если false, то добавляем слева от родителя
            parent = node
            node = node.left
    #если элемент не найден - добавляем
    if node == None:
        if leftright :
            parent.right = Node(key)
        else:
            parent.left = Node(key)
        return True
    elif node.value == key:#если найден - заканчиваем
        return False
    return root


# In[17]:


# самое базовое дерево без балансировок
# в каждой ноде доступ только к значению + правому и левому соседям, из-за этого не пройтись по родителям
# потому подключается рекурсия
# считали сколько будет элементов
pointscount = int(input())

current = 0

#в начале дерево пустое, добавляем элемент в корневую ноду
if pointscount > 0:
    a = int(input())
    root = Node(a)
    print('- -')
    current += 1

#добавляем остальные элементы
while current < pointscount:
    # добавляем элемент 
    a = int(input())
    newelement = insert(root, a)
    #поиск ближайшего большего
    nearlarge = -1
    nearlarge = nearlargefind(root, a, nearlarge)
    if newelement :#если элемент новый
        if nearlarge > 0:
            print('-',nearlarge)
        else:
            print('- -')
    else:#если элемент уже был
        if nearlarge > 0:
            print('+',nearlarge)
        else:
            print('+ -')
    current+=1


# In[ ]:





# In[ ]:




