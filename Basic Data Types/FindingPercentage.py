if __name__ == "__main__":
    n = int(input())
    students = {}
    for _ in range(n):
        student = input().split()
        students[student[0]] = list(map(float, student[1:]))
    student = input()
    print(format(sum(students[student])/len(students[student]), ".2f"))
