if __name__ == '__main__':
    N = int(input())
    sol = []
    for _ in range(N):
        operation, *items = input().split()
        items = list(map(int, items))
        if operation == "append":
            sol.append(items[0])
        elif operation == "print":
            print(sol)
        elif operation == "pop":
            sol.pop()
        elif operation == "sort":
            sol.sort()
        elif operation == "reverse":
            sol = [sol[x] for x in range(len(sol) - 1, -1, -1)]
        elif operation == "insert":
            sol.insert(items[0], items[1])
        elif operation == "remove":
            sol.remove(items[0])
