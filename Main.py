import matplotlib.pyplot as plt # Importing the Module for this Program to Work.
   
a = ['JavaScript','Python','HTML/CSS','SQL','Java'] # Giving it Data to Plot.
b = [67.8, 41.7, 63.5, 54.4, 41.1] # Giving Y-Axis Coordinates to Plot the Graph in Correct Length.

plt.plot(a, b, color='deeppink', marker='o') # Plotting the Graph.
plt.title('Linear Graph') # Giving the Title to the Graph.
plt.xlabel('Programming Language Name') # Giving Name to X-Axis.
plt.ylabel('Popularity') # Giving Name to Y-Axis.
plt.grid(True) # Giving it a Grid Background. It isn't Necessary.
plt.show() # Displaying the Graph to the User.