##############################################################
# Versao 1.001 (10/01/2022) ##################################
########################## Autores: ##########################
# Augusto de Lelis Araújo - INFIS/UFU (Uberlândia/MG) ########
# e-mail: augusto-lelis@outlook.com ##########################
# ---------------------------------------------------------- #
# Renan Maciel da Paixão - ????????????????????????????????? #
# e-mail: ?????????????????????.com ##########################
##############################################################

#----------------------------------------------------------------------
#  Continuação da escrita do arquivo informacoes.txt ---------------
#----------------------------------------------------------------------

#---------------------------------------------
exec(open("_VASProcar/informacoes.py").read())
#---------------------------------------------
inform = open("saida/informacoes.txt", "a")
#------------------------------------------

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

#----------------------------------------------------------------------

inform.write("***************************************************** \n")
inform.write("*********** Pontos-k na Zona de Brillouin *********** \n")
inform.write("***************************************************** \n")
inform.write(" \n")
      
if (Dimensao == 1):
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |   Separacao (2Pi/Param) \n")
if (Dimensao == 2):
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |   Separacao (1/Angs.) \n")
if (Dimensao == 3):
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |   Separacao (1/nm) \n")

inform.write("         |          K =  k1*B1 + k2*B2 + k3*B3          | \n")
inform.write(" \n")

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------

n_point_k = 0
energ_max = -1000.0
energ_min = +1000.0
                                              
xx = [[0]*(nk+1) for i in range(n_procar+1)]         # xx[n_procar][nk]
kx = [[0]*(nk+1) for i in range(n_procar+1)]         # kx[n_procar][nk]
ky = [[0]*(nk+1) for i in range(n_procar+1)]         # ky[n_procar][nk]
kz = [[0]*(nk+1) for i in range(n_procar+1)]         # kz[n_procar][nk]
separacao = [[0]*(nk+1) for i in range(n_procar+1)]  # separacao[n_procar][nk]

y = [[[0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)]  # separacao[n_procar][nk][nb]

if (lorbit != 10): 
   orb = [[[[[0]*(ni+1) for i in range(nb+1)] for j in range(nk+1)] for k in range(n_procar+1)] for l in range(9+1)]  # orb[9][n_procar][nk][nb][ni]

if (lorbit == 10): 
   orb = [[[[[0]*(ni+1) for i in range(nb+1)] for j in range(nk+1)] for k in range(n_procar+1)] for l in range(3+1)]  # orb[3][n_procar][nk][nb][ni]

#  orb[1][n_procar][nk][nb][ni] = Orbital S
#  orb[2][n_procar][nk][nb][ni] = Orbital Py ou P (lorbit = 10)
#  orb[3][n_procar][nk][nb][ni] = Orbital Pz ou D (lorbit = 10)
#  orb[4][n_procar][nk][nb][ni] = Orbital Px
#  orb[5][n_procar][nk][nb][ni] = Orbital Dxy
#  orb[6][n_procar][nk][nb][ni] = Orbital Dyz
#  orb[7][n_procar][nk][nb][ni] = Orbital Dz2
#  orb[8][n_procar][nk][nb][ni] = Orbital Dxz
#  orb[9][n_procar][nk][nb][ni] = Orbital Dx2

if (SO == 2):
   Sx = [[[[[0]*(ni+1) for i in range(nb+1)] for j in range(nk+1)] for k in range(n_procar+1)] for l in range(9+1)]  # Sx[9][n_procar][nk][nb][ni]
   Sy = [[[[[0]*(ni+1) for i in range(nb+1)] for j in range(nk+1)] for k in range(n_procar+1)] for l in range(9+1)]  # Sy[9][n_procar][nk][nb][ni]
   Sz = [[[[[0]*(ni+1) for i in range(nb+1)] for j in range(nk+1)] for k in range(n_procar+1)] for l in range(9+1)]  # Sz[9][n_procar][nk][nb][ni]

#----------------------------------------------------------------------

#######################################################################
########################### Loop dos PROCAR ###########################
#######################################################################

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
      
#######################################################################
########################## Loop dos Pontos_k ##########################
#######################################################################
        
    temp = 1.0; number = 0

    for point_k in range(1, (nk+1)):                                  

#----------------------------------------------------------------------

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
# Leitura das coordenadas k1, k2 e k3 de cada ponto-k -----------------
#---------------------------------------------------------------------- 
                                                                      
        VTemp = procar.readline().split()                           # Observacao: No VASP k1, k2 e k3 correspondem as coordenadas diretas de cada ponto-k na ZB, ou seja                                                         
        k1 = float(VTemp[3])                                        # K = (k1*B1 + k2*B2 + k3*b3), suas coordenadas cartesianas sao obtidas por meio das relacoes abaixo
        k2 = float(VTemp[4])                                        # que nos fornecem kx = Coord_X, ky = Coord_Y e kz = Coord_Z, entretanto, devemos nos lembrar que  
        k3 = float(VTemp[5])                                        # estas coordenadas kx, ky e kz estao em unidades de 2pi/Parametro.
        
        VTemp = procar.readline()

#----------------------------------------------------------------------
# Obtenção da distancia de separacao entre os pontos-k ----------------
#----------------------------------------------------------------------

        Coord_X = ((k1*B1x) + (k2*B2x) + (k3*B3x))
        Coord_Y = ((k1*B1y) + (k2*B2y) + (k3*B3y))
        Coord_Z = ((k1*B1z) + (k2*B2z) + (k3*B3z))

        kx[wp][point_k] = Coord_X       
        ky[wp][point_k] = Coord_Y
        kz[wp][point_k] = Coord_Z   

        if (wp == 1) and (point_k == 1):
           comp = 0.0
           xx[wp][point_k] = comp 

        if (wp != 1) or (point_k != 1):
           delta_X = Coord_X_antes - Coord_X
           delta_Y = Coord_Y_antes - Coord_Y
           delta_Z = Coord_Z_antes - Coord_Z
           comp = (delta_X**2 + delta_Y**2 + delta_Z**2)**0.5
           comp = comp + comp_antes
           xx[wp][point_k] = comp

        Coord_X_antes = Coord_X
        Coord_Y_antes = Coord_Y
        Coord_Z_antes = Coord_Z
        comp_antes = comp
        
        separacao[wp][point_k] = comp

        n_point_k = n_point_k + 1   

        inform.write(f'{n_point_k:>4}{k1:>19,.12f}{k2:>17,.12f}{k3:>17,.12f}{comp:>19,.14f} \n')

#######################################################################
########################### Loop dos Bandas ###########################
#######################################################################

        for Band_n in range (1, (nb+1)):

            VTemp = procar.readline().split()
            energ =  float(VTemp[4])

#----------------------------------------------------------------------
# Ajuste das energias para múltiplos arquivos PROCAR ------------------
#----------------------------------------------------------------------        

            if (wp == 1):                                             # y(1,1,1)                                      
               dE  = (Efermi)*(-1)
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 2):
               if (point_k == 1) and (Band_n == 1):        # y(2,1,1)
                  dE  = y[1][nk][1] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 3):
               if (point_k == 1) and (Band_n == 1):        # y(3,1,1)
                  dE  = y[2][nk][1] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 4):
               if (point_k == 1) and (Band_n == 1):        # y(4,1,1)
                  dE  = y[3][nk][1] - energ
               y[wp][point_k][Band_n] = float(energ) + float(dE)
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 5):
               if (point_k == 1) and (Band_n == 1):        # y(5,1,1)
                  dE  = y[4][nk][1] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 6):
               if (point_k == 1) and (Band_n == 1):        # y(6,1,1)
                  dE  = y[5][nk][1] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 7):
               if (point_k == 1) and (Band_n == 1):        # y(7,1,1)
                  dE  = y[6][nk][1] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 8):
               if (point_k == 1) and (Band_n == 1):        # y(8,1,1)
                  dE  = y[7][nk][1] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 9):
               if (point_k == 1) and (Band_n == 1):        # y(9,1,1)
                  dE  = y[8][nk][1] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 10):
               if (point_k == 1) and (Band_n == 1):        # y(10,1,1)
                  dE  = y[9][nk][1] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

#----------------------------------------------------------------------

            if (energ_max < auto_valor):                              # Calculo do maior auto-valor de energia.
               energ_max = auto_valor

            if (energ_min > auto_valor):                              # Calculo do menor auto-valor de energia.
               energ_min = auto_valor
              
            VTemp = procar.readline()
            VTemp = procar.readline()               
            
#######################################################################
############################ Loop dos ions ############################
#######################################################################

#======================================================================
#========================== Lendo os Orbitais =========================
#======================================================================

            for ion_n in range (1, (ni+1)):

#----------------------------------------------------------------------
                
                if (lorbit >= 11):
                   VTemp = procar.readline().split()
                   # ion = int(VTemp[0])               
                   for i in range(1,(9+1)):
                       orb[i][n_procar][point_k][Band_n][ion_n] = float(VTemp[i])
                   # tot = float(VTemp[10])
                     
                if (lorbit == 10):
                   VTemp = procar.readline().split() 
                   # ion = int(VTemp[0])
                   for i in range(1,(3+1)):
                       orb[i][n_procar][point_k][Band_n][ion_n] = float(VTemp[i])
                   # tot = float(VTemp[4])

            VTemp = procar.readline()
           
#======================================================================
#============ Analisando as componentes Sx, Sy e Sz do Spin ===========
#======================================================================

            if (SO == 2):                                                          # Condicao para calculo com acoplamento Spin-orbita
            
#======================================================================
#==================== Lendo a componente Sx do Spin ===================
#======================================================================

               for ion_n in range (1, (ni+1)):

#----------------------------------------------------------------------

                   if (lorbit >= 11):
                      VTemp = procar.readline().split()
                      # ion = int(VTemp[0])
                      for i in range(1,(9+1)):
                          Sx[i][n_procar][point_k][Band_n][ion_n] = float(VTemp[i])
                      # totsx = float(VTemp[10])                                                   

                   if (lorbit == 10):
                      VTemp = procar.readline().split() 
                      # ion = int(VTemp[0])
                      for i in range(1,(3+1)):
                          Sx[i][n_procar][point_k][Band_n][ion_n] = float(VTemp[i])
                      # totsx = float(VTemp[4]) 

#----------------------------------------------------------------------

               VTemp = procar.readline()
               
#======================================================================
#==================== Lendo a componente Sy do Spin ===================
#======================================================================

               for ion_n in range (1, (ni+1)):

#----------------------------------------------------------------------

                   if (lorbit >= 11):
                      VTemp = procar.readline().split()
                      # ion = int(VTemp[0])
                      for i in range(1,(9+1)):
                          Sy[i][n_procar][point_k][Band_n][ion_n] = float(VTemp[i])
                      # totsx = float(VTemp[10])                                                   

                   if (lorbit == 10):
                      VTemp = procar.readline().split() 
                      # ion = int(VTemp[0])
                      for i in range(1,(3+1)):
                          Sy[i][n_procar][point_k][Band_n][ion_n] = float(VTemp[i])
                      # totsx = float(VTemp[4]) 

#----------------------------------------------------------------------

               VTemp = procar.readline()

#======================================================================
#==================== Lendo a componente Sz do Spin ===================
#======================================================================            

               for ion_n in range (1, (ni+1)):

#----------------------------------------------------------------------

                   if (lorbit >= 11):
                      VTemp = procar.readline().split()
                      # ion = int(VTemp[0])
                      for i in range(1,(9+1)):
                          Sz[i][n_procar][point_k][Band_n][ion_n] = float(VTemp[i])
                      # totsx = float(VTemp[10])                                                   

                   if (lorbit == 10):
                      VTemp = procar.readline().split() 
                      # ion = int(VTemp[0])
                      for i in range(1,(3+1)):
                          Sz[i][n_procar][point_k][Band_n][ion_n] = float(VTemp[i])
                      # totsx = float(VTemp[4]) 

#----------------------------------------------------------------------

               VTemp = procar.readline()          

#----------------------------------------------------------------------
# Pulando as linhas referente a fase (LORBIT 12) ----------------------
#---------------------------------------------------------------------- 
 
#=========== Pulando as linhas referente a fase (LORBIT 12) ===========

            if (lorbit == 12):
               temp2 = ((2*ni) + 2)
               for i in range (1, (temp2 + 1)):
                   VTemp = procar.readline()

            if (lorbit != 12):
               VTemp = procar.readline()

            #######################################################################
            ######################### Fim do Loop dos ions ########################
            #######################################################################                
                  
        #######################################################################
        ######################## Fim do Loop das Bandas #######################
        #######################################################################

#----------------------------------------------------------------------
# Ignorando a linha ao final de cada ponto-k --------------------------
#---------------------------------------------------------------------- 

        if (point_k < nk):
           VTemp = procar.readline()
        
    #######################################################################
    ####################### Fim do Loop dos pontos-k ######################
    #######################################################################

    #-------------
    procar.close()
    #-------------

#######################################################################
################### Fim do Loop dos arquivos PROCAR ###################
#######################################################################

#----------------------------------------------------------------------
# Fim da escrita do arquivo "informacoes.txt" -------------------------
#---------------------------------------------------------------------- 

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

#-------------
inform.close()
#-------------

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################