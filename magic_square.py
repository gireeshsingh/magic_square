def formingMagicSquare(s):
    a=[[8,1,6],[3,5,7],[4,9,2]]
    b=[[6,1,8],[7,5,3],[2,9,4]]
    c=[[4,9,2],[3,5,7],[8,1,6]]
    d=[[2,9,4],[7,5,3],[6,1,8]]
    e=[[8,3,4],[1,5,9],[6,7,2]]
    f=[[4,3,8],[9,5,1],[2,7,6]]
    g=[[6,7,2],[1,5,9],[8,3,4]]
    h=[[2,7,6],[9,5,1],[4,3,8]]
    l=[a,b,c,d,e,f,g,h]
    m=compute_score(l,s)

    print(min(m))

def compute_score(l,s):
    i=0
    j=0
    index=0
    answer=[]
    while(index<8):
        total=0
        i=0
        while(i<3):
            j=0
            while(j<3):
                total=total+abs(l[index][i][j]-s[i][j])
                j=j+1
            i=i+1
        answer.append(total)
        index=index+1
        print("ok",answer)
    return answer

print("Enter the 3x3 matrix, one digit at a time:")
temp=[]
o=0
n=0
while(o<3):
    n=0
    templist=[]
    while(n<3):
        templist.append(int(input()))
        n=n+1
    temp.append(templist)
    o=o+1

#formingMagicSquare([[4,9,2],[3,5,7],[8,1,6]])
formingMagicSquare(temp)