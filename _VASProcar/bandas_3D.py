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

#-----------------------------------------------------------------------------
# Verificando se a pasta "Bandas_3D" existe, se não existir ela sera criada --
#-----------------------------------------------------------------------------
if os.path.isdir("saida/Bandas_3D"):
   0 == 0
else:
   os.mkdir("saida/Bandas_3D")
#----------------------------- 

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================

#-----------------------------------------
executavel = Diretorio + '/informacoes.py'
exec(open(executavel).read())
#-----------------------------------------

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("############## Plot Banda 3D ou Banda 2D em 3D: ##############")
print ("##############################################################")
print (" ")

if (escolha == -6):

   print ("##############################################################") 
   print ("## Escolha a dimensao dos eixos-k no Plot 3D: ============= ##")
   print ("##############################################################")
   print ("## [1] (kx,ky,kz) em unidades de 2pi/Param. =============== ##")
   print ("## [2] (kx,ky,kz) em unidades de 1/Angs. ================== ##")
   print ("## [3] (kx,ky,kz) em unidades de 1/nm. ==================== ##")
   print ("## [4] (k1,k2,k3) Coord. Diretas: K = k1*B1 + k2*B2 + k3*B3 ##")   
   print ("##############################################################") 
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print (" ")

if (escolha == 6):
   Dimensao = 1
   n_d = 101    

if (Dimensao < 4):
   c1 = 'kx'; c2 = 'ky'; c3 = 'kz'
if (Dimensao == 4):
   c1 = 'k1'; c2 = 'k2'; c3 = 'k3'

print ("##############################################################")
print ("## Qual plano deve ser visualizado no Plot 3D? ============ ##")
print ("##############################################################")
print (f'## [1] Plano ({c1},{c2}) ====================================== ##')
print (f'## [2] Plano ({c1},{c3}) ====================================== ##')
print (f'## [3] Plano ({c2},{c3}) ====================================== ##')
print ("##############################################################") 
Plano_k = input (" "); Plano_k = int(Plano_k)
print (" ")   

print ("##############################################################")
print ("Escolha as Bandas a serem Plotadas: ==========================")
print ("##############################################################") 
print ("Banda inicial: ===============================================")
Band_i = input (" "); Band_i = int(Band_i)
print (" ")
print ("Banda final: =================================================")
Band_f = input (" "); Band_f = int(Band_f)
print (" ")

print ("##############################################################") 
print ("## Escolha o pacote para pre-visualizar o Plot 3D: ======== ##")
print ("##############################################################")
print ("## [1] Plotly (Visualizacao mais leve) ==================== ##")
print ("## [2] Matplotlib ========================================= ##")
print ("##############################################################") 
pacote = input (" "); pacote = int(pacote)
if (pacote == 2): n_d = 101
print (" ")

print ("##############################################################")
print ("## Como prefere que seja o Plot 3D? ======================= ##")
print ("##############################################################")
print ("## [0] Pontos (Dados brutos) ============================== ##")
if (pacote == 1): print ("## [1] Superficie (Interpolacao) ========================== ##")
if (pacote == 2): print ("## [1] Superficie (Dados brutos + Triangularizacao) ======= ##")
print ("## [2] Pontos + Superficie ================================ ##")  
print ("##############################################################") 
tipo_plot = input (" "); tipo_plot = int(tipo_plot)
print (" ")

if (escolha == -6):
   if (pacote == 1 and tipo_plot > 0):
      print ("##############################################################")
      print ("Qual a dimensao-D (DxD) do GRID de interpolacao? =============")
      print ("Dica: Utilize 101 (Quanto maior mais preciso e pesado) =======")
      print ("##############################################################") 
      n_d = input (" "); n_d = int(n_d)  
      print (" ")    

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------

#------------------------------------
executavel = Diretorio + '/procar.py'
exec(open(executavel).read())
#------------------------------------

#----------------------------------------------------------------------
Band_antes   = (Band_i - 1)       # Bandas que nao serao plotadas.
Band_depois  = (Band_f + 1)       # Bandas que nao serao plotadas.
#----------------------------------------------------------------------

#======================================================================
# Gravando dados para o Plot 3D da Estrutura de Bandas ================
#======================================================================     

#----------------------------------------------------------
bandas_3D = open("saida/Bandas_3D/Bandas_3D.dat", "w")
#----------------------------------------------------------
    
for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        if (Dimensao != 4):
           bandas_3D.write(f'{kx[j][point_k]} {ky[j][point_k]} {kz[j][point_k]} ')   
        if (Dimensao == 4):
           bandas_3D.write(f'{kb1[j][point_k]} {kb2[j][point_k]} {kb3[j][point_k]} ')
        for Band_n in range (Band_i,(Band_f+1)):
           bandas_3D.write(f'{Energia[j][point_k][Band_n]} ')
        bandas_3D.write("\n")
               
#----------------
bandas_3D.close()
#----------------

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
# Copiando os codigos Bandas_3D_matplotlib.py e Bandas_3D_plotly.py para o diretório de saida --
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

import shutil

# Teste para saber se o arquivo Bandas_3D_plotly.py já se encontra no diretorio de saida
try: f = open('saida/Bandas_3D/Bandas_3D_plotly.py'); f.close(); os.remove('saida/Bandas_3D/Bandas_3D_plotly.py')
except: 0 == 0

# Teste para saber se o arquivo Bandas_3D_matplotlib.py já se encontra no diretorio de saida
try: f = open('saida/Bandas_3D/Bandas_3D_matplotlib.py'); f.close(); os.remove('saida/Bandas_3D/Bandas_3D_matplotlib.py')
except: 0 == 0
   
source = Diretorio + '/plot/plot_bandas_3D_plotly.py'
destination = 'saida/Bandas_3D/Bandas_3D_plotly.py'
shutil.copyfile(source, destination)

source = Diretorio + '/plot/plot_bandas_3D_matplotlib.py'
destination = 'saida/Bandas_3D/Bandas_3D_matplotlib.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
# Inserindo parâmetros para que os códigos de Plot possam ser executados isoladamente ----------
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

for i in range (2):

    if (i == 0): file = open('saida/Bandas_3D/Bandas_3D_plotly.py', 'r')
    if (i == 1): file = open('saida/Bandas_3D/Bandas_3D_matplotlib.py', 'r')
    lines = file.readlines()
    file.close()

    if (i == 0): linha = 18
    if (i == 1): linha = 22

    lines.insert(linha, '\n')
    linha += 1; lines.insert(linha, '#===================================================================== \n')
    linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
    linha += 1; lines.insert(linha, '#===================================================================== \n')
    linha += 1; lines.insert(linha, '\n')
    linha += 1; lines.insert(linha, f'tipo_plot = {tipo_plot}  # [0] Plotado em pontos; [1] Plotado em superficie; [2] pontos + superficie \n')   
    linha += 1; lines.insert(linha, f'Dimensao  = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
    linha += 1; lines.insert(linha, f'Plano_k   = {Plano_k}  #  [1] kxky ou k1k2; [2] kxkz ou k1k3; [3] kykz ou k2k3  \n')
    linha += 1; lines.insert(linha, f'Band_i = {Band_i}  #  Banda inicial a ser plotada \n')
    linha += 1; lines.insert(linha, f'Band_f = {Band_f}  #  Banda final a ser plotada \n')
    if (i == 0):
       linha += 1
       lines.insert(linha, f'n_d = {n_d}  #  Dimensao-D (DxD) do GRID de interpolacao para o plot via plotly \n')
    linha += 1; lines.insert(linha, '\n')
    linha += 1; lines.insert(linha, '#===================================================================== \n')

    if (i == 0): file = open('saida/Bandas_3D/Bandas_3D_plotly.py', 'w')
    if (i == 1): file = open('saida/Bandas_3D/Bandas_3D_matplotlib.py', 'w')
    file.writelines(lines)
    file.close()

#-----------------------------------------------------------------------
if (pacote == 1): executavel = 'saida/Bandas_3D/Bandas_3D_plotly.py'
if (pacote == 2): executavel = 'saida/Bandas_3D/Bandas_3D_matplotlib.py'
exec(open(executavel).read())
#-----------------------------------------------------------------------
  
#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
