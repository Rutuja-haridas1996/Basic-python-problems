thickness = 1 #This must be an odd number
c = 'H'
#print(c.center(10,' '))
#print((c*5).center(10,' '))

#Top Cone
for i in range(thickness*2):
    if i%2 != 0:
        print((c*i).center(thickness*2,' '))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2,' ') + (' '*(thickness*2)) + (c*thickness).center(thickness*2,' ')) 

# middle belt
for i in range((thickness+1)//2):
    print((c * thickness * 5).center((thickness*6)-1))
    #print((c*thickness*5).center((thickness + 1) * 5) -1)




#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2,' ') + (' '*(thickness*2)) + (c*thickness).center(thickness*2,' ')) 


#Bottom Cone
for i in range(thickness*2,0,-1):
    if i%2 != 0:
        print(' ' * (thickness * 4) + (c * i).center(thickness * 2, ' '))