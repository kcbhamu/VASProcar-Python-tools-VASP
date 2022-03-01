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
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print("================= Plotando as Projecoes =================")

#----------------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado -----
#----------------------------------------------------------------------
if os.path.isdir('saida'):
   Diretorio_saida = 'saida/Orbitais/'
else:
   Diretorio_saida = ''
#----------------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#======================================================================

banda = np.loadtxt(Diretorio_saida + 'Bandas.dat') 
banda.shape

orbitais = np.loadtxt(Diretorio_saida + 'Orbitais.dat') 
orbitais.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")  

#----------------------------------------------------------------------

if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

rx = orbitais[:,0]
ry = orbitais[:,1]

transp = 1.0
    
for l in range (1,(loop+1)):     # Loop para a analise das Projecoes

    fig, ax = plt.subplots()

    # Plot das Projeções ===================================================   

    if (l == 1):
       S = orbitais[:,2]
       P = orbitais[:,3]
       D = orbitais[:,4]
       #----------------
       ax.scatter(rx, ry, s = S, c = 'blue', alpha = transp, edgecolors = 'none', label = 'S')
       ax.scatter(rx, ry, s = P, c = 'red', alpha = transp, edgecolors = 'none', label = 'P')
       ax.scatter(rx, ry, s = D, c = 'limegreen', alpha = transp, edgecolors = 'none', label = 'D')
       #----------------------
       file = 'Orbitais_S_P_D'       
       
    if (l == 2):
       Px = orbitais[:,5]
       Py = orbitais[:,6]
       Pz = orbitais[:,7]
       #-----------------
       ax.scatter(rx, ry, s = Px, c = 'blue', alpha = transp, edgecolors = 'none', label = r'${P}_{x}$')
       ax.scatter(rx, ry, s = Py, c = 'red', alpha = transp, edgecolors = 'none', label = r'${P}_{y}$')
       ax.scatter(rx, ry, s = Pz, c = 'limegreen', alpha = transp, edgecolors = 'none', label = r'${P}_{z}$')
       #------------------
       file = 'Orbitais_P'
       
    if (l == 3):
       Dxy = orbitais[:,8]
       Dyz = orbitais[:,9]
       Dz2 = orbitais[:,10]
       Dxz = orbitais[:,11]
       Dx2 = orbitais[:,12]
       #-------------------
       ax.scatter(rx, ry, s = Dxy, c = 'blue', alpha = transp, edgecolors = 'none', label = r'${D}_{xy}$')
       ax.scatter(rx, ry, s = Dyz, c = 'red', alpha = transp, edgecolors = 'none', label = r'${D}_{yz}$')
       ax.scatter(rx, ry, s = Dz2, c = 'limegreen', alpha = transp, edgecolors = 'none', label = r'${D}_{z^{2}}$')
       ax.scatter(rx, ry, s = Dxz, c = 'rosybrown', alpha = transp, edgecolors = 'none', label = r'${D}_{xz}$')
       ax.scatter(rx, ry, s = Dx2, c = 'magenta', alpha = transp, edgecolors = 'none', label = r'${D}_{x^{2}}$')
       #------------------
       file = 'Orbitais_D'

    # Plot das Bandas =====================================================

    x = banda[:,0]

    for i in range (1,(nb+1)):
        y = banda[:,i]
        plt.plot(x, y, color = 'black', linestyle = '-', linewidth = 0.25, alpha = 0.3)

    # Destacando a energia de Fermi na estrutura de Bandas ================

    plt.plot([x[0], x[(n_procar*nk)-1]], [0.0, 0.0], color = 'red', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Destacando pontos-k de interesse na estrutura de Bandas =============

    if (dest_k > 0): 
       for j in range (len(dest_pk)):
           plt.plot([dest_pk[j], dest_pk[j]], [energ_min, energ_max], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Rotulando pontos-k de interesse na estrutura de Bandas ==============

    if (dest_k == 2): plt.xticks(dest_pk,label_pk)        
    
    #======================================================================

    plt.xlim((x[0], x[(n_procar*nk)-1]))
    plt.ylim((energ_min, energ_max))

    if (Dimensao == 1 and dest_k != 2): plt.xlabel('$2{\pi}/{a}$')
    if (Dimensao == 2 and dest_k != 2): plt.xlabel('${\AA}^{-1}$')
    if (Dimensao == 3 and dest_k != 2): plt.xlabel('${nm}^{-1}$')

    plt.ylabel('$E-E_{f}$ (eV)')

    ax.set_box_aspect(1.25/1)
    ax.legend(loc = "upper right", title = "")
    # ax.legend(loc = "best", title = "")

    if (save_png == 1): plt.savefig(Diretorio_saida + file + '.png', dpi = 300)
    if (save_pdf == 1): plt.savefig(Diretorio_saida + file + '.pdf', dpi = 300)
    if (save_eps == 1): plt.savefig(Diretorio_saida + file + '.eps', dpi = 300)

    # plt.show()

#======================================================================

print(" ")
print("============================================================")
print("= Edite o Plot das projecoes por meio dos seguintes arquivos")
print("= gerados na pasta saida\Localizacao =======================")   
print("= arquivos .agr (via Grace) ou Orbitais.py =================")
print("============================================================")

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
