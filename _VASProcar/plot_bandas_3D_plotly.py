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
import shutil
import scipy.interpolate as interp
from scipy.interpolate import griddata
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objects as go

print(" ")
print("============ Plotando as Bandas 3D (Plotly): ============")

#======================================================================
#======================================================================
# Gerando o arquivo para Plot 3D via Plotly ===========================
#======================================================================
#======================================================================

#-----------------------------------------------------------------
# Parâmetros para que este código possa ser executado isoladamente
#-----------------------------------------------------------------
# escolha = ???; tipo_plot = ???; n_d = ???; Band_i = ???; Band_f = ???; Plano_k = ???; Dimensao = ???

#----------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado
#----------------------------------------------------------------
if os.path.isdir('saida'):
   Diretorio_saida = 'saida/Bandas_3D/'
else:
   Diretorio_saida = ''
#----------------------   

banda = np.loadtxt(Diretorio_saida + 'Bandas_3D.dat') 
banda.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(". Pode demorar um pouco .")
print(".........................")

if (Plano_k == 1):     # Plano (kx,ky) ou (k1,k2)     
   eixo1 = banda[:,0]
   eixo2 = banda[:,1]
if (Plano_k == 2):     # Plano (kx,kz) ou (k1,k3)     
   eixo1 = banda[:,0]
   eixo2 = banda[:,2]
if (Plano_k == 3):     # Plano (ky,kz) ou (k2,k3)    
   eixo1 = banda[:,1]
   eixo2 = banda[:,2]

#Create meshgrid for x,y
xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)

#----------------------------------------------------------------------

fig = go.Figure()

for i in range (1,(Band_f - Band_i +2)):
    #-----------------------------------
    energ = banda[:,(i + 2)]
    label = 'Banda ' + str(Band_i + (i-1))
    #-------------------------------------
    #Grid data
    z_grid = griddata((eixo1,eixo2), energ, (x_grid,y_grid), method = 'cubic')
    #------------------------------------------------------------------
    if (tipo_plot == 0):
       fig.add_trace(go.Scatter3d(x = eixo1, y = eixo2, z = energ, name = label, mode = 'markers', marker = dict(size = 2, color = i, opacity = 0.5)))
    if (tipo_plot == 1):
       fig.add_trace(go.Surface(x = x_grid, y = y_grid, z = z_grid, name = label, opacity = 0.8, showscale = False)) 
    if (tipo_plot == 2):
       fig.add_trace(go.Scatter3d(x = eixo1, y = eixo2, z = energ, name = label, mode = 'markers', marker = dict(size = 2, color = i, opacity = 0.5)))
       fig.add_trace(go.Surface(x = x_grid, y = y_grid, z = z_grid, name = label, opacity = 0.8, showscale = False))                 

if (Dimensao == 1):
   cl = ' (2pi/a)'
if (Dimensao == 2):
   cl = ' (Angs.<sup>-1</sup>)'
if (Dimensao == 3):
   cl = ' (nm<sup>-1</sup>)'

if (Plano_k == 1 and Dimensao != 4):             # Plano (kx,ky)      
   c1 = 'k<sub>x</sub>' + cl
   c2 = 'k<sub>y</sub>' + cl
if (Plano_k == 2 and Dimensao != 4):             # Plano (kx,kz)      
   c1 = 'k<sub>x</sub>' + cl
   c2 = 'k<sub>z</sub>' + cl
if (Plano_k == 3 and Dimensao != 4):             # Plano (ky,kz)      
   c1 = 'k<sub>y</sub>' + cl
   c2 = 'k<sub>z</sub>' + cl

if (Plano_k == 1 and Dimensao == 4):             # Plano (k1,k2)      
   c1 = 'k<sub>1</sub>'
   c2 = 'k<sub>2</sub>'
if (Plano_k == 2 and Dimensao == 4):             # Plano (k1,k3)      
   c1 = 'k<sub>1</sub>'
   c2 = 'k<sub>3</sub>'
if (Plano_k == 3 and Dimensao == 4):             # Plano (k2,k3)      
   c1 = 'k<sub>2</sub>'
   c2 = 'k<sub>3</sub>'

fig.update_layout(scene = dict(
    xaxis_title = c1,
    yaxis_title = c2,
    zaxis_title = 'E-E<sub>f</sub>(eV)',
    aspectmode = 'cube'),
    width = 700, margin = dict(r = 20, b = 10, l = 10, t = 10))

# Image export using the "kaleido" engine requires the kaleido package, which can be installed using pip: pip install -U kaleido
# fig.write_image(Diretorio_saida + "Bandas_3d.png")
# fig.write_image(Diretorio_saida + "Bandas_3d.pdf")
# fig.write_image(Diretorio_saida + "Bandas_3d.eps")
                     
fig.show()

#---------------------------------------------------------------------------------------------------------------------
# Verificando se o arquivo plot_bandas_3D_plotly.py ou bandas_3D_plotly.py foram copiados para o diretório de saida --
#---------------------------------------------------------------------------------------------------------------------

try: f = open(Diretorio_saida + 'plot_bandas_3D_plotly.py'); f.close(); Plot_3D = 1
except: Plot_3D = 0

if (Plot_3D == 0):
   try: f = open(Diretorio_saida + 'bandas_3D_plotly.py'); f.close(); Plot_3D = 1
   except: Plot_3D = 0

if (Plot_3D == 0):
   source = Diretorio + '\plot_bandas_3D_plotly.py'
   destination = r'saida/Bandas_3D\plot_bandas_3D_plotly.py'
   shutil.copyfile(source, destination)

#-------------------------------------------------------------------------------------------
# Editando o código no diretório de saida para que ele possa ser executado isoladamente ----
#-------------------------------------------------------------------------------------------

try: f = open(Diretorio_saida + 'plot_bandas_3D_plotly.py'); f.close(); Plot_3D = 1
except: Plot_3D = 0 

if (Plot_3D == 1):
   #---------------------------------------------------------------
   codigo = open(Diretorio_saida + 'plot_bandas_3D_plotly.py', "r")
   codigo_new = open(Diretorio_saida + 'temp.py', "w")
   #---------------------------------------------------------------
   OLD = '# escolha = ???; tipo_plot = ???; n_d = ???; Band_i = ???; Band_f = ???; Plano_k = ???; Dimensao = ???'
   NEW = 'escolha = ' + str(escolha) + '; ' 'tipo_plot = ' + str(tipo_plot) + '; ' 'n_d = ' + str(n_d) + '; ' 'Band_i = ' + str(Band_i) + '; '  
   NEW = NEW + 'Band_f = ' + str(Band_f) + '; ' 'Plano_k = ' + str(Plano_k) + '; '  'Dimensao = ' + str(Dimensao)
   #---------------------------------------------------------------
   for line in codigo: codigo_new.write(line.replace(OLD, NEW))  # replacing the string and write to output file
   codigo.close(); codigo_new.close()
   #---------------------------------------------------------------
   os.remove(Diretorio_saida + 'plot_bandas_3D_plotly.py')
   os.rename(Diretorio_saida + 'temp.py', Diretorio_saida + 'bandas_3D_plotly.py')
 

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
