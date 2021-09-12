def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(0, len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            break

    return answer