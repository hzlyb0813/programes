def chickenrabbit(head,foot):
    chicken = 2*head-foot//2
    rabbit = head-chicken 
    return chicken,rabbit
head = 100
foot = 200
while True:
    chicken,rabbit = chickenrabbit(head,foot) 
    print('鸡有',chicken,'只。兔有',rabbit,'只。脚有',foot,'只')
    if foot>399:
        break
    foot = foot+1