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

#----------------------------------------------------------------------
# Verificando se a pasta "Potencial" existe, se não existe ela é criada
#----------------------------------------------------------------------
if os.path.isdir("saida/Potencial"):
   0 == 0
else:
   os.mkdir("saida/Potencial")
#-----------------------------

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
print ("############## Plot do Potencial Eletrostatico: ##############")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("Escolha a dimensao do eixo-x do Plot: ========================")
print ("Utilize 1 para Angs. =========================================")
print ("Utilize 2 para nm. ===========================================")
print ("##############################################################") 
Dimensao = input (" "); Dimensao = int(Dimensao)
print (" ")

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------

ion_x = [0]*(ni)
ion_y = [0]*(ni)
ion_z = [0]*(ni)

#----------------------------------------------------------------------
# Extraindo os resultados do arquivo LOCPOT ---------------------------
#----------------------------------------------------------------------

print (".............. Analisando o arquivo LOCPOT ..............")
print (" ")

#---------------------------
locpot = open("LOCPOT", "r")
#---------------------------

for i in range (8): VTemp = locpot.readline()

#--------------------------------------------------------------------------

c1x = A1x*Parametro; c1y = A1y*Parametro; c1z = A1z*Parametro
c2x = A2x*Parametro; c2y = A2y*Parametro; c2z = A2z*Parametro
c3x = A3x*Parametro; c3y = A3y*Parametro; c3z = A3z*Parametro

Parametro_1 = ((c1x*c1x) + (c1y*c1y) + (c1z*c1z))**0.5
Parametro_teste = Parametro_1

Parametro_2 = ((c2x*c2x) + (c2y*c2y) + (c2z*c2z))**0.5
if (Parametro_2 < Parametro_teste):
   Parametro_teste = Parametro_2

Parametro_3 = ((c3x*c3x) + (c3y*c3y) + (c3z*c3z))**0.5
if (Parametro_3 < Parametro_teste):
   Parametro_teste = Parametro_3

#--------------------------------------------------------------------------

for i in range (ni):
    VTemp = locpot.readline().split()
    ion_x[i] = float(VTemp[0]); ion_x[i] = ion_x[i]*A1x*Parametro
    ion_y[i] = float(VTemp[1]); ion_y[i] = ion_y[i]*A2y*Parametro
    ion_z[i] = float(VTemp[2]); ion_z[i] = ion_z[i]*A3z*Parametro
    
VTemp = locpot.readline()

VTemp = locpot.readline().split()
Grid_x = int(VTemp[0])
Grid_y = int(VTemp[1])
Grid_z = int(VTemp[2])
GRID = Grid_x*Grid_y*Grid_z

V_local = [0]*(GRID)
coord = [0]*3

passo1 = (GRID/5)
resto = passo1 - int(passo1)
if (resto == 0): passo1 = int(passo1)
if (resto != 0): passo1 = int(passo1) + 1

passo2 = 5 - ((passo1*5) -GRID)

for i in range (passo1):
    VTemp = locpot.readline().split()
    if (i < (passo1-1)):
       for j in range(5): V_local[((i)*5) + j] = float(VTemp[j])
    if (i == (passo1-1)):
       for j in range(passo2): V_local[((i)*5) + j] = float(VTemp[j])

#-------------
locpot.close()
#-------------

#----------------------------------------------------------------------
# Analisando os dados -------------------------------------------------
#----------------------------------------------------------------------
     
#------- Obtendo o valor médio do Potencial 3D em cada direção: -------

fator_x  = A1x*Parametro; escala_x = 1.0/float(GRID/Grid_x)
Vx = [0]*(Grid_x); X = [0]*(Grid_x)

fator_y  = A2y*Parametro; escala_y = 1.0/float(GRID/Grid_y)
Vy = [0]*(Grid_y); Y = [0]*(Grid_y)

fator_z  = A3z*Parametro; escala_z = 1.0/float(GRID/Grid_z)
Vz = [0]*(Grid_z); Z = [0]*(Grid_z)

for i in range (Grid_x):
    for j in range (Grid_y):  
        for k in range (Grid_z):                          
            indice = i + (j + k*Grid_y)*Grid_x
            Vx[i] = Vx[i] + V_local[indice]*escala_x
            Vy[j] = Vy[j] + V_local[indice]*escala_y
            Vz[k] = Vz[k] + V_local[indice]*escala_z

#======================================================================
# Plot do Potencial médio em uma dada direção: ========================
#====================================================================== 

import matplotlib.pyplot as plt
import numpy as np

for l in range(1,(3+1)):

    #======================================================================
    #======================================================================
    # Plot 2D do Potencial médio em uma dada direção (GRACE) ==============
    #====================================================================== 
    #======================================================================   

    if (l == 1):      
       print ("................. Analisando a direcao-X ................")       
       name = 'Potencial_x'; eixo = 'eixo-x '; t_grid = Grid_x
       dx = fator_x/20; x_inicial = (0.0 - dx); x_final = (fator_x + dx)
       dy = (max(Vx) - min(Vx))/20; y_inicial = (min(Vx) - dy); y_final = (max(Vx) + dy)
       coord[1] = min(ion_x); coord[2] = max(ion_x)      
       if (coord[1] == 0.0 and (fator_x - max(ion_x)) < Parametro_teste): coord[2] = fator_x
       
    if (l == 2):
       print ("................. Analisando a direcao-Y ................")       
       name = 'Potencial_y'; eixo = 'eixo-y '; t_grid = Grid_y
       dx = fator_y/20; x_inicial = (0.0 - dx); x_final = (fator_y + dx)
       dy = (max(Vy) - min(Vy))/20; y_inicial = (min(Vy) - dy); y_final = (max(Vy) + dy)
       coord[1] = min(ion_y); coord[2] = max(ion_y)
       if (coord[1] == 0.0 and (fator_y - max(ion_y)) < Parametro_teste): coord[2] = fator_y
       
    if (l == 3):
       print ("................. Analisando a direcao-Z ................")       
       name = 'Potencial_z'; eixo = 'eixo-z '; t_grid = Grid_z
       dx = fator_z/20; x_inicial = (0.0 - dx); x_final = (fator_z + dx)
       dy = (max(Vz) - min(Vz))/20; y_inicial = (min(Vz) - dy); y_final = (max(Vz) + dy)
       coord[1] = min(ion_z); coord[2] = max(ion_z)
       if (coord[1] == 0.0 and (fator_z - max(ion_z)) < Parametro_teste): coord[2] = fator_z

    #--------------------------------------------------------
    potencial = open('saida/Potencial/' + name + '.agr', "w")
    #--------------------------------------------------------

    potencial.write("# Grace project file \n")
    potencial.write("# \n")
    potencial.write("@version 50122 \n")
    potencial.write("@with g0 \n")
    potencial.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
    # potencial.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    potencial.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    if (Dimensao == 1):
       label = eixo + '(Angs.)'
       potencial.write(f'@    xaxis  label "{label}" \n') 
    if (Dimensao == 2):
       label = eixo + '(nm)'
       potencial.write(f'@    xaxis  label "{label}" \n') 
 
    potencial.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    potencial.write(f'@    yaxis  label "Potencial Eletrostatico (V)" \n')

    #======================================================================

    for i in range(1,(3+1)):

        if (i <= 2): color = 7 # cor Cinza
        if (i == 3): color = 2 # cor Vermelha
   
        potencial.write(f'@    s{i-1} type xy \n')
        potencial.write(f'@    s{i-1} line type 1 \n')
        potencial.write(f'@    s{i-1} line color {color} \n')
        potencial.write(f'@    s{i-1} line linewidth 2.0 \n')       
    potencial.write(f'@type xy \n')

    # Destacando a dimensão (na direção selecionada) ocupada pelos ions da rede:
            
    potencial.write(f'{coord[1]} {y_inicial} \n')
    potencial.write(f'{coord[1]} {y_final} \n')     
    potencial.write(" \n")

    potencial.write(f'{coord[2]} {y_inicial} \n')
    potencial.write(f'{coord[2]} {y_final} \n')     
    potencial.write(" \n")     
    
    # Plot do valor médio do potencial eletrostatico em uma dada direção:
    
    for i in range (t_grid):
       
        if (l == 1):
           X[i] = (float(i)/(float(Grid_x) - 1.0))*fator_x
           potencial.write(f'{X[i]} {Vx[i]} \n')

        if (l == 2):
           Y[i] = (float(i)/(float(Grid_y) - 1.0))*fator_y
           potencial.write(f'{Y[i]} {Vy[i]} \n')

        if (l == 3):
           Z[i] = (float(i)/(float(Grid_z) - 1.0))*fator_z
           potencial.write(f'{Z[i]} {Vz[i]} \n')           

    #----------------
    potencial.close()
    #----------------   

    #======================================================================
    #======================================================================
    # Plot 2D do Potencial médio em uma dada direção (Matplotlib) =========
    #====================================================================== 
    #======================================================================

    fig, ax = plt.subplots()

    # Destacando a dimensão (na direção selecionada) ocupada pelos ions da rede:

    plt.plot([coord[1], coord[1]], [y_inicial, y_final], color = 'gray', linestyle = '-', linewidth = 0.5, alpha = 1.0)
    plt.plot([coord[2], coord[2]], [y_inicial, y_final], color = 'gray', linestyle = '-', linewidth = 0.5, alpha = 1.0)

    # Plot do valor médio do potencial eletrostatico em uma dada direção:

    if (l == 1): plt.plot(X, Vx, color = 'red', linestyle = '-', linewidth = 1.0)
    if (l == 2): plt.plot(Y, Vy, color = 'red', linestyle = '-', linewidth = 1.0)
    if (l == 3): plt.plot(Z, Vz, color = 'red', linestyle = '-', linewidth = 1.0)
    
    #======================================================================

    plt.xlim((x_inicial, x_final))
    plt.ylim((y_inicial, y_final))

    plt.xlabel(label)
    plt.ylabel('Potencial Eletrostatico (V)')

    # ax.set_box_aspect(1.25/1)  

    plt.savefig('saida/Potencial/' + name + '.png', dpi=300)
    plt.savefig('saida/Potencial/' + name + '.pdf', dpi=300)
    # plt.savefig('saida/Potencial/' + name + '.eps', dpi=300)

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
