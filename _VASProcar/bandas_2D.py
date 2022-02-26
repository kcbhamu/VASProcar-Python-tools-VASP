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

#-------------------------------------------------------------------
# Verificando se a pasta "Bandas" existe, se não existe ela é criada
#-------------------------------------------------------------------
if os.path.isdir("saida/Bandas"):
   0 == 0
else:
   os.mkdir("saida/Bandas")
#--------------------------

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
print ("################ Plot da Estrutura de Bandas: ################")
print ("##############################################################")
print (" ")

if (escolha == -1):
   
   print ("##############################################################")
   print ("Quanto aos pontos-k de interesse, o que vc deseja? ===========")
   print ("[0] Nao destacar nem rotular nenhum ponto-k ==================")
   print ("[1] Destacar automaticamente os pontos-k informados no KPOINTS")
   print ("[2] Destacar e rotular os pontos-k a sua escolha =============")
   print ("##############################################################") 
   dest_k = input (" "); dest_k = int(dest_k)
   print (" ")

   if (dest_k == 2):
      print ("##############################################################")
      print ("Observacao: O arquivo label.txt sera gerado apos a leitura do ")
      print ("            arquivo PROCAR                                    ")
      print ("##############################################################") 
      print (" ")

      Dimensao = 1

   if (dest_k != 2):
      print ("##############################################################")
      print ("Escolha a dimensao do eixo-k: ================================")
      print ("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. =")
      print ("Utilize 2 para k em unidades de 1/Angs. ======================")
      print ("Utilize 3 para k em unidades de 1/nm. ========================")
      print ("##############################################################") 
      Dimensao = input (" "); Dimensao = int(Dimensao)
      print (" ")      

if (escolha == 1):

   Dimensao = 1
   dest_k = 1

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------

#------------------------------------
executavel = Diretorio + '/procar.py'
exec(open(executavel).read())
#------------------------------------

#======================================================================
# Obtenção de alguns parâmetros de ajusto do Grafico (GRACE) ==========
#======================================================================    

x_inicial = xx[1][1]
x_final   = xx[n_procar][nk]
y_inicial = energ_min
y_final   = energ_max

#======================================================================
# Obtendo o nº pontos-k a serem destacados bem como os seus rótulos ===
#======================================================================

#-----------------------------------
executavel = Diretorio + '/label.py'
exec(open(executavel).read())
#-----------------------------------

#======================================================================
#======================================================================
# Plot da Estrutura de Bandas (GRACE) =================================
#====================================================================== 
#======================================================================

#--------------------------------------------
bandas = open("saida/Bandas/Bandas.agr", "w")
#--------------------------------------------

bandas.write("# Grace project file \n")
bandas.write("# written using VASProcar (https://github.com/Augusto-Dlelis/VASProcar-Tools-Python) \n") 
bandas.write("# \n")
bandas.write("@version 50122 \n")
bandas.write("@with g0 \n")
bandas.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
bandas.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

escala_x = (x_final - x_inicial)/5
escala_y = (y_final - y_inicial)/5

bandas.write(f'@    xaxis  tick major {escala_x:.2f} \n')

palavra = '"\\f{Symbol}2p/\\f{Times-Italic}a"'
if (Dimensao == 1 and dest_k != 2): bandas.write(f'@    xaxis  label {palavra} \n') 
if (Dimensao == 2 and dest_k != 2): bandas.write(f'@    xaxis  label "1/Angs." \n') 
if (Dimensao == 3 and dest_k != 2): bandas.write(f'@    xaxis  label "1/nm" \n')

if (dest_k == 2):
   bandas.write(f'@    xaxis  tick spec type both \n')
   bandas.write(f'@    xaxis  tick spec {contador2} \n')
   for i in range (contador2):   
       bandas.write(f'@    xaxis  tick major {i}, {dest_pk[i]} \n')
       temp_r = label_pk[i]
       for j in range(30):
           if (temp_r == '[' + str(j+1) + ']'): temp_r = r_grace[j]                  
       bandas.write(f'@    xaxis  ticklabel {i}, "{temp_r}" \n')    
 
bandas.write(f'@    yaxis  tick major {escala_y:.2f} \n')
bandas.write(f'@    yaxis  label "E-Ef (eV)" \n')

#======================================================================

for i in range(nb + 1 + contador2):

    if (i <= (nb-1)): color = 1 # cor Preta
    if (i == nb):     color = 2 # cor Vermelha
    if (i > nb):      color = 7 # Cor Cinza  
   
    bandas.write(f'@    s{i} type xy \n')
    bandas.write(f'@    s{i} line type 1 \n')
    bandas.write(f'@    s{i} line color {color} \n')
    
bandas.write(f'@type xy \n')    

# Plot das Bandas =====================================================
     
for Band_n in range (1,(nb+1)):
    bandas.write(" \n")
    for j in range (1,(n_procar+1)):
        for point_k in range (1,(nk+1)):
            bandas.write(f'{xx[j][point_k]} {Energia[j][point_k][Band_n]} \n')

# Destacando a energia de Fermi na estrutura de Bandas ================
      
bandas.write(" \n")
bandas.write(f'{xx[1][1]} 0.0 \n')
bandas.write(f'{xx[n_procar][nk]} 0.0 \n')

# Destacando pontos-k de interesse na estrutura de Bandas =============

if (dest_k > 0):
   for loop in range (contador2):
       bandas.write(" \n")
       bandas.write(f'{dest_pk[loop]} {energ_min} \n')
       bandas.write(f'{dest_pk[loop]} {energ_max} \n')     

#-------------
bandas.close()
#-------------

#======================================================================
#======================================================================
# Plot da Estrutura de Bandas (Matplotlib) ============================
#====================================================================== 
#======================================================================

#======================================================================
# Gravando dados para o Plot das Bandas ===============================
#======================================================================     

#--------------------------------------------
bandas = open("saida/Bandas/Bandas.dat", "w")
#--------------------------------------------

for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        bandas.write(f'{xx[j][point_k]}')
        for Band_n in range (1,(nb+1)):
            bandas.write(f' {Energia[j][point_k][Band_n]}')
        bandas.write(f' \n')
                
#----------------
bandas.close()
#----------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo bandas.py para o diretório de saida ---------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

import shutil

# Teste para saber se o arquivo bandas.py já se encontra no diretorio de saida
try: f = open('saida/Bandas/bandas.py'); f.close(); os.remove('saida/Bandas/bandas.py')
except: 0 == 0
   
source = Diretorio + '/plot_bandas_2D.py'
destination = 'saida/Bandas/plot_bandas_2D.py'
shutil.copyfile(source, destination)
os.rename('saida/Bandas/plot_bandas_2D.py', 'saida/Bandas/bandas.py')

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código bandas.py possa ser executado isoladamente ---
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open('saida/Bandas/bandas.py', 'r')
lines = file.readlines()
file.close()

linha = 14

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}; nk  = {nk}; nb = {nb}; energ_min = {energ_min}; energ_max = {energ_max} \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da banda sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, f'dest_k = {dest_k}  #  [0] Nao destacar nem rotular nenhum ponto-k; [1] Destacar automaticamente os pontos-k informados no KPOINTS; [2] Destacar e rotular os pontos-k a sua escolha \n')
linha += 1; lines.insert(linha, f'dest_pk = {dest_pk}  #  Coordenadas dos pontos-k de interesse a serem destacados na estrutura de bandas \n')

if (dest_k == 2): 
   for i in range(contador2):
       for j in range(30):
           if (label_pk[i] == '[' + str(j+1) + ']'):
              label_pk[i] = r_matplot[j]    
   linha += 1; lines.insert(linha, f'label_pk = {label_pk}  #  Rotulos dos pontos-k de interesse a serem destacados na estrutura de bandas \n')
                         
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open('saida/Bandas/bandas.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------
executavel = 'saida/Bandas/bandas.py'
exec(open(executavel).read())
#------------------------------------

#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
