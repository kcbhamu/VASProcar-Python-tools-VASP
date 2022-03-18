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

#-----------------------------------------------------------------------------------
# Verificando se a pasta "Fermi_Surface" existe, se não existir ela sera criada ---
#-----------------------------------------------------------------------------------
if os.path.isdir("saida/Fermi_Surface"):
   0 == 0
else:
   os.mkdir("saida/Fermi_Surface")
#---------------------------------- 

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
print ("################ Plot da Superficie de Fermi: ################")
print ("##############################################################")
print (" ")

if (escolha == -10):

   print ("##############################################################") 
   print ("## Escolha a dimensao dos eixos-k no Plot: ================ ##")
   print ("##############################################################")
   print ("## [1] (kx,ky,kz) em unidades de 2pi/Param. =============== ##")
   print ("## [2] (kx,ky,kz) em unidades de 1/Angs. ================== ##")
   print ("## [3] (kx,ky,kz) em unidades de 1/nm. ==================== ##")
   print ("## [4] (k1,k2,k3) Coord. Diretas: K = k1*B1 + k2*B2 + k3*B3 ##")   
   print ("##############################################################") 
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print (" ")

if (escolha == 10):
   Dimensao = 1
   esc_band = 0
   n_d = 101

if (Dimensao < 4):
   c1 = 'kx'; c2 = 'ky'; c3 = 'kz'
if (Dimensao == 4):
   c1 = 'k1'; c2 = 'k2'; c3 = 'k3'

print ("##############################################################")
print ("## Qual plano deve ser visualizado no Plot? =============== ##")
print ("##############################################################")
print (f'## [1] Plano ({c1},{c2}) ====================================== ##')
print (f'## [2] Plano ({c1},{c3}) ====================================== ##')
print (f'## [3] Plano ({c2},{c3}) ====================================== ##')
print ("##############################################################") 
Plano_k = input (" "); Plano_k = int(Plano_k)
print (" ")   

if (escolha == -10):

   print ("##############################################################")
   print ("Qual a dimensao-D (DxD) do GRID de interpolacao? =============")
   print ("Dica: Utilize 101 (Quanto maior mais preciso e pesado) =======")
   print ("##############################################################") 
   n_d = input (" "); n_d = int(n_d)  
   print (" ")   

   print ("##############################################################")
   print ("Com relacao as bandas o que deseja analisar? =================")
   print ("[0] Plotar todas as bandas na Superficie de Fermi ============")
   print ("[1] Plotar um intervalo selecionado de bandas na Sup. de Fermi")
   print ("##############################################################")
   esc_band = input (" "); esc_band = int(esc_band)
   print (" ")

   if (esc_band == 1): 
      print ("Digite a banda inicial do intervalo: =========================")
      Band_i = input (" "); Band_i = int(Band_i)
      print(" ")
      print ("Digite a banda final do intervalo: ===========================")
      Band_f = input (" "); Band_f = int(Band_f)
      print(" ")

if (esc_band == 0):
   Band_i = 1
   Band_f = nb

print ("##############################################################")
print ("Com relacao a energia o que deseja analisar? =================")
print ("[0] Analizar um unico valor de energia =======================")
print ("[1] Analizar um range de energia =============================")
print ("##############################################################")
esc_energ = input (" "); esc_energ = int(esc_energ)
print (" ")

if (esc_energ == 0):
   n_energ = 1
   E = [0.0]*n_energ
   print ("Digite o valor de energia: ===================================")
   E[0] = input (" "); E[0] = float(E[0])
   print (" ")
   
if (esc_energ == 1):
   #-----------------------------------------------------------------------
   print ("Digite o valor inicial do range de energia: ==================")
   energ_i = input (" "); energ_i = float(energ_i)
   print (" ")
   print ("Digite o valor final do range de energia: ====================")
   energ_f = input (" "); energ_f = float(energ_f)
   print (" ")
   print ("Em quantos valores deseja dividir este range de energia? =====")
   n_energ = input (" "); n_energ = int(n_energ)
   print (" ")
   #-----------------------------------------------------------------------
   if (n_energ <= 1): n_energ = 2
   E = [0.0]*n_energ
   #----------------------------------------------------------------------- 
   for i in range(n_energ):
       E[i] = energ_i + ((energ_f - energ_i)/(n_energ - 1))*(i)

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------

#------------------------------------
executavel = Diretorio + '/procar.py'
exec(open(executavel).read())
#------------------------------------

#======================================================================
# Gravando dados para o Plot 3D da Estrutura de Bandas ================
#======================================================================     

#----------------------------------------------------------
sfermi = open("saida/Fermi_Surface/Fermi_Surface.dat", "w")
#----------------------------------------------------------
    
for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        if (Dimensao != 4):
           sfermi.write(f'{kx[j][point_k]} {ky[j][point_k]} {kz[j][point_k]} ')   
        if (Dimensao == 4):
           sfermi.write(f'{kb1[j][point_k]} {kb2[j][point_k]} {kb3[j][point_k]} ')
        for Band_n in range (1,(nb+1)):
           sfermi.write(f'{Energia[j][point_k][Band_n]} ')
        sfermi.write("\n")
               
#-------------
sfermi.close()
#-------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Fermi_Surface.py para o diretório de saida --------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

import shutil

# Teste para saber se o arquivo Fermi_Surface.py já se encontra no diretorio de saida
try: f = open('saida/Fermi_Surface/Fermi_Surface.py'); f.close(); os.remove('saida/Fermi_Surface/Fermi_Surface.py')
except: 0 == 0
 
source = Diretorio + '/plot/plot_fermi_surface.py'
destination = 'saida/Fermi_Surface/Fermi_Surface.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código de Plot possam ser executados isoladamente ---
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open('saida/Fermi_Surface/Fermi_Surface.py', 'r')
lines = file.readlines()
file.close()

linha = 22

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')  
linha += 1; lines.insert(linha, f'Dimensao  = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'Plano_k   = {Plano_k}  #  [1] kxky ou k1k2; [2] kxkz ou k1k3; [3] kykz ou k2k3  \n')
linha += 1; lines.insert(linha, f'Band_i = {Band_i}; Band_f = {Band_f}  #  Bandas inicial e final a serem introduzidas no plot da Superficie de Fermi \n')
linha += 1; lines.insert(linha, f'n_d = {n_d}  #  Dimensao-D (DxD) do GRID de interpolacao para o plot via plotly \n')
linha += 1; lines.insert(linha, f'n_energ = {n_energ}; E = {E}  #  Valores de energia a serem utilizados no plot da Superficie de Fermi \n')
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da projeção sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open('saida/Fermi_Surface/Fermi_Surface.py', 'w')
file.writelines(lines)
file.close()

#--------------------------------------------------
executavel = 'saida/Fermi_Surface/Fermi_Surface.py'
exec(open(executavel).read())
#--------------------------------------------------
  
#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
