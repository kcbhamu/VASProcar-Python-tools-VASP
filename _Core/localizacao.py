##############################################################
# Versao 1.001 (10/01/2022) ##################################
########################## Autores: ##########################
# Augusto de Lelis Araújo - INFIS/UFU (Uberlândia/MG) ########
# e-mail: augusto-lelis@outlook.com ##########################
# ---------------------------------------------------------- #
# Renan Maciel da Paixão - ????????????????????????????????? #
# e-mail: ?????????????????????.com ##########################
##############################################################

#----------------------------------------
exec(open("_Core/informacoes.py").read())
#----------------------------------------
inform = open("saida/informacoes.txt", "a")
#------------------------------------------

if os.path.isdir("temp"):
   0 == 0
else:
   os.mkdir("temp")

#######################################################
########## Lendo os parâmetros de input ###############
#######################################################  

ABC = [0]*(ni+1)            # Inicilização do vetor ABC

for i in range (1,(ni+1)):  # Por padrão todos os ions pertencem a Região C
    ABC[i] = "C"

print ("##############################################################")
print ("################## Localizacao dos Estados ###################")
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
print ("Defina as regioes (A, B, C) a serem destacadas na projecao: ==")
print ("Agora defina os ions que compoem as regioes a serem destacadas")
print ("Por padrao todos os ions pertencem a Regiao C ================")
print ("==============================================================")
print ("Quantos intervalos de ions ira fornecer abaixo? ==============")
print ("##############################################################")
loop = input (" "); loop = int(loop)
print(" ")

for i in range (1,(loop+1)):
    print (f'{i} intervalo: ==============================================')
    print ("Digite o ion inicial do intervalo ============================")
    loop_i = input (" "); loop_i = int(loop_i)
    print ("Digite o ion final do intervalo ==============================")
    loop_f = input (" "); loop_f = int(loop_f)
    print ("Qual a letra (A, B ou C) que rotula a Regiao do intervalo ====")
    loop_cha = input (" ")
    if (loop_cha == "a"):
       loop_cha = "A"
    if (loop_cha == "b"):
       loop_cha = "B"
    if (loop_cha == "c"):
       loop_cha = "C"   
    print(" ")     

    if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
       print ("")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       print ("   ERRO: Os valores de ions informados estao incorretos   ")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       print ("")
    for j in range (loop_i, (loop_f+1)):
        ABC[j] = loop_cha  

#-------------
esc = 0
esc_b = 1
destacar_efermi = 1
destacar_pontos_k = 1

#-------------
if (esc == 0):
   Band_i = 1                                                          # Banda inicial a ser Plotada.
   Band_f = nb                                                         # Banda final a ser Plotada.
   point_i = 1                                                         # Ponto-k inicial a ser Plotado.
   point_f = nk                                                        # Ponto-k final a ser Plotado.

nbb = (Band_f - Band_i) + 1
      
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

#-----------------------------------------------------------------------

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

#-----------------------------------------------------------------------
temp = open("temp/Temp.txt", "w")
contribuicao = open("saida/Contribuicao_Regioes.txt", "w")
#-----------------------------------------------------------------------

########################## Loop dos PROCAR #############################

n_point_k = 0
energ = 0.0
Band_antes  = (Band_i - 1)                                             # Bandas que nao serao plotadas.
Band_depois = (Band_f + 1)                                             # Bandas que nao serao plotadas.
energ_max = -1000.0
energ_min = +1000.0

################# Inicialização de Vetores e Matrizes: #################
                                              
xx = [[0]*(nk+1) for i in range(n_procar+1)]
kx = [[0]*(nk+1) for i in range(n_procar+1)]
ky = [[0]*(nk+1) for i in range(n_procar+1)]
kz = [[0]*(nk+1) for i in range(n_procar+1)]
separacao = [[0]*(nk+1) for i in range(n_procar+1)]
y = [[[0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)]
atomo = [0]*(ni+1)
Contrib = [0]*(ni+1)
Reg = [0]*(ni+1)
u = [0]*4

#----------------------------------------------------------------------

for wp in range (1,(n_procar+1)):
      
    contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
    contribuicao.write(f'PROCAR {wp} \n')
    contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
    contribuicao.write(" \n")

    if (wp == 1 and n_procar == 1):
       procar = open("PROCAR", "r") 
    if (wp == 1 and n_procar != 1):
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
      
######################## Loop dos Pontos_k ############################
                                                                      # Observacao: No VASP k_b1, k_b2 e k_b3 correspondem as coordenadas diretas de cada ponto-k na ZB, 
    for point_k in range(1, (nk+1)):                                  # suas coordenadas cartesianas sao obtidas por meio das relacoes abaixo que nos fornecem kx = Coord_X, 
                                                                      # ky = Coord_Y e kz = Coord_Z, entretanto, devemos nos lembrar que estas coordenadas kx, ky e kz estao 
        VTemp = procar.readline().split()                             # em unidades de 2pi/Parametro.
        k_b1 = float(VTemp[3])
        k_b2 = float(VTemp[4])
        k_b3 = float(VTemp[5]) 
        
        VTemp = procar.readline()

#---------------------------------------------------------------------

        if (n_procar == 1):
           print("Analisando o Ponto_k",point_k)

        if (n_procar > 1):
           print("Analisando o Ponto_k",point_k,"do PROCAR",wp)

        if (point_k == nk):
           print(" ")
           print("=========================================================")        

#---------------------------------------------------------------------
        
        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contribuicao.write(f'K_Point {point_k} \n')
        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contribuicao.write(" \n")      
      
################ Distancia de separacao entre os pontos-k ##############

        Coord_X = ((k_b1*B1x) + (k_b2*B2x) + (k_b3*B3x))
        Coord_Y = ((k_b1*B1y) + (k_b2*B2y) + (k_b3*B3y))
        Coord_Z = ((k_b1*B1z) + (k_b2*B2z) + (k_b3*B3z))

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

        inform.write(f'{n_point_k:>4}{k_b1:>19,.12f}{k_b2:>17,.12f}{k_b3:>17,.12f}{comp:>19,.14f} \n')

########################### Loop das Bandas ############################

        for Band_n in range (1, (nb+1)):

            Band_nn = float(Band_n)                                    # Converte a variavel inteira (Band_n) para o tipo real.

            if (esc_b == 1):
               criterio_2 = (Band_n/1.0)

            if (esc_b != 1):
               criterio_2 = (Band_n/2.0)

            int_crit_2 = int(criterio_2)                               # Retorna a parte inteira do numero real (criterio_2).
            resto_crit_2 = (criterio_2 % 1.0)                          # Retorna a parte fracionaria do numero real (criterio_2).
          
            if (esc_b == 1) or (esc_b == 2):                           # (esc_b == 1) Condicao para plotar/analisar todas as bandas (pares e impares).
               rest = 0.0                                              # (esc_b == 2) Condicao para plotar/analisar somente as bandas pares.
               
            if (esc_b == 3):
               rest = 0.5                                              # (esc_b == 3) Condicao para plotar/analisar somente as bandas impares.

            if (Band_n > Band_antes and Band_n < Band_depois and resto_crit_2 == rest):
               VTemp = procar.readline().split()
               energ =  float(VTemp[4])
            
            if (Band_n == Band_i):
               contribuicao.write("================================================================= \n")

            contribuicao.write(f'Banda {Band_n} \n')
            contribuicao.write("================================================================= \n")

########################## Ajuste das energias #########################

            if (wp == 1):                                              # y(1,1,1)                                 
               dE  = (Efermi)*(-1)
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 2):
               if (point_k == point_i) and (Band_n == Band_i):         # y(2,1,1)
                  dE  = y[1][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 3):
               if (point_k == point_i) and (Band_n == Band_i):         # y(3,1,1)
                  dE  = y[2][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 4):
               if (point_k == point_i) and (Band_n == Band_i):         # y(4,1,1)
                  dE  = y[3][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = float(energ) + flost(dE)
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 5):
               if (point_k == point_i) and (Band_n == Band_i):         # y(5,1,1)
                  dE  = y[4][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 6):
               if (point_k == point_i) and (Band_n == Band_i):         # y(6,1,1)
                  dE  = y[5][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 7):
               if (point_k == point_i) and (Band_n == Band_i):         # y(7,1,1)
                  dE  = y[6][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 8):
               if (point_k == point_i) and (Band_n == Band_i):         # y(8,1,1)
                  dE  = y[7][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 9):
               if (point_k == point_i) and (Band_n == Band_i):         # y(9,1,1)
                  dE  = y[8][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 10):
               if (point_k == point_i) and (Band_n == Band_i):         # y(10,1,1)
                  dE  = y[9][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

########################################################################

            if (energ_max < auto_valor):                               # Calculo do maior auto-valor de energia.
               energ_max = auto_valor

            if (energ_min > auto_valor):                               # Calculo do menor auto-valor de energia.
               energ_min = auto_valor
              
            VTemp = procar.readline()
            VTemp = procar.readline()  
          
            orb_total = 0.0
            Lado_A = 0.0
            Lado_B = 0.0
            Centro = 0.0
            Prop_A = 0.0
            Prop_B = 0.0
            Prop_C = 0.0
            Soma = 0.0
            Soma_A = 0.0
            Soma_B = 0.0
            Soma_C = 0.0
            
############################ Loop dos ions #############################

#====================== Lendo o Orbital Total ==========================

            for ion_n in range (1, (ni+1)):
                atomo[ion_n] = ion_n
                temp_sm = ABC[ion_n]
                Reg[ion_n] = ABC[ion_n]

                if (temp_sm == "A"):
                   if (lorbit >= 11):
                      VTemp = procar.readline().split()
                      ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                      dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); tot = float(VTemp[10])
                   if (lorbit == 10):
                      VTemp = procar.readline().split() 
                      ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); tot = float(VTemp[4])
                   #-----------------------------
                   Lado_A = Lado_A + tot
                   orb_total = orb_total + tot
                   Contrib[ion_n] = tot
                   Soma_A = Soma_A + Contrib[ion_n]

                if (temp_sm == "B"):
                   if (lorbit >= 11):
                       VTemp = procar.readline().split()
                       ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                       dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); tot = float(VTemp[10])
                   if (lorbit == 10):
                       VTemp = procar.readline().split() 
                       ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); tot = float(VTemp[4])
                   #-----------------------------
                   Lado_B = Lado_B + tot
                   orb_total = orb_total + tot
                   Contrib[ion_n] = tot
                   Soma_B = Soma_B + Contrib[ion_n]

                if (temp_sm == "C"):
                   if (lorbit >= 11):
                       VTemp = procar.readline().split()
                       ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                       dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); tot = float(VTemp[10])
                   if (lorbit == 10):
                       VTemp = procar.readline().split() 
                       ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); tot = float(VTemp[4])
                   #-----------------------------
                   Centro = Centro + tot
                   orb_total = orb_total + tot
                   Contrib[ion_n] = tot
                   Soma_C = Soma_C + Contrib[ion_n]

#-----------------------------------------------------------------------

            peso_inicial = 0.0

            if (orb_total != 0.0):
               Prop_A = ((Lado_A/orb_total) + peso_inicial)*peso_total
               Prop_B = ((Lado_B/orb_total) + peso_inicial)*peso_total
               Prop_C = ((Centro/orb_total) + peso_inicial)*peso_total
            if (orb_total == 0.0):
               Prop_A = 0.0
               Prop_B = 0.0

            temp.write(f'{comp} {auto_valor} {Prop_A} {Prop_B} {Prop_C} \n')
      
#-----------------------------------------------------------------------
            if (orb_total != 0.0):
               Soma_A = (Soma_A/orb_total)*100
               Soma_B = (Soma_B/orb_total)*100
               Soma_C = (Soma_C/orb_total)*100
            if (orb_total == 0.0):
               Soma_A = 0.0
               Soma_B = 0.0
               Soma_C = 0.0

            contribuicao.write(f'Regiao A = {Soma_A:7,.3f}% \n')
            contribuicao.write(f'Regiao B = {Soma_B:7,.3f}% \n')
            contribuicao.write(f'Regiao C = {Soma_C:7,.3f}% \n')
            contribuicao.write("=================== \n")
            
#-----------------------------------------------------------------------

            for j in range (1,(ni+1)):
               rotulo_temp[j] = rotulo[j]

            nj = (ni - 1)
                     
            for k in range (1,(nj+1)):
                wy = (ni - k)
                for l in range (1,(wy+1)):
                    if (Contrib[l] < Contrib[l+1]):
                     tp1 = Contrib[l]
                     Contrib[l] = Contrib[l+1]
                     Contrib[l+1] = tp1
                     #--------------------
                     tp2 = atomo[l]
                     atomo[l] = atomo[l+1]
                     atomo[l+1] = tp2
                     #--------------------                    
                     tp3 = Reg[l]
                     Reg[l] = Reg[l+1]
                     Reg[l+1] = tp3
                     #--------------------
                     tp4 = rotulo_temp[l]
                     rotulo_temp[l] = rotulo_temp[l+1]
                     rotulo_temp[l+1] = tp4                     

            for ion_n in range (1,(ni+1)):
                Contrib[ion_n] = (Contrib[ion_n]/orb_total)*100
                Soma = Soma + Contrib[ion_n]
                
                if (Reg[ion_n] == "A"):
                   palavra = "(Regiao A)"
                if (Reg[ion_n] == "B"):
                   palavra = "(Regiao B)"
                if (Reg[ion_n] == "C"):
                   palavra = "(Regiao C)"

                contribuicao.write(f'{rotulo_temp[ion_n]:>2}: ion {atomo[ion_n]:<3} | Contribuicao: {Contrib[ion_n]:6,.3f}% | Soma: {Soma:>7,.3f}% | {palavra} \n')

            contribuicao.write(" \n")

#-----------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%% Analisandos os Orbitais %%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            VTemp = procar.readline()

#***********************************************************************
#     Condicao para calculo com acoplamento Spin-Orbita.
#***********************************************************************

            if (SO == 2):
#================================ Sx ===================================

               for ion_n in range (1, (ni+1)):
                   VTemp = procar.readline()

               VTemp = procar.readline()

#================================ Sy ===================================

               for ion_n in range (1, (ni+1)):
                   VTemp = procar.readline()

               VTemp = procar.readline()

#================================ Sz ===================================

               for ion_n in range (1, (ni+1)):
                   VTemp = procar.readline()

               VTemp = procar.readline()


#============= Pulando as linhas referente a fase (LORBIT 12) ==========

            if (lorbit == 12):
               temp2 = ((2*ni) + 2)
               for i in range (1, (temp2 + 1)):
                   VTemp = procar.readline()

            if (lorbit != 12):
               VTemp = procar.readline()
              
            if (Band_n < Band_f):
               contribuicao.write("================================================================= \n")

#==================== Bandas excluidas do calculo ======================

            if (Band_n <= Band_antes and Band_n >= Band_depois and resto_crit_2 == rest): # Continuacao do if que regula as Bandas que serao plotadas ou nao.          

               if (lorbit == 12):                                      # Valido somente para LORBIT = 12.
                  if (SO == 1):                                        # Para calculo sem acoplamento Spin-Orbita.
                     temp3 = 6 + 3*ni
                  if (SO == 2):                                        # Para calculo com acoplamento Spin-Orbita.
                     temp3 = 9 + 6*ni

               if (lorbit != 12):                                      # Valido somente para LORBIT = 1O ou 11.
                  if (SO == 1):                                        # Para calculo sem acoplamento Spin-Orbita.
                     temp3 = 5 + ni
                  if (SO == 2):                                        # Para calculo com acoplamento Spin-Orbita.
                     temp3 = 8 + 4*ni

               for i in range (1,(temp3+1)):                           # Esta parte do codigo pula/exclui as Bandas de energia em cada ponto K, que nao foram selecionadas para serem plotadas.
                   VTemp = procar.readline()                               

#================== Ignorar linhas ao final de cada K point ============

        if (point_k < nk):
            VTemp = procar.readline()

        
    #-----------------------------------------------------------------------
    # Fim do laço/loop dos pontos-k ----------------------------------------
    #-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Fim do laço/loop dos procar ------------------------------------------
#-----------------------------------------------------------------------

   #--------------
    procar.close()
   #--------------

#-----------    
temp.close()
contribuicao.close()
#-------------------

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
        
#-------------
inform.close()
#-------------

#========== ! Obtendo os pontos-k a serem destacados nos gráficos ======

#------------------------------------
inform = open("saida/informacoes.txt", "r")
#------------------------------------

if (SO == 1):
   for i in range (1, (39+1)):
       VTemp = inform.readline()

if (SO == 2):
   for i in range (1, (46+1)):
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

################## Parametros para ajustes dos Graficos ################

x_inicial = xx[1][1]
x_final   = xx[n_procar][point_f]
y_inicial = energ_min
y_final   = energ_max

# Parametros que ajustam os contornos do grafico: ######################

# delta_xi = ((xx(point_f))/100)*2.5                                   # Aumenta ou diminui a distancia do grafico com relacao a borda Esquerda.
# delta_xf = delta_xi                                                  # Aumenta ou diminui a distancia do grafico com relacao a borda Direita.
# delta_yi = (sqrt(((energ_max - energ_min)/100)**2))*2.5              # Aumenta ou diminui a distancia do grafico com relacao a borda Inferior.
# delta_yf = delta_yi                                                  # Aumenta ou diminui a distancia do grafico com relacao a borda Superior.

# x_inicial = x_inicial - delta_xi
# x_final   = x_final   + delta_xf
# y_inicial = y_inicial - delta_yi
# y_final   = y_final   + delta

################## Plot das Projeções da Localização: ##################

########################################################################
################## Agora sera escrito o arquivo de saida ###############
########################################################################

localizacao = open("saida/Localizacao__estados.agr", "w")

######## Plot da Localizacao no arquivo "Localizacao_dos_estados.agr" ##

localizacao.write("# Grace project file \n")
localizacao.write("# \n")
localizacao.write("@version 50122 \n")
localizacao.write("@with string \n")
localizacao.write("@    string on \n")
localizacao.write("@    string 0.1, 0.96 \n")
localizacao.write(f'@    string def "E(eV)" \n')
localizacao.write("@with string \n")
localizacao.write("@    string on \n")

if (Dimensao == 1):
   localizacao.write("@    string 0.66, 0.017 \n")
   localizacao.write(f'@    string def "(2pi/Param.)" \n')
if (Dimensao == 2):
   localizacao.write("@    string 0.70, 0.017 \n")
   localizacao.write(f'@    string def "(1/Angs.)" \n')
if (Dimensao == 3):
   localizacao.write("@    string 0.73, 0.017 \n")
   localizacao.write(f'@    string def "(1/nm)" \n')

localizacao.write("@with g0 \n")
localizacao.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
localizacao.write("@    view 0.1, 0.075, 0.8, 0.95 \n")

escala_x = (x_final - x_inicial)/5
escala_y = (y_final - y_inicial)/5

localizacao.write(f'@    xaxis  tick major {escala_x:.2f} \n')
localizacao.write(f'@    yaxis  tick major {escala_y:.2f} \n')

# Obs.: Codigo das cores
# Codigo de cores para a localizacao dos estados nas regioes A, B e C
# Branco=0, Preto=1, Vermelho=2, Verde=3, Azul=4, Amarelo=5, Marrom=6, Cinza=7
# Violeta=8, Cyan=9, Magenta=10, Laranja=11, Indigo=12, Marron=13, Turquesa=14

cor_A = 4
cor_B = 2
cor_C = 3

for i in range (1,(3+1)):
    if (i == 1):
       grac='s0'; color = cor_A
    if (i == 2):
       grac='s1'; color = cor_B
    if (i == 3):
       grac='s2'; color = cor_C

    localizacao.write(f'@    {grac} type xysize \n')
    localizacao.write(f'@    {grac} symbol 1 \n')
    localizacao.write(f'@    {grac} symbol color {color} \n')
    localizacao.write(f'@    {grac} symbol fill color {color} \n')
    localizacao.write(f'@    {grac} symbol fill pattern 1 \n')
    localizacao.write(f'@    {grac} line type 0 \n')
    localizacao.write(f'@    {grac} line color {color} \n')

localizacao.write("@type xysize \n")
# localizacao.write(" \n")

#-----------------------------------------------------------------------

wm = 1
wn = 3

for t in range (wm,(wn+1)):

    if (t == 1):
       print (" ")
       print ("Analisando a Localizacao dos Estados (Regiao A)")
    if (t == 2):
       print (" ")
       print ("Analisando a Localizacao dos Estados (Regiao B)")
    if (t == 3):
       print (" ")
       print ("Analisando a Localizacao dos Estados (Regiao C)")

#-----------------------------------------------------------------------
    num_tot = n_procar*(nk*nbb)
#-----------------------------------------------------------------------

    temp = open("temp/Temp.txt", "r")

#-----------------------------------------------------------------------

    for j in range (1,(num_tot+1)):
        VTemp = temp.readline().split()
        cp = float(VTemp[0]); av = float(VTemp[1]); u[1] = float(VTemp[2]); u[2] = float(VTemp[3]); u[3] = float(VTemp[4]);   
        localizacao.write(f'{cp} {av} {u[t]} \n')

    localizacao.write(" \n")

    temp.close()

###################### Plot da Estrutura de Bandas ######################

for Band_n in range (Band_i,(Band_f+1)):
    localizacao.write(" \n")
    for i in range (1,(n_procar+1)):
        for point_k in range (1,(nk+1)):
            localizacao.write(f'{xx[i][point_k]} {y[i][point_k][Band_n]} 0.0 \n')

# Destacando a Energia de Fermi na Estrutura de Bandas.
      
if (destacar_efermi == 1):
   localizacao.write(" \n")
   localizacao.write(f'{xx[1][1]} 0.0 0.0 \n')
   localizacao.write(f'{xx[n_procar][nk]} 0.0 0.0 \n')

# Destacando pontos-k de interesse na estrutura de Bandas.

if (destacar_pontos_k == 1):
   for loop in range (1,(contador2+1)):
       localizacao.write(" \n")
       localizacao.write(f'{dest_pk[loop]} {energ_min} 0.0 \n')
       localizacao.write(f'{dest_pk[loop]} {energ_max} 0.0 \n')

# Destacando alguns pontos-K de interesse, na Estrutura de Bandas.

if (n_procar > 1):
   wr = n_procar + 1
   for loop in range (1,(wr+1)):
       localizacao.write(" \n")
       if (loop != wr):
          localizacao.write(f'{xx[loop][1]} {energ_min} 0.0 \n')
          localizacao.write(f'{xx[loop][1]} {energ_max} 0.0 \n')
       if (loop == wr):
          localizacao.write(f'{xx[n_procar][nk]} {energ_min} 0.0 \n')
          localizacao.write(f'{xx[n_procar][nk]} {energ_max} 0.0 \n')

#-----------------------------------------------------------------------
localizacao.close()
#-----------------------------------------------------------------------

################ Excluindo o arquivo temporario gerado #################

os.remove("temp/Temp.txt")
os.rmdir("temp")

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

