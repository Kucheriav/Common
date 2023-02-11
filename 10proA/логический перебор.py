print('M P D S')
for M in range(2):
    for P in range(2):
        for D in range(2):
            for S in range(2):
                s1 = M <= P
                s2 = D == (M and P and S)
                s3 = S == (D or M)
                f = s1 and s2 and s3
                if f:
                    print(M, P, D, S, int(f))
