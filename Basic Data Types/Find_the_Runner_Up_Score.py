if __name__ == "__main__":
    n = int(input())
    participants = list(map(int, input().split()))
    participants.sort(reverse=True)
    for member in range(n - 1):
        if participants[member] > participants[member + 1]:
            print(participants[member + 1])
            break
