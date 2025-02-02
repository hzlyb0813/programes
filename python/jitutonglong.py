import sys
head = int(input('head？'))
foot = int(input('foot？'))
if foot%2>0:
    print('你输错了')
    sys.exit()
chicken = 2*head-foot//2
rabbit = head-chicken    
if chicken<0 or rabbit<0:
    print('你输错了') 
else:    
    print('鸡有',chicken,'只。兔有',rabbit,'只。')   
