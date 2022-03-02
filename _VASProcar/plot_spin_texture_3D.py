#########################################################################################
## VASProcar -- https://github.com/Augusto-Dlelis/VASProcar-Tools-Python ################
## Autores: #############################################################################
## =================================================================================== ##
## Augusto de Lelis Araujo - Federal University of Uberlandia (Uberlândia/MG - Brazil) ##
## e-mail: augusto-lelis@outlook.com                                                   ##
## =================================================================================== ##
## Renan da Paixão Maciel - Uppsala University (Uppsala/Sweden) #########################
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

#----------------------------------------------------------------------

print(" ")
print("================ Plotando a Textura de Spin 2D_3D ================")
print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")

#----------------------------------------------------------------------

# normalizacao = 1  # [0] = sem normalização  //  [1] = com normalização

#----------------------------------------------------------------------

spin_textura = np.loadtxt("saida/Spin_Texture/Spin_Texture.dat")
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

#----------------------------------------------------------------------

print(".... Quase concluido ....")
print(".........................")

#----------------------------------------------------------------------

font = {'family' : 'arial',  
        'color'  : 'black',  
        'weight' : 'normal',  
        'size'   : 10,  
        } 

fig = plt.figure()

ax = fig.add_subplot(111)
ax.axis('equal')
# ax.set_axis_off()

#----------------------------------------------------------------------=

if (Dimensao == 1):
   cl = r' $(2{\pi}/{a})$'
if (Dimensao == 2):
   cl = r' $({\AA}^{-1})$'
if (Dimensao == 3):
   cl = r' $({nm}^{-1})$' 

if (Plano_k == 1 and Dimensao != 4):             # Plano (kx,ky)      
   c1 = r'${k}_{x}$' + cl
   c2 = r'${k}_{y}$' + cl
if (Plano_k == 2 and Dimensao != 4):             # Plano (kx,kz)      
   c1 = r'${k}_{x}$' + cl
   c2 = r'${k}_{z}$' + cl
if (Plano_k == 3 and Dimensao != 4):             # Plano (ky,kz)      
   c1 = r'${k}_{y}$' + cl
   c2 = r'${k}_{z}$' + cl

if (Plano_k == 1 and Dimensao == 4):             # Plano (k1,k2)      
   c1 = r'${k}_{1}$'
   c2 = r'${k}_{2}$'
if (Plano_k == 2 and Dimensao == 4):             # Plano (k1,k3)      
   c1 = r'${k}_{1}$'
   c2 = r'${k}_{3}$'
if (Plano_k == 3 and Dimensao == 4):             # Plano (k2,k3)      
   c1 = r'${k}_{2}$'
   c2 = r'${k}_{3}$'

ax.set_xlabel(c1, fontdict = font)
ax.set_ylabel(c2, fontdict = font)

#----------------------------------------------------------------------

# Criação de uma escala de cor normalizada com os valores de Sz.
norm = mpl.colors.Normalize(Spin_Sz.min(), Spin_Sz.max())
icmap = 'coolwarm'
sm = mpl.cm.ScalarMappable(cmap = icmap, norm = norm)

# Define uma escala de Sz[min, max] com a marcação de 5 valores na escala.
tk = np.linspace(Spin_Sz.min(), Spin_Sz.max(), 5, endpoint = True)
plt.colorbar(sm, ticks = tk, shrink = 0.5, format='%.2f', label = '$S_{z}$')

# width = espessura do vetor // scale = comprimento do vetor
# pivot = 'mid' (VERIFICAR)
# scale_units = 'inches' (VERIFICAR)
ax.quiver(eixo1, eixo2, Spin_Sx, Spin_Sy, Spin_Sz, width = 0.001, scale = 10, scale_units = 'inches', cmap = icmap, norm = norm)
  
fig = plt.gcf()
fig.set_size_inches(8,6)

if (save_png == 1): plt.savefig('saida/Spin_Texture/Spin_Texture.png', dpi=300, pad_inches = 0)
if (save_pdf == 1): plt.savefig('saida/Spin_Texture/Spin_Texture.pdf', dpi=300, pad_inches = 0)
if (save_eps == 1): plt.savefig('saida/Spin_Texture/Spin_Texture.eps', dpi=300, pad_inches = 0)

plt.show()

#======================================================================
   
print(" ")
print("=========================================================")
print("= Edite o Plot3D por meio dos seguintes arquivos gerados ")
print("= na pasta saida\Bandas_3D ==============================")   
print("= Bandas_3D_matplotlib.py e Bandas_3D_plotly.py =========")
print("=========================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
