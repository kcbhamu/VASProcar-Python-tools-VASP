##############################################################
# Versao 1.001 (10/01/2022) ##################################
########################## Autores: ##########################
# Augusto de Lelis Araújo - INFIS/UFU (Uberlândia/MG) ########
# e-mail: augusto-lelis@outlook.com ##########################
# ---------------------------------------------------------- #
# Renan Maciel da Paixão - ????????????????????????????????? #
# e-mail: ?????????????????????.com ##########################
##############################################################

import os

#------------------------------------------------------------------------------------------------------
# Verificando se a pasta _input ou os arquivos de input existem, caso algum esteja ausente ele é criado
#------------------------------------------------------------------------------------------------------
# exec(open("_Core/input.py").read())   
#----------------------------------

#----------------------------------------------------------------
# Verificando se a pasta saida existe, se não existe ela é criada
#----------------------------------------------------------------
if os.path.isdir("saida"):
   0 == 0
else:
   os.mkdir("saida")
#-------------------   

#----------------------------------------------------------------------
# Cores utilizadas no plot das Projeções: -----------------------------
#----------------------------------------------------------------------

# Obs.: Codigo das cores
# Branco  = 0,  Preto = 1, Vermelho = 2,  Verde   = 3,  Azul   = 4,  Amarelo = 5,  Marrom   = 6, Cinza = 7
# Violeta = 8,  Cyan  = 9, Magenta  = 10, Laranja = 11, Indigo = 12, Marron  = 13, Turquesa = 14
                                                                        
cor = [1]*10   # Inicialização do vetor cor

cor[1] = 1    # Cor da componente Nula do Spin (Preto)            
cor[2] = 2    # Cor da componente Up do Spin   (Vermelho)         
cor[3] = 4    # Cor da componente Down do Spin (Azul)
cor[4] = 4    # Cor do Orbital S (Azul)
cor[5] = 2    # Cor do Orbital P (Vermelho)
cor[6] = 3    # Cor do Orbital D (Verde)
cor[7] = 4    # Cor do Orbital Px (Azul)
cor[8] = 2    # Cor do Orbital Py (Vermelho)
cor[9] = 3    # Cor do Orbital Pz (Verde)

#----------------------------------------------------------------------
# Obtenção do nº de arquivos PROCAR: ----------------------------------
#----------------------------------------------------------------------

try: f = open('PROCAR'); f.close(); n_procar = 1
except: 0 == 0
try: f = open('PROCAR.1'); f.close(); n_procar = 1
except: 0 == 0
try: f = open('PROCAR.2'); f.close(); n_procar = 2
except: 0 == 0
try: f = open('PROCAR.3'); f.close(); n_procar = 3
except: 0 == 0
try: f = open('PROCAR.4'); f.close(); n_procar = 4
except: 0 == 0
try: f = open('PROCAR.5'); f.close(); n_procar = 5
except: 0 == 0
try: f = open('PROCAR.6'); f.close(); n_procar = 6
except: 0 == 0
try: f = open('PROCAR.7'); f.close(); n_procar = 7
except: 0 == 0
try: f = open('PROCAR.8'); f.close(); n_procar = 8
except: 0 == 0
try: f = open('PROCAR.9'); f.close(); n_procar = 9
except: 0 == 0
try: f = open('PROCAR.10'); f.close(); n_procar = 10
except: 0 == 0

#----------------------------------------------------------------------
# Execução dos Códigos: -----------------------------------------------
#----------------------------------------------------------------------

exec(open("_Core/informacoes.py").read())

print ("##############################################################")
print ("################### O que deseja calcular? ###################")
print ("##############################################################")
print ("Digite [1]: Estrutura de Bandas ==============================")
print ("Digite [2]: Projecao dos Orbitais (S, P, D) ==================")
if (SO == 2):
   print ("Digite [3]: Projecao das Componentes de Spin (Sx, Sy, Sz) =")
print ("Digite [4]: Contribuicao dos Orbitais e ions para os estados =")
print ("Digite [5]: Projecao da Localizacao dos estados ==============")
print ("Digite [?]: Em Breve =========================================")
print ("##############################################################")
escolha = input (" "); escolha = int(escolha)
print(" ")

if (escolha == 1):
   exec(open("_Core/bandas.py").read())

if (escolha == 2):
   exec(open("_Core/projecao_orbitais.py").read())

if (escolha == 3):
   exec(open("_Core/projecao_spin.py").read())

if (escolha == 4):
   exec(open("_Core/contribuicao.py").read())

if (escolha == 5):
   exec(open("_Core/localizacao.py").read())














