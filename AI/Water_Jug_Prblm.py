a = int(input('Enter the capacity of 1st jug:'))
b = int(input('Enter the capacity of 2nd jug:'))
c = int(input('Enter the goal capacity to reach:'))
# assuming 1st jug's capacity is greater than 2nd jug
if b>a:
    print('Invalid Input')
    exit()
dictjug = {}
dictjug[a], dictjug[b] = 0, 0
if b==a:
    print('No solution exists for this pair of jugs')
    exit()
diff = a-b
if c%diff!=0:
    print('No solution exists for this pair of jugs')
    exit()
while(1):
    print('Fill the jug 1 to its full capacity')
    dictjug[a]=a
    print('Water in Jug 1:',dictjug[a],' Water in Jug 2:',dictjug[b])
    print('Empty water from jug 1 into jug 2 till jug 2 fills to brim')
    add = b-dictjug[b]
    dictjug[b]+=add
    dictjug[a]-=add
    print('Water in Jug 1:',dictjug[a],' Water in Jug 2:',dictjug[b])
    if dictjug[a]==c:
        print('Goal state reached!')
        break
    print('Throw away water in jug 2')
    dictjug[b]=0
    print('Water in Jug 1:',dictjug[a],' Water in Jug 2:',dictjug[b])
    print('Empty remaining water from jug 1 into jug 2')
    dictjug[b]=dictjug[a]
    dictjug[a]=0
    print('Water in Jug 1:',dictjug[a],' Water in Jug 2:',dictjug[b])