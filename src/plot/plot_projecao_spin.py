
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print("================= Plotando as Projecoes =================")

#----------------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado -----
#----------------------------------------------------------------------
if os.path.isdir('output'):
   dir_output = 'output/Spin/'
else:
   dir_output = ''
#----------------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#======================================================================

banda = np.loadtxt(dir_output + 'Bandas.dat') 
banda.shape

spin = np.loadtxt(dir_output + 'Spin.dat') 
spin.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")  

#----------------------------------------------------------------------

rx = spin[:,0]
ry = spin[:,1]

for l in range (1,(3+1)):

    fig, ax = plt.subplots()

    # Plot das Projeções ===================================================
    
    if (l == 1):
       Si_u = spin[:,2]
       Si_d = spin[:,3]
       palavra = r'$S_{x}$'; file = 'Spin_Sx'
    if (l == 2):
       Si_u = spin[:,4]
       Si_d = spin[:,5]
       palavra = r'$S_{y}$'; file = 'Spin_Sy'
    if (l == 3):
       Si_u = spin[:,6]
       Si_d = spin[:,7]
       palavra = r'$S_{z}$'; file = 'Spin_Sz'

    ax.scatter(rx, ry, s = Si_u, c = 'red',  alpha = transp, edgecolors = 'none', label = palavra + r'$\uparrow$')
    ax.scatter(rx, ry, s = Si_d, c = 'blue', alpha = transp, edgecolors = 'none', label = palavra + r'$\downarrow$')   

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
    ax.legend(loc="upper right", title="")
    # ax.legend(loc="best", title="")

    if (save_png == 1): plt.savefig(dir_output + file + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_output + file + '.pdf', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_output + file + '.eps', dpi = 600)

    # plt.show()

#======================================================================

if (dir_output != ''):
   print(" ")
   print("============================================================")
   print("= Edite o Plot das projecoes por meio dos seguintes arquivos")
   print("= gerados na pasta output\Localizacao ======================")   
   print("= arquivos .agr (via Grace) ou Spin.py =====================")
   print("============================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
