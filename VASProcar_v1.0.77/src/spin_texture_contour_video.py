
def execute_python_file(filename: str):
   return exec(open(main_dir + str(filename)).read(), globals())

#-----------------------------------------------------------------------------
# Verificando se a pasta "Spin_Texture" existe, se não existe ela é criada ---
#-----------------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Spin_Texture'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Spin_Texture')
#----------------------------------------------

#-----------------------------------------------------------------------------
# Verificando se a subpasta "figures" existe, se não existe ela é criada -----
#-----------------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Spin_Texture/figures'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Spin_Texture/figures')
#-------------------------------------------------------   

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = 'informacoes.py')

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

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
   
if (escolha == 1):
   Dimensao = 1
   n_d = 101
   pulo = 0
   transp = 1.0
   fator = 1.0
   tipo_contour = 0

if (escolha == -1):   

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
   print ("## ======================================================== ##")
   print ("## !!!!! Utilize a opcao [4] apenas no caso de (B1, B2, B3) ##")
   print ("## !!!!! serem vetores cartesianos: [a,0,0] [0,a,0] [0,0,a] ##")   
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

print ("##############################################################")
print ("## Qual componente ou vetor de Spin deve ser analisado? === ##")
print ("##############################################################")
print ("## [1] Sx     [2] Sy     [3] Sz =========================== ##")
print ("## [4] SxSy   [5] SxSz   [6] SySz ========================= ##")
print ("##############################################################") 
tipo_spin = input (" "); tipo_spin = int(tipo_spin)
print (" ")

if (escolha == -1):  

   print ("##############################################################")  
   print ("Qual a dimensao-D (DxD) de interpolacao no plot da banda? ====")
   print ("Dica: Utilize 101 (Quanto maior mais preciso e pesado) =======")
   print ("##############################################################") 
   n_d = input (" "); n_d = int(n_d)  
   print (" ")

   print ("##############################################################")  
   print ("Digite [0] caso deseje manter a densidade de vetores de Spin. ")
   print ("==============================================================")
   print ("Caso deseje reduzir a densidade, digite um numero inteiro > 0,")
   print ("correspondendo ao numero de vetores de Spin ignorados de forma")
   print ("intercalada ao longo do percurso da curva de nivel da banda.  ") 
   print ("##############################################################") 
   pulo = input (" "); pulo = int(pulo)  
   print (" ")
   if (pulo < 0): pulo = 0

   print ("##############################################################")  
   print ("Para manter o comprimento dos vetores de Spin, Digite 1.0     ")
   print ("Para aumentar o comprimento, Digite um valor Positivo >  1.0  ")
   print ("Para diminuir o comprimento, Digite um valor Negativo < -1.0  ")
   print ("==============================================================")
   print ("Estes valores correspondem a quantas vezes, o comprimento do  ") 
   print ("vetor sera multiplicado (aumentado) ou dividido (diminuido).  ")
   print ("##############################################################")    
   fator = input (" "); fator = float(fator)  
   print (" ")

   print ("##############################################################")
   print ("Digite o valor de transparencia [0.0 a 1.0] a ser aplicada aos")
   print ("vetores de Spin, quanto menor o valor mais suaves serao as    ")
   print ("cores, quanto maior mais intensas serao.                      ")
   print ("##############################################################")
   transp = input (" "); transp = float(transp)
   print(" ")

print ("##############################################################")
print ("Quantas figuras deseja que aparecam por segundo no video? ====")
print ("Dica: Escolha entre 1 e 8 ====================================")
print ("##############################################################")
n_fig = input (" "); n_fig = int(n_fig)  
print (" ")
   
if (n_fig <= 0): n_fig = 1

save_png = 1
save_pdf = 0
save_eps = 0   

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------
execute_python_file(filename = 'procar.py') 

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

#--------------------------------------------------------------------
spin = open(dir_files + '/output/Spin_Texture/Spin_Texture.dat', 'w')
#--------------------------------------------------------------------
    
for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        if (Dimensao != 4):
           spin.write(f'{kx[j][point_k]} {ky[j][point_k]} {kz[j][point_k]} {Energia[j][point_k][Band]} {tot_sx[j][point_k][Band]} ')
           spin.write(f'{tot_sy[j][point_k][Band]} {tot_sz[j][point_k][Band]} \n')       
        if (Dimensao == 4):
           spin.write(f'{kb1[j][point_k]} {kb2[j][point_k]} {kb3[j][point_k]} {Energia[j][point_k][Band]} {tot_sx[j][point_k][Band]} ')
           spin.write(f'{tot_sy[j][point_k][Band]} {tot_sz[j][point_k][Band]} \n')
               
#-----------
spin.close()
#-----------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Spin_Texture_Video.py para o diretório de saida ---
#----------------------------------------------------------------------
#----------------------------------------------------------------------

# Teste para saber se o arquivo Spin_Texture_Video.py já se encontra no diretorio de saida
try: f = open(dir_files + '/output/Spin_Texture/Spin_Texture_Video.py'); f.close(); os.remove(dir_files + '/output/Spin_Texture/Spin_Texture_Video.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_spin_texture_contour_video.py'
destination = dir_files + '/output/Spin_Texture/Spin_Texture_Video.py'
shutil.copyfile(source, destination)

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Spin_Texture_Video.py possa ser executado isoladamente ---
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

file = open(dir_files + '/output/Spin_Texture/Spin_Texture_Video.py', 'r')
lines = file.readlines()
file.close()

linha = 11

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'nk = {nk}  #  Numero de pontos-k do calculo \n')
linha += 1; lines.insert(linha, f'Band = {Band}  #  Banda que esta sendo analisada \n')
linha += 1; lines.insert(linha, f'fator = {fator}  #  Fator pelo qual o comprimento dos vetores de spin serao aumentados ou diminuidos \n')
linha += 1; lines.insert(linha, f'pulo = {pulo}  #  Numero de vetores de Spin que sao ignorados de forma intercalada ao longo do percurso da curva de nivel da banda \n')
linha += 1; lines.insert(linha, f'n_d = {n_d}  #  Dimensao-D (DxDxD) de interpolacao no plot \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'Plano_k = {Plano_k}  #  [1] Plano (kx,ky) ou (k1,k2); [2] Plano (kx,kz) ou (k1,k3); [3] Plano (ky,kz) ou (k2,k3) \n')
linha += 1; lines.insert(linha, f'transp = {transp}  #  Transparencia aplicada ao gradiente de cores do plot 2D das Curvas de Nivel \n')
linha += 1; lines.insert(linha, f'tipo_spin = {tipo_spin}  #  Componente ou Vetor de Spin a ser analisado, onde: [1] Sx; [2] Sy; [3] Sz; [4] SxSy; [5] SxSz; [6] SySz \n')
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
linha += 1; lines.insert(linha, f'n_fig = {n_fig}  #  Numero de figuras que aparecem no video por segundo \n')
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da banda sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Spin_Texture/Spin_Texture_Video.py', 'w')
file.writelines(lines)
file.close()

#--------------------------------------------------------------------------
exec(open(dir_files + '/output/Spin_Texture/Spin_Texture_Video.py').read())
#--------------------------------------------------------------------------
