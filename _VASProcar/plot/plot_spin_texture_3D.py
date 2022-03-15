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
import scipy.interpolate as interp
from scipy.interpolate import griddata
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

#----------------------------------------------------------------------

print(" ")
print("============= Plotando a Textura de Spin 3D (Plotly) =============")

#--------------------------------------------------------------------------

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
# Estrutura do arquivo para Plot via Plotly ===========================
#======================================================================
#======================================================================

spin_textura = np.loadtxt(Diretorio_saida + 'Spin_Texture.dat')
spin_textura.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")

print(" ")
print("===================================================================")
print("Observacao: O resultado encontra-se nos arquivos .html, os quais ==")
print("            sao abertos via navegador =============================") 
print("===================================================================")

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
   rotulo1 = 'SxSy'
   
if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3)
   eixo1  = spin_textura[:,0]
   eixo2  = spin_textura[:,2]  
   rotulo1 = 'SxSz'
   
if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3)
   eixo1  = spin_textura[:,1]
   eixo2  = spin_textura[:,2]      
   rotulo1 = 'SySz'     

#----------------------------------------------------------------------

# Create meshgrid for x,y
xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)

# Grid data
z_grid = griddata((eixo1,eixo2), energia, (x_grid,y_grid), method = 'cubic')

#----------------------------------------------------------------------



if (Plano_k == 1 and Dimensao < 4):                
   ca = 'k<sub>x</sub>'; cb = 'k<sub>y</sub>'; cc = 'E-E<sub>f</sub>(eV)'
   sa = 'S<sub>x</sub>  |  '; sb = 'S<sub>y</sub>  |  '; sc = 'S<sub>z</sub>  |  '
if (Plano_k == 2 and Dimensao < 4):                  
   ca = 'k<sub>x</sub>'; cb = 'k<sub>z</sub>'; cc = 'E-E<sub>f</sub>(eV)'   
   sa = 'S<sub>x</sub>  |  '; sb = 'S<sub>z</sub>  |  '; sc = 'S<sub>y</sub>  |  '   
if (Plano_k == 3 and Dimensao < 4):                  
   ca = 'k<sub>y</sub>'; cb = 'k<sub>z</sub>'; cc = 'E-E<sub>f</sub>(eV)'   
   sa = 'S<sub>y</sub>  |  '; sb = 'S<sub>z</sub>  |  '; sc = 'S<sub>x</sub>  |  ' 

if (Plano_k == 1 and Dimensao == 4):                 
   ca = 'k<sub>1</sub>'; cb = 'k<sub>2</sub>'; cc = 'E-E<sub>f</sub>(eV)'
   sa = 'S<sub>x</sub>  |  '; sb = 'S<sub>y</sub>  |  '; sc = 'S<sub>z</sub>  |  '
if (Plano_k == 2 and Dimensao == 4):                 
   ca = 'k<sub>1</sub>'; cb = 'k<sub>3</sub>'; cc = 'E-E<sub>f</sub>(eV)'   
   sa = 'S<sub>x</sub>  |  '; sb = 'S<sub>z</sub>  |  '; sc = 'S<sub>y</sub>  |  ' 
if (Plano_k == 3 and Dimensao == 4):                
   ca = 'k<sub>2</sub>'; cb = 'k<sub>3</sub>'; cc = 'E-E<sub>f</sub>(eV)'   
   sa = 'S<sub>y</sub>  |  '; sb = 'S<sub>z</sub>  |  '; sc = 'S<sub>x</sub>  |  '

#-------------------------------------- 

if (Dimensao == 1): cd = ' (2' + '\u03C0' + '/a)'             #  (2pi/a)
if (Dimensao == 2): cd = ' (' + '\u212B' + '<sup>-1</sup>)'   #  (Angs.^-1)
if (Dimensao == 3): cd = ' (nm<sup>-1</sup>)'                 #  (nm^-1)
if (Dimensao == 4): cd = ' '
   
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
    
    fig = go.Figure()

#----------------------------------------------------------------------

    if (i == 1):
       c1 = sa + ca + cd
       c2 = cb + cd
       c3 = cc
       rotulo = 'Sx'
    if (i == 2):
       c1 = ca + cd
       c2 = sb + cb + cd
       c3 = cc
       rotulo = 'Sy'
    if (i == 3):
       c1 = ca + cd
       c2 = cb + cd
       c3 = sc + cc
       rotulo = 'Sz'
      
    if (i == 4):
      
       c1 = sa + ca + cd
       c2 = sb + cb + cd
       c3 = sc + cc

       if (Plano_k == 1):  # Plano (kx,ky) ou (k1,k2)       
          Spin_S1 = Spin_Sx
          Spin_S2 = Spin_Sy
          Spin_S3 = Spin_Sz
          rotulo = 'SxSy'
         
       if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3)
          Spin_S1 = Spin_Sx
          Spin_S2 = Spin_Sz
          Spin_S3 = Spin_Sy
          rotulo = 'SxSz'
         
       if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3)
          Spin_S1 = Spin_Sy
          Spin_S2 = Spin_Sz
          Spin_S3 = Spin_Sx
          rotulo = 'SySz'

#-----------------------------------------------------------------------    

    fig.add_trace(go.Surface(x = x_grid, y = y_grid, z = z_grid, opacity = 0.25, colorscale = ["gray", "gray"], showscale = False))

    
    if (i == 1): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = S1_d, v = nulo, w = nulo, opacity = 0.75,
                                       colorscale = ["blue", "blue"], showscale = False, sizemode = "absolute", sizeref = 1.0))
    if (i == 1): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = S1_u, v = nulo, w = nulo, opacity = 0.75,
                                       colorscale = ["red", "red"], showscale = False, sizemode = "absolute", sizeref = 1.0))

    if (i == 2): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = nulo, v = S2_d, w = nulo, opacity = 0.75,
                                       colorscale = ["blue", "blue"], showscale = False, sizemode = "absolute", sizeref = 1.0))
    if (i == 2): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = nulo, v = S2_u, w = nulo, opacity = 0.75,
                                       colorscale = ["red", "red"], showscale = False, sizemode = "absolute", sizeref = 1.0))

    if (i == 3): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = nulo, v = nulo, w = S3_d, opacity = 0.75,
                                       colorscale = ["blue", "blue"], showscale = False, sizemode = "absolute", sizeref = 1.0))
    if (i == 3): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = nulo, v = nulo, w = S3_u, opacity = 0.75,
                                       colorscale = ["red", "red"], showscale = False, sizemode = "absolute", sizeref = 1.0))

    if (i == 4): fig.add_trace(go.Cone(x = eixo1, y = eixo2, z = energia, u = Spin_S1, v = Spin_S2, w = Spin_S3, opacity = 0.75,
                                       colorscale = ["black", "black"], showscale = False, sizemode = "absolute", sizeref = 1.0))
     
    fig.update_layout(scene = dict(xaxis_title = c1, yaxis_title = c2, zaxis_title = c3, aspectmode = 'cube'),
                      margin = dict(r = 20, b = 10, l = 10, t = 10))

    fig.write_html(Diretorio_saida + 'Spin_Texture_3D_' + rotulo + '.html')

    # Image export using the "kaleido" engine requires the kaleido package, which can be installed using pip: pip install -U kaleido
    # fig.write_image(Diretorio_saida + 'Spin_Texture_3D_' + rotulo + '.png')
    # fig.write_image(Diretorio_saida + 'Spin_Texture_3D_' + rotulo + '.pdf')
    # fig.write_image(Diretorio_saida + 'Spin_Texture_3D_' + rotulo + '.eps')

    # fig.show()

#======================================================================

print(" ")
print("===============================================================")
print("= Edite os vetores gerados, modificando o valor da variavel ===")
print("= sizeref =====================================================")   
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
