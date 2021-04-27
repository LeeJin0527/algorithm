
answer = int(input(),16)

for i in range(1,16):
    print(format('%X'%(answer)) + "*" + format('%X'%(i)) +"=" +format('%X'%(answer * i)))
    
