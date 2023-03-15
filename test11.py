"""
game369 = int(input())

for i in range(1,game369+1):
    ones = i%10
    tens = i//10
    if ones in [3,6,9] or tens in [3,6,9]:
        print('X',end=' ')
    else:
        print(i,end=' ')
"""

"""
my_list = []

for i in range(10):
    row = list(map(int, input().split()))
    my_list.append(row)


for i in range(len(my_list)):
    my_list[1][1] = 9
    for j in range(len(my_list[i])):
        if j != 0 or j != 9:    
            if my_list[i][j-1] == 9 and my_list[i][j+1] == 0:
                my_list[i][j] = 9
        


for row in my_list:
    print(row)

"""
my_list = []

# 10 * 10 2차원 리스트 생성
for i in range(10):
    row = list(map(int, input().split()))
    my_list.append(row)

# 개미의 초기 위치 
x, y = 1, 1

while True:
    # 도착점에 도달하면 2->9로 바꾸고 while 문 종료
    if my_list[x][y] == 2:
        my_list[x][y] = 9
        break

    # 현재 방행에서 오른쪽으로 이동
    elif my_list[x][y+1] != 1:      # 만약 오른쪽 열이 1이 아니라면
        my_list[x][y] = 9           # 현재 위치 0 -> 9 로 변경
        y += 1                      # 열값 추가(오른쪽 이동 완료)
    # 만약 오른쪽이 막혔다면 아래로 이동
    elif my_list[x][y+1] == 1:      # 만약 오른쪽 열이 1이라면 (벽으로 막혔다면)
        if my_list[x+1][y] != 1:    # 그 상태에서 아래쪽이 1이 아니라면 (바닥이 뚫려 있다면)
            my_list[x][y] = 9       # 0 -> 9 로 변경
            x += 1                  # 행값 추가(아래쪽 이동 완료)

        # 만약 이동 중 사방이 뚫려있다면    
        else:
            my_list[x][y] = 9
            break

for row in my_list:
    for col in row:
        print(col, end=' ')
    print()