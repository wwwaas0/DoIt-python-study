# 나이와 이름이 가입한 순서대로
# 회원들을 나이가 증가하는 순으로, 
# 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

N = int(input())
dict_users = {} # 딕셔너리 선언
for _ in range(N):
    users = []
    users = input().split()
    age = int(users[0])
    name = users[1]

    # 만약 해당 age가 dict_users에 없다면
    if age not in dict_users:
        dict_users[age]=[]
    
    dict_users[age].append(name)

# 키 값 오름차순으로 정렬
keys = sorted(dict_users.keys())

for i in keys:
    for x in dict_users[i]:
        print(i, x)