#How many seconds are there in 42 minutes 42 seconds?
print (42 * 60 + 42)

#How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
print (10 / 1.61) 

#If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

#avg pace mile/min
print (412.482/60)

#avg pace mile/sec
print (2562/6.211180124223602)

# 9/4/2018 Exercise 1 
# What is the volume of a sphere with radius 5?
pi = 3.14
r_cubed = 5 * 5 * 5
vol = 4 / 3 

print('The volume of a sphere with a radius of 5 is {}'.format(vol * pi * r_cubed))

#Suppose the cover price of a book is $24.95, but bookstores get a 40\% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
initial_ship = 3
additional_ship = (3/4)
price = 24.95
discount = (6/10)

print('The total wholesale cost for 60 copies of the books is {}'.format(price * discount * 60 + initial_ship * 1 + additional_ship * 59))

#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

start = 6 + 52 / 60.0
easy = (8 + 15 / 60.0 ) / 60.0
fast= (7 + 12 / 60.0) / 60.0
total_run = 2 * easy + 3 * fast
bfast_hr = start + total_run
bfast_min = (bfast_hr-int(bfast_hr))*60
bfast_sec= (bfast_min-int(bfast_min))*60

print ('You will finish and have breakfast by', int(bfast_hr),':', int (bfast_min),':', int (bfast_sec) )

#If my average grade rises from 82 to 89. What is the percentage of the increase? Format the result as 'xx.x%'. Keep one figure after decimal point.

perc_inc = ((((89 - 82) / 82) * 100))

print('The percentage increase is {:.2f}%'.format(perc_inc))