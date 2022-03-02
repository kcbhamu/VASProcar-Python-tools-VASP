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

#-----------------------------------------------------------------
# Verificando se a pasta "Spin_Texture" existe, se não existe ela é criada
#-----------------------------------------------------------------
if os.path.isdir("saida/Spin_Texture"):
   0 == 0
else:
   os.mkdir("saida/Spin_Texture")
#------------------------

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
print ("##### (Em Edicao !!!) Projecao 2D da Textura de Spin 3D: #####")
print ("##############################################################")
print (" ")
   
if (escolha == -62):

   print ("##############################################################") 
   print ("## Escolha a dimensao dos eixos-k no Plot 3D: ============= ##")
   print ("##############################################################")
   print ("## [1] (kx,ky,kz) em unidades de 2pi/Param. =============== ##")
   print ("## [2] (kx,ky,kz) em unidades de 1/Angs. ================== ##")
   print ("## [3] (kx,ky,kz) em unidades de 1/nm. ==================== ##") 
   print ("## [4] (k1,k2,k3) Coord. Diretas: K = k1*B1 + k2*B2 + k3*B3 ##")
   print ("## ======================================================== ##")
   print ("## !!! A opcao [4] pode resultar em problemas, caso B1, B2  ##")
   print ("## e B3 nao sejam cartesianos: [a,0,0] [0,a,0] [0,0,a]      ##")   
   print ("##############################################################") 
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print (" ")

if (escolha == 62):
   Dimensao = 1

if (Dimensao < 4):
   c1 = 'kx'; c2 = 'ky'; c3 = 'kz'
if (Dimensao == 4):
   c1 = 'k1'; c2 = 'k2'; c3 = 'k3'

print ("##############################################################")
print ("## Qual plano deve ser visualizado no Plot 3D? ============ ##")
print ("##############################################################")
print (f'## [1] Plano ({c1},{c2}) ====================================== ##')
print (f'## [2] Plano ({c1},{c3}) ====================================== ##')
print (f'## [3] Plano ({c2},{c3}) ====================================== ##')
print ("##############################################################") 
Plano_k = input (" "); Plano_k = int(Plano_k)
print (" ")  

print ("##############################################################")
print ("Qual banda quer analisar? ====================================")
print ("##############################################################") 
Band_i = input (" "); Band_i = int(Band_i)
print (" ")

Band_f = Band_i

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------

#------------------------------------
executavel = Diretorio + '/procar.py'
exec(open(executavel).read())
#------------------------------------  

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------   

tot_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sx[n_procar][nk][nb]
tot_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sy[n_procar][nk][nb]
tot_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sz[n_procar][nk][nb]

total_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sx[n_procar][nk][nb]
total_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sy[n_procar][nk][nb]
total_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sz[n_procar][nk][nb]

#  tot_si (i = x,y,z)   = Soma de todos os orbitais (para ions selecionados) de Sx
#  total_si (i = x,y,z) = Soma de todos os orbitais (para todos os ions) de Sx
                                              
#----------------------------------------------------------------------

for wp in range(1, (n_procar+1)):
    for point_k in range(1, (nk+1)):                                  
        for Band_n in range (1, (nb+1)):
            for ion_n in range (1, (ni+1)):
                for orb_n in range(1,(n_orb+1)):
                    tot_sx[wp][point_k][Band_n] = tot_sx[wp][point_k][Band_n] + Sx[wp][orb_n][point_k][Band_n][ion_n]
                    tot_sy[wp][point_k][Band_n] = tot_sy[wp][point_k][Band_n] + Sy[wp][orb_n][point_k][Band_n][ion_n]
                    tot_sz[wp][point_k][Band_n] = tot_sz[wp][point_k][Band_n] + Sz[wp][orb_n][point_k][Band_n][ion_n]      
 
            #----------------------------------------------------------           
            # Fim do Loop dos ions ------------------------------------
            #----------------------------------------------------------                 
        #----------------------------------------------------------
        # Fim do Loop das Bandas ----------------------------------
        #----------------------------------------------------------      
    #----------------------------------------------------------
    # Fim do Loop dos pontos-k --------------------------------
    #----------------------------------------------------------    
#----------------------------------------------------------
# Fim do Loop dos arquivos PROCAR -------------------------
#----------------------------------------------------------
    
#======================================================================
# Gravando os dados para o Plot da Textura de Spin 3D =================
#======================================================================

#---------------------------------------------------------
spin_3D = open("saida/Spin_Texture/Spin_Texture.dat", "w")
#---------------------------------------------------------
    
for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        Band_n = Band_i 
        if (Dimensao != 4):
           spin_3D.write(f'{kx[j][point_k]} {ky[j][point_k]} {kz[j][point_k]} {Energia[j][point_k][Band_n]} {tot_sx[j][point_k][Band_n]} ')
           spin_3D.write(f'{tot_sy[j][point_k][Band_n]} {tot_sz[j][point_k][Band_n]} \n')       
        if (Dimensao == 4):
           spin_3D.write(f'{kb1[j][point_k]} {kb2[j][point_k]} {kb3[j][point_k]} {Energia[j][point_k][Band_n]} {tot_sx[j][point_k][Band_n]} ')
           spin_3D.write(f'{tot_sy[j][point_k][Band_n]} {tot_sz[j][point_k][Band_n]} \n')
               
#----------------
spin_3D.close()
#----------------

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

#----------------------------------------------------------------------

print(" ")
print("================ Plotando a Textura de Spin 2D_3D ================")
print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")

#---------------------------------------------------------------------
normalizacao = 1  # [0] = sem normalização  //  [1] = com normalização
#---------------------------------------------------------------------

spin_textura = np.loadtxt("saida/Spin_Texture/Spin_Texture.dat")
spin_textura.shape

#----------------------------------------------------------------------

E  = spin_textura[:,3]
Spin_Sx = spin_textura[:,4]
Spin_Sy = spin_textura[:,5]
Spin_Sz = spin_textura[:,6]

if (Plano_k == 1):  # Plano (kx,ky) ou (k1,k2)
   eixo1  = spin_textura[:,0]
   eixo2  = spin_textura[:,1]
   #---------------------------------------------
   norma = ((Spin_Sx**2) + (Spin_Sy**2))**0.5
   if (norma.min() > 0.01 and normalizacao == 1):
      Spin_Sx = Spin_Sx/norma
      Spin_Sy = Spin_Sy/norma
   if (Spin_Sz.max() > 0.01):   
      Spin_Sz = Spin_Sz/Spin_Sz.max()       
   #---------------------------------------------
   Si_min  = Spin_Sz.min()
   Si_max  = Spin_Sz.max()      
   rotulo = '${S}_{z}$'
   
if (Plano_k == 2):  # Plano (kx,kz) ou (k1,k3)
   eixo1  = spin_textura[:,0]
   eixo2  = spin_textura[:,2]
   #---------------------------------------------
   norma = ((Spin_Sx**2) + (Spin_Sz**2))**0.5
   if (norma.min() > 0.01 and normalizacao == 1):
      Spin_Sx = Spin_Sx/norma
      Spin_Sz = Spin_Sz/norma
   if (Spin_Sy.max() > 0.01):     
      Spin_Sy = Spin_Sy/Spin_Sy.max()     
   #---------------------------------------------
   Si_min  = Spin_Sy.min()
   Si_max  = Spin_Sy.max()
   rotulo = '${S}_{y}$'
   
if (Plano_k == 3):  # Plano (ky,kz) ou (k2,k3)
   eixo1  = spin_textura[:,1]
   eixo2  = spin_textura[:,2]
   #---------------------------------------------
   norma = ((Spin_Sy**2) + (Spin_Sz**2))**0.5
   if (norma.min() > 0.01 and normalizacao == 1):
      Spin_Sy = Spin_Sy/norma
      Spin_Sz = Spin_Sz/norma
   if (Spin_Sx.max() > 0.01):     
      Spin_Sx = Spin_Sx/Spin_Sx.max()     
   #---------------------------------------------
   Si_min  = Spin_Sx.min()
   Si_max  = Spin_Sx.max()   
   rotulo = '${S}_{x}$'     

#----------------------------------------------------------------------

print(".... Quase concluido ....")
print(".........................")

#----------------------------------------------------------------------

font = {'family' : 'arial',  
        'color'  : 'black',  
        'weight' : 'normal',  
        'size'   : 10,  
        } 

fig = plt.figure()

ax = fig.add_subplot(111)
ax.axis('equal')
# ax.set_axis_off()

#----------------------------------------------------------------------=

if (Dimensao == 1):
   cl = r' $(2{\pi}/{a})$'
if (Dimensao == 2):
   cl = r' $({\AA}^{-1})$'
if (Dimensao == 3):
   cl = r' $({nm}^{-1})$' 

if (Plano_k == 1 and Dimensao != 4):             # Plano (kx,ky)      
   c1 = r'${S}_{x}$  |  ' + r'${k}_{x}$' + cl
   c2 = r'${S}_{y}$  |  ' + r'${k}_{y}$' + cl
if (Plano_k == 2 and Dimensao != 4):             # Plano (kx,kz)      
   c1 = r'${S}_{x}$  |  ' + r'${k}_{x}$' + cl
   c2 = r'${S}_{z}$  |  ' + r'${k}_{z}$' + cl
if (Plano_k == 3 and Dimensao != 4):             # Plano (ky,kz)      
   c1 = r'${S}_{y}$  |  ' + r'${k}_{y}$' + cl
   c2 = r'${S}_{z}$  |  ' + r'${k}_{z}$' + cl

if (Plano_k == 1 and Dimensao == 4):             # Plano (k1,k2)      
   c1 = '${S}_{x}$  |  ' + r'${k}_{1}$'
   c2 = '${S}_{y}$  |  ' + r'${k}_{2}$'
if (Plano_k == 2 and Dimensao == 4):             # Plano (k1,k3)      
   c1 = '${S}_{x}$  |  ' + r'${k}_{1}$'
   c2 = '${S}_{z}$  |  ' + r'${k}_{3}$'
if (Plano_k == 3 and Dimensao == 4):             # Plano (k2,k3)      
   c1 = '${S}_{y}$  |  ' + r'${k}_{2}$'
   c2 = '${S}_{z}$  |  ' + r'${k}_{3}$'

ax.set_xlabel(c1, fontdict = font)
ax.set_ylabel(c2, fontdict = font)

#----------------------------------------------------------------------

# Criação de uma escala de cor normalizada com os valores de Si com i = (x,y,z).
norm = mpl.colors.Normalize(Si_min, Si_max)
icmap = 'coolwarm'
sm = mpl.cm.ScalarMappable(cmap = icmap, norm = norm)

# Define uma escala de Si com i = (x,y,z) com a marcação de 5 valores na escala.
tk = np.linspace(Si_min, Si_max, 5, endpoint = True)
plt.colorbar(sm, ticks = tk, shrink = 0.5, format='%.2f', label = rotulo)

# width = espessura do vetor // scale = comprimento do vetor
# pivot = 'mid' (VERIFICAR)
# scale_units = 'inches' (VERIFICAR)

if (Plano_k == 1):  ax.quiver(eixo1, eixo2, Spin_Sx, Spin_Sy, Spin_Sz, width = 0.001, scale = 10, scale_units = 'inches', cmap = icmap, norm = norm)
if (Plano_k == 2):  ax.quiver(eixo1, eixo2, Spin_Sx, Spin_Sz, Spin_Sy, width = 0.001, scale = 10, scale_units = 'inches', cmap = icmap, norm = norm)
if (Plano_k == 3):  ax.quiver(eixo1, eixo2, Spin_Sy, Spin_Sz, Spin_Sx, width = 0.001, scale = 10, scale_units = 'inches', cmap = icmap, norm = norm)
  
fig = plt.gcf()
fig.set_size_inches(8,6)

if (save_png == 1): plt.savefig('saida/Spin_Texture/Spin_Texture.png', dpi=300, pad_inches = 0)
if (save_pdf == 1): plt.savefig('saida/Spin_Texture/Spin_Texture.pdf', dpi=300, pad_inches = 0)
if (save_eps == 1): plt.savefig('saida/Spin_Texture/Spin_Texture.eps', dpi=300, pad_inches = 0)

plt.show()

#======================================================================
   
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
