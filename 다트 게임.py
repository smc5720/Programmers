def solution(dartResult):
    answer = 0
    stack = []
    dartResult = list(dartResult)

    while dartResult:
        tmp = dartResult.pop()
        if tmp != '0':
            if '0' < tmp and tmp <= '9': 
                stack.append(int(tmp))
            else:
                stack.append(tmp)
        else:
            if dartResult[-1] == '1':
                dartResult.pop()
                stack.append(10)
            else:
                stack.append(0)
    
    star_cnt = 0
    shop_cnt = 0

    while stack:
        tmp = stack.pop()
        if tmp == '*':
            star_cnt += 2
        if tmp == '#':
            shop_cnt += 1
        elif tmp == 'T' or tmp == 'D' or tmp == 'S':
            num = stack.pop()
            print(num)
            if tmp == 'T':
                num = num ** 3
            if tmp == 'D':
                num = num ** 2
            if star_cnt > 0:
                num *= 2
                star_cnt -= 1
            if shop_cnt > 0:
                num *= -1
                shop_cnt -= 1
            #answer += num

    return answer