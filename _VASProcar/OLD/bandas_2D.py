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

#-------------------------------------------------------------------
# Verificando se a pasta "Bandas" existe, se não existe ela é criada
#-------------------------------------------------------------------
if os.path.isdir("saida/Bandas"):
   0 == 0
else:
   os.mkdir("saida/Bandas")
#--------------------------

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
print ("################ Plot da Estrutura de Bandas: ################")
print ("##############################################################")
print (" ")

if (escolha == -1):
   
   print ("##############################################################")
   print ("Quanto aos pontos-k de interesse, o que vc deseja? ===========")
   print ("[0] Nao destacar nem rotular nenhum ponto-k ==================")
   print ("[1] Destacar automaticamente os pontos-k informados no KPOINTS")
   print ("[2] Destacar e rotular os pontos-k a sua escolha =============")
   print ("##############################################################") 
   dest_k = input (" "); dest_k = int(dest_k)
   print (" ")

   if (dest_k == 2):
      print ("##############################################################")
      print ("Observacao: O arquivo label.txt sera gerado apos a leitura do ")
      print ("            arquivo PROCAR                                    ")
      print ("##############################################################") 
      print (" ")

      Dimensao = 1

   if (dest_k != 2):
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
   dest_k = 1

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------

#------------------------------------
executavel = Diretorio + '/procar.py'
exec(open(executavel).read())
#------------------------------------

#======================================================================
# Obtenção de alguns parâmetros de ajusto do Grafico (GRACE) ==========
#======================================================================    

x_inicial = xx[1][1]
x_final   = xx[n_procar][nk]
y_inicial = energ_min
y_final   = energ_max

#======================================================================
# Obtendo o nº pontos-k a serem destacados bem como os seus rótulos ===
#======================================================================

#-----------------------------------
executavel = Diretorio + '/label.py'
exec(open(executavel).read())
#-----------------------------------

#======================================================================
#======================================================================
# Plot da Estrutura de Bandas (GRACE) =================================
#====================================================================== 
#======================================================================

#--------------------------------------------
bandas = open("saida/Bandas/Bandas.agr", "w")
#--------------------------------------------

bandas.write("# Grace project file \n")
bandas.write("# written using VASProcar (https://github.com/Augusto-Dlelis/VASProcar-Tools-Python) \n") 
bandas.write("# \n")
bandas.write("@version 50122 \n")
bandas.write("@with g0 \n")
bandas.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
bandas.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

escala_x = (x_final - x_inicial)/5
escala_y = (y_final - y_inicial)/5

bandas.write(f'@    xaxis  tick major {escala_x:.2f} \n')

palavra = '"\\f{Symbol}2p/\\f{Times-Italic}a"'
if (Dimensao == 1 and dest_k != 2): bandas.write(f'@    xaxis  label {palavra} \n') 
if (Dimensao == 2 and dest_k != 2): bandas.write(f'@    xaxis  label "1/Angs." \n') 
if (Dimensao == 3 and dest_k != 2): bandas.write(f'@    xaxis  label "1/nm" \n')

if (dest_k == 2):
   bandas.write(f'@    xaxis  tick spec type both \n')
   bandas.write(f'@    xaxis  tick spec {contador2} \n')
   for i in range (contador2):   
       bandas.write(f'@    xaxis  tick major {i}, {dest_pk[i]} \n')
       temp_r = label_pk[i]
       for j in range(30):
           if (temp_r == '[' + str(j+1) + ']'): temp_r = r_grace[j]                  
       bandas.write(f'@    xaxis  ticklabel {i}, "{temp_r}" \n')    
 
bandas.write(f'@    yaxis  tick major {escala_y:.2f} \n')
bandas.write(f'@    yaxis  label "E-Ef (eV)" \n')

#======================================================================

for i in range(nb + 1 + contador2):

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

if (dest_k > 0):
   for loop in range (contador2):
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

if (dest_k > 0): 
   for j in range (contador2):
       plt.plot([dest_pk[j], dest_pk[j]], [energ_min, energ_max], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)

# Rotulando pontos-k de interesse na estrutura de Bandas ==============

if (dest_k == 2): 
    for i in range(contador2):
        for j in range(30):
            if (label_pk[i] == '[' + str(j+1) + ']'): label_pk[i] = r_matplot[j] 

if (dest_k == 2): plt.xticks(dest_pk,label_pk)    
    
#======================================================================

plt.xlim((xx[1][1], xx[n_procar][nk]))
plt.ylim((energ_min, energ_max))

if (Dimensao == 1 and dest_k != 2): plt.xlabel('$2{\pi}/{a}$')
if (Dimensao == 2 and dest_k != 2): plt.xlabel('${\AA}^{-1}$')
if (Dimensao == 3 and dest_k != 2): plt.xlabel('${nm}^{-1}$')

plt.ylabel('$E-E_{f}$ (eV)')

ax.set_box_aspect(1.25/1)

if (save_png == 1): plt.savefig('saida/Bandas/Bandas.png', dpi=300)
if (save_pdf == 1): plt.savefig('saida/Bandas/Bandas.pdf', dpi=300)
if (save_eps == 1): plt.savefig('saida/Bandas/Bandas.eps', dpi=300)

# plt.show()

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
