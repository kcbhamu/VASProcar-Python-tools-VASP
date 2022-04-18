
import os
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

print(" ")
print("============== Plotando as Curvas de Nivel ==============")

#------------------------------------------------------------------------
# Teste para saber quais diretorios devem ser corretamente informados ---
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '\output\Level_Countour\\'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#====================================================================== 

countour = np.loadtxt(dir_output + 'Level_Countour.dat') 
countour.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(". Pode demorar um pouco .")
print(".........................")

if (Plano_k == 1):     # Plano (kx,ky) ou (k1,k2)     
   eixo1 = countour[:,0]
   eixo2 = countour[:,1]
if (Plano_k == 2):     # Plano (kx,kz) ou (k1,k3)     
   eixo1 = countour[:,0]
   eixo2 = countour[:,2]
if (Plano_k == 3):     # Plano (ky,kz) ou (k2,k3)    
   eixo1 = countour[:,1]
   eixo2 = countour[:,2]

energ = countour[:,(Band + 2)]

#-------------------------------------------------------------------------  

if (tipo_contour == 1):
   levels_n = [0.0]*n_contour
   for i in range(n_contour):
       levels_n[i] = energ_i + ((energ_f - energ_i)/(n_contour - 1))*(i)

# Create meshgrid for x,y,z ----------------------------------------------

xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)
z_grid = griddata((eixo1,eixo2), energ, (x_grid,y_grid), method = 'cubic')

#-------------------------------------------------------------------------

font = {'family' : 'arial',  
        'color'  : 'black',  
        'weight' : 'normal',  
        'size'   : 10,  
        }

#-------------------------------------------------------------------------

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

   

#=========================================================================
# Plot 2D das Curvas de Nível: ===========================================
#=========================================================================

fig, ax = plt.subplots()

cmap_gray = (mpl.colors.ListedColormap(['darkgray', 'darkgray']))

if (tipo_contour == 0):
   cp = plt.contourf(x_grid, y_grid, z_grid, levels = n_contour, cmap = "bwr", alpha = transp, antialiased = True)
   cp = plt.contour(x_grid, y_grid, z_grid, levels = n_contour, linestyles = '-', cmap = cmap_gray, linewidths = 0.5, alpha = 1.0, antialiased = True)

if (tipo_contour > 0):
   cp = plt.contourf(x_grid, y_grid, z_grid, levels = levels_n, cmap = "bwr", alpha = transp, antialiased = True)
   cp = plt.contour(x_grid, y_grid, z_grid, levels = levels_n, linestyles = '-', cmap = cmap_gray, linewidths = 0.5, alpha = 1.0, antialiased = True)

plt.clabel(cp, inline = False, colors = 'black', fontsize = 8)

plt.xlabel(c1, fontdict = font)
plt.ylabel(c2, fontdict = font)

ax.set_box_aspect(1.0/1)

if (save_png == 1): plt.savefig(dir_output + "Level_Countour_2D.png", dpi = 600, pad_inches = 0)
if (save_pdf == 1): plt.savefig(dir_output + "Level_Countour_2D.pdf", dpi = 600, pad_inches = 0)
if (save_eps == 1): plt.savefig(dir_output + "Level_Countour_2D.eps", dpi = 600, pad_inches = 0)

# plt.show()



#=========================================================================
# Plot 3D das Curvas de Nível: ===========================================
#=========================================================================

fig = plt.figure()
ax = plt.axes(projection='3d')

cmap_black = (mpl.colors.ListedColormap(['black', 'black']))

if (tipo_contour == 0): plt.contour(x_grid, y_grid, z_grid, levels = n_contour, linestyles = '-', cmap = cmap_black, alpha = 1.0, antialiased = True)
if (tipo_contour > 0):  plt.contour(x_grid, y_grid, z_grid, levels = levels_n,  linestyles = '-', cmap = cmap_black, alpha = 1.0, antialiased = True)

plt.xlabel(c1, fontdict = font)
plt.ylabel(c2, fontdict = font)
ax.set_zlabel(r'$E-{E}_{f}(eV)$', fontdict = font)

# ax.set_xlim((-5,5))
# ax.set_ylim((-5,5))
# ax.set_zlim((-5,5))
# ax.view_init(elev = 5, azim = 45)
  
fig = plt.gcf()
fig.set_size_inches(8,6)

if (save_png == 1): plt.savefig(dir_output + "Level_Countour_3D.png", dpi = 600, pad_inches = 0)
if (save_pdf == 1): plt.savefig(dir_output + "Level_Countour_3D.pdf", dpi = 600, pad_inches = 0)
if (save_eps == 1): plt.savefig(dir_output + "Level_Countour_3D.eps", dpi = 600, pad_inches = 0)

plt.show()

#======================================================================
   
if (dir_output != ''):
   print(" ")
   print("=========================================================")
   print("= Edite os Plots por meio do arquivo Level_Countour.py ==")
   print("= gerado na pasta output\Level_Countour =================")   
   print("=========================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
