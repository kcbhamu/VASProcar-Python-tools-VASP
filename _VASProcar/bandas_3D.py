##############################################################
# Versao 1.001 (10/01/2022) ##################################
########################## Autores: ##########################
# Augusto de Lelis Araújo - INFIS/UFU (Uberlândia/MG) ########
# e-mail: augusto-lelis@outlook.com ##########################
# ---------------------------------------------------------- #
# Renan Maciel da Paixão - ????????????????????????????????? #
# e-mail: ?????????????????????.com ##########################
##############################################################

#---------------------------------------------
exec(open("_VASProcar/informacoes.py").read())
#---------------------------------------------
inform = open("saida/informacoes.txt", "a")
#------------------------------------------

#######################################################
########## Lendo os parâmetros de input ###############
#######################################################

# if (leitura == 0 and escolha == -6):
#    print ("##############################################################")
#    print ("############### Plot da Estrutura de Bandas 3D ###############")
#    print ("##############################################################") 
#    print ("Escolha a dimensao do eixo-k: ================================")
#    print ("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. =")
#    print ("Utilize 2 para k em unidades de 1/Angs. ======================")
#    print ("Utilize 3 para k em unidades de 1/nm. ========================")
#    print ("##############################################################") 
#    Dimensao = input (" "); Dimensao = int(Dimensao)
#    print (" ")

if (leitura == 0 and escolha == 6):
   Dimensao = 1

print ("##############################################################")
print ("Escolha as Bandas a serem Plotadas: ==========================")
print ("##############################################################") 
print ("Banda inicial: ===============================================")
Band_i = input (" "); Band_i = int(Band_i)
print (" ")
print ("Banda final: =================================================")
Band_f = input (" "); Band_f = int(Band_f)
print (" ")

###########################################################################

# if (leitura == 1):
#   #----------------------------------------------
#    entrada = open("input/input_bandas.txt", "r")
#   #----------------------------------------------
   
#    for i in range(6):
#        VTemp = entrada.readline()
#   Dimensao = int(VTemp)

#   #--------------
#   entrada.close()
#   #--------------

###########################################################################    

esc_b = 1                                      # Plotar todas as bandas (tanto com numeração par quanto com numeração ímpar) !!! REMOVER ESTA OPÇÃO DO CÓDIGO !!!
destacar_efermi = 1                            # Destacar o nível de fermi nos gráficos.
destacar_pontos_k = 1                          # Destacar pontos-k nos gráficos.

point_i = 1
point_f = nk

#-----------------------------------------------------------------

# Band_antes   = (Band_i  - 1)       # Bandas que nao serao plotadas.
# Band_depois  = (Band_f  + 1)       # Bandas que nao serao plotadas.
# point_antes  = (point_i - 1)       # K_points que nao serao plotados.
# point_depois = (point_f + 1)       # K_points que nao serao plotados.
# ion_antes  = (ion_i - 1)       # ions que nao serao analisados.
# ion_depois = (ion_f + 1)       # ions que nao serao analisados.

#-----------------------------------------------------------------

#*****************************************************************
# Dimensao = 1 >> k em unidades de 2pi/Param com Param em Angs. **
# Dimensao = 2 >> k em unidades de 1/Angs. ***********************
# Dimensao = 3 >> K em unidades de 1/nm **************************
#*****************************************************************

if (Dimensao == 1):
   fator_zb = 1.0

if (Dimensao == 2):
   fator_zb = (2*3.1415926535897932384626433832795)/Parametro

if (Dimensao == 3):
   fator_zb = (10*2*3.1415926535897932384626433832795)/Parametro

B1x = B1x*fator_zb
B1y = B1y*fator_zb
B1z = B1z*fator_zb
B2x = B2x*fator_zb
B2y = B2y*fator_zb
B2z = B2z*fator_zb
B3x = B3x*fator_zb
B3y = B3y*fator_zb
B3z = B3z*fator_zb

#-----------------------------------------------------------------

inform.write("***************************************************** \n")
inform.write("*********** Pontos-k na Zona de Brillouin *********** \n")
inform.write("***************************************************** \n")
inform.write(" \n")
      
if (Dimensao == 1):
   inform.write("Pontos-k |          Coord. Diretas M1, M2 e M3          |   Separacao (2Pi/Param) \n")
if (Dimensao == 2):
   inform.write("Pontos-k |          Coord. Diretas M1, M2 e M3          |   Separacao (1/Angs.) \n")
if (Dimensao == 3):
   inform.write("Pontos-k |          Coord. Diretas M1, M2 e M3          |   Separacao (1/nm) \n")

inform.write("         |          K =  M1*B1 + M2*B2 + M3*B3          | \n")
inform.write(" \n")

########################## Loop dos PROCAR #############################

wp = 0
n_point_k = 0
energ_max = -1000.0
energ_min = +1000.0

################# Inicialização de Vetores e Matrizes: #################
                                              
xx  = [[0]*(nk+1) for i in range(n_procar+1)]
kx  = [[0]*(nk+1) for i in range(n_procar+1)]
ky  = [[0]*(nk+1) for i in range(n_procar+1)]
kz  = [[0]*(nk+1) for i in range(n_procar+1)]
kb1 = [[0]*(nk+1) for i in range(n_procar+1)]
kb2 = [[0]*(nk+1) for i in range(n_procar+1)]
kb3 = [[0]*(nk+1) for i in range(n_procar+1)]
separacao = [[0]*(nk+1) for i in range(n_procar+1)]
y = [[[0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)]    

for wp in range(1, (n_procar+1)):

    if (wp == 1) and (n_procar == 1):
       procar = open("PROCAR", "r")
    if (wp == 1) and (n_procar != 1):
       procar = open("PROCAR.1", "r")
    if (wp == 2):
       procar = open("PROCAR.2", "r")
    if (wp == 3):
       procar = open("PROCAR.3", "r")
    if (wp == 4):
       procar = open("PROCAR.4", "r")
    if (wp == 5):
       procar = open("PROCAR.5", "r")
    if (wp == 6):
       procar = open("PROCAR.6", "r")
    if (wp == 7):
       procar = open("PROCAR.7", "r")
    if (wp == 8):
       procar = open("PROCAR.8", "r")
    if (wp == 9):
       procar = open("PROCAR.9", "r")
    if (wp == 10):
       procar = open("PROCAR.10", "r")

    for i in range(3):
        VTemp = procar.readline()
      
######################### Loop dos Pontos_k ###########################

    temp = 1.0; number = 0

    for point_k in range(1, (nk+1)):                                  

#######################################################################

        if (n_procar == 1 and point_k == 1):
           print("===========================")
           print("Analisando o arquivo PROCAR")
           print("===========================")

        if (n_procar > 1 and point_k == 1):
           print("==============================")
           print("Analisando o arquivo PROCAR",wp)
           print("==============================")          

#----------------------------------------------------------------------
# Calculando a porcentagem de leitura do arquivo PROCAR ---------------
#----------------------------------------------------------------------

        porc = (point_k/nk)*100        

        if (porc >= temp):
           print(f'Processado {porc:>3,.0f}%')                 
           number += 1
           if (number == 1):
              temp = 10.0
           if (number == 2):
              temp = 25.0
           if (number >= 3):
              temp = temp + 25.0
              
#----------------------------------------------------------------------               
                                                                      
        VTemp = procar.readline().split()                             # Observacao: No VASP k_b1, k_b2 e k_b3 correspondem as coordenadas diretas de cada ponto-k na ZB,                                                         
        k_b1 = float(VTemp[3])                                        # suas coordenadas cartesianas sao obtidas por meio das relacoes abaixo que nos fornecem kx = Coord_X,
        k_b2 = float(VTemp[4])                                        # ky = Coord_Y e kz = Coord_Z, entretanto, devemos nos lembrar que estas coordenadas kx, ky e kz estao 
        k_b3 = float(VTemp[5])                                        # em unidades de 2pi/Parametro.

        kb1[wp][point_k] = k_b1
        kb2[wp][point_k] = k_b2
        kb3[wp][point_k] = k_b3
        
        VTemp = procar.readline()

############### Distancia de separacao entre os pontos-k ##############

        Coord_X = ((k_b1*B1x) + (k_b2*B2x) + (k_b3*B3x))
        Coord_Y = ((k_b1*B1y) + (k_b2*B2y) + (k_b3*B3y))
        Coord_Z = ((k_b1*B1z) + (k_b2*B2z) + (k_b3*B3z))

        kx[wp][point_k] = Coord_X       
        ky[wp][point_k] = Coord_Y
        kz[wp][point_k] = Coord_Z   

        if (wp == 1) and (point_k == point_i):
           comp = 0.0
           xx[wp][point_k] = comp 

        if (wp != 1) or (point_k != point_i):
           delta_X = Coord_X_antes - Coord_X
           delta_Y = Coord_Y_antes - Coord_Y
           delta_Z = Coord_Z_antes - Coord_Z
           comp = (delta_X**2 + delta_Y**2 + delta_Z**2)**0.5
           comp = comp + comp_antes
           xx[wp][point_k] = comp

        # if (wp == 1) and (point_k == point_i):
           # comp = 0.0
           # xx[wp][point_k] = comp 

        # if (wp != 1) or (point_k != point_i):
           # delta_X = Coord_X_antes - Coord_X
           # delta_Y = Coord_Y_antes - Coord_Y
           # delta_Z = Coord_Z_antes - Coord_Z
           # comp = (delta_X**2 + delta_Y**2 + delta_Z**2)**0.5
           # comp = comp + comp_antes
           # xx[wp][point_k] = comp

        Coord_X_antes = Coord_X
        Coord_Y_antes = Coord_Y
        Coord_Z_antes = Coord_Z
        comp_antes = comp
        
        separacao[wp][point_k] = comp

        n_point_k = n_point_k + 1   

        inform.write(f'{n_point_k:>4}{k_b1:>19,.12f}{k_b2:>17,.12f}{k_b3:>17,.12f}{comp:>19,.14f} \n')

########################## Loop das Bandas ############################

        for Band_n in range (1, (nb+1)):

            if (esc_b == 1):
               Band_nn = float(Band_n)                                # Converte a variavel inteira (Band_n) para o tipo real.
               criterio_2 = (Band_n/1.0)
               int_crit_2 = int(criterio_2)                           # Retorna a parte inteira do numero real (criterio_2).
               resto_crit_2 = (criterio_2 % 1.0)                      # Retorna a parte fracionaria do numero real (criterio_2).

            if (esc_b != 1):
               Band_nn = float(Band_n)                                # Converte a variavel inteira (Band_n) para o tipo real.
               criterio_2 = (Band_n/2.0)
               int_crit_2 = int(criterio_2)                           # Retorna a parte inteira do numero real (criterio_2).
               resto_crit_2 = (criterio_2 % 1.0)                      # Retorna a parte fracionaria do numero real (criterio_2).

            if (esc_b == 1) or (esc_b == 2):
               rest = 0.0
               
            if (esc_b == 3):
               rest = 0.5

            if (resto_crit_2 == rest):
               VTemp = procar.readline().split()
               energ =  float(VTemp[4])

######################### Ajuste das energias #########################        

            if (wp == 1):                                             # y(1,1,1)                                      
               dE  = (Efermi)*(-1)
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 2):
               if (point_k == point_i) and (Band_n == Band_i):        # y(2,1,1)
                  dE  = y[1][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 3):
               if (point_k == point_i) and (Band_n == Band_i):        # y(3,1,1)
                  dE  = y[2][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 4):
               if (point_k == point_i) and (Band_n == Band_i):        # y(4,1,1)
                  dE  = y[3][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = float(energ) + flost(dE)
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 5):
               if (point_k == point_i) and (Band_n == Band_i):        # y(5,1,1)
                  dE  = y[4][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 6):
               if (point_k == point_i) and (Band_n == Band_i):        # y(6,1,1)
                  dE  = y[5][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 7):
               if (point_k == point_i) and (Band_n == Band_i):        # y(7,1,1)
                  dE  = y[6][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 8):
               if (point_k == point_i) and (Band_n == Band_i):        # y(8,1,1)
                  dE  = y[7][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 9):
               if (point_k == point_i) and (Band_n == Band_i):        # y(9,1,1)
                  dE  = y[8][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 10):
               if (point_k == point_i) and (Band_n == Band_i):        # y(10,1,1)
                  dE  = y[9][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

#######################################################################

            if (energ_max < auto_valor):                              # Calculo do maior auto-valor de energia.
               energ_max = auto_valor

            if (energ_min > auto_valor):                              # Calculo do menor auto-valor de energia.
               energ_min = auto_valor
              
            VTemp = procar.readline()
            VTemp = procar.readline()                 
            
############################ Loop dos ions #############################

#========================== Lendo os Orbitais ==========================

            for ion_n in range (1, (ni+1)):
                VTemp = procar.readline().split()            

            VTemp = procar.readline()

#=======================================================================
#========== Pulando as linhas referentes as componentes de Spin ========
#=======================================================================

            if (SO == 2):                                                          # Condicao para calculo com acoplamento Spin-orbita

               n_skip = (3*ni + 3)

               for ion_n in range (1, (n_skip+1)):
                   VTemp = procar.readline()          
 
#============= Pulando as linhas referente a fase (LORBIT 12) ==========

            if (lorbit == 12):
               temp2 = ((2*ni) + 2)
               for i in range (1, (temp2 + 1)):
                   VTemp = procar.readline()

            if (lorbit != 12):
               VTemp = procar.readline()

            #-----------------------------------------------------------------------
            # Fim do laço/loop dos ions --------------------------------------------
            #-----------------------------------------------------------------------                  
                  
        #-----------------------------------------------------------------------
        # Fim do laço/loop das bandas ------------------------------------------
        #-----------------------------------------------------------------------

#================== Ignorar linhas ao final de cada ponto-k ============

        if (point_k < nk):
           VTemp = procar.readline()
        
    #-----------------------------------------------------------------------
    # Fim do laço/loop dos pontos-k ----------------------------------------
    #-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Fim do laço/loop dos procar ------------------------------------------
#-----------------------------------------------------------------------

#=============== Fim da escrita do arquivo "informacoes.txt" ===========

inform.write(" \n")

if (Dimensao == 1):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao (2Pi/Param) \n")
   inform.write("         |                  (2Pi/Param)                 | \n")
if (Dimensao == 2):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao (1/Angs.) \n")
   inform.write("         |                   (1/Angs.)                  | \n")
if (Dimensao == 3):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao (1/nm) \n")
   inform.write("         |                    (1/nm)                    | \n")
 
inform.write(" \n")

n_point_k = 0

for i in range (1,(n_procar+1)):
    for j in range (1, (nk+1)):
        n_point_k += 1
        inform.write(f'{n_point_k:>4}{kx[i][j]:>19,.12f}{ky[i][j]:>17,.12f}{kz[i][j]:>17,.12f}{separacao[i][j]:>19,.14f} \n')
        
inform.close()

#=======================================================================

#-------------
procar.close()
#-------------
    
########### Arquivo para o Plot 3D da Estrutura de Bandas: ############

#-------------------------------------
bandas_3D = open("saida/Bandas_3D.dat", "w")
#-------------------------------------
    
# for Band_n in range (Band_i,(Band_f+1)):
    # bandas_3D.write(" \n")
#     for j in range (1,(n_procar+1)):
#         for point_k in range (1,(nk+1)):
#             if (Band_n == 4):
#                bandas_3D.write(f'{kb1[j][point_k]} {kb2[j][point_k]} {kb3[j][point_k]} {y[j][point_k][Band_n]} \n')

for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        bandas_3D.write(f'{kb1[j][point_k]} ')
        bandas_3D.write(f'{kb2[j][point_k]} ')
        bandas_3D.write(f'{kb3[j][point_k]} ')
        for Band_n in range (Band_i,(Band_f+1)):
            bandas_3D.write(f'{y[j][point_k][Band_n]} ')
        bandas_3D.write("\n")

# print (" ".join([function(Word) for Word in split]))
               
#----------------
bandas_3D.close()
#----------------

#---------------------------------------------
exec(open("_VASProcar/plot_bandas_3D.py").read())
#---------------------------------------------

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################
