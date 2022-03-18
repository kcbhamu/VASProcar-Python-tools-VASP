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
import linecache 
import pandas as pd
import shutil

#--------------------------------------------------------------------------
# Variaveis que definem a espessura e o comprimento dos vetores no plot ---
#--------------------------------------------------------------------------
espessura = 0.001
comprimento = 10
#----------------

print(" ")
print("=========== Plotando a Textura de Spin 2D (Matplotlib) ===========")

#----------------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado -----
#----------------------------------------------------------------------
if os.path.isdir('saida'):
   Diretorio_saida = 'saida/Spin_Texture/'
else:
   Diretorio_saida = ''
#----------------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#====================================================================== 

spin_textura = np.loadtxt(Diretorio_saida + 'Spin_Texture.dat')
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

S1_u = [0.0]*nk; S1_d = [0.0]*nk
S2_u = [0.0]*nk; S2_d = [0.0]*nk
S3_u = [0.0]*nk; S3_d = [0.0]*nk
nulo = [0.0]*nk

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

#-------------------------------------- 

if (Dimensao == 1): cc = r' $(2{\pi}/{a})$'
if (Dimensao == 2): cc = r' $({\AA}^{-1})$'
if (Dimensao == 3): cc = r' $({nm}^{-1})$'
if (Dimensao == 4): cc = ' '
   
#----------------------------------------------------------------------

for i in range(nk):
   
    if (Plano_k == 1):  # Plano (kx,ky) ou (k1,k2) 
       if (Spin_Sx[i] > 0.0): S1_u[i] = Spin_Sx[i]
       if (Spin_Sx[i] < 0.0): S1_d[i] = Spin_Sx[i]
       if (Spin_Sy[i] > 0.0): S2_u[i] = Spin_Sy[i]
       if (Spin_Sy[i] < 0.0): S2_d[i] = Spin_Sy[i]
       if (Spin_Sz[i] > 0.0): S3_u[i] = Spin_Sz[i]
       if (Spin_Sz[i] < 0.0): S3_d[i] = Spin_Sz[i]
       
    if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3) 
       if (Spin_Sx[i] > 0.0): S1_u[i] = Spin_Sx[i]
       if (Spin_Sx[i] < 0.0): S1_d[i] = Spin_Sx[i]
       if (Spin_Sz[i] > 0.0): S2_u[i] = Spin_Sz[i]
       if (Spin_Sz[i] < 0.0): S2_d[i] = Spin_Sz[i]
       if (Spin_Sy[i] > 0.0): S3_u[i] = Spin_Sy[i]
       if (Spin_Sy[i] < 0.0): S3_d[i] = Spin_Sy[i]
       
    if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3) 
       if (Spin_Sy[i] > 0.0): S1_u[i] = Spin_Sy[i]
       if (Spin_Sy[i] < 0.0): S1_d[i] = Spin_Sy[i]
       if (Spin_Sz[i] > 0.0): S2_u[i] = Spin_Sz[i]
       if (Spin_Sz[i] < 0.0): S2_d[i] = Spin_Sz[i]
       if (Spin_Sx[i] > 0.0): S3_u[i] = Spin_Sx[i]
       if (Spin_Sx[i] < 0.0): S3_d[i] = Spin_Sx[i]

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

   ax.set_xlabel(c1, fontdict = font)
   ax.set_ylabel(c2, fontdict = font)

#----------------------------------------------------------------------

   # plt.scatter(eixo1, eixo2, color = 'gray', s = 1, alpha = 0.5)
   
   if (i == 1): ax.quiver(eixo1, eixo2, S1_d, nulo, color = 'blue', width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle')
   if (i == 1): ax.quiver(eixo1, eixo2, S1_u, nulo, color = 'red', width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle')
   
   if (i == 2): ax.quiver(eixo1, eixo2, nulo, S2_d, color = 'blue', width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle')
   if (i == 2): ax.quiver(eixo1, eixo2, nulo, S2_u, color = 'red', width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle')
   
   if (i == 3): ax.quiver(eixo1, eixo2, S3_d, nulo, color = 'blue', width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle')
   if (i == 3): ax.quiver(eixo1, eixo2, S3_u, nulo, color = 'red', width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle')

   if (i == 4): ax.quiver(eixo1, eixo2, Spin_S1, Spin_S2, color = 'black', width = espessura, scale = comprimento, scale_units = 'inches', pivot = 'middle')
 
   fig = plt.gcf()
   fig.set_size_inches(8,6)

   if (save_png == 1): plt.savefig(Diretorio_saida + 'Spin_Texture_' + rotulo + '.png', dpi = 600, pad_inches = 0)
   if (save_pdf == 1): plt.savefig(Diretorio_saida + 'Spin_Texture_' + rotulo + '.pdf', dpi = 600, pad_inches = 0)
   if (save_eps == 1): plt.savefig(Diretorio_saida + 'Spin_Texture_' + rotulo + '.eps', dpi = 600, pad_inches = 0)

   # plt.show()

#======================================================================   

if (Diretorio_saida != ''):
   print(" ")
   print("===============================================================")
   print("= Edite os vetores gerados, modificando o valor das variaveis =")
   print("= [espessura] e [comprimento] no arquivo Spin_Texture_2D.py ===")   
   print("===============================================================") 
   
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
