##############################################################
# Versao 1.001 (10/01/2022) ##################################
########################## Autores: ##########################
# Augusto de Lelis Araújo - INFIS/UFU (Uberlândia/MG) ########
# e-mail: augusto-lelis@outlook.com ##########################
# ---------------------------------------------------------- #
# Renan Maciel da Paixão - ????????????????????????????????? #
# e-mail: ?????????????????????.com ##########################
##############################################################

import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.colors as mcolors
from scipy.interpolate import griddata
import pandas as pd

###########################################################################
## Preencha abaixo as Bandas que deseja plotar: ======================== ##
###########################################################################

Band_i = ???  # Banda inicial a ser plotada.                           
Band_f = ???  # Banda final a ser plotada.

###########################################################################           

print(" ")
print("================= Plotando as Bandas 3D =================")
print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")

###########################################################################

font = {'family' : 'arial',  
        'color'  : 'black',  
        'weight' : 'normal',  
        'size'   : 13,  
        } 

###########################################################################

E = [0]*((Band_f - Band_i)+2)
Z = [0]*((Band_f - Band_i)+2)

banda = np.loadtxt("Bandas_3D.dat")
banda.shape

nk = len(banda)

number = 0
E_min = +1000.0
E_max = -1000.0

###########################################################################

for i in range (Band_i,(Band_f+1)):

    number += 1
    Band = int(number + 2)

    if (number == 1):
       k1  = banda[:,0]
       k2  = banda[:,1]

    E[number] = banda[:,Band]

# =============== Cria matrizes 1D a partir das matrizes 2D ===============

    x = k1.reshape(nk)
    y = k2.reshape(nk)
    z = E[number].reshape(nk)
    xyz = {'x': x, 'y': y, 'z': z}

# ========================= Recria as matrizes 2D =========================

    df = pd.DataFrame(xyz, index=range(len(xyz['x'])))

    if (df['z'].min() < E_min):
       E_min = df['z'].min()
    if (df['z'].max() > E_max):
       E_max = df['z'].max()

    tx = np.linspace(df['x'].min(), df['x'].max(), len(df['x'].unique()))
    ty = np.linspace(df['y'].min(), df['y'].max(), len(df['y'].unique()))
    X,Y = np.meshgrid(tx, ty)
    Z[number] = griddata((df['x'], df['y']), df['z'], (X,Y), method = 'cubic')

###########################################################################

print(".... Quase concluido ....")
print(".........................")

###########################################################################

fig = plt.figure()

ax = fig.add_subplot(projection="3d")

colormap = plt.cm.get_cmap('coolwarm')
normalize = mcolors.Normalize(vmin = E_min, vmax = E_max)

number = 0

for i in range (Band_i,(Band_f+1)):
    number += 1
    ax.plot_surface(X, Y, Z[number], alpha = 0.9, rstride = 1, cstride = 1, cmap = colormap, norm = normalize, edgecolor='black', linewidth = 0.0, antialiased = False)
    # ax.contourf(X, Y, Z[i], zdir = 'z', alpha = 0.9, offset = #####, cmap = cmap1)

ax.set_xlabel(r'${k}_{1}$', fontdict = font)
ax.set_ylabel(r'${k}_{2}$', fontdict = font)
ax.set_zlabel(r'$E(eV)$', fontdict = font)
# ax.set_xlim((-5,5))
# ax.set_zylim((-5,5))
# ax.set_zlim((-5,5))
ax.set_xticks([])
ax.view_init(elev = 5, azim = 45)
  
fig = plt.gcf()
fig.set_size_inches(8,6)

plt.savefig('Bandas_3D.png',dpi=300,pad_inches = 0)
plt.savefig('Bandas_3D.pdf',dpi=300,pad_inches = 0)

plt.show()

###########################################################################

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

