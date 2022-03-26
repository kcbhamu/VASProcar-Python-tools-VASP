
import os
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.colors as colors
from scipy.interpolate import griddata
import pandas as pd

#--------------------------------------------------------------------------
# Variaveis que definem a espessura e o comprimento dos vetores no plot ---
#--------------------------------------------------------------------------
espessura = 0.005  #  Utilize espessura = 100 caso queira plotar apenas a cabeça triangular da seta e eliminar a cauda, 
comprimento = 2.5     #  o qual facilita em ajustar a dimensao/volume dos vetores por meio do ajuste da variavel comprimento.
#----------------

print(" ")
print("======== Plotando a Textura de Spin 2D (Curvas de Nivel) ========")

#----------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado
#----------------------------------------------------------------
if os.path.isdir('output'):
   dir_output = 'output/Spin_Texture/'
else:
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#====================================================================== 

spin = np.loadtxt(dir_output + 'Spin_Texture.dat') 
spin.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(". Pode demorar um pouco .")
print(".........................")

if (Plano_k == 1):     # Plano (kx,ky) ou (k1,k2)     
   eixo1 = spin[:,0]
   eixo2 = spin[:,1]
   
if (Plano_k == 2):     # Plano (kx,kz) ou (k1,k3)     
   eixo1 = spin[:,0]
   eixo2 = spin[:,2]
   
if (Plano_k == 3):     # Plano (ky,kz) ou (k2,k3)    
   eixo1 = spin[:,1]
   eixo2 = spin[:,2]

energia = spin[:,3]
Spin_Sx = spin[:,4]
Spin_Sy = spin[:,5]
Spin_Sz = spin[:,6]

pulo = (pulo + 1)
levels = [0]*1

#----------------------------------------------------------------------
   
if (Dimensao < 4 and Plano_k == 1):
   ca = r'${k}_{x}$'; cb = r'${k}_{y}$'
   sa = r'${S}_{x}$  |  '; sb = r'${S}_{y}$  |  '; sc = r'${S}_{z}$  |  '  
if (Dimensao < 4 and Plano_k == 2):
   ca = r'${k}_{x}$'; cb = r'${k}_{z}$'
   sa = r'${S}_{x}$  |  '; sb = r'${S}_{z}$  |  '; sc = r'${S}_{y}$  |  ' 
if (Dimensao < 4 and Plano_k == 3):
   ca = r'${k}_{y}$'; cb = r'${k}_{z}$'
   sa = r'${S}_{y}$  |  '; sb = r'${S}_{z}$  |  '; sc = r'${S}_{x}$  |  ' 
   
#--------------------------------------   

if (Dimensao == 4 and Plano_k == 1):
   ca = r'${k}_{1}$'; cb = r'${k}_{2}$'
   sa = r'${S}_{x}$  |  '; sb = r'${S}_{y}$  |  '; sc = r'${S}_{z}$  |  '
if (Dimensao == 4 and Plano_k == 2):
   ca = r'${k}_{1}$'; cb = r'${k}_{3}$'
   sa = r'${S}_{x}$  |  '; sb = r'${S}_{z}$  |  '; sc = r'${S}_{y}$  |  ' 
if (Dimensao == 4 and Plano_k == 3):
   ca = r'${k}_{2}$'; cb = r'${k}_{3}$'
   sa = r'${S}_{y}$  |  '; sb = r'${S}_{z}$  |  '; sc = r'${S}_{x}$  |  ' 

#-------------------------------------- 

if (Dimensao == 1): cc = r' $(2{\pi}/{a})$'
if (Dimensao == 2): cc = r' $({\AA}^{-1})$'
if (Dimensao == 3): cc = r' $({nm}^{-1})$'
if (Dimensao == 4): cc = ' '

# Create meshgrid for x,y ------------------------------------------------

xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)

e_grid = griddata((eixo1,eixo2), energia, (x_grid,y_grid), method = 'cubic')

#=========================================================================
# Plot 2D da Projecao do Spin sobre as Curvas de Nível: ==================
#=========================================================================

for i in range (1,(4+1)):

   font = {'family': 'arial', 'color': 'black', 'weight': 'normal', 'size': 10}

   map_black = (mpl.colors.ListedColormap(['black', 'black']))

   fig = plt.figure()
   ax = fig.add_subplot(111)

#-----------------------------------------------------------------------

   if (i == 1):
      c1 = sa + ca + cc
      c2 = cb + cc
      rotulo = 'Sx'
      
   if (i == 2):
      c1 = ca + cc
      c2 = sb + cb + cc      
      rotulo = 'Sy'
      
   if (i == 3):
      c1 = sc + ca + cc
      c2 = cb + cc      
      rotulo = 'Sz'
      
   if (i == 4):     
      c1 = sa + ca + cc
      c2 = sb + cb + cc

#-----------------------------------------------------------------------

   for j in range(n_contour):

       if (min(energia) < levels_n[j] and max(energia) > levels_n[j]):
       
          #---------------------------------------------------------------------------------------------------------------------------------------
          levels[0] = levels_n[j]
          cs = plt.contour(x_grid, y_grid, e_grid, levels, linestyles = '-', cmap = map_black, linewidths = 0.5, alpha = 1.0, antialiased = True)
          #---------------------------------------------------------------------------------------------------------------------------------------
          paths = cs.collections[0].get_paths()
          verts = [xx.vertices for xx in paths]
          points = np.concatenate(verts)
          #---------------------------------------------------------------------------------------------------------------------------------------
          new_Sx = griddata((eixo1,eixo2), Spin_Sx, (points[::pulo,0], points[::pulo,1]))
          new_Sy = griddata((eixo1,eixo2), Spin_Sy, (points[::pulo,0], points[::pulo,1]))
          new_Sz = griddata((eixo1,eixo2), Spin_Sz, (points[::pulo,0], points[::pulo,1]))
          #---------------------------------------------------------------------------------------------------------------------------------------

          if (i == 4 and Plano_k == 1):  # Plano (kx,ky) ou (k1,k2)       
             Spin_S1 = new_Sx
             Spin_S2 = new_Sy
             rotulo = 'SxSy'
         
          if (i == 4 and Plano_k == 2):  # Plano (kx,kz) ou (k1,k3)
             Spin_S1 = new_Sx
             Spin_S2 = new_Sz
             rotulo = 'SxSz'
         
          if (i == 4 and Plano_k == 3):  # Plano (ky,kz) ou (k2,k3)
             Spin_S1 = new_Sy
             Spin_S2 = new_Sz
             rotulo = 'SySz' 

          #---------------------------------------------------------------------------------------------------------------------------------------          
       
          passo = len(new_Sx)
          nulo = [0.0]*passo
          angle = [0]*passo
   
          for k in range(passo):
              #----------------------------------------
              if (i == 1):
                 v_spin = [new_Sx[k], 0.0]
                 
              if (i == 2):
                 v_spin = [0.0, new_Sy[k]]
                 
              if (i == 3):
                 v_spin = [new_Sz[k], 0.0]
                 
              if (i == 4):
                 v_spin = [Spin_S1[k], Spin_S2[k]]
              #----------------------------------------
              u = v_spin / np.linalg.norm(v_spin)
              v = [1.0, 0.0]
              dot_product = np.dot(u, v)
              angle[k] = np.arccos(dot_product) / np.pi * 180
              c = np.cross(u,v)
              if (c > 0):
                 angle[k] += 180

          #---------------------------------------------------------------------------------------------------------------------------------------
          # map_red_blue = colors.ListedColormap(['red', 'blue','red', 'blue'])
          # boundaries = [0, 90, 180, 270, 360] 
          #---------------------------------------------------------------------------------------------------------------------------------------
          map_red_blue = colors.LinearSegmentedColormap.from_list("", ["red","white","red","white","blue","white","blue","white","red"])
          norma = colors.Normalize(0, 360)
          #---------------------------------------------------------------------------------------------------------------------------------------
          if (i == 1):
             ax.quiver(points[::pulo,0], points[::pulo,1], new_Sx, nulo, angle, cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                       alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'tail', minlength = 0.0)
             
          if (i == 2):
             ax.quiver(points[::pulo,0], points[::pulo,1], nulo, new_Sy, angle, cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                       alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'tail', minlength = 0.0)
             
          if (i == 3):
             ax.quiver(points[::pulo,0], points[::pulo,1], new_Sz, nulo, angle, cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                       alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'tail', minlength = 0.0)
             
          if (i == 4):
             ax.quiver(points[::pulo,0], points[::pulo,1], Spin_S1, Spin_S2, angle, cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                       alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'tail', minlength = 0.0)             
          #---------------------------------------------------------------------------------------------------------------------------------------       
          # plt.quiver(points[::pulo,0], points[::pulo,1], Spin_S1, Spin_S2, angle,
          #            scale_units = "xy", angles = "xy", pivot = 'tail', cmap = map_red_blue, norm = norma, linewidths = 0.5, edgecolor = 'black', alpha = transp)   
          #---------------------------------------------------------------------------------------------------------------------------------------
          ax.clabel(cs, inline = False, colors = 'black', fontsize = 8)   

#----------------------------------------------------------------------

   ax.set_xlabel(c1, fontdict = font)
   ax.set_ylabel(c2, fontdict = font)
   ax.set_box_aspect(1.0/1)   

#----------------------------------------------------------------------

   if (save_png == 1): plt.savefig(dir_output + 'Spin_Texture_Contour_' + rotulo + '.png', dpi = 600, pad_inches = 0)
   if (save_pdf == 1): plt.savefig(dir_output + 'Spin_Texture_Contour_' + rotulo + '.pdf', dpi = 600, pad_inches = 0)
   if (save_eps == 1): plt.savefig(dir_output + 'Spin_Texture_Contour_' + rotulo + '.eps', dpi = 600, pad_inches = 0)

   fig = plt.gcf()
   fig.set_size_inches(8,6)
   # plt.show()

#======================================================================
   
if (dir_output != ''):
   print(" ")
   print("============================================================")
   print("= Edite os Plots por meio do arquivo Spin_Texture_Contour.py")
   print("= gerado na pasta output\Spin_Texture ======================")   
   print("============================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
