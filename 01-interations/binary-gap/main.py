def solution(N):
    n_bin = bin(int(N))[2:]
    if n_bin.count('0') == 0 or n_bin.count('1') == 1:
        print('0')
    else:
        max_gap = 0
        count = 0
        for i in n_bin:
            if i == '0':
                count += 1
            else:
                if count > max_gap:
                    max_gap = count
                count = 0
        print(max_gap)    
    pass


solution(529)