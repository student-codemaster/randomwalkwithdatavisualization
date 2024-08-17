import matplotlib.pyplot as plt
from random_walk import RandomWalk

# keep making new walks as long as the program is active
while True:
      #make a random walk and plot the points
    plt.title('Random  Walk',fontsize=25)
    plt.xlabel('random x values ',fontsize=14)
    plt.ylabel('random y values',fontsize=14)
    rw = RandomWalk(50000)
    rw.fill_walk()

   

    point_number = list(range(rw.num_points))
    
    plt.scatter(rw.x_values,rw.y_values,c=point_number,cmap=plt.cm.Blues,edgecolors='none',s=10)

    #emphasize the first and last points
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    plt.scatter(-500,1,c='black',edgecolor='none',s=100)

    plt.tick_params(axis='both',labelsize=20)

    plt.show()
    keep_running = input('make another walk?(y/n):')
    if keep_running == 'n':
       break 