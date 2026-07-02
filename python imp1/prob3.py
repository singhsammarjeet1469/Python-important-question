# spam checking old tradition
p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
a=input('enter the message:')
if(p1 in a or p2 in a or p3 in a or p4 in a):
    print('this is  the scam:')
else:
    print('not scam')