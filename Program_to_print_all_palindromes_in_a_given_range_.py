min = int(input())
max = int(input())
for num in range(min, max + 1):
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10
    if(num == reverse):
        print("%d"%num, end =' ')
