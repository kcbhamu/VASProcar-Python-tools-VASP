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
   Diretorio_saida = 'saida/Localizacao/'
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

localizacao = np.loadtxt(Diretorio_saida + 'Localizacao.dat') 
localizacao.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")  

#----------------------------------------------------------------------

fig, ax = plt.subplots()

# Plot das Projeções ===================================================

rx = localizacao[:,0]
ry = localizacao[:,1] 
ra = localizacao[:,2]
rb = localizacao[:,3]
rc = localizacao[:,4]
rd = localizacao[:,5]
re = localizacao[:,6]          

transp = 1.0

if (num_A == 1): ax.scatter(rx, ry, s = ra, c = 'blue', alpha = transp, edgecolors = 'none', label = 'A')
if (num_B == 1): ax.scatter(rx, ry, s = rb, c = 'red', alpha = transp, edgecolors = 'none', label = 'B')
if (num_C == 1): ax.scatter(rx, ry, s = rc, c = 'limegreen', alpha = transp, edgecolors = 'none', label = 'C')
if (num_D == 1): ax.scatter(rx, ry, s = rd, c = 'rosybrown', alpha = transp, edgecolors = 'none', label = 'D')
if (num_E == 1): ax.scatter(rx, ry, s = re, c = 'magenta', alpha = transp, edgecolors = 'none', label = 'E')

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

if (save_png == 1): plt.savefig(Diretorio_saida + 'Localizacao_estados.png', dpi = 300)
if (save_pdf == 1): plt.savefig(Diretorio_saida + 'Localizacao_estados.pdf', dpi = 300)
if (save_eps == 1): plt.savefig(Diretorio_saida + 'Localizacao_estados.eps', dpi = 300)


# plt.show()

#======================================================================

print(" ")
print("============================================================")
print("= Edite o Plot das projecoes por meio dos seguintes arquivos")
print("= gerados na pasta saida\Localizacao =======================")   
print("= arquivos .agr (via Grace) ou localizacao.py ==============")
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
