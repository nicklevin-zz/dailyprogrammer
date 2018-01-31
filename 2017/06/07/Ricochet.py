# From: https://www.reddit.com/r/dailyprogrammer/comments/5vb1wf/20170221_challenge_303_easy_ricochet/
# A particle starts in the upper left corner of a grid of a user-specifed height and width,
#  and moving at a user-specified velocity. The particle is moving at a 45 degree angle
#  towards the lower-right and will therefore mirror its direction whenever it hits a wall.
#
# This program computes the amount of time and ricochets it takes for the particle
# to hit a corner, and also outputs which corner (ex. 'LL' = Lower-left)

# Input is specified '{height} {width} {velocity}'
# Output is '{corner} {ricochets} {time}'
# ex. Input = '6 6 3' -> Output = 'LR 0 2'
#     Input = '8 3 1' -> Output = 'LL 9 24'


#grab input
(y_max, x_max, velocity) = list(map(int, input("Enter '{y-max} {x-max} {velocity}': ").split()))

print("Y-Max = " + str(y_max) + " --- X-Max = " + str(x_max) + " --- Velocity = " + str(velocity))

y_offset = 1   #start particle going towards bottom-right of box
x_offset = 1
x = 0
y = 0
time = 0
ricochets = 0
endCorner = 'nope'

while endCorner == 'nope' :
    time = time + 1
    for i in range(velocity) :  #each time period, execute a movement
                                # velocity # of times

        x += x_offset           #change particle position
        y += y_offset

        #check for hitting a corner
        if (x == 0 or x == x_max) and (y == 0 or y == y_max):
            if x == 0 :
                if y == 0:
                    endCorner = 'UL'
                else :
                    endCorner = 'LL'
            elif y == 0 :
                endCorner = 'UR'
            else :
                endCorner = 'LR'
            break               #we are done once we hit a corner

        #check for hitting a wall in the x-direction
        if x == 0 or x == x_max :
            x_offset = -(x_offset)  #reverse direction
            ricochets = ricochets + 1

        #check for hitting a wall in the y-direction
        if y == 0 or y == y_max :
            y_offset = -(y_offset) #reverse direction
            ricochets = ricochets + 1

print(endCorner + ' ' + str(ricochets) + ' ' + str(time))
