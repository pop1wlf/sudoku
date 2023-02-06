#!/usr/bin/python3
import time

# 找出空位置所在区块的所有值
def getBlockList(index, sList):
    # 所在区块数组
    blockList = []
    
    # 区块分布
    # 1 | 2 | 3
    # 4 | 5 | 6
    # 7 | 8 | 9
    indexI = index[0]
    indexJ = index[1]
    if 0 <= indexI <= 2 and 0 <= indexJ <= 2:
        # 区块1
        blockList = sList[0][0:3] + sList[1][0:3] + sList[2][0:3]
    elif 0 <= indexI <= 2 and 3 <= indexJ <= 5:
        # 区块2
        blockList = sList[0][3:6] + sList[1][3:6] + sList[2][3:6]
    elif 0 <= indexI <= 2 and 6 <= indexJ <= 8:
        # 区块3
        blockList = sList[0][6:] + sList[1][6:] + sList[2][6:]
    elif 3 <= indexI <= 5 and 0 <= indexJ <= 2:
        # 区块4
        blockList = sList[3][0:3] + sList[4][0:3] + sList[5][0:3]
    elif 3 <= indexI <= 5 and 3 <= indexJ <= 5:
        # 区块5
        blockList = sList[3][3:6] + sList[4][3:6] + sList[5][3:6]
    elif 3 <= indexI <= 5 and 6 <= indexJ <= 8:
        # 区块6
        blockList = sList[3][6:] + sList[4][6:] + sList[5][6:]
    elif 6 <= indexI <= 8 and 0 <= indexJ <= 2:
        # 区块7
        blockList = sList[6][0:3] + sList[7][0:3] + sList[8][0:3]
    elif 6 <= indexI <= 8 and 3 <= indexJ <= 5:
        # 区块8
        blockList = sList[6][3:6] + sList[7][3:6] + sList[8][3:6]
    elif 6 <= indexI <= 8 and 6 <= indexJ <= 8:
        # 区块9
        blockList = sList[6][6:] + sList[7][6:] + sList[8][6:]

    return blockList

# 找出空位置（0）
def findBlank(sList):
    indexI = 0
    indexJ = 0
    for i in sList:
        for j in i:
            # 找出空位置
            if 0 == j:
                return [indexI, indexJ]
            indexJ += 1
        indexJ = 0
        indexI += 1
    return []

# 判断数字是否有效
def checkSu(sList, i, index):
    # 取出所在行的所有数字
    rowList = sList[index[0]]
    # 取出所在列的所有数字
    columnList = [x[index[1]] for x in sList]
    # 取出所在区块的所有数字
    blockList = getBlockList([index[0], index[1]], sList)

    if i not in rowList + columnList + blockList:
        # 有效数字
        return True
    else:
        # 无效数字
        return False

# 迭代循环算出结果
def solveS(sList):
    # 迭代查找下一个空位置
    index = findBlank(sList)

    if len(index) == 0:
        # 没有空位置，则数独完成
        return True
    else:
        # 找到空位置，记录坐标
        r, c = index

    # 无脑在空位置中迭代试错数字1-9
    for i in range(1, 10, 1):
        # 判断有效数字
        if checkSu(sList, i, index):
            sList[r][c] = i
            # 数字有效则迭代下一个空位置
            if solveS(sList):
                return True
            
            # 无效数字则回溯此次操作
            sList[r][c] = 0

    return False

def main():
    # 创建数独
    #         0 1 2 3 4 5 6 7 8
    sList = [[0,0,3,0,0,0,0,0,6], # 0
             [0,6,0,3,2,9,0,0,0], # 1
             [9,0,8,4,0,0,0,0,3], # 2
             [0,1,0,0,0,3,0,0,0], # 3
             [0,0,9,0,0,0,0,8,0], # 4
             [0,7,0,1,9,0,0,0,2], # 5
             [0,0,0,0,0,5,7,0,0], # 6
             [4,0,0,2,0,6,0,1,0], # 7
             [0,0,0,0,0,4,9,0,5]] # 8

    # 迭代循环算出结果
    t1 = time.time()
    solveS(sList)
    t = time.time() - t1
    
    # 打印结果
    print(sList)
    print(t)

if __name__ == '__main__':
    main()