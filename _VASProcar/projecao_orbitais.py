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

#---------------------------------------------------------------------
# Verificando se a pasta "Orbitais" existe, se não existe ela é criada
#---------------------------------------------------------------------
if os.path.isdir("saida/Orbitais"):
   0 == 0
else:
   os.mkdir("saida/Orbitais")
#----------------------------

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
print ("############### Projecao dos Orbitais (S,P,D): ###############")
print ("##############################################################") 
print (" ")

if (escolha == -2):
   
   print ("##############################################################")
   print ("Escolha a dimensao do eixo-k: ================================")
   print ("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. =")
   print ("Utilize 2 para k em unidades de 1/Angs. ======================")
   print ("Utilize 3 para k em unidades de 1/nm. ========================")
   print ("##############################################################")
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print(" ")

   print ("##############################################################")
   print ("Digite o peso/tamanho das esferas na projecao: ===============")
   print ("Digite um valor entre 0.0 e 1.0 ==============================")
   print ("##############################################################")
   peso_total = input (" "); peso_total = float(peso_total)
   print(" ")

   print ("##############################################################")
   print ("O que vc deseja Plotar/Analisar? =============================")
   print ("Digite 0 para analisar todos os ions da rede =================")
   print ("Digite 1 para analisar ions selecionados =====================")
   print ("##############################################################")
   esc = input (" "); esc = int(esc)

   if (esc == 1):

      sim_nao = ["nao"]*(ni + 1)             # Inicialização do vetor sim_nao
      
      print (" ")
      print ("##############################################################")
      print ("Especifique os ions selecionados em intervalos ===============")
      print ("Quantos intervalos de ions ira fornecer abaixo? ==============")
      print ("##############################################################")
      loop = input (" "); loop = int(loop)
      for i in range (1,(loop+1)):
          print (" ")
          print (f'{i} intervalo: ==============================================')
          print ("Digite o ion inicial do intervalo ============================")
          loop_i = input (" "); loop_i = int(loop_i)
          print ("Digite o ion final do intervalo ==============================")
          loop_f = input (" "); loop_f = int(loop_f)
          if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
             print (" ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("   ERRO: Os valores de ions informados estao incorretos   ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print (" ")
          for i in range(loop_i, (loop_f + 1)):
             sim_nao[i] = "sim"

   print (" ")

if (escolha == 2):   
   Dimensao = 1
   peso_total = 1.0
   esc = 0

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------

#---------------------------------------------
exec(open("_VASProcar/procar.py").read())
#---------------------------------------------     

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------
   
soma_orb = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(n_orb+1)] for k in range(n_procar+1)]                    # soma_orb[n_procar][n_orb][nk][nb]
total = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                                                 # tot[n_procar][nk][nb]
 
#  orb      = [procar.py] Parcela do Orbital (S, P ou D) referente a cada ion "ni".
#  soma_orb = Soma do Orbital (S, P ou D) sobre todos os ions "ni" selecionados.
#  tot      = Soma sobre todos os orbitais e todos os ions.

#======================================================================
# Calculo do peso (% de contribuição) de cada orbital =================
#====================================================================== 

for wp in range(1, (n_procar+1)):
    for point_k in range(1, (nk+1)):                                  
        for Band_n in range (1, (nb+1)):
            for ion_n in range (1, (ni+1)):            
                #------------------------------------------------------                
                if (esc == 1):
                   temp_sn = sim_nao[ion_n]
                #------------------------------------------------------                              
                for orb_n in range(1,(n_orb+1)):
                    total[wp][point_k][Band_n] = total[wp][point_k][Band_n] + orb[wp][orb_n][point_k][Band_n][ion_n]
                    if (esc == 0 or (esc == 1 and temp_sn == "sim")):
                       soma_orb[wp][orb_n][point_k][Band_n] = soma_orb[wp][orb_n][point_k][Band_n] + orb[wp][orb_n][point_k][Band_n][ion_n]                    
            #----------------------------------------------------------           
            # Fim do Loop dos ions ------------------------------------
            #----------------------------------------------------------  
            for orb_n in range (1, (n_orb+1)):
                if (total[wp][point_k][Band_n] != 0.0):
                   soma_orb[wp][orb_n][point_k][Band_n] = ( soma_orb[wp][orb_n][point_k][Band_n]/total[wp][point_k][Band_n] )*peso_total                   
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
# Plot das Projeções dos Orbitais (GRACE) =============================
#====================================================================== 
#======================================================================
                          
if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

# Rotulo dos Orbitais ================================================= 

t_orb = [0]*(12)
t_orb[1] = 'S'; t_orb[2] = 'P'; t_orb[3] = 'D'; t_orb[4] = 'Px'; t_orb[5] = 'Py'; t_orb[6] = 'Pz'
t_orb[7] = 'Dxy'; t_orb[8] = 'Dyz'; t_orb[9] = 'Dz2'; t_orb[10] = 'Dxz'; t_orb[11] = 'Dx2'

#======================================================================

print (" ")          
print ("============================================")

for i in range (1,(loop+1)):     # Loop para a analise das Projecoes
        
#-----------------------------------------------------------------------

    if (i == 1):
       #----------------------------------------------------------
       projection = open("saida/Orbitais/Orbitais_S_P_D.agr", "w")
       #----------------------------------------------------------
       print ("Analisando a Projecao dos Orbitais (S, P, D)")        
       s = 1; t = (3+1)
       
    if (i == 2):
       #------------------------------------------------------
       projection = open("saida/Orbitais/Orbitais_P.agr", "w")     
       #------------------------------------------------------
       print ("Analisando a Projecao dos Orbitais (Px, Py, Pz)") 
       s = 4; t = (6+1)
       
    if (i == 3):
       #------------------------------------------------------
       projection = open("saida/Orbitais/Orbitais_D.agr", "w")
       #------------------------------------------------------
       print ("Analisando a Projecao dos Orbitais (Dxy, Dyz, Dz2, Dxz, Dx2)") 
       s = 7; t = (11+1)   

# Escrita do arquivo ".agr" do GRACE ===================================

    projection.write("# Grace project file \n")
    projection.write("# \n")
    projection.write("@version 50122 \n")
    projection.write("@with string \n")
    projection.write("@    string on \n")
    projection.write(f'@    string {fig_xmin}, {fig_ymax + 0.01} \n')
    projection.write(f'@    string def "E(eV)" \n')
    projection.write("@with string \n")
    projection.write("@    string on \n")

    if (Dimensao == 1):
       projection.write(f'@    string {fig_xmax - 0.14}, {fig_ymin - 0.058} \n')
       projection.write(f'@    string def "(2pi/Param.)" \n')
    if (Dimensao == 2):
       projection.write(f'@    string {fig_xmax - 0.10}, {fig_ymin - 0.058} \n')
       projection.write(f'@    string def "(1/Angs.)" \n')
    if (Dimensao == 3):
       projection.write(f'@    string {fig_xmax - 0.07}, {fig_ymin - 0.058} \n')
       projection.write(f'@    string def "(1/nm)" \n')

    projection.write("@with g0 \n")
    projection.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
    projection.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    projection.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    projection.write(f'@    yaxis  tick major {escala_y:.2f} \n')        
    projection.write(f'@    legend {fig_xmax + leg_x}, {fig_ymax + leg_y} \n')
       
    for j in range (s,t):
          
        if (j == (s+0)): grac='s0'; color = cor_orb[j]        # Cor dos Orbitais (S,Px,Dxy)
        if (j == (s+1)): grac='s1'; color = cor_orb[j]        # Cor dos Orbitais (P,Py,Dyz)
        if (j == (s+2)): grac='s2'; color = cor_orb[j]        # Cor dos Orbitais (D,Pz,Dz2)
        if (j == (s+3)): grac='s3'; color = cor_orb[j]        # Cor do Orbital Dxz
        if (j == (s+4)): grac='s4'; color = cor_orb[j]        # Cor do Orbital Dx2
           
        projection.write(f'@    {grac} type xysize \n')
        projection.write(f'@    {grac} symbol 1 \n')
        projection.write(f'@    {grac} symbol color {color} \n')
        projection.write(f'@    {grac} symbol fill color {color} \n')
        projection.write(f'@    {grac} symbol fill pattern 1 \n')
        projection.write(f'@    {grac} line type 0 \n')
        projection.write(f'@    {grac} line color {color} \n')
        projection.write(f'@    {grac} legend  "{t_orb[j]}" \n')

    for j in range(nb+1+contador2):

        if (j <= (nb-1)): color = 1 # cor Preta
        if (j == nb):     color = 2 # cor Vermelha
        if (j > nb):      color = 7 # Cor Cinza
   
        projection.write(f'@    s{j+(t-s)} type xysize \n')
        projection.write(f'@    s{j+(t-s)} line type 1 \n')
        projection.write(f'@    s{j+(t-s)} line color {color} \n') 

    projection.write("@type xysize")
    projection.write(" \n")
      
# Plot dos Orbitais ===================================================

    for j in range (s,t):

        for wp in range (1, (n_procar+1)):
            for point_k in range (1, (nk+1)):
                for Band_n in range (1, (nb+1)):
                    #------------------------------------------------------
                    if (j == 1): # Orbital S
                       orbital = soma_orb[wp][1][point_k][Band_n]
                    #-------------------- lorbit = 10 ---------------------
                    if (j == 2 and lorbit == 10): # Orbital P
                       orbital = soma_orb[wp][2][point_k][Band_n]
                    if (j == 3 and lorbit == 10): # Orbital D
                       orbital = soma_orb[wp][3][point_k][Band_n]
                    #-------------------- lorbit >= 11 --------------------                     
                    if (j == 2 and lorbit >= 11): # Orbital P = Px + Py + Pz
                       orbital = soma_orb[wp][2][point_k][Band_n] + soma_orb[wp][3][point_k][Band_n] + soma_orb[wp][4][point_k][Band_n]
                    if (j == 3 and lorbit >= 11): # Orbital D = Dxy + Dyz + Dz2 + Dxz + Dx2
                       orbital = soma_orb[wp][5][point_k][Band_n] + soma_orb[wp][6][point_k][Band_n] + soma_orb[wp][7][point_k][Band_n] + soma_orb[wp][8][point_k][Band_n] + soma_orb[wp][9][point_k][Band_n]
                    #------------------------------------------------------
                    if (j == 4): # Orbital Px 
                       orbital = soma_orb[wp][4][point_k][Band_n]
                    if (j == 5): # Orbital Py 
                       orbital = soma_orb[wp][2][point_k][Band_n]
                    if (j == 6): # Orbital pz 
                       orbital = soma_orb[wp][3][point_k][Band_n]
                    #------------------------------------------------------
                    if (j == 7): # Orbital Dxy 
                       orbital = soma_orb[wp][5][point_k][Band_n]
                    if (j == 8): # Orbital Dyz 
                       orbital = soma_orb[wp][6][point_k][Band_n]
                    if (j == 9): # Orbital Dz2 
                       orbital = soma_orb[wp][7][point_k][Band_n]
                    if (j == 10): # Orbital Dxz 
                       orbital = soma_orb[wp][8][point_k][Band_n]
                    if (j == 11): # Orbital Dx2 
                       orbital = soma_orb[wp][9][point_k][Band_n]
                    #------------------------------------------------------                       
                    if (wp == 1 and point_k == 1 and Band_n == 1):    
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} 0.0 \n')
                    if (orbital > 0.0):    
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} {orbital} \n')
          
        projection.write(" \n")
       
# Plot da estrutura de Bandas =========================================
    
    for Band_n in range (1,(nb+1)):
        projection.write(" \n")
        for i in range (1,(n_procar+1)):
            for point_k in range (1,(nk+1)):
                projection.write(f'{xx[i][point_k]} {Energia[i][point_k][Band_n]} 0.0 \n')

# Destacando a energia de Fermi na estrutura de Bandas ================

    projection.write(" \n")
    projection.write(f'{xx[1][1]} 0.0 0.0 \n')
    projection.write(f'{xx[n_procar][nk]} 0.0 0.0 \n')

# Destacando pontos-k de interesse na estrutura de Bandas =============

    for loop in range (1,(contador2+1)):
        projection.write(" \n")
        projection.write(f'{dest_pk[loop]} {energ_min} 0.0 \n')
        projection.write(f'{dest_pk[loop]} {energ_max} 0.0 \n')

    #-----------------
    projection.close()
    #-----------------

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(".... Quase concluido ....")
print(".........................")
    

#======================================================================
#======================================================================
# Plot das Projeções dos Orbitais (Matplotlib) ========================
#====================================================================== 
#======================================================================

import matplotlib.pyplot as plt
import numpy as np

if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

for l in range (1,(loop+1)):     # Loop para a analise das Projecoes

    rx = [0]*(n_procar*nk*nb)
    ry = [0]*(n_procar*nk*nb)

    if (l == 1):
       s = 1; t = (3+1)
       S = [0]*(n_procar*nk*nb)
       P = [0]*(n_procar*nk*nb)
       D = [0]*(n_procar*nk*nb)
       
    if (l == 2):
       s = 4; t = (6+1)
       Px = [0]*(n_procar*nk*nb)
       Py = [0]*(n_procar*nk*nb)
       Pz = [0]*(n_procar*nk*nb)
       
    if (l == 3):
       s = 7; t = (11+1)  
       Dxy = [0]*(n_procar*nk*nb)
       Dyz = [0]*(n_procar*nk*nb)
       Dz2 = [0]*(n_procar*nk*nb)
       Dxz = [0]*(n_procar*nk*nb)
       Dx2 = [0]*(n_procar*nk*nb)
       
    fig, ax = plt.subplots()

    # Plot das Projeções ===================================================

    number = -1
    for k in range (1,(nb+1)):
        for i in range (1,(n_procar+1)):
            for j in range (1,(nk+1)):
                number += 1
                rx[number] = xx[i][j]
                ry[number] = Energia[i][j][k]

                if (l == 1):
                   S[number] = ((soma_orb[i][1][j][k])*(peso_total**0.5)*6)**2

                if (l == 1 and lorbit == 10):
                   P[number] = ((soma_orb[i][2][j][k])*(peso_total**0.5)*6)**2
                   D[number] = ((soma_orb[i][3][j][k])*(peso_total**0.5)*6)**2

                if (l == 1 and lorbit >= 11):
                   P[number] = ((soma_orb[i][2][j][k] + soma_orb[i][3][j][k] + soma_orb[i][4][j][k])*(peso_total**0.5)*6)**2
                   D[number] = ((soma_orb[i][5][j][k] + soma_orb[i][6][j][k] + soma_orb[i][7][j][k] + soma_orb[i][8][j][k] + soma_orb[i][9][j][k])*(peso_total**0.5)*6)**2                
                      
                if (l == 2):
                   Px[number] = ((soma_orb[i][4][j][k])*(peso_total**0.5)*6)**2
                   Py[number] = ((soma_orb[i][2][j][k])*(peso_total**0.5)*6)**2
                   Pz[number] = ((soma_orb[i][3][j][k])*(peso_total**0.5)*6)**2
                                         
                if (l == 3):
                   Dxy[number] = ((soma_orb[i][5][j][k])*(peso_total**0.5)*6)**2
                   Dyz[number] = ((soma_orb[i][6][j][k])*(peso_total**0.5)*6)**2
                   Dz2[number] = ((soma_orb[i][7][j][k])*(peso_total**0.5)*6)**2
                   Dxz[number] = ((soma_orb[i][8][j][k])*(peso_total**0.5)*6)**2
                   Dx2[number] = ((soma_orb[i][9][j][k])*(peso_total**0.5)*6)**2


    if (l == 1):
       ax.scatter(rx, ry, s = S, c = 'blue', alpha = 1.0, edgecolors = 'none', label = 'S')
       ax.scatter(rx, ry, s = P, c = 'red', alpha = 1.0, edgecolors = 'none', label = 'P')
       ax.scatter(rx, ry, s = D, c = 'limegreen', alpha = 1.0, edgecolors = 'none', label = 'D')

    if (l == 2):
       ax.scatter(rx, ry, s = Px, c = 'blue', alpha = 1.0, edgecolors = 'none', label = 'Px')
       ax.scatter(rx, ry, s = Py, c = 'red', alpha = 1.0, edgecolors = 'none', label = 'Py')
       ax.scatter(rx, ry, s = Pz, c = 'limegreen', alpha = 1.0, edgecolors = 'none', label = 'Pz')

    if (l == 3):
       ax.scatter(rx, ry, s = Dxy, c = 'blue', alpha = 1.0, edgecolors = 'none', label = 'Dxy')
       ax.scatter(rx, ry, s = Dyz, c = 'red', alpha = 1.0, edgecolors = 'none', label = 'Dyz')
       ax.scatter(rx, ry, s = Dz2, c = 'limegreen', alpha = 1.0, edgecolors = 'none', label = 'Dz2')
       ax.scatter(rx, ry, s = Dxz, c = 'rosybrown', alpha = 1.0, edgecolors = 'none', label = 'Dxz')
       ax.scatter(rx, ry, s = Dx2, c = 'magenta', alpha = 1.0, edgecolors = 'none', label = 'Dx2')

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
        plt.plot(x, y, color = 'black', linestyle = '-', linewidth = 0.25, alpha = 0.3)

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
    ax.legend(loc="upper right", title="")
    # ax.legend(loc="best", title="")

    if (l == 1): 
       plt.savefig('saida/Orbitais/Orbitais_S_P_D.png', dpi = 300)
       plt.savefig('saida/Orbitais/Orbitais_S_P_D.pdf', dpi = 300)
       # plt.savefig('saida/Orbitais/Orbitais_S_P_D.eps', dpi = 300)

    if (l == 2): 
       plt.savefig('saida/Orbitais/Orbitais_P.png', dpi = 300)
       plt.savefig('saida/Orbitais/Orbitais_P.pdf', dpi = 300)
       # plt.savefig('saida/Orbitais/Orbitais_P.eps', dpi = 300)

    if (l == 3): 
       plt.savefig('saida/Orbitais/Orbitais_D.png', dpi = 300)
       plt.savefig('saida/Orbitais/Orbitais_D.pdf', dpi = 300)
       # plt.savefig('saida/Orbitais/Orbitais_D.eps', dpi = 300)

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
