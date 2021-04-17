def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(0, len(phone_book) - 1):
        if answer == False:
            break

        for j in range(i + 1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                answer = False
                break

    return answer