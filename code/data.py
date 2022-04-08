def getgrade(tmp, dic, weight): #获取总分并添加到数据库中
    def findindex(str):
        lst = tmp[0]
        for i in range(len(lst)):
            if lst[i] == str:
                return i+3
        return -1
    # print(tmp)
    i1 = findindex("思想品德素质")
    i2 = findindex("学业成绩")
    i3 = findindex("身心素质")
    i4 = findindex("创新实践能力")
    i5 = findindex("学院特色")
    # print(i1)
    # print(dic)
    for k in dic.keys():
        grade = weight[0] * dic[k][i1] + weight[1] * dic[k][i2] + weight[2] * dic[k][i3] + weight[3] * dic[k][i4] + weight[4] * dic[k][i5]
        length = len(dic[k])
        if length < 9:
            dic[k].append(grade)
        else:
            dic[k][length-1] = grade