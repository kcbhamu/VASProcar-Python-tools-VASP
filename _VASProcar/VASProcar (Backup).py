print (" ")
print ("##############################################################################################")
print ("# Versao 1.0.1 (20/01/2022) ##################################################################")
print ("########################## Autores: ##########################################################")
print ("# Augusto de Lelis Araujo - Federal University of Uberlandia (Uberlandia/MG - Brazil) ########")
print ("# e-mail: augusto-lelis@outlook.com                                                   ########")
print ("# ========================================================================================== #")
print ("# Renan Maciel da Paixao - Uppsala University (Uppsala/Sweden) ###############################")
print ("# e-mail: renan.maciel@physics.uu.se                           ###############################")
print ("##############################################################################################")
print (" ")

import os

########################################################################
###### Forma de obtenção dos parâmetros de input do código: ############
###### [Leitura = 1] Os parâmetros são lidos de arquivos de input ######
###### [Leitura = 0] Os parâmetros são introduzidos pelo usuário #######
#################### durante a execução do código ######################
########################################################################

leitura = 0

#----------------------------------------------------------------------
# Cores utilizadas no plot das Projeções: -----------------------------
#----------------------------------------------------------------------

# Obs.: Codigo das cores
# Branco  = 0,  Preto = 1, Vermelho = 2,  Verde   = 3,  Azul   = 4,  Amarelo = 5,  Marrom   = 6, Cinza = 7
# Violeta = 8,  Cyan  = 9, Magenta  = 10, Laranja = 11, Indigo = 12, Marron  = 13, Turquesa = 14
                                                                        
cor = [1]*10  # Inicialização do vetor cor

              # Valores padrão:
cor[1] = 1    # Cor da componente Nula do Spin (Preto)            
cor[2] = 2    # Cor da componente Up do Spin   (Vermelho)         
cor[3] = 4    # Cor da componente Down do Spin (Azul)
cor[4] = 4    # Cor do Orbital S  (Azul)
cor[5] = 2    # Cor do Orbital P  (Vermelho)
cor[6] = 3    # Cor do Orbital D  (Verde)
cor[7] = 4    # Cor do Orbital Px (Azul)
cor[8] = 2    # Cor do Orbital Py (Vermelho)
cor[9] = 3    # Cor do Orbital Pz (Verde)

cor_A  = 4    # Cor da Região A (Azul)
cor_B  = 2    # Cor da Região B (Vermelho)
cor_C  = 3    # Cor da Região C (Verde)

#----------------------------------------------------------------------
# Coordenadas que definem as proporcões dos gráficos 2D: --------------
#----------------------------------------------------------------------
                   # Valores padrão:
fig_xmin = 0.1     # 0.1
fig_xmax = 0.8     # 0.8
fig_ymin = 0.075   # 0.075
fig_ymax = 0.95    # 0.95

#----------------------------------------------------------------
# Verificando se a pasta saida existe, se não existe ela é criada
#----------------------------------------------------------------
if os.path.isdir("saida"):
   0 == 0
else:
   os.mkdir("saida")
#-------------------

#----------------------------------------------------------------------
# Obtenção do nº de arquivos PROCAR a serem lidos: --------------------
#----------------------------------------------------------------------

n_procar = 0

try: f = open('PROCAR'); f.close(); n_procar = 1
except: 0 == 0

for i in range (1,100): 
    try: f = open('PROCAR.'+str(i)); f.close(); n_procar = i
    except: 0 == 0

#--------------------------------------------------------------    

print ("##############################################################")
print ("# Obtendo informações da rede e do calculo efetuado: ======= #")
print ("##############################################################")
print (" ")
print ("........................ ")
print ("... Espere um momento ...")
print (".........................")
print (" ")

#----------------------------------------------------------------------

exec(open("_VASProcar/informacoes.py").read())

if (leitura == 1):
   #-----------------------------------------------------------------------------------------------------
   # Verificando se a pasta input ou os arquivos de input existem, caso algum esteja ausente ele é criado
   #-----------------------------------------------------------------------------------------------------
   exec(open("_VASProcar/input.py").read())   

#----------------------------------------------------------------------
# Execução dos Códigos: -----------------------------------------------
#----------------------------------------------------------------------

if (leitura == 0):
   print ("##############################################################")
   print ("################### O que deseja calcular? ###################")
   print ("##############################################################")
   print ("## Estrutura de Bandas: =================================== ##")
   print ("## [1]: Configuracao Padrao   --   [-1]: Personalizado      ##")
   print ("##############################################################")
   print ("## Projecao dos Orbitais (S, P, D): ======================= ##")
   print ("## [2]: Configuracao Padrao   --   [-2]: Personalizado      ##")
   print ("##############################################################")
   if (SO == 2):
      print ("## Projecao das Componentes de Spin (Sx, Sy, Sz): ========= ##")
      print ("## [3]: Configuracao Padrao   --   [-3]: Personalizado      ##")
      print ("##############################################################")
   print ("## Contribuicao dos Orbitais e ions para os estados: ====== ##")
   print ("## [4]: Configuracao Padrao   --   [-4]: Personalizado      ##")
   print ("##############################################################")
   print ("## Projecao da Localizacao dos estados (Regioes A,B,C) ==== ##")
   print ("## [5]: Configuracao Padrao   --   [-5]: Personalizado      ##")  
   print ("##############################################################")
   print ("## Plot Bandas 3D ========================================= ##")
   print ("## [6] : Plot Banda 3D  ou  Plot Banda 2D em 3D             ##")
   print ("## [61]: Criar arquivo KPOINTS (Plano 2D na ZB)             ##")
   print ("## [62]: Criar arquivo KPOINTS (Malha 3D na ZB)             ##")   
   if (SO == 2):
      print ("## [63]: (Em Edição !!!) Projecao 2D da Textura de Spin 3D  ##")   
   print ("##############################################################")   

if (leitura == 1):
   print ("##############################################################")
   print ("################### O que deseja calcular? ###################")
   print ("## ======================== Digite ======================== ##")
   print ("##############################################################")
   print ("## [1] Estrutura de Bandas                                  ##")
   print ("## [2] Projecao dos Orbitais (S, P, D)                      ##")
   if (SO == 2):
      print ("## [3] Projecao das Componentes Spin (Sx, Sy, Sz)          ##")
   print ("## [4] Contribuicao dos Orbitais e ions para os estados     ##")
   print ("## [5] Proj. da Localizacao dos estados (Regioes A,B,C)     ##")
   print ("## [6] Plot Banda 3D  ou  Plot Banda 2D em 3D               ##")
   print ("## [61] Criar arquivo KPOINTS (Plano 2D na ZB)              ##")
   print ("## [62]: Criar arquivo KPOINTS (Malha 3D na ZB)             ##")   
   if (SO == 2):
      print ("## [63]: (Em Edição !!!) Projecao 2D da Textura de Spin 3D  ##")   
   print ("##############################################################")
   
escolha = input (" "); escolha = int(escolha)
print(" ")

if (escolha == 1 or escolha == -1):
   exec(open("_VASProcar/bandas.py").read())

if (escolha == 2 or escolha == -2):
   exec(open("_VASProcar/projecao_orbitais.py").read())

if (escolha == 3 or escolha == -3):
   exec(open("_VASProcar/projecao_spin.py").read())

if (escolha == 4 or escolha == -4):
   exec(open("_VASProcar/contribuicao.py").read())

if (escolha == 5 or escolha == -5):
   exec(open("_VASProcar/localizacao.py").read())

if (escolha == 6 or escolha == -6):
   exec(open("_VASProcar/bandas_3D.py").read())

if (escolha == 61 or escolha == -61):
   exec(open("_VASProcar/kpoints_plano_2D.py").read())

if (escolha == 62 or escolha == -62):
   exec(open("_VASProcar/kpoints_malha_3D.py").read())   

if (escolha == 63 or escolha == -63):
   exec(open("_VASProcar/spin_texture_3D.py").read())
   
############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################
