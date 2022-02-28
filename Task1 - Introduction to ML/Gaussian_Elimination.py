
def gaussianElimentaion (a,n):
    # Elimination
    for k in range(n-1):
        for i in range(k+1,n):
            if a[i][k]==0:continue
            factor=a[k][k]/a[i][k]
            b[i]=b[k]-b[i]*factor
            for j in range (k,n):
                a[i][j]=a[k][j]-a[i][j]*factor

    #check if the system has no sol or infinite sol
    for i in range(n) :
        if a[i][i]==0 :
            return("sys has no sol.")
    # Back-Substitution
    x=[0]*n
    x[n-1]=b[n-1]/a[n-1][n-1]
    for i in range (n-2,-1,-1):
        summation=0
        for j in range (i+1,n):
            summation+=a[i][j]*x[j]
        x[i]=(b[i]-summation)/a[i][i]
    return x

if __name__ == "__main__":
    n = int(input("Enter the no. of variables: "))
    #taking the variables coefficients
    a=[]
    print("Enter the coefficients of the variables")
    for i in range(1,n+1):
        a.append(list(map(int, input().split())))
    # taking the equations' constants
    b = list(map(int,input("Enter the constants of the equations: ").strip().split()))[:n]
    
    x = gaussianElimentaion(a,n)
    print("The solution of the system:")
    print (x)