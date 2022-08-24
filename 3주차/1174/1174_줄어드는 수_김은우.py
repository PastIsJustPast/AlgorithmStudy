def desc_num(n):
    if n <= 10:
        return n-1
        
    ans = list(map(str, range(10)))
    new_ans = []
    cnt = 10

    while True:
        if ans[0] == '9876543210':
            return -1
        
        nums = list(map(str, range(10)))
        for i in nums:
            for j in ans:
                num = i + j

                #내림수인지 검사            
                flag = 0
                for k in range(1, len(num)):
                    if num[k-1] <= num[k]:
                        flag = 1
                        break
                
                #내림수라면 배열에 저장
                if flag == 0 :
                    cnt += 1
                    new_ans.append(num)
                    
                    #n번째 수를 찾으면 종료
                    if cnt == n :
                        return int(num)
                    
        ans = new_ans
        new_ans = []
            
print(desc_num(int(input())))