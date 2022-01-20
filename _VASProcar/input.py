#########################################################################################
## Versao 1.0.1 (20/01/2022) ############################################################
########################### Autores: ####################################################
## Augusto de Lelis Araujo - Federal University of Uberlandia (Uberlandia/MG - Brazil) ##
## e-mail: augusto-lelis@outlook.com                                                   ##
## =================================================================================== ##
## Renan Maciel da Paixao - Uppsala University (Uppsala/Sweden) #########################
## e-mail: renan.maciel@physics.uu.se                           #########################
#########################################################################################

import os

########### Verificando se a pasta _input e os arquivos de input existem: ###########

if os.path.isdir("input"):
   #------------------------------------------------------------------------
   try: f = open('input/input_bandas.txt'); f.close(); input_Bandas = 1
   except: input_Bandas = 0   
   #------------------------------------------------------------------------
   try: f = open('input/input_projecoes.txt'); f.close(); input_Projecoes = 1
   except: input_Projecoes = 0
   #------------------------------------------------------------------------------
   try: f = open('input/input_localizacao.txt'); f.close(); input_Localizacao = 1
   except: input_Localizacao = 0       
   #--------------------------------------------------------------------------------
   try: f = open('input/input_contribuicao.txt'); f.close(); input_Contribuicao = 1
   except: input_Contribuicao = 0
        
else:
   #-----------------
   os.mkdir("input")
   
   tag = 0
   input_Bandas = 0
   input_Projecoes = 0
   input_Localizacao = 0
   input_Contribuicao = 0
   
############## Gerando qualquer arquivo de input que esteja faltando: ##############

if (input_Bandas == 0):
   entrada = open("input/input_bandas.txt", "w")
   #-------------------------------------------------------------------------------------------------------
   entrada.write("-------------------------------------------------------------------------------------- \n")
   entrada.write("Escolha a dimensao do eixo-k: \n")
   entrada.write("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. \n")
   entrada.write("Utilize 2 para k em unidades de 1/Angs. \n")
   entrada.write("Utilize 3 para k em unidades de 1/nm. \n")
   entrada.write(f'1 \n')
   entrada.write("-------------------------------------------------------------------------------------- \n")
   #-------------------------------------------------------------------------------------------------------
   entrada.close()

########################################################################################################### 

if (input_Projecoes == 0):
   entrada = open("input/input_projecoes.txt", "w")
   #-------------------------------------------------------------------------------------------------------
   entrada.write("-------------------------------------------------------------------------------------- \n")
   entrada.write("Escolha a dimensao do eixo-k: \n")
   entrada.write("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. \n")
   entrada.write("Utilize 2 para k em unidades de 1/Angs. \n")
   entrada.write("Utilize 3 para k em unidades de 1/nm. \n")
   entrada.write("1 \n")
   entrada.write("-------------------------------------------------------------------------------------- \n")
   entrada.write("Digite o tamanho/peso das esferas do grafico: \n")
   entrada.write("Digite um valor entre 0.0 e 1.0 \n")
   entrada.write("1.0 \n")
   entrada.write("-------------------------------------------------------------------------------------- \n")
   entrada.write("O que vc deseja Plotar/Analisar? \n")
   entrada.write("Digite 0 - Analisar todos os ions. \n")
   entrada.write("Digite 1 - Analisar ions selecionados. \n")
   entrada.write("0 \n")
   entrada.write("-------------------------------------------------------------------------------------- \n")
   entrada.write("Especifique os ions selecionados em intervalos. \n")
   entrada.write("Quantos intervalos de ions ira fornecer abaixo? \n")   
   entrada.write("2 \n")
   entrada.write("============================================================== \n")
   entrada.write("Defina abaixo os intervalos de ions: ion_inicial ion_final \n")
   entrada.write("1   1    ! 1º intervalo de ions que serão levados em consideração nas projeções. \n")
   entrada.write(f'2   {ni}    ! 2º intervalo de ions que serão levados em consideração nas projeções. \n')
   entrada.write("-------------------------------------------------------------------------------------- \n")
   #-------------------------------------------------------------------------------------------------------
   entrada.close()

###########################################################################################################   

if (input_Localizacao == 0):
   entrada = open("input/input_localizacao.txt", "w")
   #-------------------------------------------------------------------------------------------------------
   entrada.write("-------------------------------------------------------------------------------------- \n")
   entrada.write("Escolha a dimensao do eixo-k: \n")
   entrada.write("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. \n")
   entrada.write("Utilize 2 para k em unidades de 1/Angs. \n")
   entrada.write("Utilize 3 para k em unidades de 1/nm. \n")
   entrada.write("1 \n")
   entrada.write("-------------------------------------------------------------------------------------- \n")
   entrada.write("Digite o tamanho/peso das esferas do grafico: \n")
   entrada.write("Digite um valor entre 0.0 e 1.0 \n")
   entrada.write("1.0 \n")
   entrada.write("-------------------------------------------------------------------------------------- \n") 
   entrada.write("Defina as regioes (A, B, C) a serem destacadas na projecao: \n")
   entrada.write("Defina intervalos de ions que compoem as regioes. \n")
   entrada.write("Por padrao todos os ions pertencem inicialmente a Regiao C. \n")
   entrada.write("============================================================== \n")
   entrada.write("Quantos intervalos de ions ira fornecer abaixo? \n") 
   if (ni < 3):
      entrada.write("2 \n")
   if (ni >= 3):
      entrada.write("3 \n")
   entrada.write("============================================================== \n")
   entrada.write("Defina abaixo os intervalos de ions: ion_inicial ion_final Regiao: \n")    
   entrada.write("1   1   A    ! intervalo de ions pertencentes a região A. \n")
   entrada.write("2   2   B    ! intervalo de ions pertencentes a região B. \n")
   if (ni >= 3):
      entrada.write(f'3   {ni}   C    ! intervalo de ions pertencentes a região C. \n')
   entrada.write("-------------------------------------------------------------------------------------- \n")
   #-------------------------------------------------------------------------------------------------------
   entrada.close()

###########################################################################################################   

if (input_Contribuicao == 0):
   entrada = open("input/input_contribuicao.txt", "w")
   #-------------------------------------------------------------------------------------------------------
   entrada.write("############################################################ \n")
   entrada.write("###### Quais Bandas e pontos-k deseja analisar: ############ \n")
   entrada.write("############################################################ \n")
   entrada.write(" \n")
   entrada.write("------------------------------------------------------------- \n")
   entrada.write("Ponto-k inicial a ser analisado: \n")
   entrada.write("1 \n")
   entrada.write("------------------------------------------------------------- \n")
   entrada.write("Ponto-k final a ser analisado: \n")
   entrada.write(f'{nk} \n')
   entrada.write("------------------------------------------------------------- \n")
   entrada.write("Banda inicial a ser analisada: \n")
   entrada.write("1 \n")
   entrada.write("------------------------------------------------------------- \n")
   entrada.write("Banda final a ser analisada: \n")
   entrada.write(f'{nb} \n')
   entrada.write("------------------------------------------------------------- \n")
   #-------------------------------------------------------------------------------------------------------
   entrada.close()

###########################################################################################################   
