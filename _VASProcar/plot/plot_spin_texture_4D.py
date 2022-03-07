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

print(" ")
print("============= Plotando a Textura de Spin 4D (Plotly) =============")

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

xs = spin_textura[:,0]
ys = spin_textura[:,1]
zs = spin_textura[:,2]
cs = spin_textura[:,3]
cs = (cs - min(cs))/(max(cs) - min(cs))

Spin_Sx = spin_textura[:,4]
Spin_Sy = spin_textura[:,5]
Spin_Sz = spin_textura[:,6]

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(". Pode demorar um pouco .")
print(".........................")

print(" ")
print("===================================================================")
print("Observacao: Caso a pagina no navegador de internet fique em loading")
print("            infinito ou apresente alguma mensagem de erro, aperte  ")
print("            F5 para recarregar a pagina, ou abra o arquivo .html   ")   
print("===================================================================")

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

if (Dimensao == 1):
   cc = ' (2pi/a)'
if (Dimensao == 2):
   cc = ' (Angs.<sup>-1</sup>)'
if (Dimensao == 3):
   cc = ' (nm<sup>-1</sup>)'

if (Dimensao < 4):
   c1 = 'S<sub>x</sub>  |  k<sub>x</sub>' + cc
   c2 = 'S<sub>y</sub>  |  k<sub>y</sub>' + cc
   c3 = 'S<sub>z</sub>  |  k<sub>z</sub>' + cc
if (Dimensao == 4):
   c1 = 'S<sub>x</sub>  |  k<sub>1</sub>'
   c2 = 'S<sub>y</sub>  |  k<sub>2</sub>'
   c3 = 'S<sub>z</sub>  |  k<sub>3</sub>'

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

fig.add_trace(go.Cone(x = xs, y = ys, z = zs, u = Spin_Sx, v = Spin_Sy, w = Spin_Sz, opacity = 0.75,
                      colorscale = ["black", "black"], showscale = False, sizemode = "absolute", sizeref = 1.0))

fig.update_layout(scene = dict(
    xaxis_title = c1,
    yaxis_title = c2,
    zaxis_title = c3,
    aspectmode = 'cube'),
    width = 700,
    margin = dict(r = 20, b = 10, l = 10, t = 10))

fig.write_html(Diretorio_saida + 'Spin_Texture_4D.html')

# Image export using the "kaleido" engine requires the kaleido package, which can be installed using pip: pip install -U kaleido
# fig.write_image(Diretorio_saida + 'Spin_Texture_4D.png')
# fig.write_image(Diretorio_saida + 'Spin_Texture_4D.pdf')
# fig.write_image(Diretorio_saida + 'Spin_Texture_4D.eps')

fig.show() 
                     
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
