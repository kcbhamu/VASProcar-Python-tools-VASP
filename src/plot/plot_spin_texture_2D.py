
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
import linecache 
import pandas as pd
import shutil

#--------------------------------------------------------------------------
# Variaveis que definem a espessura e o comprimento dos vetores no plot ---
#--------------------------------------------------------------------------
espessura = 0.0015  #  Utilize espessura = 100 caso queira plotar apenas a cabeça triangular da seta e eliminar a cauda, 
comprimento = 5     #  o qual facilita em ajustar a dimensao/volume dos vetores por meio do ajuste da variavel comprimento.
#--------------

print(" ")
print("=========== Plotando a Textura de Spin 2D (Matplotlib) ===========")

#----------------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado -----
#----------------------------------------------------------------------
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

spin_textura = np.loadtxt(dir_output + 'Spin_Texture.dat')
spin_textura.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")

#----------------------------------------------------------------------

energia = spin_textura[:,3]
Spin_Sx = spin_textura[:,4]
Spin_Sy = spin_textura[:,5]
Spin_Sz = spin_textura[:,6]

pulo = (pulo + 1)
transp = 1.0

#-------------------------------------- 

if (Plano_k == 1):  # Plano (kx,ky) ou (k1,k2)
   eixo1  = spin_textura[:,0]
   eixo2  = spin_textura[:,1]
   
if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3)
   eixo1  = spin_textura[:,0]
   eixo2  = spin_textura[:,2]
   
if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3)
   eixo1  = spin_textura[:,1]
   eixo2  = spin_textura[:,2]
   
#-------------------------------------- 
   
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

#------------------------------------------

if (Dimensao == 1): cc = r' $(2{\pi}/{a})$'
if (Dimensao == 2): cc = r' $({\AA}^{-1})$'
if (Dimensao == 3): cc = r' $({nm}^{-1})$'
if (Dimensao == 4): cc = ' '

#----------------------------------------------------------------------

for i in range (1,(4+1)):

   font = {'family': 'arial', 'color': 'black', 'weight': 'normal', 'size': 10} 

   fig = plt.figure()

   ax = fig.add_subplot(111)
   ax.axis('equal')

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

      if (Plano_k == 1):  # Plano (kx,ky) ou (k1,k2)       
         Spin_S1 = Spin_Sx
         Spin_S2 = Spin_Sy
         rotulo = 'SxSy'
         
      if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3)
         Spin_S1 = Spin_Sx
         Spin_S2 = Spin_Sz
         rotulo = 'SxSz'
         
      if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3)
         Spin_S1 = Spin_Sy
         Spin_S2 = Spin_Sz
         rotulo = 'SySz'

#-----------------------------------------------------------------------

   passo = len(Spin_Sx)
   nulo = [0.0]*passo
   angle = [0]*passo
   
   for k in range(passo):
       #----------------------------------------
       if (i == 1):
          v_spin = [Spin_Sx[k], 0.0]
          
       if (i == 2):
          v_spin = [0.0, Spin_Sy[k]]
          
       if (i == 3):
          v_spin = [Spin_Sz[k], 0.0]
          
       if (i == 4):
          v_spin = [Spin_S1[k], Spin_S2[k]]
       #---------------------------------------------------------------------------
       u = v_spin / np.linalg.norm(v_spin)
       v = [1.0, 0.0]  #  Vetor de referencia para o angulo, deve ser mantido fixo.
       dot_product = np.dot(u, v)
       angle[k] = np.arccos(dot_product) / np.pi * 180
       if (u[1] < 0.0):
          angle[k] = 360 - angle[k]
      
#-----------------------------------------------------------------------

   ax.set_xlabel(c1, fontdict = font)
   ax.set_ylabel(c2, fontdict = font)

#----------------------------------------------------------------------

   # plt.scatter(eixo1, eixo2, color = 'gray', s = 1, alpha = 0.5)

   #---------------------------------------------------------------------------------------------------------------------------------------
   # map_red_blue = colors.LinearSegmentedColormap.from_list("", ["red","white","red","white","blue","white","blue","white","red"])
   # map_red_blue = colors.LinearSegmentedColormap.from_list("", ["red","magenta","red","magenta","blue","magenta","blue","magenta","red"])
   # map_red_blue = colors.LinearSegmentedColormap.from_list("", ["red","pink","red","magenta","blue","cyan","blue","magenta","red"])
   map_red_blue = colors.LinearSegmentedColormap.from_list("", ["red","pink","pink","pink","red","magenta","magenta","magenta","blue",
                                                                       "cyan","cyan","cyan","blue","magenta","magenta","magenta","red"])
   norma = colors.Normalize(0, 360)
   #---------------------------------------------------------------------------------------------------------------------------------------   
   
   if (i == 1):
      ax.quiver(eixo1[::pulo], eixo2[::pulo], Spin_Sx[::pulo], nulo[::pulo], angle[::pulo], cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle', minlength = 0.0)
      
   if (i == 2):
      ax.quiver(eixo1[::pulo], eixo2[::pulo], nulo[::pulo], Spin_Sy[::pulo], angle[::pulo], cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle', minlength = 0.0)
   
   if (i == 3):
      ax.quiver(eixo1[::pulo], eixo2[::pulo], Spin_Sz[::pulo], nulo[::pulo], angle[::pulo], cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle', minlength = 0.0)

   if (i == 4):
      ax.quiver(eixo1[::pulo], eixo2[::pulo], Spin_S1[::pulo], Spin_S2[::pulo], angle[::pulo], cmap = map_red_blue, norm = norma, linewidths = 0.25, edgecolor = 'black',
                alpha = transp, width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle', minlength = 0.0)
 
   fig = plt.gcf()
   fig.set_size_inches(8,6)

   if (save_png == 1): plt.savefig(dir_output + 'Spin_Texture_' + rotulo + '.png', dpi = 600, pad_inches = 0)
   if (save_pdf == 1): plt.savefig(dir_output + 'Spin_Texture_' + rotulo + '.pdf', dpi = 600, pad_inches = 0)
   if (save_eps == 1): plt.savefig(dir_output + 'Spin_Texture_' + rotulo + '.eps', dpi = 600, pad_inches = 0)

   # plt.show()

#======================================================================   

if (dir_output != ''):
   print(" ")
   print("===============================================================")
   print("= Edite os vetores gerados, modificando o valor das variaveis =")
   print("= [espessura] e [comprimento] no arquivo Spin_Texture_2D.py ===")   
   print("===============================================================") 
   
#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
