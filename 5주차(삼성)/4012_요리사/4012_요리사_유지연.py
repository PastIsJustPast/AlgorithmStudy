from itertools import combinations

n = int(input())
first_index_list = []
index_list = []
count = 99999
t1_num = 0
t2_num = 0
t1_num_sum = 0
t2_num_sum = 0


# 이차원 리스트 만듦
for i in range(n):
  k = int(input())
  first_index_list = [i for i in range(k)]
  index_list = list(combinations(first_index_list, k // 2))
  mylist = [list(map(int,input().split())) for _ in range(k)]  
  
  for j in range(len(index_list)//2):
  
    t1 = list(combinations(index_list[j], 2))
    t2 = list(combinations(tuple(set(first_index_list).difference(index_list[j])), 2))
  

    for j in range(len(t1)):
      
      t1_num =  mylist[t1[j][0]][t1[j][1]] + mylist[t1[j][1]][t1[j][0]]
      t2_num =  mylist[t2[j][0]][t2[j][1]] + mylist[t2[j][1]][t2[j][0]]
      
      t1_num_sum += t1_num
      t2_num_sum += t2_num
  
    if abs(t1_num_sum - t2_num_sum) < count:
      count = abs(t1_num_sum - t2_num_sum)
  
    t1_num_sum = 0
    t2_num_sum = 0

  #print("#"+str(i+1)+" "+str(count))
  print('#{} {}'.format(i + 1, count))
  count = 99999


  # 메모리 80,036 kb 실행시간 765 ms 코드길이 1,034