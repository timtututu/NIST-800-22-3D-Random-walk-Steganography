import matplotlib.pyplot as plt
import numpy as np
from numpy import empty
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
from IPython.display import HTML
length=12500001
octdata=empty(length*8)
finaloctdata=empty(len(octdata)//3+1)

#readData
def readdata():
    with open(r'C:\Users\user\Desktop\college\final_project_AES\putty_rewrite' , 'rb') as f:
        data = f.read()
    temp=1
    times=1
    print(bin(data[0]))
    for i in range(0,int(length)):
        c=(data[i])& (0b00001111)
        d=(data[i]>>4)& (0b00001111)
        for j in range(0,4):
            octdata[4*times-temp]=d&0b0001
            d>>=1
            temp+=1
        times+=1
        temp=1
        for j in range(0,4):
            octdata[4*times-temp]=c&0b0001
            c>>=1
            temp+=1
        times+=1
        temp=1  
    convertTime=0
    for i in range(0,int(len(finaloctdata))):
        if (3*convertTime+2)<=len(octdata):
            finaloctdata[convertTime]=octdata[3*convertTime]*2*2+octdata[3*convertTime+1]*2+octdata[3*convertTime+2]
            convertTime+=1

def randomWalk3D(numSteps):
  dirs = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
  # set up a 2D array to store the locations visited
  locations = np.zeros( (numSteps, 3) , dtype="int")   # numSteps rows, 3 columns
  # take steps
  for i in range(1, numSteps):
    if int(finaloctdata[i])>0 and int(finaloctdata[i])<7:
        r = int(finaloctdata[i])-1
        #print(int(r))  random integer from {0,1,2,3,4,5}
        move = dirs[int(r)]           # direction to move
        locations[i] = locations[i-1] + move  # store the next location
    else:
        locations[i] = locations[i-1]
  return locations
# function to draw each frame of the animation

def update(num, data, line):
    ax.cla()
    xmins = min(0,min(data.T[:num+1,0]))
    xmaxs = max(10, max(data.T[:num+1,0]))
    ax.set_xlim(xmins, xmaxs)
    ymins = min(0, min(data.T[:num+1,1]))
    ymaxs = max(10, max(data.T[:num+1,1]))
    ax.set_ylim(ymins,ymaxs)
    zmins = min(0, min(data.T[:num+1,2]))
    zmaxs = max(10, max(data.T[:num+1,2]))
    ax.set_zlim(zmins,zmaxs)
    line, = ax.plot([], [],[], lw=2)
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])
    ax.plot(data[0,:num], data[1,:num], data[2,:num])


# generate the random walk
readdata()
numSteps = len(finaloctdata)
locations = randomWalk3D(numSteps).T
# set up the plot
#ax = plt.axes(projection='3d')
fig = plt.figure()
ax = p3.Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)
line, = ax.plot(locations[0, 0:1], locations[1, 0:1], locations[2, 0:1])

ax.set_xlim3d([-10.0, 10.0])
ax.set_xlabel('X')

ax.set_ylim3d([-10.0, 10.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-10.0, 10.0])
ax.set_zlabel('Z')
# make the animation
ani = animation.FuncAnimation(fig, update, numSteps, fargs=(locations, line), interval=0.001, blit=False)
plt.show()
