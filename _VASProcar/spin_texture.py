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
# Verificando se a pasta "Spin_Texture" existe, se não existe ela é criada ---
#-----------------------------------------------------------------------------
if os.path.isdir("saida/Spin_Texture"):
   0 == 0
else:
   os.mkdir("saida/Spin_Texture")
#--------------------------------

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
print ("O que deseja analisar quanto a Textura de Spin? ==============")
print ("[1] Plot 2D em um Plano (Si_Sj com i,j = x,y,z) na ZB ========")
print ("[2] Plot 3D (Si_Sj_E com i,j = x,y,z) na ZB ==================")
print ("[3] Plot 4D (Sx_Sy_Sz_isosuperficie) na ZB ================== ")
print ("##############################################################") 
escolha_d = input (" "); escolha_d = int(escolha_d)  
print (" ")

if (escolha == 62):
   normalizacao = 1
   Dimensao = 1
   if (escolha_d == 2): n_d = 101
   if (escolha_d == 3): n_d = 31
   if (escolha_d == 3): n_iso = 15

if (escolha == -62):
   print ("##############################################################") 
   print ("## Escolha a dimensao dos eixos-k no Plot: ================ ##")
   print ("##############################################################")
   print ("## [1] (kx,ky,kz) em unidades de 2pi/Param. =============== ##")
   print ("## [2] (kx,ky,kz) em unidades de 1/Angs. ================== ##")
   print ("## [3] (kx,ky,kz) em unidades de 1/nm. ==================== ##") 
   print ("## [4] (k1,k2,k3) Coord. Diretas: K = k1*B1 + k2*B2 + k3*B3 ##")
   print ("## ======================================================== ##")
   print ("## !!!! Utilize a opcao [4] apenas no caso de B1, B2 e B3   ##")
   print ("## !!!! serem vetores cartesianos: [a,0,0] [0,a,0] [0,0,a]  ##")   
   print ("##############################################################") 
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print (" ")

if (Dimensao < 4):
   c1 = 'kx'; c2 = 'ky'; c3 = 'kz'
if (Dimensao == 4):
   c1 = 'k1'; c2 = 'k2'; c3 = 'k3'     

if (escolha_d != 3):
   print ("##############################################################")
   print ("## Qual plano deve ser visualizado no Plot? =============== ##")
   print ("##############################################################")
   print (f'## [1] Plano ({c1},{c2}) ====================================== ##')
   print (f'## [2] Plano ({c1},{c3}) ====================================== ##')
   print (f'## [3] Plano ({c2},{c3}) ====================================== ##')
   print ("##############################################################") 
   Plano_k = input (" "); Plano_k = int(Plano_k)
   print (" ")

if (escolha == -62):
   
   if (escolha_d == 2):     
      print ("##############################################################")  
      print ("Qual a dimensao-D (DxD) de interpolacao no plot da banda? ====")
      print ("Dica: Utilize 101 (Quanto maior mais preciso e pesado) =======")
      print ("##############################################################") 
      n_d = input (" "); n_d = int(n_d)  
      print (" ")
      
   # if (escolha_d == 3):      
   #    print ("##############################################################")  
   #    print ("Qual a dimensao-D (DxDxD) de interpolacao no plot da banda? ==")
   #    print ("Dica: Utilize 31 (Quanto maior mais preciso e pesado) ========")
   #    print ("##############################################################") 
   #    n_d = input (" "); n_d = int(n_d)  
   #    print (" ")     

print ("##############################################################")
print ("Qual banda quer analisar? ====================================")
print ("##############################################################") 
Band = input (" "); Band = int(Band)
print (" ")

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------

#------------------------------------
executavel = Diretorio + '/procar.py'
exec(open(executavel).read())
#------------------------------------  

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------   

tot_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sx[n_procar][nk][nb]
tot_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sy[n_procar][nk][nb]
tot_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sz[n_procar][nk][nb]

total_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sx[n_procar][nk][nb]
total_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sy[n_procar][nk][nb]
total_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sz[n_procar][nk][nb]

#  tot_si (i = x,y,z)   = Soma de todos os orbitais (para ions selecionados) de Sx
#  total_si (i = x,y,z) = Soma de todos os orbitais (para todos os ions) de Sx
                                              
#----------------------------------------------------------------------

for wp in range(1, (n_procar+1)):
    for point_k in range(1, (nk+1)):                                  
        for Band_n in range (1, (nb+1)):
            for ion_n in range (1, (ni+1)):
                for orb_n in range(1,(n_orb+1)):
                    tot_sx[wp][point_k][Band_n] = tot_sx[wp][point_k][Band_n] + Sx[wp][orb_n][point_k][Band_n][ion_n]
                    tot_sy[wp][point_k][Band_n] = tot_sy[wp][point_k][Band_n] + Sy[wp][orb_n][point_k][Band_n][ion_n]
                    tot_sz[wp][point_k][Band_n] = tot_sz[wp][point_k][Band_n] + Sz[wp][orb_n][point_k][Band_n][ion_n]      
 
            #----------------------------------------------------------           
            # Fim do Loop dos ions ------------------------------------
            #----------------------------------------------------------                 
        #----------------------------------------------------------
        # Fim do Loop das Bandas ----------------------------------
        #----------------------------------------------------------      
    #----------------------------------------------------------
    # Fim do Loop dos pontos-k --------------------------------
    #----------------------------------------------------------    
#----------------------------------------------------------
# Fim do Loop dos arquivos PROCAR -------------------------
#----------------------------------------------------------
    
#======================================================================
# Gravando os dados para o Plot da Textura de Spin ====================
#======================================================================

#---------------------------------------------------------
spin_3D = open("saida/Spin_Texture/Spin_Texture.dat", "w")
#---------------------------------------------------------
    
for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        if (Dimensao != 4):
           spin_3D.write(f'{kx[j][point_k]} {ky[j][point_k]} {kz[j][point_k]} {Energia[j][point_k][Band]} {tot_sx[j][point_k][Band]} ')
           spin_3D.write(f'{tot_sy[j][point_k][Band]} {tot_sz[j][point_k][Band]} \n')       
        if (Dimensao == 4):
           spin_3D.write(f'{kb1[j][point_k]} {kb2[j][point_k]} {kb3[j][point_k]} {Energia[j][point_k][Band]} {tot_sx[j][point_k][Band]} ')
           spin_3D.write(f'{tot_sy[j][point_k][Band]} {tot_sz[j][point_k][Band]} \n')
               
#--------------
spin_3D.close()
#--------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Spin_Texture_?D.py para o diretório de saida ------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

if (escolha_d == 1): name = '2D'
if (escolha_d == 2): name = '3D'
if (escolha_d == 3): name = '4D'

import shutil

# Teste para saber se o arquivo Spin_Texture_?D.py já se encontra no diretorio de saida
try: f = open('saida/Spin_Texture/Spin_Texture_' + name + '.py'); f.close(); os.remove('saida/Spin_Texture/Spin_Texture_' + name + '.py')
except: 0 == 0
   
source = Diretorio + '/plot/plot_spin_texture_' + name + '.py'
destination = 'saida/Spin_Texture/Spin_Texture_' + name + '.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Bandas.py possa ser executado isoladamente ---
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open('saida/Spin_Texture/Spin_Texture_' + name + '.py', 'r')
lines = file.readlines()
file.close()

if (escolha_d == 1): linha = 24
if (escolha_d == 2): linha = 17
if (escolha_d == 3): linha = 18

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
if (escolha_d != 3): linha += 1; lines.insert(linha, f'Plano_k = {Plano_k}  #  [1] Plano (kx,ky) ou (k1,k2); [2] Plano (kx,kz) ou (k1,k3); [3] Plano (ky,kz) ou (k2,k3) \n')
if (escolha_d == 2): linha += 1; lines.insert(linha, f'n_d = {n_d}  #  Dimensao-D (DxD) de interpolacao no plot da banda \n')
# if (escolha_d == 3): linha += 1; lines.insert(linha, f'n_d = {n_d}  #  Dimensao-D (DxDxD) de interpolacao no plot da banda \n')
if (escolha_d == 1): linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da banda sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, f'nk = {nk} \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open('saida/Spin_Texture/Spin_Texture_' + name + '.py', 'w')
file.writelines(lines)
file.close()

#------------------------------------------------------------------------
if (escolha_d == 1): executavel = 'saida/Spin_Texture/Spin_Texture_2D.py'
if (escolha_d == 2): executavel = 'saida/Spin_Texture/Spin_Texture_3D.py'
if (escolha_d == 3): executavel = 'saida/Spin_Texture/Spin_Texture_4D.py'
exec(open(executavel).read())
#------------------------------------------------------------------------
   
#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
