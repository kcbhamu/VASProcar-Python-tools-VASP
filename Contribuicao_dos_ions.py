
print ("")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print ("Versao 2.001 (23/01/2018) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print ("Autor: Augusto de Lelis Araújo - INFIS/UFU (Uberlândia/MG)")
print ("e-mail: augusto-lelis@outlook.com %%%%%%%%%%%%%%%%%%%%%%%%")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print ("")



############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### BLOCO 1: OBTENÇÃO DE INFORMAÇÕES DO SISTEMA ########################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################



print ("#######################################################")
print ("############ Lendo o arquivo de input #################")
print ("#######################################################")
print ("")

################################################

entrada = open("input_Contribuicao_ions.txt", "r")

for i in range(7):
    VTemp = entrada.readline()
Band_i = int(VTemp)                            # Banda inicial a ser analisada.

for i in range(3):
    VTemp = entrada.readline()
Band_f = int(VTemp)                            # Banda final a ser analisada.

for i in range(3):
    VTemp = entrada.readline()
point_i = int(VTemp)                            # Ponto-k inicial a ser analisada.

for i in range(3):
    VTemp = entrada.readline()
point_f = int(VTemp)                            # Ponto-k final a ser analisada.

entrada.close()

################################################

Band_antes   = (Band_i  -1)                    # Bandas que não serão analisadas
Band_depois  = (Band_f  +1)                    # Bandas que não serão analisadas
point_antes  = (point_i -1)                    # Pontos-k que não serão analisados
point_depois = (point_f +1)                    # Pontos-k que não serão analisados

################################################

print ("#######################################################")
print ("########## Analisando o arquivo OUTCAR ################")
print ("######## Buscando informacoes do Sistema ##############")
print ("#######################################################")
print ("")

outcar = open("OUTCAR", "r")

################################################

palavra = 'Dimension'                          # Dimension e uma palavra presente em uma linha anterior as linhas que contem a informacao sobre o número de pontos-k (nk), bandas (nb) e ions (ni).

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
nk = int(VTemp[3])
nb = int(VTemp[14])

VTemp = outcar.readline().split()
ni = int(VTemp[11])

#-----------------------------------------------------------------------
# Verificacao se o calculo foi realizado com ou sem o acoplamento SO
#-----------------------------------------------------------------------

palavra = 'ICHARG'                             # ICHARG e uma palavra presente em uma linha anterior a linha que contem a informacao sobre a variavel ISPIN.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
ispin = int(VTemp[2])                          # Leitura do valor associado a variavel ISPIN.


if ispin == 2:
   print ("--------------------------------------------------------")
   print ("--------------------------------------------------------")
   print ("Este programa não foi compilado para analisar um cálculo")
   print ("com polarização de Spin (ISPIN = 2)")
   print ("********************************************************")
   print ("Modifique o códifo fonte, ou refaça seu cálculo")
   print ("********************************************************")
   print ("--------------------------------------------------------")
   print ("--------------------------------------------------------")
   
################################################

palavra = 'LNONCOLLINEAR'                      # LNONCOLLINEAR e uma palavra presente em uma linha anterior a linha que contem a informacao sobre a variavel LSORBIT.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
lsorbit = VTemp[2]                             # Leitura do valor associado a variavel LSORBIT.

if (lsorbit == "F"):
   SO = 1
if (lsorbit == "T"):
   SO = 2

#-----------------------------------------------------------------------
# Verificacao do numero de eletrons do sistema.
#----------------------------------------------------------------------- 
 
palavra = 'VCA'                                # VCA e uma palavra presente em uma linha anterior a linha que contem a informacao sobre a variavel NELECT.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
n_eletrons = float(VTemp[2])                          # Leitura do valor associado a variavel NELECT.

#-----------------------------------------------------------------------
# Verificacao do LORBIT utilizado para a geracao do arquivo PROCAR.
#-----------------------------------------------------------------------
 
palavra = 'LELF'                               # LELF e uma palavra presenta em uma linha anterior a linha que contem a informacao sobre a variavel LORBIT.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
lorbit = int(VTemp[2])                              # Leitura do valor associado a variavel LORBIT.

#-----------------------------------------------

outcar.close() 

#-----------------------------------------------------------------------
# Obtendo os rótulos dos ions presentes no arquivo CONTCAR.
#-----------------------------------------------------------------------

contcar = open("contcar", "r")

for i in range(6):
    VTemp = contcar.readline().split() 
types = len(VTemp)                                                     # Obtenção do número de diferentes tipos de ions que compoem a rede.

#----------------------------------------------

label = [0]*(types+1)
ion_label = [0]*(ni+1)
rotulo = [0]*(ni+1)
rotulo_temp = [0]*(ni+1)

#----------------------------------------------

for i in range (1,(types+1)):
    label[i] = VTemp[(i-1)]                                            # Obtenção dos rótulos/abreviações que rotulam cada tipo de ion da rede.

VTemp = contcar.readline().split()                                    

for i in range (1,(types+1)):            
    ion_label[i] = int(VTemp[(i-1)])                                   # Obtenção do número de ions correspondentes a cada rótulo/abreviação.

contcar.close()

#----------------------------------------------

contador = 0

for i in range (1,(types+1)):
    number = ion_label[i]
    for j in range (1,(number+1)):
        contador += 1
        rotulo[contador] = label[i]

        

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### BLOCO 2: EXTRAÇÃO DOS RESULTADOS ###################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################



print ("")
print ("Rodando: ##############################################")
print ("####### Rodando: ######################################")
print ("############### Rodando: ##############################")
print ("####################### Rodando: ######################")
print ("############################### Rodando: ##############")
print ("####################################### Rodando: ######")
print ("############################################## Rodando:")
print ("")
print ("")

#-----------------------------------------------------------------------

contribuicao = open("Contribuicao_dos_ions.txt", "w")
procar = open("PROCAR", "r")

#-----------------------------------------------------------------------

atomo = [0]*(ni+1)
tot = [0]*(ni+1)

for i in range(3):
    VTemp = procar.readline()
      
######################## Loop dos Pontos_k ############################
                                                                      
for point_k in range(1, (nk+1)):                                     

    if (point_k > point_antes and point_k < point_depois):            # Criterio para definir quais pontos-k serão analisados.            

        VTemp = procar.readline().split()
        k_b1 = float(VTemp[3])
        k_b2 = float(VTemp[4])
        k_b3 = float(VTemp[5]) 
        VTemp = procar.readline()

        print(f'Analisando o ponto-k {point_k}')

        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  \n")
        contribuicao.write(f'Ponto-k {point_k}: Coord. Diretas ({k_b1}, {k_b2}, {k_b3}) \n')
        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  \n")
        contribuicao.write(" \n")

########################## Loop das Bandas ############################

        for Band_n in range (1, (nb+1)):

            if (point_k == point_f and Band_n == Band_depois):        # Criterio para interromper a execução do programa.
               break

            if (Band_n > Band_antes and Band_n < Band_depois):        # Criterio para definir quais bandas serão analisadas.

               if (Band_n == Band_i):
                  contribuicao.write("===========================================================  \n")
                   
               contribuicao.write(f'Banda {Band_n} \n')
               contribuicao.write("===========================================================  \n")

               for i in range(3):
                   VTemp = procar.readline()

               orb_total = 0.0
               soma = 0.0                   
            
############################ Loop dos ions #############################

#====================== Lendo o Orbital Total ==========================

               for ion_n in range (1, (ni+1)):
                   atomo[ion_n] = ion_n
                   if (lorbit >= 11):
                      VTemp = procar.readline().split()
                      ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                      dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); total = float(VTemp[10])
                   if (lorbit == 10):
                      VTemp = procar.readline().split() 
                      ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); total = float(VTemp[4])
                   tot[ion_n] = total
                   orb_total = orb_total + total               

#-----------------------------------------------------------------------

               for j in range (1,(ni+1)):
                   rotulo_temp[j] = rotulo[j]

               nj = (ni - 1)
               
               for k in range (1,(nj+1)):
                   w = (ni - k)
                   for l in range (1,(w+1)):
                       if (tot[l] < tot[l+1]):
                          tp1 = tot[l]
                          tot[l] = tot[l+1]
                          tot[l+1] = tp1                        
                          #--------------------
                          tp2 = atomo[l]
                          atomo[l] = atomo[l+1]
                          atomo[l+1] = tp2                   
                          #--------------------
                          tp4 = rotulo_temp[l]
                          rotulo_temp[l] = rotulo_temp[l+1]
                          rotulo_temp[l+1] = tp4                          

               for ion_n in range (1,(ni+1)):
                   tot[ion_n] = (tot[ion_n]/orb_total)*100
                   soma = soma + tot[ion_n]                

                   contribuicao.write(f'{rotulo_temp[ion_n]:>2}: ion {atomo[ion_n]:<3} | Contribuicao: {tot[ion_n]:>6,.3f}% | Soma: {soma:>7,.3f}% \n')

               VTemp = procar.readline()                              # Pulando a linha que contém a soma do S_total de todos os ions

               if (SO == 2):                                          # Condição para cálculo com acoplamento Spin-àrbita
                  #-----------------------------
                  for ion_n in range (1,(ni+1)):
                      VTemp = procar.readline()
                  VTemp = procar.readline()                           # Pulando a linha que contém a soma do Sx de todos os ions
                  #-----------------------------
                  for ion_n in range (1,(ni+1)):
                      VTemp = procar.readline()
                  VTemp = procar.readline()                           # Pulando a linha que contém a soma do Sy de todos os ions
                  #-----------------------------
                  for ion_n in range (1,(ni+1)):
                      VTemp = procar.readline()
                  VTemp = procar.readline()                           # Pulando a linha que contém a soma do Sz de todos os ions                    
                  #-----------------------------

#============ Pulando as linhas referente a fase (LORBIT 12) =========

               if (lorbit == 12):
                  temp2 = ((2*ni)+2)
                  for i in range (1,(temp2+1)):
                      VTemp = procar.readline()
               if (lorbit != 12):
                  VTemp = procar.readline()

               if (Band_n < (Band_f+1)):
                  contribuicao.write("=========================================================== \n")
                  contribuicao.write(" \n")

#=================== Bandas excluidas do cálculo =====================

            if (Band_n <= Band_antes or Band_n >= Band_depois):       # Continuação do if que regula as Bandas que serão plotadas ou não.

               if (lorbit == 12):                                     # Válido somente para LORBIT = 12
                  if (SO == 1):                                       # Para cálculo sem acoplamento Spin-órbita.
                     temp3 = (6 + 3*ni)
                  if (SO == 2):                                       # Para cálculo com acoplamento Spin-órbita.
                     temp3 = (9 + 6*ni)
              
               if (lorbit != 12):                                     # Válido somente para LORBIT = 1O ou 11
                  if (SO == 1):                                       # Para cálculo sem acoplamento Spin-órbita.
                     temp3 = (5 + ni)
                  if (SO == 2):                                       # Para cálculo com acoplamento Spin-órbita.
                     temp3 = (8 + 4*ni)
          
               for i in range (1,(temp3+1)):                          # Esta parte do código pula/exclui as Bandas de energia em cada ponto-K, 
                   VTemp = procar.readline()                          # que não foram selecionadas para serem plotadas             
          
         #------------------------
         # Fim do loop das Bandas.
         #------------------------
        
#================== Ignorar linha ao final de cada K-point =============

        if (point_k < nk):
           VTemp = procar.readline()
       
#==================== K_points excluídos do cálculo ====================

    if (point_k <= point_antes or point_k >= point_depois):            # Continuação do if que regula os K_points que serão analisados ou não.

       if (lorbit == 12):                                              # Válido somente para LORBIT = 12
          if (SO == 1):                                                
              temp3 = ((6 + 3*ni)*nb + 3)                              # Para cálculo sem acoplamento Spin-órbita.
          if (SO == 2):
              temp3 = ((9 + 6*ni)*nb + 3)                              # Para cálculo com acoplamento Spin-órbita.
            
       if (lorbit != 12):                                              # Válido somente para LORBIT = 10 ou 11
          if (SO == 1):             
             temp3 = ((5 + ni)*nb + 3)                                 # Para cálculo sem acoplamento Spin-órbita.
          if (SO == 2):        
             temp3 = ((8 + 4*ni)*nb + 3)                               # Para cálculo com acoplamento Spin-órbita.
            
       for i in range (1,(temp3+1)):                                   # Esta parte do código pula/exclui os K_points que não foram selecionados para serem plotados.
           VTemp = procar.readline()          
            
#--------------------------
# Fim do loop dos K_points.
#--------------------------

procar.close()
contribuicao.close()

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################

