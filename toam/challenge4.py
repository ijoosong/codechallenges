'''
Initially, I wanted to do a weighted edge graph traversal where there would be weighted portions (i.e. the words google offers and the words at the center) and no matter where the traversal started, it would begin randomly traversing with those weights in mind.  I started to do a markov chain as well as doing an in depth random traversal and at the end, it was taking me too long so I started to create my own point class where I could find the direction of the weighted areas.  Ultimately, I realized, this shouldnt take me more than an hour so I wrote this simple simulation.  The comments below will be adequate in showing what is happening and when.  A basic synopsis of it would be that the viewer scrolls in, looks at the middle, reads the words while outlining with the mouse, scrolls up, and scrolls back down to the sign up now button and hovers over it.  The random is to simulate a users noise.
'''
import random

def simulate_mouse():
    '''returns [x, y, timestamp in seconds] of mouse simulation'''
    li = [[0, 130, 0], [50, 130, 0.1], [150, 130, 0.2]]
    timestamp = .2
    xp=75
    yp=130
    for x in range(1,149):
        #reads google offers in middle
        if x<21:
            li.append([xp+x*7,yp+random.randint(-2,2),round(timestamp+x*.1,1)])
        #stop and get ready to move across to "the"
        elif x == 21:
            li.append([150, 135, round(timestamp+x*.1,1)])
            xp = 80
            yp = 145
        #reads "the best of your city"
        elif x < 42:
            li.append([xp+(x-21)*7, yp+random.randint(-2,2), round(timestamp+x*.1,1)])
        #stops and goes back to "even"
        elif x == 42:
            xp = 200
            yp = 145
            li.append([xp, yp, round(timestamp+x*.1,1)])
        #reads "even better prices"
        elif x < 62:
            li.append([xp-(x-42)*6, yp-(x-42)*5, round(timestamp+x*.1,1)])
        #stops and goes up to top titlebar
        elif x == 62:
            xp = 75
            yp = 60
            li.append([xp, yp, round(timestamp+x*.1,1)])
        #read title bar
        elif x < 83:
            li.append([xp+(x-62)*7, yp+random.randint(-2,2), round(timestamp+x*.1,1)])
        #stops and goes down to button
        elif x == 83:
            xp = 230
            yp = 60
            li.append([xp, yp, round(timestamp+x*.1,1)])
        #goes down to button
        elif x < 104:
            li.append([xp-(x-83)*4, yp+(x-83)*8,round(timestamp+x*.1,1)])
        #hovers around button
        elif x == 104:
            xp = 150
            yp = 195
            li.append([xp, yp, round(timestamp+x*.1,1)])
        else:
            li.append([xp+random.randint(-5, 5), yp+random.randint(-3,3), round(timestamp+x*.1,1)])
    return li
