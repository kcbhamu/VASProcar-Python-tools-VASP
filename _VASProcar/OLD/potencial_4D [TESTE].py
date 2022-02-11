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

#-------------------------------------------------------------------------
# Verificando se a pasta "Potencial_4D" existe, se não existe ela é criada
#-------------------------------------------------------------------------
if os.path.isdir("saida/Potencial_4D"):
   0 == 0
else:
   os.mkdir("saida/Potencial_4D")
#--------------------------------

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
print ("############# Plot 4D do Potencial Eletrostatico: ############")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("Escolha a dimensao do Plot: ==================================")
print ("Utilize 1 para Angs. =========================================")
print ("Utilize 2 para nm. ===========================================")
print ("##############################################################") 
Dimensao = input (" "); Dimensao = int(Dimensao)
print (" ")

#----------------------------------------------------------------------
# Extraindo os resultados do arquivo LOCPOT ---------------------------
#----------------------------------------------------------------------

print (".............. Analisando o arquivo LOCPOT ..............")
print (" ")

#---------------------------
locpot = open("LOCPOT", "r")
#---------------------------

for i in range (ni + 9): VTemp = locpot.readline()

VTemp = locpot.readline().split()
Grid_x = int(VTemp[0])
Grid_y = int(VTemp[1])
Grid_z = int(VTemp[2])

GRID = Grid_x*Grid_y*Grid_z
V_local = [0]*(GRID)

passo1 = (GRID/5)
resto = passo1 - int(passo1)
if (resto == 0): passo1 = int(passo1)
if (resto != 0): passo1 = int(passo1) + 1

passo2 = 5 - ((passo1*5) -GRID)

for i in range (passo1):
    VTemp = locpot.readline().split()
    if (i < (passo1-1)):
       for j in range(5): V_local[((i)*5) + j] = float(VTemp[j])
    if (i == (passo1-1)):
       for j in range(passo2): V_local[((i)*5) + j] = float(VTemp[j])

#-------------
locpot.close()
#-------------

#----------------------------------------------------------------------
# Analisando os dados -------------------------------------------------
#----------------------------------------------------------------------
     
fator_x  = A1x*Parametro
fator_y  = A2y*Parametro
fator_z  = A3z*Parametro

#-------------------------------------------------------
pot4D = open('saida/Potencial_4D/Potencial_4D.dat', "w")
#-------------------------------------------------------

number = -1
for i in range (Grid_x):
    X = (float(i)/(float(Grid_x) - 1.0))*fator_x
    for j in range (Grid_y):
        Y = (float(j)/(float(Grid_y) - 1.0))*fator_y
        for k in range (Grid_z):
            number += 1
            Z = (float(k)/(float(Grid_z) - 1.0))*fator_z
            pot4D.write(f'{X} {Y} {Z} {V_local[number]} \n')

#------------
pot4D.close()
#------------




import shutil
import scipy.interpolate as interp
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objects as go

#======================================================================
#======================================================================
# Plot 4D via Plotly ==================================================
#======================================================================
#======================================================================

  

data = np.loadtxt('saida/Potencial_4D/Potencial_4D.dat')
data.shape

xs = data[:,0]
ys = data[:,1]
zs = data[:,2]
cs = data[:,3]
cs = (cs - min(cs))/(max(cs) - min(cs))

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(". Pode demorar um pouco .")
print(".........................")

n_d = 31

points = np.array([xs, ys, zs]).T
xi = np.linspace(min(xs), max(xs), n_d)
yi = np.linspace(min(ys), max(ys), n_d)
zi = np.linspace(min(zs), max(zs), n_d)
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
    surface_count = n_iso, # needs to be a large number for good volume rendering
    colorscale='Jet'
    ))

# fig.add_trace(go.Scatter3d(x = x1, y = y1, z = z1,
#                            mode = 'markers', 
#                            line = dict(color = 'black', width = 4)
#                           ))

if (Dimensao == 1):
   cl = ' (Angs.)'
if (Dimensao == 2):
   cl = ' (nm)'

c1 = 'eixo-x' + cl
c2 = 'eixo-y' + cl
c3 = 'eixo-z' + cl

fig.update_layout(scene = dict(
    xaxis_title = c1,
    yaxis_title = c2,
    zaxis_title = c3,
    aspectmode = 'cube'),
    width = 700,
    margin = dict(r = 20, b = 10, l = 10, t = 10))

# Image export using the "kaleido" engine requires the kaleido package, which can be installed using pip: pip install -U kaleido

# fig.write_image(Diretorio_saida + 'plot_4d.png')
# fig.write_image(Diretorio_saida + 'plot_4d.pdf')
# fig.write_image(Diretorio_saida + 'plot_4d.eps')

fig.show() 


































           
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
