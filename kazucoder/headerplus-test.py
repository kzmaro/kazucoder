#1入力1出力用

def main(N):
#user zone

    #=int(input())
    #M = N * N
    #print(M)


    return M
#-----------------------------------------------------------
#Judge zone
with open('test1.txt','r',encoding='utf-8') as f:
    tes=f.readlines()
    #print(tes)
    check=[]
    ok=True

    txtsize=8

    for i in range(txtsize):
        check.append(int(tes[i]))
    print(check)
    for i in range(0,txtsize,2):
        if main(check[i])==check[i+1]:
            pass
        else:
            ok=False
    print("OK"if ok else "NG")