from django.shortcuts import render

# Create your views here.
def index(request):
        c=''
        try:
            if request.method=='POST':
                n1=eval(request.POST.get('num1'))
                n2=eval(request.POST.get('num2'))
                op=request.POST.get('op')
                
                if op=='+':
                    c=n1+n2
                elif op=='-':
                    c=n1-n2
                elif op=='*':
                    c=n1*n2
                elif op=='/':
                    c=n1/n2     
        except:
            c='invalid ops............'            
        print(c)           
        return render(request,'index.html',{'c':c})


def num(request):
    p=''
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            if n1%2==0:
                p='Even'
            else:    
                p='Odd'
    except:
        p='invalid...........'
    print(p)    
    return render(request,'num.html',{'p':p})        

def pnum(request):
    pn=''

    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            if n1>1:
                for i in range(2,int(n1/2)+1):
                    if n1%i==0 :
                        pn="NOT PRIME"
                    else:
                        pn="PRIME"
            else:pn="NOT PRIME"

    except:
        pn='invalid....'
    print(pn)
    return render(request,'pnum.html',{'pn':pn})    

def hcf(request):
    mn=''
    hcf=''
    try:
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        if n2>n1:
            mn=n1
        else :
            mn=n2
        for i in range(1,mn+1):
            if n1%i==0 and n2%i==0:
                hcf = i
    except:
        mn='invalid....'
    print(hcf)        
    return render(request,'hcf.html',{'hcf':hcf})   


