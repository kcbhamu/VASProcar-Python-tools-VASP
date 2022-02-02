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

#----------------------------------------------------------------------
# Verificando se a pasta "Plot_4D" existe, se não existe ela é criada
#----------------------------------------------------------------------
if os.path.isdir("saida/Plot_4D"):
   0 == 0
else:
   os.mkdir("saida/Plot_4D")
#-----------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================

#---------------------------------------------
exec(open("_VASProcar/informacoes.py").read())
#---------------------------------------------

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

if (escolha == 7):
   Dimensao = 1

print ("##############################################################")
print ("Escolha a Banda a ser analisada: =============================")
print ("##############################################################") 
Band = input (" "); Band = int(Band)
print (" ")

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------

#---------------------------------------------
exec(open("_VASProcar/procar.py").read())
#--------------------------------------------

#======================================================================
#======================================================================
# Obtendo dados para o Plot 4D ========================================
#======================================================================
#======================================================================

import scipy.interpolate as interp
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objects as go

#--------------------------------------------
temp = open("saida/Plot_4D/plot_4d.dat", "w")
#--------------------------------------------

for i in range (1,(n_procar+1)):
    for j in range (1,(nk+1)):
        if (Dimensao < 4):
           temp.write(f'{kx[i][j]} {ky[i][j]} {kz[i][j]} {Energia[i][j][Band]} \n')
        if (Dimensao == 4):
           temp.write(f'{kb1[i][j]} {kb2[i][j]} {kb3[i][j]} {Energia[i][j][Band]} \n')
temp.close()

data = np.loadtxt("saida/Plot_4D/plot_4d.dat")
data.shape

xs = data[:,0]
ys = data[:,1]
zs = data[:,2]
cs = data[:,3]
cs = (cs - max(cs))/(min(cs) - max(cs))

# print('x:', (min(xs), max(xs)))
# print('y:', (min(ys), max(ys)))
# print('z:', (min(zs), max(zs)))
# print('c:', (min(cs), max(cs)))

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
    opacity = 0.1,      # needs to be small to see through all surfaces
    surface_count = 15, # needs to be a large number for good volume rendering
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

# fig.write_image("saida/Plot_4D/plot_4d.png")
# fig.write_image("saida/Plot_4D/plot_4d.pdf")
# fig.write_image("saida/Plot_4D/plot_4d.eps")
                     
fig.show()

#======================================================================
    
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
