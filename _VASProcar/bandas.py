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
print ("################ Plot da Estrutura de Bandas: ################")
print ("##############################################################")
print (" ")

if (escolha == -1):
   
   print ("##############################################################")
   print ("Escolha a dimensao do eixo-k: ================================")
   print ("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. =")
   print ("Utilize 2 para k em unidades de 1/Angs. ======================")
   print ("Utilize 3 para k em unidades de 1/nm. ========================")
   print ("##############################################################") 
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print (" ")

if (escolha == 1):

   Dimensao = 1

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------

#---------------------------------------------
exec(open("_VASProcar/procar.py").read())
#---------------------------------------------   

#======================================================================
# Obtenção de alguns parâmetros de ajusto do Grafico (GRACE) ==========
#======================================================================    

x_inicial = xx[1][1]
x_final   = xx[n_procar][nk]
y_inicial = energ_min
y_final   = energ_max

#======================================================================
# Obtendo o nº pontos-k a serem destacados na estrutura de Bandas =====
#======================================================================

#------------------------------------------
inform = open("saida/informacoes.txt", "r")
#------------------------------------------

palavra = 'Pontos-k |'                          

for line in inform:   
    if palavra in line: 
       break

VTemp = inform.readline()
VTemp = inform.readline()
       
nk_total = nk*n_procar

contador2 = 0
dest_pk = [0]*(100)                    # Inicialização do vetor dest_pk de dimensão 100.

for i in range (1, (nk_total+1)):
    VTemp = inform.readline().split()
    r1 = int(VTemp[0]); r2 = float(VTemp[1]); r3 = float(VTemp[2]); r4 = float(VTemp[3]); comprimento = float(VTemp[4])
    if (i != 1) and (i != (nk_total+1)):  
       dif = comprimento - comprimento_old     
       if(dif == 0.0):
          contador2 += 1
          dest_pk[contador2] = comprimento
          
    comprimento_old = comprimento

#-------------
inform.close()
#-------------

#======================================================================
#======================================================================
# Plot da Estrutura de Bandas (GRACE) =================================
#====================================================================== 
#======================================================================

#-------------------------------------
bandas = open("saida/Bandas.agr", "w")
#-------------------------------------

bandas.write("# Grace project file \n")
bandas.write("# \n")
bandas.write("@version 50122 \n")
bandas.write("@with string \n")
bandas.write("@    string on \n")

bandas.write(f'@    string {fig_xmin}, {fig_ymax + 0.01} \n')
bandas.write(f'@    string def "E(eV)" \n')
bandas.write("@with string \n")
bandas.write("@    string on \n")

if (Dimensao == 1):
   bandas.write(f'@    string {fig_xmax - 0.14}, {fig_ymin - 0.058} \n')
   bandas.write(f'@    string def "(2pi/Param.)" \n')
if (Dimensao == 2):
   bandas.write(f'@    string {fig_xmax - 0.10}, {fig_ymin - 0.058} \n')
   bandas.write(f'@    string def "(1/Angs.)" \n')
if (Dimensao == 3):
   bandas.write(f'@    string {fig_xmax - 0.07}, {fig_ymin - 0.058} \n')
   bandas.write(f'@    string def "(1/nm)" \n')

bandas.write("@with g0 \n")
bandas.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
bandas.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

escala_x = (x_final - x_inicial)/5
escala_y = (y_final - y_inicial)/5
bandas.write(f'@    xaxis  tick major {escala_x:.2f} \n')
bandas.write(f'@    yaxis  tick major {escala_y:.2f} \n')

#======================================================================

for i in range(nb+1+contador2):

    if (i <= (nb-1)): color = 1 # cor Preta
    if (i == nb):     color = 2 # cor Vermelha
    if (i > nb):      color = 7 # Cor Cinza  
   
    bandas.write(f'@    s{i} type xy \n')
    bandas.write(f'@    s{i} line type 1 \n')
    bandas.write(f'@    s{i} line color {color} \n')
    
bandas.write(f'@type xy \n')    

# Plot das Bandas =====================================================
     
for Band_n in range (1,(nb+1)):
    bandas.write(" \n")
    for j in range (1,(n_procar+1)):
        for point_k in range (1,(nk+1)):
            bandas.write(f'{xx[j][point_k]} {Energia[j][point_k][Band_n]} \n')

# Destacando a energia de Fermi na estrutura de Bandas ================
      
bandas.write(" \n")
bandas.write(f'{xx[1][1]} 0.0 \n')
bandas.write(f'{xx[n_procar][nk]} 0.0 \n')

# Destacando pontos-k de interesse na estrutura de Bandas =============

for loop in range (1,(contador2+1)):
    bandas.write(" \n")
    bandas.write(f'{dest_pk[loop]} {energ_min} \n')
    bandas.write(f'{dest_pk[loop]} {energ_max} \n')     

#-------------
bandas.close()
#-------------

#======================================================================
#======================================================================
# Plot da Estrutura de Bandas (Matplotlib) ============================
#====================================================================== 
#======================================================================

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Plot das Bandas =====================================================

x = [0]*(n_procar*nk)
y = [0]*(n_procar*nk)

for k in range (1,(nb+1)):
    number = -1
    for i in range (1,(n_procar+1)):
        for j in range (1,(nk+1)):
            number += 1
            if (k == 1): x[number] = xx[i][j]
            y[number] = Energia[i][j][k]
    plt.plot(x, y, color = 'black', linestyle = '-', linewidth = 0.25)

# Destacando a energia de Fermi na estrutura de Bandas ================

plt.plot([xx[1][1], xx[n_procar][nk]], [0.0, 0.0], color = 'red', linestyle = '-', linewidth = 0.1, alpha = 1.0)

# Destacando pontos-k de interesse na estrutura de Bandas =============

for j in range (1,(contador2+1)):
    plt.plot([dest_pk[j], dest_pk[j]], [energ_min, energ_max], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)      
    
#======================================================================

plt.xlim((xx[1][1], xx[n_procar][nk]))
plt.ylim((energ_min, energ_max))

if (Dimensao == 1):
   plt.xlabel("(2pi/Param.)")
if (Dimensao == 2):
   plt.xlabel("(1/Angs.)")
if (Dimensao == 3):
   plt.xlabel("(1/nm)")

plt.ylabel("E(eV)")

ax.set_box_aspect(1.25/1)

plt.savefig('saida/Bandas.png', dpi=300)
plt.savefig('saida/Bandas.pdf', dpi=300)

# plt.show()

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
