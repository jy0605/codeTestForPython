### 쌀랑해요 코드트리 1번


### 쌀랑해요 코드트리 2번
a, b, d = map(int, input().split(' '))

namuposition = 0
spenttime = 0

# 초기값 설정
namuposition += a
spenttime += a

while namuposition < d:
    spenttime += b # 대기
    
    namuposition += a # 움직임
    spenttime += a

# 남우 position이 거리보다 더 멀리 갔을 때 position 재설정
if namuposition > d:
    spenttime -= (namuposition - d)
    namuposition = d

# 이제 뒤바뀝니다.
namuposition -= b
spenttime += b

while namuposition > 0:
    spenttime += a # 대기
    
    namuposition -= b # 움직임
    spenttime += b

# 출발점보다 더 멀리 이동했을 경우도 있으므로 0으로 재설정
if namuposition < 0:
    spenttime -= (0 - namuposition)
    namuposition -= namuposition


print(spenttime)




### 쌀랑해요 코드트리 3번
arrField = [list() for i in range(n)]

for i in range(n): # 여기에서 m 설정 안해주면, 에러나도록 테스트케이스가 뭔가 있나봄
    thisLinearray = list(map(int, input().split(' ')))
    arrField[i] = list(thisLinearray)

print(arrField)



### 쌀랑해요 코드트리 4번
n, m = map(int, input().split(' '))

arrField = [list() for i in range(n)]
for i in range(n): 
    thisLinearray = list(map(int, input().split(' ')))
    arrField[i] = thisLinearray

arrFriends = [list() for j in range(m)]
for i in range(m):
    thisLinearray = list(map (int, input().split(' ')))
    arrFriends[i] = thisLinearray


fruitscnt = 0
for friend in arrFriends:
    i = friend[0]
    j = friend[1]

    fruitscnt += arrField[i][j]
    arrField[i][j] = 0

    nearNode = list()
    nearNode.append(arrField[i+1][j])
    nearNode.append(arrField[i][j+1])

    if i != 0:
        nearNode.append(arrField[i-1][j])
    if j != 0:
        nearNode.append(arrField[i][j-1])

    
   
### 쌀랑해요 코드트리 5번

