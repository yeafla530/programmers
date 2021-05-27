# 처음 풀이 
# 효율성 문제에서 실패
def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    # print(phone_book)
    for i in range(len(phone_book)-1):
        for x in range(i+1, len(phone_book)):
            if phone_book[x].find(phone_book[i]) == 0:
                return False
        
    return answer


# 두번째 풀이
# string sort시 앞의 숫자별로 정렬됨 
# 해시 사용
# 통과 (2.86ms, 10.4MB)
def solution(phone_book):
    answer = True
    # ["12", "13", "123", "132", "1235"]
    # ['12', '123', '1235', '13', '132']
    phone_book.sort()
    # print(phone_book)

    
    # print(dic)
    for i in range(len(phone_book)-1):
        length = len(phone_book[i])
        if hash(phone_book[i]) == hash(phone_book[i+1][:length]): 
            # print(hash(phone_book[i]), hash(phone_book[i+1][:length]))
            return False
        
    return answer

# 세번째 풀이
# 해쉬의 정석
# 근데 굳이?라는 생각이...
# if ... in이 dict를 탐색할 때 사용하는 것
# 두번째 풀이가 시간은 더 줄일 수 있었음
# 통과 (5.34ms, 10.4MB)
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            print(temp)
            if temp in hash_map and temp != phone_number:
                print(temp, hash_map)
                return False
    return answer