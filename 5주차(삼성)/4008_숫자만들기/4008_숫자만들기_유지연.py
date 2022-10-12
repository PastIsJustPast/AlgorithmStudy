from itertools import permutations
import math


def oper_add(op_num):
  op_list = []
  for _ in range(op_num[0]):
    op_list.append('+')

  for _ in range(op_num[1]):
    op_list.append('-')
  
  for _ in range(op_num[2]):
    op_list.append('*')

  for _ in range(op_num[3]):
    op_list.append('/')

  return op_list

def sosu(ans):
  if ans < 0 :
    ans =math.ceil(ans)
  else :
    ans = math.floor(ans)

  return ans

def caculate(op_list, num_list):
  ans = ""
  num = 0
  result = []
  for i in op_list:
    for j in range(len(num_list)-1):
      ans += str(num_list[j])+i[j]
    ans += str(num_list[-1])
    #print(ans)
    #ans값 구해서 result에 넣음
    for k in range(len(ans)):
      if k == 0:
        pass
      elif k == 1:
        num = sosu(eval(ans[0]+ans[1]+ans[2]))
      elif k % 2 == 1:#연산자
        num = sosu(eval(str(num)+ans[k]+ans[k+1]))
      else:#숫자
        pass
      
    result.append(num)
    ans = ""

  return result


  
result = []
T = int(input())
for i in range(T):
  N = int(input())
  op_num = list(map(int,input().split()))
  num_list = list(map(int, input().split()))

  op_list = oper_add(op_num)
  result = permutations(op_list,N-1)
  result = set(result)
  
  #print(list(result))
  #print(num_list)
  #print(caculate(result, num_list))
  answer = max(caculate(result, num_list))-min(caculate(result, num_list))
  print('#{} {}'.format(i + 1, answer))
  
  # 결과값은 맞았으나, eval을 쓰면 안된다고 함 ㅠ



"""
random_list = ['A', 'B', 'B', 'C'] 
result = permutations(random_list,4)
result =set(result)
print(list(result))
# [('A', 'B', 'B'), ('B', 'A', 'B'), ('B', 'B', 'A')]
"""