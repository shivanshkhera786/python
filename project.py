print("Name:Shivansh Khera\nReg no.:12206142\nRoll No.:66\nSection:K22GP\nProject No.:18")
#x:- hour | y:- minute
def find_angle(x,y):
# Because input can be in 24 hour format also so have to convert it into 12 hour format
    if x>12:
        x=x-12
# angle subtended per hour is 360/12=30 and angle subtended per minute is 360/60=6
    hr_hand=(x*30)+(y*0.5)
    min_hand=y*6
    diff=hr_hand-min_hand
# we have to take value of smaller angle between minute and hour hand
    if diff>180:
        diff=360-diff
# if the difference of hour hand and minute hand comes in negative so we have to convert it into positive value
    if diff<0:
        diff=-(diff)
    if diff==360:
        diff=0
    return diff
#taking input in hh:mm format
time=input("Enter time:")
x,y=time.split(":")
print(find_angle(int(x),int(y)))