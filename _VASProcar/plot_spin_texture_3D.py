#########################################################################################
## Versao 1.0.1 (20/01/2022) ############################################################
########################### Autores: ####################################################
## Augusto de Lelis Araujo - Federal University of Uberlandia (Uberlandia/MG - Brazil) ##
## e-mail: augusto-lelis@outlook.com                                                   ##
## =================================================================================== ##
## Renan Maciel da Paixao - Uppsala University (Uppsala/Sweden) #########################
## e-mail: renan.maciel@physics.uu.se                           #########################
#########################################################################################

import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.colors as mcolors
from scipy.interpolate import griddata
import linecache 
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
print("================ Plotando a Textura de Spin 2D_3D ================")
print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")

#===========================================================================

# normalizacao = 1  # [0] = sem normalização  //  [1] = com normalização

#===========================================================================

spin_textura = np.loadtxt("saida/Spin_3D.dat")
spin_textura.shape

number = 0
# E_min = +1000.0
# E_max = -1000.0

for i in range (Band_i,(Band_f+1)):

    number += 1
    Band = int(number + 2)

    if (number == 1):
       if (Plano_k == 1):  # Plano (kx,ky) ou (k1,k2)      
          eixo1  = spin_textura[:,0]
          eixo2  = spin_textura[:,1]
       if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3)      
          eixo1  = spin_textura[:,0]
          eixo2  = spin_textura[:,2]
       if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3)      
          eixo1  = spin_textura[:,1]
          eixo2  = spin_textura[:,2]  
          
    E  = spin_textura[:,3]
    Spin_Sx = spin_textura[:,4]
    Spin_Sy = spin_textura[:,5]
    Spin_Sz = spin_textura[:,6]

    norma = ((Spin_Sx**2) + (Spin_Sy**2))**0.5
    
    # if (norma > 0.01):
       # if (normalizacao == 1):
       # Spin_Sx = Spin_Sx/norma
       # Spin_Sy = Spin_Sy/norma
       # Spin_Sz = Spin_Sz/Spin_Sz.max()

    Spin_Sx = Spin_Sx/norma
    Spin_Sy = Spin_Sy/norma
    Spin_Sz = Spin_Sz/Spin_Sz.max()        

###########################################################################

print(".... Quase concluido ....")
print(".........................")

###########################################################################

fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_axis_off()
ax.axis('equal')

# Criação de uma escala de cor normalizada com os valores de Sz.
norm = mpl.colors.Normalize(Spin_Sz.min(), Spin_Sz.max())
icmap = 'coolwarm'
sm = mpl.cm.ScalarMappable(cmap = icmap, norm = norm)

# Define uma escala de Sz[min, max] com a marcação de 5 valores na escala.
tk = np.linspace(Spin_Sz.min(), Spin_Sz.max(), 5, endpoint = True)
plt.colorbar(sm, ticks = tk, shrink = 0.5, format='%.2f')

# width = espessura do vetor // scale = comprimento do vetor
# pivot = 'mid' (VERIFICAR)
# scale_units = 'inches' (VERIFICAR)
ax.quiver(eixo1, eixo2, Spin_Sx, Spin_Sy, Spin_Sz, width = 0.001, scale = 10, scale_units = 'inches', cmap = icmap, norm = norm)
  
fig = plt.gcf()
fig.set_size_inches(8,6)

plt.savefig('saida/Spin_Texture_2D_3D.png', dpi=300, pad_inches = 0)
plt.savefig('saida/Spin_Texture_2D_3D.pdf', dpi=300, pad_inches = 0)

plt.show()

###########################################################################

# source = r'_VASProcar\saida_plot_bandas_3D.py'
# destination = r'saida\Plot_Bandas_3D.py'
# shutil.copyfile(source, destination)

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
