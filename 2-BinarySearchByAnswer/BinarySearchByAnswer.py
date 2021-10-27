#!/usr/bin/env python
# coding: utf-8

# In[3]:


# нужно проверить покрываются ли все точки. слева направо идем, подставляем отрезки.  
# идем скраю т.к. нужно покрыть все точки, т.е. в лучшем случае перекроется несколько, в худшем - только выбранная
# смотрим, какие точки были покрыты, постепенно двигаясь
def answercheck(arraylengths, segmentsize, k, N):#длины между точками, длина отрезка, мах отрезков, всего точек
    segments = 0;
    index = 0;
    # проход по непокрытым точкам (если превышается число нужных отрезков - сразу конец)
    while (index < N and segments < k + 1):
        segmentsizebuff = segmentsize;
        segments += 1;
        
        # проверка сколько точек покрыто отрезком (возможно одна)
        while segmentsizebuff >= 0 and index < N:
            segmentsizebuff -= arraylengths[index];
            index += 1;
    # если получается разделить на нужное число отрезков
    if(segments <= k):
        return True
    return False


# In[2]:


# прохождение по ответам
def binarysearchbyanswer(arraylengths, maxright, k, N):
    left = 0 #минимальная длина отрезка
    right = maxright#максимальная длина отрезка
    middle = int((left + right)/2)

    while (left < right - 1):
        # если ответ не подходит - сужаем границу справа (увеличиваем рассматриваемое значение), иначе слева
        if (not answercheck(arraylengths, middle, k, N)):
            left = middle;
        else:
            right = middle;
            answer = middle;#сохранили лучший подходящий на данной итерации ответ (если все слева не подходят)
        middle = int((left + right)/2); # новая середина
    return answer #возврат полученного ответа


# In[3]:


# нам важны не точки, а рассточния между соседними точками. 0 индекс от 0 до 1; 1 от 1 до 2; n-1 от n-1 до n
def lengthsfrompoints(arraypoints, N):
    arraylengths = []
    i = 0
    while(i < N-1):
        arraylengths.append(arraypoints[i+1]-arraypoints[i]);
        i+=1;
    #добавляем расстояние от последней точки до самой себя (чтобы всегда исполнялось)
    arraylengths.append(0);
    return arraylengths


# In[5]:


# считали размер массива
N = int(input())
# число отрезков
k = int(input())
# считывание данных в массив
arraypoints = []
current = 0
while current < N:
    arraypoints.append(int(input()))
    current+=1
# расчет длин между точками чтобы высчитать лишь один раз а не на каждой проверке
arraylengths = lengthsfrompoints(arraypoints, N)
maxright = arraypoints[N-1] - arraypoints[0]
# производим бинарный поиск по ответу и выводим
print(str(binarysearchbyanswer(arraylengths, maxright, k, N)))
    


# In[ ]:





# In[ ]:




