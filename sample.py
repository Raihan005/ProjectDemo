import random
def cat():
    msg = ''
    meows = ['meow','Meow..',"Meowww","MEOW","MEWOOOWWWW...",'meOWW',"MeOw..","MEEowW","Meoooww..."]
    purs = 'purrrrrr......'
    cmd = random.randint(0,1)
    if cmd == 0:
        len = random.randint(10,20)
        position = -1
        while position!= 0:
            position = random.randint(0,8)
            msg = msg+meows[position]+" "
            len-=1
        return msg
    else:
        return purs 