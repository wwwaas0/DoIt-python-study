nums = input().split()
N = int(nums[0]) #듣도 못한 사람의 수
M = int(nums[1]) # 보도 못한 사람의 수

# no_sees = []
# no_sees_hears = []
no_sees = set()
no_sees_hears = set()

for _ in range(N):
    no_see = input()
    no_sees.add(no_see)

for _ in range(M):
    no_hear = input()
    if no_hear in no_sees:
        no_sees_hears.add(no_hear)

print(len(no_sees_hears))
for name in sorted(no_sees_hears):
    print(name)