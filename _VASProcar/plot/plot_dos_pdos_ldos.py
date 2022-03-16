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
print("==================== Plotando a DOS: ====================")

#----------------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado -----
#----------------------------------------------------------------------
if os.path.isdir('saida'):
   Diretorio_saida = 'saida/DOS/'
else:
   Diretorio_saida = ''
#----------------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#======================================================================

dos = np.loadtxt(Diretorio_saida + 'DOS_pDOS_lDOS.dat') 
dos.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")  

#======================================================================

if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

transp = 0.25
linew = 0.5

energia = dos[:,0]

for l in range (1,(loop+1)):     # Loop para a analise das Projecoes

    fig, ax = plt.subplots() 

    # Plot das Projeções ===================================================

    if (l == 1):
       #-----------------
       dos_tot = dos[:,1]
       l_dos   = dos[:,2]
       dos_S   = dos[:,3]
       dos_P   = dos[:,4]
       dos_D   = dos[:,5]
       #-------------------------------
       ax.plot(dos_tot, energia, color = 'gray', linestyle = '-', linewidth = linew, label = r'${DOS}$')
       ax.fill(dos_tot, energia, color = 'gray', alpha = transp)
       if (esc == 1):
          ax.plot(l_dos, energia, color = 'magenta', linestyle = '-', linewidth = linew, label = r'${l-DOS}$')
          ax.fill(l_dos, energia, color = 'magenta', alpha = transp)          
       ax.plot(dos_S, energia, color = 'blue', linestyle = '-', linewidth = linew, label = r'${S}$')
       ax.fill(dos_S, energia, color = 'blue', alpha = transp)
       ax.plot(dos_P, energia, color  = 'red', linestyle = '-', linewidth = linew, label = r'${P}$')
       ax.fill(dos_P, energia, color  = 'red', alpha = transp)
       ax.plot(dos_D, energia, color  = 'limegreen', linestyle = '-', linewidth = linew, label = r'${D}$')
       ax.fill(dos_D, energia, color  = 'limegreen', alpha = transp)
       #-------------------------------
       if (esc == 0): file = 'DOS_pDOS'
       if (esc == 1): file = 'DOS_pDOS_lDOS'
       
    if (l == 2):
       #----------------
       dos_Px = dos[:,6]
       dos_Py = dos[:,7]
       dos_Pz = dos[:,8]
       #-----------------------------
       ax.plot(dos_P, energia, color  = 'gray', linestyle = '-', linewidth = linew, label = r'${P}$')
       ax.fill(dos_P, energia, color  = 'gray', alpha = transp)
       ax.plot(dos_Px, energia, color = 'blue', linestyle = '-', linewidth = linew, label = r'${P}_{x}$')
       ax.fill(dos_Px, energia, color = 'blue', alpha = transp)
       ax.plot(dos_Py, energia, color = 'red', linestyle = '-', linewidth = linew, label = r'${P}_{y}$')
       ax.fill(dos_Py, energia, color = 'red', alpha = transp)
       ax.plot(dos_Pz, energia, color = 'limegreen', linestyle = '-', linewidth = linew, label = r'${P}_{z}$')
       ax.fill(dos_Pz, energia, color = 'limegreen', alpha = transp)
       #-----------------------------
       if (esc == 0): file = 'pDOS_P'
       if (esc == 1): file = 'pDOS_lDOS_P'


    if (l == 3):
       #------------------
       dos_Dxy = dos[:,9]
       dos_Dyz = dos[:,10]
       dos_Dz2 = dos[:,11]
       dos_Dxz = dos[:,12]
       dos_Dx2 = dos[:,13]        
       #-----------------------------
       ax.plot(dos_D, energia, color   = 'gray', linestyle = '-', linewidth = linew, label = r'${D}$')
       ax.fill(dos_D, energia, color   = 'gray', alpha = transp)
       ax.plot(dos_Dxy, energia, color = 'blue', linestyle = '-', linewidth = linew, label = r'${D}_{xy}$')
       ax.fill(dos_Dxy, energia, color = 'blue', alpha = transp)
       ax.plot(dos_Dyz, energia, color = 'red', linestyle = '-', linewidth = linew, label = r'${D}_{yz}$')
       ax.fill(dos_Dyz, energia, color = 'red', alpha = transp)
       ax.plot(dos_Dz2, energia, color = 'limegreen', linestyle = '-', linewidth = linew, label = r'${D}_{z^{2}}$')
       ax.fill(dos_Dz2, energia, color = 'limegreen', alpha = transp)
       ax.plot(dos_Dxz, energia, color = 'rosybrown', linestyle = '-', linewidth = linew, label = r'${D}_{xz}$')
       ax.fill(dos_Dxz, energia, color = 'rosybrown', alpha = transp)
       ax.plot(dos_Dx2, energia, color = 'magenta', linestyle = '-', linewidth = linew, label = r'${D}_{x^{2}}$')
       ax.fill(dos_Dx2, energia, color = 'magenta', alpha = transp)
       #-----------------------------
       if (esc == 0): file = 'pDOS_D'
       if (esc == 1): file = 'pDOS_lDOS_D'

    # Destacando a energia de Fermi na estrutura de Bandas ================

    plt.plot([x_inicial, x_final], [0.0, 0.0], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    #======================================================================

    plt.xlim((x_inicial, x_final))
    plt.ylim((energ_min, energ_max))

    plt.xlabel("Density of States")
    plt.ylabel('$E-E_{f}$ (eV)')

    ax.set_box_aspect(1.25/1)
    ax.legend(loc="upper right", title="")
    # ax.legend(loc="best", title="")

    if (save_png == 1): plt.savefig(Diretorio_saida + file + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(Diretorio_saida + file + '.pdf', dpi = 600)
    if (save_eps == 1): plt.savefig(Diretorio_saida + file + '.eps', dpi = 600)

    # plt.show()
    
#======================================================================

if (Diretorio_saida != ''):
   print(" ")
   print("============================================================")
   print("= Edite o Plot da DOS por meio dos seguintes arquivos ======")
   print("= gerados na pasta saida\DOS ===============================")   
   print("= arquivos .agr (via Grace) ou DOS_pDOS_lDOS.py ============")
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
