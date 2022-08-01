if __name__ == "__main__":
    n = int(input())
    students = []
    for _ in range(n):
        name = input()
        marks = float(input())
        students.append([name, marks])
    students.sort(key=lambda row: [row[1], row[0]])

    for index in range(n):
        if students[index][1] < students[index + 1][1]:
            print(students[index + 1][0])
            while index + 2 < n and students[index + 1][1] == students[index + 2][1]:
                print(students[index + 2][0])
                index += 1
            break
