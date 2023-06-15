def solution(today, terms, privacies):
    answer = []
    
    # 약관 종류
    termList = dict()
    for t in terms:
        a, b = t.split()
        termList[a] = int(b)
    
    # 현재 날짜(년, 월, 일)
    y, m, d = map(int, today.split("."))
    
    # 인덱스
    i = 1
    
    for p in privacies:
        date, term = p.split()
        
        # 개인정보 수집 일자
        dy, dm, dd = map(int, date.split("."))
        
        # 개인 정보 유효기간
        dm += termList[term]
        dd -= 1
        
        # 12월을 넘어가는 월
        if dm > 12:
            dy += dm // 12
            dm %= 12
        
        if dm == 0:
            dy -= 1
            dm =12
        
        # 하루 전이 월이 바뀔
        if dd == 0:
            dm -=  1
            dd = 28

        if y > dy:
            answer.append(i)
        elif y == dy:
            if m > dm:
                answer.append(i)
            elif m == dm:
                if d > dd:
                    answer.append(i)
        print(dy, dm, dd)        
        i += 1
    
    return answer