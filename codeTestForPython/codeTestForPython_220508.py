### �Ҷ��ؿ� �ڵ�Ʈ�� 1��


### �Ҷ��ؿ� �ڵ�Ʈ�� 2��
a, b, d = map(int, input().split(' '))

namuposition = 0
spenttime = 0

# �ʱⰪ ����
namuposition += a
spenttime += a

while namuposition < d:
    spenttime += b # ���
    
    namuposition += a # ������
    spenttime += a

# ���� position�� �Ÿ����� �� �ָ� ���� �� position �缳��
if namuposition > d:
    spenttime -= (namuposition - d)
    namuposition = d

# ���� �ڹٲ�ϴ�.
namuposition -= b
spenttime += b

while namuposition > 0:
    spenttime += a # ���
    
    namuposition -= b # ������
    spenttime += b

# ��������� �� �ָ� �̵����� ��쵵 �����Ƿ� 0���� �缳��
if namuposition < 0:
    spenttime -= (0 - namuposition)
    namuposition -= namuposition


print(spenttime)




### �Ҷ��ؿ� �ڵ�Ʈ�� 3��
arrField = [list() for i in range(n)]

for i in range(n): # ���⿡�� m ���� �����ָ�, ���������� �׽�Ʈ���̽��� ���� �ֳ���
    thisLinearray = list(map(int, input().split(' ')))
    arrField[i] = list(thisLinearray)

print(arrField)



### �Ҷ��ؿ� �ڵ�Ʈ�� 4��
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

    
   
### �Ҷ��ؿ� �ڵ�Ʈ�� 5��

