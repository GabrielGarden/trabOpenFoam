import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
import pandas as pd

data = pd.read_csv('OpenFOAMdata/fireFoamCase3/t8.csv')
x = data['Points_0']
y = data['Points_1']
temp = data['T']
uMag = data['U_Magnitude']

x = np.asarray(x)
y = np.asarray(y)

var = np.asarray(temp)
# var = np.asarray(uMag)

triang = tri.Triangulation(x, y)
fig1, ax1 = plt.subplots(figsize=(16,5))
ax1.set_aspect('equal')
tcf = ax1.tricontourf(triang, var, levels=15, cmap='jet')
colorbar = fig1.colorbar(tcf, shrink=0.4, aspect=20)
plt.xlabel('X [m]')
plt.ylabel('Y [m]')


colorbar.set_label('Temperature [K]')
# colorbar.set_label('Velocity Magnitude [m/s]')

ax1.set_title('Temperature Contour Plot at t = 8s')
# ax1.set_title('Velocity Magnitude Plot at t = 30s')

plt.tight_layout()
# plt.savefig('temp-t8-case3.pdf', bbox_inches='tight', dpi=300)
plt.show()
