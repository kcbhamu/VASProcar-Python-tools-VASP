
########### Verificando se a pasta _input e os arquivos de input existem: ###########

if os.path.isdir("_input"):
   #------------------------------------------------------------------------
   try: f = open('_input/input_Texturas.txt'); f.close(); input_Texturas = 1
   except: input_Texturas = 0
   #------------------------------------------------------------------------------
   try: f = open('_input/input_Localizacao.txt'); f.close(); input_Localizacao = 1
   except: input_Localizacao = 0       
   #--------------------------------------------------------------------------------
   try: f = open('_input/input_Contribuicao.txt'); f.close(); input_Contribuicao = 1
   except: input_Contribuicao = 0
        
else:
   #-----------------
   os.mkdir("_input")
   input_Texturas = 0
   input_Localizacao = 0
   input_Contribuicao = 0
   
############## Gerando qualquer arquivo de input que esteja faltando: ##############

if (input_Texturas == 0):
   input = open("_input/input_Texturas.txt", "w")
   #-------------------------------------------------------------------------------------------------------
   input.write("-------------------------------------------------------------------------------------- \n")
   input.write("Escolha a dimensao do eixo-k: \n")
   input.write("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. \n")
   input.write("Utilize 2 para k em unidades de 1/Angs. \n")
   input.write("Utilize 3 para k em unidades de 1/nm. \n")
   input.write("1 \n")
   input.write("-------------------------------------------------------------------------------------- \n")
   input.write("Projecoes a serem analisadas: \n")
   input.write("Digite 77 - Para Plotar apenas a Estrutura de Bandas. \n")
   input.write("Digite 99 - Analisar as Projecoes de Spin (Sx, Sy e Sz). \n")
   input.write("Digite -99 - Analisar as Projecoes dos Orbitais (S, P e D). \n")
   input.write("Digite 100 - Analisar todas as projeções (Spin e Orbitais). \n")
   input.write("77 \n")
   input.write("-------------------------------------------------------------------------------------- \n")
   input.write("Digite o tamanho/peso das esferas do grafico: \n")
   input.write("1.0 \n")
   input.write("-------------------------------------------------------------------------------------- \n")
   input.write("O que vc deseja Plotar/Analisar: \n")
   input.write("Digite 0 - Analisar todos os ions. \n")
   input.write("Digite 1 - Analisar ions selecionados (ions_selecionados.txt). \n")
   input.write("0 \n")
   input.write("-------------------------------------------------------------------------------------- \n")
   input.write("Adicione nas linhas abaixo o nº de intervalos de ions que serão projetados: \n")
   input.write("1              ! Nº de intervalos de Valores a serem lidos abaixo. \n")
   input.write("1   2  sim     ! 1º intervalo de ions que serão levados em consideração nas projeções. \n")
   input.write("7  16  sim     ! 2º intervalo de ions que serão levados em consideração nas projeções. \n")
   input.write("25 33  sim     ! 3º intervalo de ions que serão levados em consideração nas projeções.  \n")
   #-------------------------------------------------------------------------------------------------------
   input.close()

###########################################################################################################   

if (input_Localizacao == 0):
   input = open("_input/input_Localizacao.txt", "w")
   #-------------------------------------------------------------------------------------------------------
   input.write("------------------------------------------------------------- \n")
   input.write("Escolha a dimensao do eixo-k: \n")
   input.write("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. \n")
   input.write("Utilize 2 para k em unidades de 1/Angs. \n")
   input.write("Utilize 3 para k em unidades de 1/nm. \n")
   input.write("1 \n")
   input.write("------------------------------------------------------------------------------ \n")
   input.write("Digite o tamanho/peso das esferas do grafico: \n")
   input.write("1.0 \n")
   input.write("------------------------------------------------------------------------------ \n")
   input.write("Digite o valor minimo de Contribuição do estado a ser mostrado no Plot: \n")
   input.write("0.0 \n")
   input.write("-------------------------------------------------------------------------------------- \n")
   input.write("Adicione nas linhas abaixo o nº de intervalos de ions que definem as regiões: \n")
   input.write("1           ! Nº de linhas a serem lidas abaixo. \n")
   input.write("1   2  A    ! intervalo de ions pertencentes a região A. \n")
   input.write("5   7  B    ! intervalo de ions pertencentes a região B. \n")
   input.write("9  16  C    ! intervalo de ions pertencentes a região C. \n")
   input.write("25 33  A    ! intervalo de ions pertencentes a região A. \n")
   #-------------------------------------------------------------------------------------------------------
   input.close()

###########################################################################################################   

if (input_Contribuicao == 0):
   input = open("_input/input_Contribuicao.txt", "w")
   #-------------------------------------------------------------------------------------------------------
   input.write("############################################################ \n")
   input.write("###### Quais Bandas e pontos-k você deseja analisar: ####### \n")
   input.write("############################################################ \n")
   input.write(" \n")
   input.write("------------------------------------------------------------- \n")
   input.write("Banda inicial a ser Analisada: \n")
   input.write("1 \n")
   input.write("------------------------------------------------------------- \n")
   input.write("Banda final a ser Analisada: \n")
   input.write("2 \n")
   input.write("------------------------------------------------------------- \n")
   input.write("Ponto-k inicial a ser Analisado: \n")
   input.write("1 \n")
   input.write("------------------------------------------------------------- \n")
   input.write("Ponto-k final a ser Analisado: \n")
   input.write("2 \n")
   input.write("------------------------------------------------------------- \n")
   #-------------------------------------------------------------------------------------------------------
   input.close()
