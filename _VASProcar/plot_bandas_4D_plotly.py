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

#======================================================================
#======================================================================
# Gerando o arquivo para Plot 4D via Plotly ===========================
#======================================================================
#======================================================================

#-----------------------------------------------------------------
# Parâmetros para que este código possa ser executado isoladamente
#-----------------------------------------------------------------
# n_iso: Numero de isosuperficies
# n_d: Dimensao-D (DxDxD) do GRID de interpolacao
# n_iso = ???, n_d = ???, Band = ???, Band_1 = ???; Band_2 = ???; Dimensao = ???

#----------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado
#----------------------------------------------------------------
if os.path.isdir('saida'):
   Diretorio_saida = 'saida/Plot_4D/'
   pasta = 0
else:
   Diretorio_saida = ''
   pasta = 1
#----------------------  

data = np.loadtxt(Diretorio_saida + 'plot_4d.dat')
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
   cl = ' (2pi/a)'
if (Dimensao == 2):
   cl = ' (Angs.<sup>-1</sup>)'
if (Dimensao == 3):
   cl = ' (nm<sup>-1</sup>)'

if (Dimensao < 4):
   c1 = 'k<sub>x</sub>' + cl
   c2 = 'k<sub>y</sub>' + cl
   c3 = 'k<sub>z</sub>' + cl
if (Dimensao == 4):
   c1 = 'k<sub>1</sub>'
   c2 = 'k<sub>2</sub>'
   c3 = 'k<sub>3</sub>'

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
                     
#================================================================================

if (pasta == 0):
   #-------------------------------------------------------------------------
   # Copiando o arquivo plot_bandas_4D_plotly.py para o diretório de saida --
   #-------------------------------------------------------------------------

   try: f = open(Diretorio_saida + 'plot_bandas_4D_plotly.py'); f.close(); os.remove(Diretorio_saida + 'plot_bandas_4D_plotly.py')
   except: 0 == 0

   try: f = open(Diretorio_saida + 'plot_4D.py'); f.close(); os.remove(Diretorio_saida + 'plot_4D.py')
   except: 0 == 0

   source = Diretorio + '\plot_bandas_4D_plotly.py'
   destination = Diretorio_saida + 'plot_bandas_4D_plotly.py'
   shutil.copyfile(source, destination)

   #-------------------------------------------------------------------------------------------
   # Editando o código no diretório de saida para que ele possa ser executado isoladamente ----
   #-------------------------------------------------------------------------------------------

   codigo = open(Diretorio_saida + 'plot_bandas_4D_plotly.py', "r")
   codigo_new = open(Diretorio_saida + 'temp.py', "w")
   #------------------------------------------------------------------------------------
   OLD = '# n_iso = ???, n_d = ???, Band = ???, Band_1 = ???; Band_2 = ???; Dimensao = ???'
   NEW = 'n_iso = ' + str(n_iso) + '; ' 'n_d = ' + str(n_d) + '; ' 'Band = ' + str(Band) + '; '
   NEW = NEW + 'Band_1 = ' + str(Band_1) + '; ' 'Band_2 = ' + str(Band_2) + '; ' 'Dimensao = ' + str(Dimensao)
   #------------------------------------------------------------------------------------
   for line in codigo: codigo_new.write(line.replace(OLD, NEW))  # replacing the string and write to output file
   codigo.close(); codigo_new.close()
   #------------------------------------------------------------------------------------
   os.remove(Diretorio_saida + 'plot_bandas_4D_plotly.py')
   os.rename(Diretorio_saida + 'temp.py', Diretorio_saida + 'plot_4D.py')

   print(" ")
   print("=========================================================")
   print("= Edite o Plot4D por meio do arquivo plot_4D.py gerado = ")
   print("= na pasta ""saida\Plot_4D"" ============================")   
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
