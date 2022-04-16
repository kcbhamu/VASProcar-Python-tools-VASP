
def execute_python_file(filename: str):
   return exec(open(main_dir + str(filename)).read(), globals())

#----------------------------------------------------------------------------------
# Verificando se a pasta "Fermi_Surface" existe, se não existir ela sera criada ---
#----------------------------------------------------------------------------------
if os.path.isdir("output/Fermi_Surface"):
   0 == 0
else:
   os.mkdir("output/Fermi_Surface")
#----------------------------------

#-------------------------------------------------------------------------------
# Verificando se a subpasta "figures" existe, se não existir ela sera criada ---
#-------------------------------------------------------------------------------
if os.path.isdir("output/Fermi_Surface/figures"):
   0 == 0
else:
   os.mkdir("output/Fermi_Surface/figures")
#------------------------------------------     

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = '/informacoes.py')

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("################ Plot da Superficie de Fermi: ################")
print ("##############################################################")
print (" ")

if (escolha == -10):
   #------------------------
   print ("##############################################################")
   print ("Com relacao as bandas o que deseja analisar? =================")
   print ("[0] Plotar todas as bandas na Superficie de Fermi ============")
   print ("[1] Plotar um intervalo selecionado de bandas na Sup. de Fermi")
   print ("##############################################################")
   esc_band = input (" "); esc_band = int(esc_band)
   print (" ")
   #------------------------
   if (esc_band == 1): 
      print ("Digite a banda inicial do intervalo: =========================")
      Band_i = input (" "); Band_i = int(Band_i)
      print(" ")
      print ("Digite a banda final do intervalo: ===========================")
      Band_f = input (" "); Band_f = int(Band_f)
      print(" ")

print ("##############################################################")
print ("Qual o numero de Energias que deseja analisar? ===============")
print ("##############################################################")
n_energ = input (" "); n_energ = int(n_energ)
print(" ")

if (n_energ <= 0):
   n_energ = 1

print ("##############################################################")
print ("Com relacao aos valores de energias: =========================")
print ("[0] Devem ser obtidas automaticamente pelo codigo ============")
print ("[1] Devem varrer um determinado range de energia =============")
print ("[2] Desejo especificar cada valor de energia manualmente =====")   
print ("##############################################################")
esc_energ = input (" "); esc_energ = int(esc_energ)
print(" ")

if (esc_energ == 1):  
   print ("Digite o valor inicial do range de energia: ==================")
   energ_i = input (" "); energ_i = float(energ_i)
   print (" ")
   print ("Digite o valor final do range de energia: ====================")
   energ_f = input (" "); energ_f = float(energ_f)
   print (" ")

if (esc_energ == 2):
   #-----------------------------------------------------------------------
   print ("##############################################################")
   print ("!!! Observacao importante !!! =============================== ")
   print ("Digite os valores de energia em ordem crescente ============= ")
   print ("##############################################################")    
   print (" ")
   #-----------------------------------------------------------------------
   E = [0.0]*n_energ
   #-----------------------------------------------------------------------
   for i in range(n_energ):
       print (f'### Digite o valor da energia numero {i+1}:')
       valor_energ = input (" "); valor_energ = float(valor_energ)
       E[i] = valor_energ
       print(" ") 

print ("##############################################################")
print ("Deseja compilar um video apartir das figuras geradas? ========")
print ("[0] NAO ======================================================")
print ("[1] SIM ======================================================")
print ("==============================================================")
print ("Observacao: Nao serao geradas imagens em .pdf ou .eps ========")
print ("##############################################################")
video = input (" "); video = int(video)
print (" ")

if (video == 1):
   #-----------------------------------------------------------------------
   print ("##############################################################")
   print ("Quantas figuras deseja que aparecam por segundo no video? ====")
   print ("Dica: Escolha entre 1 e 8 ====================================")
   print ("##############################################################")
   n_fig = input (" "); n_fig = int(n_fig)  
   print (" ")
   #-------------------------
   if (n_fig <= 0): n_fig = 1
   #-------------------------
   save_png = 1
   save_pdf = 0
   save_eps = 0

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

if (esc_band == 0):
   Band_i = 1
   Band_f = nb

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

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------
execute_python_file(filename = '/procar.py')

#======================================================================
# Gravando dados para o Plot 3D da Estrutura de Bandas ================
#======================================================================     

#-----------------------------------------------------------
sfermi = open("output/Fermi_Surface/Fermi_Surface.dat", "w")
#-----------------------------------------------------------
    
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
try: f = open('output/Fermi_Surface/Fermi_Surface.py'); f.close(); os.remove('output/Fermi_Surface/Fermi_Surface.py')
except: 0 == 0
 
source = main_dir + '/plot/plot_fermi_surface.py'
destination = 'output/Fermi_Surface/Fermi_Surface.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código de Plot possam ser executados isoladamente ---
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open('output/Fermi_Surface/Fermi_Surface.py', 'r')
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
linha += 1; lines.insert(linha, f'Band_i = {Band_i}  #  Banda inicial a ser introduzida no plot da Superficie de Fermi \n')
linha += 1; lines.insert(linha, f'Band_f = {Band_f}  #  Banda final a ser introduzida no plot da Superficie de Fermi \n')
linha += 1; lines.insert(linha, f'n_d = {n_d}  #  Dimensao-D (DxD) do GRID de interpolacao para o plot via plotly \n')
linha += 1; lines.insert(linha, f'esc_energ = {esc_energ}  #  Forma de obtenção das energias: Onde [0] é automatico; [1] range de energia e [2] informado manualmente \n')
linha += 1; lines.insert(linha, f'n_energ = {n_energ}  #  Numero de energias a serem utilizadas no plot das Superficies de Fermi \n')
#--------------------------------
if (esc_energ == 1):
   linha += 1; lines.insert(linha, f'energ_i = {energ_i}; energ_f = {energ_f}  #  Energia inicial e final do Range de energia no plot das Superficies de Fermi \n')
if (esc_energ == 2):
   linha += 1; lines.insert(linha, f'E = {E}  #  Valores de energia especificadas manualmente no plot das Superficies de Fermi \n')
if (esc_energ < 2):
   linha += 1; lines.insert(linha, f'E = [0.0, 0.0, 0.0, 0.0, 0.0]  #  Valores das Curvas de Nivel especificados manualmente \n')
#--------------------------------
linha += 1; lines.insert(linha, f'video = {video}  #  Escolha se um video deve ser gerado ou nao, onde [0] = NAO e [1] = SIM \n')
if (video == 1):
   linha += 1; lines.insert(linha, f'n_fig = {n_fig}  #  Numero de figuras que aparecem no video por segundo \n')
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da projeção sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open('output/Fermi_Surface/Fermi_Surface.py', 'w')
file.writelines(lines)
file.close()

#---------------------------------------------------------
exec(open('output/Fermi_Surface/Fermi_Surface.py').read())
#---------------------------------------------------------
