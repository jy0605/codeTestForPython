# �ĸ����� �ڵ�Ʈ�� 1��
'''
print('           *********')
print('      *****         ****')
print('    **                  **')
print('   *                      *')
print(' **                        **')
print('*                            *')
print('*                            *')
print('**                          **')
print(' **  *    ****  ****    *  **')
print('   ** ***** ****** ***** **')
print('             ****')
print('             ****')
print('             ****')
print('             ****')
print('            ******')
print('           ********')
'''
# �ĸ����� �ڵ�Ʈ�� 2��
'''
n = input()
fi_input = input().split(' ')
fi = list()

for i in range(int(n)):
  fi.append(int(fi_input[i]))

fi_cp = fi.copy()

maxFi = max(fi)
minFi = min(fi_cp)
fi.pop(fi.index(maxFi))
fi_cp.pop(fi_cp.index(minFi))
nextMaxFi = max(fi)
nextMinFi = min(fi_cp)
maxMultiplyValue = maxFi * nextMaxFi;
minMultiplyValue = minFi * nextMinFi;

resMultiplyValue = maxMultiplyValue if maxMultiplyValue > minMultiplyValue else minMultiplyValue;
print(resMultiplyValue)
'''


# �ĸ����� �ڵ�Ʈ�� 3��
n, m = map(int, input().split(' '))
arrField = [list() for i in range(n)]

for i in range(n): # ���⿡�� m ���� �����ָ�, ���������� �׽�Ʈ���̽��� ���� �ֳ���
    thisLineInfo_str = input().split(' ')
    thisLinearray = list(thisLineInfo_str[i] for i in range(m))
    thisLineInfo = map(int, thisLinearray)
    arrField[i] = list(thisLineInfo)

firstL, firstR = map(int, input().split(' '))
secL, secR = map(int, input().split(' '))

for i in range(firstL-1, firstR, 1):
  try:
    indexOfCriminal = arrField[i].index(1)
    arrField[i][indexOfCriminal] = 0
  except:
    pass

numberOfRestCriminals = 0

for i in range(secL-1, secR, 1):
  try:
    indexOfCriminal = arrField[i].index(1)
    arrField[i][indexOfCriminal] = 0
  except:
    pass

for i in range(n):
  numberOfRestCriminals += arrField[i].count(1)

print(numberOfRestCriminals)

