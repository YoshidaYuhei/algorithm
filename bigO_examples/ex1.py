# coding=utf-8
'''
計算量オーダーはO(N)
配列が2回操作しているかどうかは関係ない
配列の全要素を1度全て走査する
'''


def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for j in array:
        product *= j
    return str(sum) + ", " + str(product)