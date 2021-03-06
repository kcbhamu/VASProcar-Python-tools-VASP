
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print("========== Plot 2D do Potencial Eletrostatico: ==========")

#------------------------------------------------------------------------
# Teste para saber quais diretorios devem ser corretamente informados ---
#------------------------------------------------------------------------
if os.path.isdir('src'):
   0 == 0
   dir_output = dir_files + '/output/Potencial/'
else:
   dir_files = ''
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#======================================================================   

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................") 

#==========================================================================

for l in range(1,(3+1)):

    fig, ax = plt.subplots()

    #======================================================================

    if (l == 1):
       #-----------------------------------------------------
       potencial = np.loadtxt(dir_output + 'Potencial_X.dat') 
       potencial.shape
       #------------------
       X  = potencial[:,0]
       Vx = potencial[:,1]
       #------------------

    if (l == 2):
       #-----------------------------------------------------
       potencial = np.loadtxt(dir_output + 'Potencial_Y.dat') 
       potencial.shape
       #------------------
       Y  = potencial[:,0]
       Vy = potencial[:,1]
       #------------------

    if (l == 3):
       #-----------------------------------------------------
       potencial = np.loadtxt(dir_output + 'Potencial_Z.dat') 
       potencial.shape
       #------------------
       Z  = potencial[:,0]
       Vz = potencial[:,1]
       #------------------

    # Plot do valor m??dio do potencial eletrostatico em uma dada dire????o:

    if (l == 1):
        plt.plot(X, Vx, color = 'red', linestyle = '-', linewidth = 1.0)
        name = 'Potencial_x'; eixo = 'X '; coord = ion_x
        dx = fator_x/20; x_inicial = (0.0 - dx); x_final = (fator_x + dx)
        dy = (max(Vx) - min(Vx))/20; y_inicial = (min(Vx) - dy); y_final = (max(Vx) + dy)  
        
    if (l == 2):
        plt.plot(Y, Vy, color = 'red', linestyle = '-', linewidth = 1.0)
        name = 'Potencial_y'; eixo = 'Y '; coord = ion_y
        dx = fator_y/20; x_inicial = (0.0 - dx); x_final = (fator_y + dx)
        dy = (max(Vy) - min(Vy))/20; y_inicial = (min(Vy) - dy); y_final = (max(Vy) + dy)
        
    if (l == 3):
        plt.plot(Z, Vz, color = 'red', linestyle = '-', linewidth = 1.0)
        name = 'Potencial_z'; eixo = 'Z '; coord = ion_z
        dx = fator_z/20; x_inicial = (0.0 - dx); x_final = (fator_z + dx)
        dy = (max(Vz) - min(Vz))/20; y_inicial = (min(Vz) - dy); y_final = (max(Vz) + dy)  

    # Destacando as coordenadas dos ions da rede:

    if (destaque == 1):
       for i in range(ni):
           plt.plot([coord[i], coord[i]], [y_inicial, y_final], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 0.5)
    
    #======================================================================

    if (Dimensao == 1):
       label = eixo + '($\AA$)'

    if (Dimensao == 2):
       label = eixo + '(nm)'        
    
    #======================================================================

    plt.xlim((x_inicial, x_final))
    plt.ylim((y_inicial, y_final))

    plt.xlabel(label)
    plt.ylabel('Potencial Eletrostatico (V)')

    # ax.set_box_aspect(1.25/1)  

    if (save_png == 1): plt.savefig(dir_output + name + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_output + name + '.pdf', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_output + name + '.eps', dpi = 600)

    # plt.show()

#======================================================================

if (dir_output != ''):
   print(" ")
   print("============================================================")
   print("= Edite o Plot do Potencial por meio do arquivo Potencial.py")
   print("= gerado na pasta output/Potencial =========================")   
   print("============================================================")

#--------------------------------------------------------------------
print(" ")
print("======================= Concluido ==========================")
#--------------------------------------------------------------------
    
