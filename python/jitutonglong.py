t = int(input('头数？'))
j = int(input('脚数？'))
if j%2>0:
    print('你输错了') 
ji = 2*t-j//2
tu = t-ji    
if ji<0 or tu<0:
    print('你输错了') 
else:    
    print('鸡有',ji,'只。兔有',tu,'只。')   
