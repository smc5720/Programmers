def solution(enroll, referral, seller, amount):
    answer = []
    account = {}
    parent = {}

    def func(p, money):
        tax = int(money * 0.1)
        account[p] += money - tax
        if parent[p] == '-' or tax == 0:
            return
        return func(parent[p], tax)


    for i in enroll:
        # 판매원들의 계좌를 입력한다.
        account[i] = 0
    
    for i in range(len(referral)):
        # 판매원의 추천인이 누구인지 저장한다.
        parent[enroll[i]] = referral[i]

    for i in range(len(seller)):
        # 현재 수익을 낸 사람의 이름이다.
        p = seller[i]
        # 판매원이 발생시킨 이익이다.
        money = amount[i] * 100
        # 추천인에게 납부할 금액이다.
        func(p, money)

    for i in enroll:
        answer.append(account[i])

    return answer