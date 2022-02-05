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
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objects as go

print("================== Plot 4D (ISOSUPERFICIE): ==================")
print("")

#======================================================================
#======================================================================
# Gerando o arquivo para Plot 4D via Plotly ===========================
#======================================================================
#======================================================================

#-----------------------------------------------------------------
# Parâmetros para que este código possa ser executado isoladamente
#-----------------------------------------------------------------
# escolha = ???; n_sup = ???, esc = ???, Band = ???, Band_1 = ???; Band_2 = ???; Dimensao = ???

#----------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado
#----------------------------------------------------------------
if os.path.isdir('saida'):
   Diretorio_saida = 'saida/Plot_4D/'
   pasta = 1
else:
   Diretorio_saida = ''
   pasta = 0
#----------------------  

#--------------------------------------------------------------------------
# Verificando se a pasta "Plot_4D" existe, e se ela necessita de ser criada
#--------------------------------------------------------------------------
if (pasta == 1):
   if os.path.isdir("saida/Plot_4D"):
      0 == 0
   else:
      os.mkdir("saida/Plot_4D")
#-----------------------------

if (pasta == 1):

   #======================================================================
   # Extraindo informações dos arquivos OUTCAR e CONTCAR =================
   #======================================================================
   
   #-----------------------------------------
   executavel = Diretorio + '/informacoes.py'
   exec(open(executavel).read())
   #-----------------------------------------

   #======================================================================
   # Obtenção dos parâmetros de input ====================================
   #======================================================================

   print ("##############################################################")
   print ("########################## Plot 4D: ##########################")
   print ("##############################################################")
   print (" ")

   if (escolha == -7):

      print ("##############################################################") 
      print ("## Escolha a dimensao dos eixos-k no Plot: ================ ##")
      print ("##############################################################")
      print ("## [1] (kx,ky,kz) em unidades de 2pi/Param. =============== ##")
      print ("## [2] (kx,ky,kz) em unidades de 1/Angs. ================== ##")
      print ("## [3] (kx,ky,kz) em unidades de 1/nm. ==================== ##")
      print ("## [4] (k1,k2,k3) Coord. Diretas: K = k1*B1 + k2*B2 + k3*B3 ##")   
      print ("##############################################################") 
      Dimensao = input (" "); Dimensao = int(Dimensao)
      print (" ")

      print ("##############################################################")
      print ("Quantas superficies deseja obter no Plot: ====================")
      print ("Dica: Comece por 15 ==========================================")
      print ("##############################################################") 
      n_sup = input (" "); n_sup = int(n_sup)
      print (" ")   

   if (escolha == 7):
      Dimensao = 1
      n_sup = 15

   print ("##############################################################")
   print ("O que deseja analisar? =======================================")
   print ("[1] Dispersao de energia 3D de uma dada banda ================")
   print ("[2] Magnitude de separacao entre 2 bandas ====================")
   print ("##############################################################") 
   esc = input (" "); esc = int(esc)
   print (" ")

   if (esc == 1):
      print ("Escolha a Banda a ser analisada: =============================")
      Band = input (" "); Band = int(Band)
      print (" ")
      Band_1 = 0; Band_2 = 0

   if (esc == 2):
      print ("Informe a 1 Banda: ===========================================")
      Band_1 = input (" "); Band_1 = int(Band_1)
      print ("Informe a 2 Banda: ===========================================")
      Band_2 = input (" "); Band_2 = int(Band_2)     
      print (" ")
      Band = 0

   #----------------------------------------------------------------------
   # Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
   #----------------------------------------------------------------------

   #------------------------------------
   executavel = Diretorio + '/procar.py'
   exec(open(executavel).read())
   #------------------------------------

   #======================================================================
   #======================================================================
   # Obtendo dados para o Plot 4D ========================================
   #======================================================================
   #======================================================================

   #------------------------------------------------
   temp = open(Diretorio_saida + 'plot_4d.dat', "w")
   #------------------------------------------------

   for i in range (1,(n_procar+1)):
       for j in range (1,(nk+1)):
           if (Dimensao < 4):
              x = kx[i][j]
              y = ky[i][j]
              z = kz[i][j]          
           if (Dimensao == 4):
              x = kb1[i][j]
              y = kb2[i][j]
              z = kb3[i][j]
           if (esc == 1):    
              e = Energia[i][j][Band]
           if (esc == 2):    
              e = (Energia[i][j][Band_2] - Energia[i][j][Band_1])
              e = (e**2)**0.5 
           temp.write(f'{x} {y} {z} {e} \n')

   temp.close()

data = np.loadtxt(Diretorio_saida + 'plot_4d.dat')
data.shape

xs = data[:,0]
ys = data[:,1]
zs = data[:,2]
cs = data[:,3]
cs = (cs - min(cs))/(max(cs) - min(cs))

# print('x:', (min(xs), max(xs)))
# print('y:', (min(ys), max(ys)))
# print('z:', (min(zs), max(zs)))
# print('c:', (min(cs), max(cs)))

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(". Pode demorar um pouco .")
print(".........................")

points = np.array([xs, ys, zs]).T
ni = 30
xi = np.linspace(min(xs), max(xs), ni)
yi = np.linspace(min(ys), max(ys), ni)
zi = np.linspace(min(zs), max(zs), ni)
xi, yi, zi = np.meshgrid(xi, yi, zi, indexing='ij')
newpts = np.array([xi, yi, zi]).T
ci = interp.griddata(points, cs, newpts)
ci.shape

ids = np.argsort(cs)
x1 = xs[ids]
y1 = ys[ids]
z1 = zs[ids]
c1 = cs[ids]

x1 = [x1[0], x1[0]]
y1 = [y1[0], z1[0]]
z1 = [z1[0], y1[0]]

#----------------------------------------------------------------------

fig = go.Figure()

# Greys, YlGnBu, Greens, YlOrRd, Bluered, RdBu
# Reds, Blues, Picnic, Rainbow, Portland, Jet
# Hot, Blackbody, Earth, Electric, Viridis, Cividis

fig.add_trace(go.Volume(
    x = xi.flatten(),
    y = yi.flatten(),
    z = zi.flatten(),
    value = ci.T.flatten(),
    isomin = 0.0,
    isomax = 1.0,
    opacity = 0.1,         # needs to be small to see through all surfaces
    surface_count = n_sup, # needs to be a large number for good volume rendering
    colorscale='Jet'
    ))

# fig.add_trace(go.Scatter3d(x = x1, y = y1, z = z1,
#                            mode = 'markers', 
#                            line = dict(color = 'black', width = 4)
#                           ))

if (Dimensao < 4):
   fig.update_layout(scene = dict(
       xaxis_title = 'k<sub>x</sub>',
       yaxis_title = 'k<sub>y</sub>',
       zaxis_title = 'k<sub>z</sub>',
       aspectmode = 'cube'),
       width = 700,
       margin = dict(r = 20, b = 10, l = 10, t = 10))

if (Dimensao == 4):
   fig.update_layout(scene = dict(
       xaxis_title = 'k<sub>1</sub>',
       yaxis_title = 'k<sub>2</sub>',
       zaxis_title = 'k<sub>3</sub>',
       aspectmode = 'cube'),
       width = 700,
       margin = dict(r = 20, b = 10, l = 10, t = 10))

# Image export using the "kaleido" engine requires the kaleido package, which can be installed using pip: pip install -U kaleido

# fig.write_image(Diretorio_saida + 'plot_4d.png')
# fig.write_image(Diretorio_saida + 'plot_4d.pdf')
# fig.write_image(Diretorio_saida + 'plot_4d.eps')
                     
fig.show()

#-----------------------------------------------------------------------------
# Verificando se o arquivo plot_4D.py foi copiado para o diretório de saida --
#-----------------------------------------------------------------------------

try: f = open(Diretorio_saida + 'plot_4D_plolty.py'); f.close(); Plot_4D = 1
except: Plot_4D = 0

if (Plot_4D == 0):
   try: f = open(Diretorio_saida + 'plot_4D.py'); f.close(); Plot_4D = 1
   except: Plot_4D = 0

if (Plot_4D == 0):
   source = Diretorio + '\plot_4D_plotly.py'
   destination = r'saida/Plot_4D\plot_4D_plolty.py'
   shutil.copyfile(source, destination)

#-------------------------------------------------------------------------------------------
# Editando o código no diretório de saida para que ele possa ser executado isoladamente ----
#-------------------------------------------------------------------------------------------

try: f = open(Diretorio_saida + 'plot_4D_plolty.py'); f.close(); Plot_4D = 1
except: Plot_4D = 0 

if (Plot_4D == 1):
   #--------------------------------------------------------
   codigo = open(Diretorio_saida + 'plot_4D_plolty.py', "r")
   codigo_new = open(Diretorio_saida + 'temp.py', "w")
   #--------------------------------------------------------
   OLD = '# escolha = ???; n_sup = ???, esc = ???, Band = ???, Band_1 = ???; Band_2 = ???; Dimensao = ???'
   NEW = 'escolha = ' + str(escolha) + '; ' 'n_sup = ' + str(n_sup) + '; ' 'esc = ' + str(esc) + '; ' 'Band = ' + str(Band) + '; ' 
   NEW = NEW + 'Band_1 = ' + str(Band_1) + '; ' 'Band_2 = ' + str(Band_2) + '; ' 'Dimensao = ' + str(Dimensao)
   #--------------------------------------------------------
   for line in codigo: codigo_new.write(line.replace(OLD, NEW))  # replacing the string and write to output file
   codigo.close(); codigo_new.close()
   #--------------------------------------------------------
   os.remove(Diretorio_saida + 'plot_4D_plolty.py')
   os.rename(Diretorio_saida + 'temp.py', Diretorio_saida + 'plot_4D.py')

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
