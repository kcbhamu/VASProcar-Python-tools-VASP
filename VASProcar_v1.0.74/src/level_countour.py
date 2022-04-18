
def execute_python_file(filename: str):
   return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------------------
# Verificando se a pasta "Level_Countour" existe, se não existir ela sera criada ---
#-----------------------------------------------------------------------------------
if os.path.isdir(dir_files + '\output\Level_Countour'):
   0 == 0
else:
   os.mkdir(dir_files + '\output\Level_Countour')
#------------------------------------------------ 

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = 'informacoes.py')

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("################## Plot das Curvas de Nivel ##################")
print ("##############################################################")
print (" ")

print ("##############################################################")
print ("Qual banda quer analisar? ====================================")
print ("##############################################################") 
Band = input (" "); Band = int(Band)
print (" ")

print ("##############################################################")
print ("Qual o numero de Curvas de Nivel (Energias) que deseja obter? ")
print ("##############################################################")
n_contour = input (" "); n_contour = int(n_contour)
print(" ")

if (n_contour <= 0):
   n_contour = 1

if (escolha == 11):
   Dimensao = 1
   tipo_contour = 0
   n_d = 101
   transp = 1.0
   
if (escolha == -11):

   print ("##############################################################")
   print ("Com relacao as energias das Curvas de Nivel: =================")
   print ("[0] Devem ser obtidas automaticamente pelo codigo ============")
   print ("[1] Devem varrer um determinado range de energia =============")
   print ("[2] Desejo especificar cada valor de energia manualmente =====")   
   print ("##############################################################")
   tipo_contour = input (" "); tipo_contour = int(tipo_contour)
   print(" ")

   if (tipo_contour == 1):    
      print ("Digite o valor inicial do range de energia: ==================")
      energ_i = input (" "); energ_i = float(energ_i)
      print (" ")
      print ("Digite o valor final do range de energia: ====================")
      energ_f = input (" "); energ_f = float(energ_f)
      print (" ")

   if (tipo_contour == 2):
      print ("##############################################################")
      print ("!!! Observacao importante !!! =============================== ")
      print ("Digite os valores de energia em ordem crescente ============= ")
      print ("##############################################################")    
      print (" ")
      #-----------------------------------------------------------------------
      levels_n = [0.0]*n_contour
      #-----------------------------------------------------------------------
      for i in range(n_contour):
          print (f'### Digite o valor da Curva de Nivel numero {i+1}:')
          valor_contour = input (" "); valor_contour = float(valor_contour)
          levels_n[i] = valor_contour
          print(" ") 

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

if (escolha == -11):

   print ("##############################################################")
   print ("Qual a dimensao-D (DxD) do GRID de interpolacao? =============")
   print ("Dica: Utilize 101 (Quanto maior mais preciso e pesado) =======")
   print ("##############################################################") 
   n_d = input (" "); n_d = int(n_d)  
   print (" ")

   print ("##############################################################")
   print ("Digite o valor de transparencia [0.0 a 1.0] a ser aplicado no ")
   print ("gradiente de cores das Curvas de Nivel, quanto menor o valor  ")
   print ("mais suaves serao as cores, quanto maior mais intensas serao. ")
   print ("##############################################################")
   transp = input (" "); transp = float(transp)
   print(" ")

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------
execute_python_file(filename = 'procar.py')

#======================================================================
# Gravando dados para o Plot 3D da Estrutura de Bandas ================
#======================================================================     

#----------------------------------------------------------------------------
countour = open(dir_files + '\output\Level_Countour\Level_Countour.dat', 'w')
#----------------------------------------------------------------------------
    
for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        if (Dimensao != 4):
           countour.write(f'{kx[j][point_k]} {ky[j][point_k]} {kz[j][point_k]} ')   
        if (Dimensao == 4):
           countour.write(f'{kb1[j][point_k]} {kb2[j][point_k]} {kb3[j][point_k]} ')
        for Band_n in range (1,(nb+1)):
           countour.write(f'{Energia[j][point_k][Band_n]} ')
        countour.write("\n")
               
#---------------
countour.close()
#---------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Level_Countour.py para o diretório de saida -------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

import shutil

# Teste para saber se o arquivo Level_Countour.py já se encontra no diretorio de saida
try: f = open(dir_files + '\output\Level_Countour\Level_Countour.py'); f.close(); os.remove(dir_files + '\output\Level_Countour\Level_Countour.py')
except: 0 == 0
 
source = main_dir + '\plot\plot_level_countour.py'
destination = dir_files + '\output\Level_Countour\Level_Countour.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código de Plot possam ser executados isoladamente ---
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open(dir_files + '\output\Level_Countour\Level_Countour.py', 'r')
lines = file.readlines()
file.close()

linha = 12

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')  
linha += 1; lines.insert(linha, f'Dimensao  = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'Plano_k   = {Plano_k}  #  [1] kxky ou k1k2; [2] kxkz ou k1k3; [3] kykz ou k2k3  \n')
linha += 1; lines.insert(linha, f'Band = {Band}  #  Banda a ser analisada \n')
linha += 1; lines.insert(linha, f'n_d = {n_d}  #  Dimensao-D (DxD) do GRID de interpolacao para o plot via plotly \n')
linha += 1; lines.insert(linha, f'transp = {transp}  #  Transparencia aplicada ao gradiente de cores do plot 2D das Curvas de Nivel \n')
linha += 1; lines.insert(linha, f'tipo_contour = {tipo_contour}  #  Forma de obtenção das energias das Curvas de Nivel: Onde [0] é automatico; [1] range de energia e [2] informado manualmente \n')
linha += 1; lines.insert(linha, f'n_contour = {n_contour}  #  Numero de Curvas de Nivel a serem obtidas \n')
#--------------------------------
if (tipo_contour == 1):
   linha += 1; lines.insert(linha, f'energ_i = {energ_i}; energ_f = {energ_f}  #  Energia inicial e final do Range de energia das Curvas de Nivel \n')
if (tipo_contour == 2):
   linha += 1; lines.insert(linha, f'levels_n = {levels_n}  #  Valores das Curvas de Nivel especificadas manualmente \n')
if (tipo_contour < 2):
   linha += 1; lines.insert(linha, f'levels_n = [0.0, 0.0, 0.0, 0.0, 0.0]  #  Valores das Curvas de Nivel especificados manualmente \n')
#--------------------------------
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da projeção sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '\output\Level_Countour\Level_Countour.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------------------------------------------
exec(open(dir_files + '\output\Level_Countour\Level_Countour.py').read())
#------------------------------------------------------------------------
