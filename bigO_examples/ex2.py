# coding=utf-8
'''
計算量オーダはO(N**2)
N個の配列がN回捜査される
2重ループは基本2乗
'''


def foo(array):
    for i in array:
        for j in array:
            print(str(i) + ", " + str(j))
