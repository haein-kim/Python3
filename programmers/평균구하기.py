# https://programmers.co.kr/learn/courses/30/lessons/12944

def soultion(arr):
    sum = 0
    for i in arr:
        sum += i
    return(sum / len(arr))
