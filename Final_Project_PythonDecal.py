
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression


Column_Names_3 = ['R.A_3', 'Declination_3', 'Velocity_Dispursion_(Log)', 'Error_VD', 'i_band', 'Physical_Size_R_0', 'Error_R', 'Surface_Brightness', 'Error_Surface_Brightness', 'Absolute_Magnitude', 'Error_AM', 'Absolute_Magnitude_Model', 'Error_AMM', 'K-Correction', 'Number_of_neighboors_Local_Density']
Data_Set_3 = pd.read_csv('table3c.dat', delim_whitespace = True, names = Column_Names_3)

Data_Set_3 = Data_Set_3.drop_duplicates()

Column_Names_2 = ['R.A_2', 'Declination_2', 'Redshift_(z)', 'Redshift_Error', 'S/N', 'i_band', 'Half-Light_Radius', 'Error_Half-Light', 'Apparent_Magnitude_Fitted', 'Error_Apparent_Magnitude', 'Model_Magnitude', 'Error_Model_Magnitude', 'Axis_Ratio_b/a', 'Error_Axis_Ratio']
Data_Set_2 = pd.read_csv('table2c.dat', delim_whitespace = True, names = Column_Names_2)

Data_Set_2 = Data_Set_2.drop_duplicates()

Surface_Brightness = Data_Set_3['Surface_Brightness']

Surface_Brightness_Error = Data_Set_3['Error_Surface_Brightness']

Velocity_Dispersion_Log = Data_Set_3['Velocity_Dispursion_(Log)']

Error_VD = Data_Set_3['Error_VD']

Half_Light_Radius = Data_Set_2['Half-Light_Radius']

Error_HLR = Data_Set_2['Error_Half-Light']

SB_Log = np.log10(Surface_Brightness)

Half_Light = np.log10(Half_Light_Radius)

#Plot 1: Velocity vs Surface Brightness

plt.figure()
plt.scatter(Velocity_Dispersion_Log, SB_Log, marker = '.', color = 'blue')
plt.xlabel('Velocity Dispersion (Log)')
plt.ylabel('Surface Brightness (Log)')
plt.title('Velocity Dispersion vs Surface Brightness')
plt.savefig("VD_vs_SB")

plt.figure()
plt.scatter(Velocity_Dispersion_Log, SB_Log, marker = '.', color = 'blue')
plt.xlabel('Velocity Dispersion (Log)')
plt.ylabel('Surface Brightness (Log)')
plt.title('Velocity Dispersion vs Surface Brightness')
plt.savefig("VD_vs_SB_fit")

z_fit = np.polyfit(Velocity_Dispersion_Log, SB_Log, 1)
p = np.poly1d(z_fit)
plt.plot(Velocity_Dispersion_Log, p(Velocity_Dispersion_Log), "r--")
plt.savefig("VD_vs_SB_fit")


#Plot 2: The Fundamental Plane 

x = Half_Light
y = SB_Log
z = Velocity_Dispersion_Log

fig = plt.figure()
ax =fig.add_subplot(111, projection = '3d')
ax.scatter(x, y, z, color = 'blue', marker = '.')
ax.set_xlabel('Half-Light Radius (Log)')
ax.set_zlabel('Surface Brightness (Log)')
ax.set_ylabel('Velocity Dispersion (Log)')
ax.set_title('The Fundamental Plane')
plt.savefig("The_Fundamental_Plane")
ax.grid(False)

#Attention:  This next part of the code was an attempt to make a plane fit for the fundumental plane 3d model.
#            It was not up to the standards I wanted (It just wouldn't align with the actual plane) so I have
#            refraned from including it in the final paper. But it is here for your viewing pleasure.


#fig = plt.figure()

#X = np.column_stack((Half_Light, SB_Log))
#model = LinearRegression()
#model.fit(X, Velocity_Dispersion_Log)

#x_plane = np.linspace(0, 2, 8)
#y_plane = np.linspace(0, 2, 8)
#x_plane, y_plane = np.meshgrid(x_plane, y_plane)
#z_plane = model.coef_[0] * x_plane + model.coef_[1] * y_plane + model.intercept_
#ax.plot_surface(x_plane, y_plane, z_plane, alpha=0.5)
#ax.set_xlim(-.5,2) # Half-light 
#ax.set_ylim(1.2,1.4) # Velocity Dispersion
#ax.set_zlim(1.5,3) #Surface Brightness

#ax =fig.add_subplot(111, projection = '3d')
#ax.scatter(x, y, z, color = 'blue', marker = '.')
#ax.set_xlabel('Half-Light Radius (Log)')
#ax.set_zlabel('Surface Brightness (Log)')
#ax.set_ylabel('Velocity Dispersion (Log)')
#ax.set_title('The Fundamental Plane')
#ax.grid(False)



#Plot 3: Half-Light Radius vs Surface Brightness

plt.figure()
plt.scatter(Half_Light, SB_Log, marker = '.', color = 'blue')
plt.xlabel('Half-Light Radius (Log)')
plt.ylabel('Surface Brightness (Log)')
plt.title('Half-Light Radius vs Surface Brightness')
plt.savefig("HL_vs_SB")

plt.figure()
plt.scatter(Half_Light, SB_Log, marker = '.', color = 'blue')
plt.xlabel('Half-Light Radius (Log)')
plt.ylabel('Surface Brightness (Log)')
plt.title('Half-Light Radius vs Surface Brightness')

z_fit = np.polyfit(Half_Light, SB_Log, 1)
p = np.poly1d(z_fit)
plt.plot(Half_Light, p(Half_Light), "r--")
plt.savefig("HL_vs_SB_fit")


# Plot 4: Velocity Dispursion vs Half-Light Radius

plt.figure()
plt.scatter(Half_Light, Velocity_Dispersion_Log, marker = '.', color = 'blue')
plt.xlabel('Half-Light Radius (Log)')
plt.ylabel('Velocity Dispersion (Log)')
plt.title('Half-Light Radius vs Velocity Dispersion')
plt.savefig("HL_vs_VD")

plt.figure()
plt.scatter(Half_Light, Velocity_Dispersion_Log, marker = '.', color = 'blue')
plt.xlabel('Half-Light Radius (Log)')
plt.ylabel('Velocity Dispersion (Log)')
plt.title('Half-Light Radius vs Velocity Dispersion')

z_fit = np.polyfit(Half_Light, Velocity_Dispersion_Log, 1)
p = np.poly1d(z_fit)
plt.plot(Half_Light, p(Half_Light), "r--")
plt.savefig("HL_vs_VD_fit")

plt.show()
