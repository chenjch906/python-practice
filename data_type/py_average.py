#!/bin/python

if __name__ == '__main__':
    average = 0
    num = 0
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name,scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores

    query_name = raw_input()
    for i in student_marks[query_name]:
        average += i
        num += 1
    print("%.2f"%float(average/num))
