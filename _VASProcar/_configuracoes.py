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
print ("## [1] Estrutura de Bandas (Plot 2D, 3D ou isosuperficie):  ##")
print ("## ======================================================== ##")

if (SO == 2):
   print ("## Componentes de Spin Sx|Sy|Sz e Vetores SiSj | SxSySz:    ##")
   print ("## -------------------------------------------------------- ##")
   print ("## Plot 2D das Componentes Sx|Sy|Sz em [k-points, E(eV)]    ##")
   print ("## [2] Padrao   --   [-2] Personalizado                     ##")    
   print ("## -------------------------------------------------------- ##")
   print ("## Projecoes 2D|3D|Isosuperficie das Componentes Sx|Sy|Sz   ##")
   print ("## e dos vetores SiSj e SxSySz                              ##")
   print ("## [21] Padrao  --   [-21] Personalizado                    ##")    
   print ("## ======================================================== ##")

print ("## Projecao dos Orbitais S, P e D (Plot 2D):                ##")
print ("## [3]: Configuracao Padrao   --   [-3]: Personalizado      ##")
print ("## ======================================================== ##")
print ("## DOS, p-DOS e l-DOS (Plot 2D):                            ##")
print ("## [4]: Configuracao Padrao   --   [-4]: Personalizado      ##")
print ("## ======================================================== ##")
print ("## Projecao da Localizacao dos estados em regioes (Plot 2D) ##")
print ("## [5]: Configuracao Padrao   --   [-5]: Personalizado      ##")  
print ("## ======================================================== ##")
print ("## Contribuicao de Orbitais e ions nos estados (Tabela):    ##")
print ("## [6]: Configuracao Padrao   --   [-6]: Personalizado      ##")
print ("## ======================================================== ##")
print ("## Potencial Eletrostatico em X,Y,Z (Plot 2D):              ##")
print ("## [7]: Configuracao Padrao   --   [-7]: Personalizado      ##")
print ("## ======================================================== ##")
print ("## Densidade de Carga Parcial em X,Y,Z (Plot 2D):           ##")
print ("## [8]: Configuracao Padrao   --   [-8]: Personalizado      ##")
print ("## ======================================================== ##")
print ("##           !!!!! EM TESTES - Nao Funcional !!!!!          ##")
print ("## Funcao de Onda em X,Y,Z - Parte Real e Imag. (Plot 2D):  ##")
print ("## [9]: Configuracao Padrao   --   [-9]: Personalizado      ##")
print ("## ======================================================== ##")
print ("## [777] Gerar arquivo KPOINTS (Plano 2D ou Malha 3D na ZB) ##")
print ("## ======================================================== ##")
print ("## [888] Efetuar verificacao e correcao de arquivos do VASP ##")
print ("##############################################################")

escolha = input (" "); escolha = int(escolha)
print(" ")

#======================================================================

if (escolha == 1 or escolha == -1):
   print ("##############################################################")
   print ("###################### Escolha a opcao: ######################")
   print ("##############################################################")
   print ("## Plot 2D da Estrutura de Bandas: [k-points, E(eV)]        ##")
   print ("## [1] Padrao   --   [-1] Personalizado                     ##")
   print ("## ======================================================== ##")
   print ("## Plot 3D da Estrutura de Bandas: [ki, kj, E(eV)]          ##")
   print ("## [11] Padrao  --   [-11] Personalizado                    ##")
   print ("## ======================================================== ##")
   print ("## Isosuperficie das bandas: [kx, ky, kz, E(eV) ou dE(eV)]  ##")
   print ("## [12] Padrao  --   [-12] Personalizado                    ##")
   print ("##############################################################")
   escolha = input (" "); escolha = int(escolha)
   print(" ")

#----------------------------------------------------------------------
# Copiando arquivo para a pasta de saida: -----------------------------
#---------------------------------------------------------------------- 

import shutil

source = Diretorio + '/etc/BibTeX.dat'
destination = 'saida/BibTeX.dat'
shutil.copyfile(source, destination)

source = Diretorio + '/etc/DOI.png'
destination = 'saida/DOI.png'
shutil.copyfile(source, destination)

#----------------------------------------------------------------------
# Execução dos Códigos: -----------------------------------------------
#----------------------------------------------------------------------   

if (escolha == 1   or escolha == -1):   executavel = Diretorio + '/bandas_2D.py'
if (escolha == 11  or escolha == -11):  executavel = Diretorio + '/bandas_3D.py'
if (escolha == 12  or escolha == -12):  executavel = Diretorio + '/bandas_4D.py'
if (escolha == 2   or escolha == -2):   executavel = Diretorio + '/projecao_spin.py' 
if (escolha == 21  or escolha == -21):  executavel = Diretorio + '/spin_texture.py'
if (escolha == 3   or escolha == -3):   executavel = Diretorio + '/projecao_orbitais.py'
if (escolha == 4   or escolha == -4):   executavel = Diretorio + '/dos_pdos_ldos.py'
if (escolha == 5   or escolha == -5):   executavel = Diretorio + '/projecao_localizacao.py'
if (escolha == 6   or escolha == -6):   executavel = Diretorio + '/contribuicao.py'  
if (escolha == 7   or escolha == -7):   executavel = Diretorio + '/potencial.py'
if (escolha == 8   or escolha == -8):   executavel = Diretorio + '/parchg.py'
if (escolha == 9   or escolha == -9):   executavel = Diretorio + '/WaveFunction.py'  
if (escolha == 777 or escolha == -777): executavel = Diretorio + '/kpoints_malha_2D_3D.py'    
if (escolha == 888 or escolha == -888): executavel = Diretorio + '/correction_file.py'

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
