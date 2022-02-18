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

########################################################################
################## Configurações Gerais do VASProcar: ##################
########################################################################

#-----------------------------------------------------------------------
# Com relação ao parâmetro de rede, escolha: ---------------------------
#-----------------------------------------------------------------------
# [1] Utilizar o parâmetro informado no arquivo CONTCAR.
# [2] Adotar como parâmetro o menor valor entre os modulos dos vetores
#     primitivos da rede cristalina (A1, A2 e A3). 
#-----------------------------------------------------------------------
param_estim = 1

#-----------------------------------------------------------------------
# Com relação ao Plot dos Gráficos via Matplotlib, como deseja salvar? 
# Marque [0] para desabilitar ou [1] para habilitar o respectivo formato
#-----------------------------------------------------------------------
save_png = 1
save_pdf = 0
save_eps = 0
#-----------------------------------------------------------------------

#----------------------------------------------------------------------
# Cores utilizadas no plot das Projeções: (GRACE) ---------------------
#----------------------------------------------------------------------

# Obs.: Codigo das cores
# Branco  = 0,  Preto = 1, Vermelho = 2,  Verde   = 3,  Azul   = 4,  Amarelo = 5,  Marrom   = 6, Cinza = 7
# Violeta = 8,  Cyan  = 9, Magenta  = 10, Laranja = 11, Indigo = 12, Marron  = 13, Turquesa = 14
                                                                        
cor_spin = [1]*4   # Inicialização do vetor cor_spin
cor_orb  = [1]*12  # Inicialização do vetor cor_orb

                   # Valores padrão:
                   #------------------------------------------
cor_spin[1] = 1    # Cor da componente Nula do Spin (Preto)            
cor_spin[2] = 2    # Cor da componente Up do Spin   (Vermelho)         
cor_spin[3] = 4    # Cor da componente Down do Spin (Azul)
                   #------------------------------------------
cor_orb[1]  = 4    # Cor do Orbital S   (Azul)
cor_orb[2]  = 2    # Cor do Orbital P   (Vermelho)
cor_orb[3]  = 3    # Cor do Orbital D   (Verde)
cor_orb[4]  = 4    # Cor do Orbital Px  (Azul)
cor_orb[5]  = 2    # Cor do Orbital Py  (Vermelho)
cor_orb[6]  = 3    # Cor do Orbital Pz  (Verde)
cor_orb[7]  = 4    # Cor do Orbital Dxy (Azul)
cor_orb[8]  = 2    # Cor do Orbital Dyz (Vermelho)
cor_orb[9]  = 3    # Cor do Orbital Dz2 (Verde)
cor_orb[10] = 6    # Cor do Orbital Dxz (Marrom)
cor_orb[11] = 10   # Cor do Orbital Dx2 (Magenta)
                   #------------------------------------------
cor_A  = 4         # Cor da Região A (Azul)
cor_B  = 2         # Cor da Região B (Vermelho)
cor_C  = 3         # Cor da Região C (Verde)
cor_D  = 6         # Cor da Região D (Marrom)
cor_E  = 10        # Cor da Região E (Magenta)

#----------------------------------------------------------------------
# Dimensoes que definem as proporcões dos gráficos 2D: (GRACE) --------
#----------------------------------------------------------------------
                   # Valores padrão:
fig_xmin = 0.12    # 0.12
fig_xmax = 0.82    # 0.82
fig_ymin = 0.075   # 0.075
fig_ymax = 0.95    # 0.95

#----------------------------------------------------------------------
# Posição da legenda em relação ao gráfico: (GRACE) -------------------
#----------------------------------------------------------------------
                # Valores padrão:
leg_x = -0.11   # Dentro do gráfico: leg_x = -0.11   leg_y = -0.01
leg_y = -0.01   # Fora do gráfico:   leg_x = +0.025  leg_y = 0.0

#----------------------------------------------------------------------
# Verificando se a pasta saida existe, se não existe ela é criada -----
#----------------------------------------------------------------------
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

#----------------------------------------------------------------------
# Extraindo informações do calculo nos arquivos CONTCAR e PROCAR ------
#----------------------------------------------------------------------   

print ("##############################################################")
print ("# Obtendo informacoes da rede e do calculo efetuado: ======= #")
print ("##############################################################")
print (" ")
print (".........................")
print ("... Espere um momento ...")
print (".........................")
print (" ")

#-------------------------------------------
executavel = Diretorio + '/informacoes_b.py'
exec(open(executavel).read())
#-------------------------------------------

#-----------------------------------------------------------------------
# Obtenção dos parâmetros de input do código: --------------------------
#-----------------------------------------------------------------------

print ("##############################################################")
print ("################### O que deseja calcular? ###################")
print ("##############################################################")
print ("## Estrutura de Bandas (Plot 2D): ========================= ##")
print ("## [1]: Configuracao Padrao   --   [-1]: Personalizado      ##")
print ("## ======================================================== ##")
print ("## DOS, p-DOS e l-DOS (Plot 2D):                            ##")
print ("## [11]: Configuracao Padrao   --   [-11]: Personalizado    ##")
print ("## ======================================================== ##")
print ("## Potencial Eletrostatico em X,Y,Z (Plot 2D): ============ ##")
print ("## [12]: Configuracao Padrao   --   [-12]: Personalizado    ##")
print ("##############################################################")
print ("## Densidade de Carga Parcial em X,Y,Z (Plot 2D): ========= ##")
print ("## [13]: Configuracao Padrao   --   [-13]: Personalizado    ##")
print ("##############################################################")
print ("## Funcao de Onda em X,Y,Z (Plot 2D): ===================== ##")
print ("##           !!!!! EM TESTES - Nao Funcional !!!!!          ##")
print ("## [14]: Configuracao Padrao   --   [-14]: Personalizado    ##")
print ("##############################################################")
print ("## Projecao dos Orbitais S, P e D (Plot 2D): ============== ##")
print ("## [2]: Configuracao Padrao   --   [-2]: Personalizado      ##")
print ("##############################################################")
if (SO == 2):
   print ("## Projecao das Componentes de Spin Sx,Sy,Sz (Plot 2D): === ##")
   print ("## [3]: Configuracao Padrao   --   [-3]: Personalizado      ##")
   print ("##############################################################")
print ("## Contribuicao de Orbitais e ions nos estados: (Tabela) == ##")
print ("## [4]: Configuracao Padrao   --   [-4]: Personalizado      ##")
print ("##############################################################")
print ("## Projecao da Localizacao dos estados em regioes (Plot 2D) ##")
print ("## [5]: Configuracao Padrao   --   [-5]: Personalizado      ##")  
print ("##############################################################")
print ("## Banda 3D  ou  Banda 2D em 3D: (Plot 3D >> ki, kj, E)     ##")
print ("## [6] Padrao  --  [-6] Personalizado                       ##")
print ("## ======================================================== ##")
print ("## [61] Gerar arquivo KPOINTS (Plano 2D ou Malha 3D na ZB)  ##")
print ("## ======================================================== ##")
if (SO == 2):
   print ("## Projecao 2D da Textura de Spin 3D (Plot 2D)              ##")
   print ("##           !!!!! EM TESTES - Nao Funcional !!!!!          ##")
   print ("## [62] Padrao  --  [-62] Personalizado                     ##")    
print ("##############################################################")
print ("## ISOSUPERFICIES: (Plot 4D >> kx, ky, kz, E ou dE)         ##")
print ("## [7] Padrao  --  [-7] Personalizado                       ##")
print ("##############################################################")
print ("## [999] Efetuar verificacao e correcao de arquivos do VASP ##")
print ("##############################################################")

escolha = input (" "); escolha = int(escolha)
print(" ")

#----------------------------------------------------------------------
# Execução dos Códigos: -----------------------------------------------
#----------------------------------------------------------------------   

if (escolha == 1   or escolha == -1):   executavel = Diretorio + '/bandas_2D.py'  
if (escolha == 11  or escolha == -11):  executavel = Diretorio + '/dos_pdos_ldos.py'
if (escolha == 12  or escolha == -12):  executavel = Diretorio + '/potencial.py'
if (escolha == 13  or escolha == -13):  executavel = Diretorio + '/parchg.py'
if (escolha == 14  or escolha == -14):  executavel = Diretorio + '/WaveFunction.py'
if (escolha == 2   or escolha == -2):   executavel = Diretorio + '/projecao_orbitais.py' 
if (escolha == 3   or escolha == -3):   executavel = Diretorio + '/projecao_spin.py'  
if (escolha == 4   or escolha == -4):   executavel = Diretorio + '/contribuicao.py'  
if (escolha == 5   or escolha == -5):   executavel = Diretorio + '/localizacao.py'
if (escolha == 6   or escolha == -6):   executavel = Diretorio + '/bandas_3D.py'    
if (escolha == 61  or escolha == -61):  executavel = Diretorio + '/kpoints_malha_2D_3D.py'  
if (escolha == 62  or escolha == -62):  executavel = Diretorio + '/spin_texture_3D.py'   
if (escolha == 7   or escolha == -7):   executavel = Diretorio + '/bandas_4D.py'     
if (escolha == 999 or escolha == -999): executavel = Diretorio + '/correction_file.py'

#----------------------------
exec(open(executavel).read())   
#----------------------------

#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
