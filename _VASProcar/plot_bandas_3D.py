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
import shutil

####################################################################################################################################
## Desmarque e preencha os dados abaixo para executar este código isoladamente: ================================================= ##
####################################################################################################################################
# escolha   = ???  # [6] Bandas 3D // [77] Bandas 2D em 3D // [66] Gerar KPOINTS 3D                                               ##
# Band_i    = ???  # Banda inicial a ser plotada.                                                                                 ##                          
# Band_f    = ???  # Banda final a ser plotada.                                                                                   ##
# Plano_k   = ???  # [1] Plano (kx,ky) ou (k1,k2) // [2] Plano (kx,kz) ou (k1,k3) // [3] Plano (ky,kz) ou (k2,k3)                 ##
# Dimensao  = ???  # [1] (kx,ky,kz) 2pi/Param. // [2] (kx,ky,kz) 1/Angs. // [3] (kx,ky,kz) 1/nm. // [4] (k1,k2,k3) Coord. Diretas ##                               
# tipo_plot = ???  # [0] Plotado em pontos // [1] Plotado superficies                                                             ##
####################################################################################################################################

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

###########################################################################

banda = np.loadtxt("saida/Bandas_3D.dat")
banda.shape

number = 0
# E_min = +1000.0
# E_max = -1000.0

for i in range (Band_i,(Band_f+1)):

    number += 1
    Band = int(number + 2)

    if (number == 1):
       if (Plano_k == 1):  # Plano (kx,ky) ou (k1,k2)      
          eixo1  = banda[:,0]
          eixo2  = banda[:,1]
       if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3)      
          eixo1  = banda[:,0]
          eixo2  = banda[:,2]
       if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3)      
          eixo1  = banda[:,1]
          eixo2  = banda[:,2]
          
    E[number] = banda[:,Band]

###########################################################################

print(".... Quase concluido ....")
print(".........................")

###########################################################################

fig = plt.figure()

# ax = fig.add_subplot(projection="3d")
ax = plt.axes(projection='3d')

# colormap = plt.cm.get_cmap('coolwarm')
# normalize = mcolors.Normalize(vmin = E_min, vmax = E_max)

number = 0

for i in range (Band_i,(Band_f+1)):
    number += 1

    if ((escolha == 6 or escolha == -6) and tipo_plot == 0):
       ax.scatter(eixo1, eixo2, E[number], s=1.0, alpha = 0.9, antialiased = False)
    if ((escolha == 6 or escolha == -6) and tipo_plot == 1):
       ax.plot_trisurf(eixo1, eixo2, E[number], alpha = 0.9, cmap = 'coolwarm', edgecolor='black', linewidth = 0.0, antialiased = False)
       # ax.plot_trisurf(eixo1, eixo2, E[number], alpha = 0.9, cmap = colormap, norm = normalize, edgecolor='black', linewidth = 0.0, antialiased = False)
    if (escolha == 77 or escolha == -77):
       ax.plot(eixo1, eixo2, E[number], alpha = 0.9, linewidth = 1.0, antialiased = False)

    # ax.contourf(X, Y, Z[i], zdir = 'z', alpha = 0.9, offset = #####, cmap = cmap1)

if (Plano_k == 1 and Dimensao != 4):             # Plano (kx,ky)      
   ax.set_xlabel(r'${k}_{x}$', fontdict = font)
   ax.set_ylabel(r'${k}_{y}$', fontdict = font)
if (Plano_k == 2 and Dimensao != 4):             # Plano (kx,kz)      
   ax.set_xlabel(r'${k}_{x}$', fontdict = font)
   ax.set_ylabel(r'${k}_{z}$', fontdict = font)
if (Plano_k == 3 and Dimensao != 4):             # Plano (ky,kz)      
   ax.set_xlabel(r'${k}_{y}$', fontdict = font)
   ax.set_ylabel(r'${k}_{z}$', fontdict = font)

if (Plano_k == 1 and Dimensao == 4):             # Plano (k1,k2)      
   ax.set_xlabel(r'${k}_{1}$', fontdict = font)
   ax.set_ylabel(r'${k}_{2}$', fontdict = font)
if (Plano_k == 2 and Dimensao == 4):             # Plano (k1,k3)      
   ax.set_xlabel(r'${k}_{1}$', fontdict = font)
   ax.set_ylabel(r'${k}_{3}$', fontdict = font)
if (Plano_k == 3 and Dimensao == 4):             # Plano (k2,k3)      
   ax.set_xlabel(r'${k}_{2}$', fontdict = font)
   ax.set_ylabel(r'${k}_{3}$', fontdict = font)   

ax.set_zlabel(r'$E(eV)$', fontdict = font)

# ax.set_xlim((-5,5))
# ax.set_zylim((-5,5))
# ax.set_zlim((-5,5))

ax.view_init(elev = 5, azim = 45)
  
fig = plt.gcf()
fig.set_size_inches(8,6)

plt.savefig('saida/Bandas_3D.png', dpi = 300, pad_inches = 0)
plt.savefig('saida/Bandas_3D.pdf', dpi = 300, pad_inches = 0)

plt.show()

###########################################################################

source = r'_VASProcar\saida_plot_bandas_3D.py'
destination = r'saida\Plot_Bandas_3D.py'
shutil.copyfile(source, destination)

###########################################################################

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################
