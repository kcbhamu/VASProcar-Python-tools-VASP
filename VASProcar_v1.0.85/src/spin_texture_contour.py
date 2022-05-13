
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

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = '_informacoes.py')

#======================================================================
# Analisando a variação das coordenadas dos pontos-k ==================
#======================================================================
execute_python_file(filename = '_var_kpoints.py')
#-----------------------------------------------

soma_1 = dk[0] + dk[1] + dk[2]
soma_2 = dk[3] + dk[4] + dk[5]

if (soma_1 != 2 and soma_2 != 2):
   print("===========================================================")
   print("!!! ERROR !!!                                              ")
   print("===========================================================")
   print("O calculo efetuado nao corresponde a um plano 2D na Zona de")
   print("Brillouin: Plano kikj com i,j = x,y,z  or  i,j = 1,2,3     ")
   print("Dica: -----------------------------------------------------")
   print("Para gerar o arquivo KPOINTS correto, utilize a opcao [888]")
   print("===========================================================")
   confirmacao = input (" ")
   exit()

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("Qual banda quer analisar? ====================================")
print ("##############################################################") 
Band = input (" "); Band = int(Band)
print (" ")

if (escolha == -1):
   print ("##############################################################")
   print ("Quanto a energia dos estados, o que vc deseja? ===============")
   print ("[0] Manter o valor padrao de saida do VASP ===================")
   print ("[1] Deslocar o nivel de Fermi para 0.0 eV ====================")
   print ("##############################################################") 
   esc_fermi = input (" "); esc_fermi = int(esc_fermi)
   print (" ") 

print ("##############################################################")
print ("Qual o numero de Curvas de Nivel que deseja obter? ===========")
print ("##############################################################")
n_contour = input (" "); n_contour = int(n_contour)
print(" ")

if (n_contour <= 0):
   n_contour = 1

print ("##############################################################")
print ("Com relacao as energias das Curvas de Nivel: =================")
print ("[0] Devem ser obtidas automaticamente pelo codigo ============")
print ("[1] Devem varrer um determinado range de energia =============")
print ("[2] Desejo especificar cada valor de energia manualmente =====")   
print ("##############################################################")
tipo_contour = input (" "); tipo_contour = int(tipo_contour)
print(" ")

if (tipo_contour == 1):    
   print ("##############################################################")
   print ("Escolha o intervalo de Energia a ser analisado: ============= ")
   print ("Digite como nos exemplos abaixo ============================= ")
   print ("--------------------------------------------------------------")
   print ("Energ_inicial Energ_final: -4.5 6.9                           ")
   print ("Energ_inicial Energ_final:  0.0 5.5                           ")
   print ("##############################################################") 
   print (" ")
   energ_i, energ_f = input ("Energ_inicial Energ_final: ").split()
   energ_i = float(energ_i)
   energ_f = float(energ_f)
   print (" ")

if (tipo_contour == 2):
   #-------------------------
   levels_n = [0.0]*n_contour
   #-------------------------
   print ("##############################################################")
   print ("Digite os valores de Energia como nos exemplos abaixo ======= ")
   print ("--------------------------------------------------------------")
   print ("Energias: -4.5 -2.0 -1.0  0.0  1.0  3.0 5.0                   ")
   print ("Energias:  0.2  0.5  0.78 1.23 9.97                           ")
   print ("--------------------------------------------------------------")
   print ("!!! Observacao importante !!! =============================== ")
   print ("Sempre digite os valores de energia em ordem crescente ====== ")
   print ("##############################################################") 
   print (" ")
   levels_n = input ("Energias: ").split()
   for i in range(n_contour):
       levels_n[i] = float(levels_n[i])
   print (" ")

#--------------------------------------------------------------------------   

if (escolha == -1):

   print ("##############################################################")
   print ("Deseja rotular as energias sobre as Curvas de Nivel? =========")
   print ("[0] NAO                                                       ")
   print ("[1] SIM                                                       ")
   print ("##############################################################")
   rot_energ = input (" "); rot_energ = int(rot_energ)   
   print (" ")
   
   print ("##############################################################")
   print ("O que vc deseja Plotar/Analisar? =============================")
   print ("Digite 0 para analisar todos os ions da rede =================")
   print ("Digite 1 para analisar ions selecionados =====================")
   print ("##############################################################")
   esc = input (" "); esc = int(esc)
   print (" ")
   
   if (esc == 1):

      #-------------------------
      sim_nao = ["nao"]*(ni + 1)  #  Inicialização do vetor sim_nao
      #-------------------------
      
      print ("##############################################################")
      print ("Os ions devem ser selecionados por meio de intervalos ======= ")
      print ("Quantos intervalos de ions vc ira fornecer abaixo? ===========")
      print ("##############################################################")
      loop = input (" "); loop = int(loop)
      print (" ")

      print ("##############################################################")
      print ("Escolha os intervalos de ions a serem analisados: =========== ")
      print ("Digite como nos exemplos abaixo ============================= ")
      print ("--------------------------------------------------------------")
      print ("ion_inicial ion_final: 3  3                                   ")
      print ("ion_inicial ion_final: 15 27                                  ")          
      print ("##############################################################") 
      print (" ")      

      for i in range (1,(loop+1)):

          print (f'{i} intervalo: =================================================')
          print (" ")
          loop_i, loop_f = input ("ion_inicial ion_final: ").split()
          loop_i = int(loop_i)
          loop_f = int(loop_f)
          print (" ")

          if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
             print (" ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("   ERRO: Os valores de ions informados estao incorretos   ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print (" ")
             
          for i in range(loop_i, (loop_f + 1)):
              sim_nao[i] = "sim"   

#-----------------------------------------------------------------------------

if (soma_1 == 2 or soma_2 == 2):
   #----------------------------------   
   if (soma_2 == 2 and escolha == -1):
      print ("##############################################################") 
      print ("## Escolha a dimensao dos eixos-k no Plot 3D: ============= ##")
      print ("##############################################################")
      print ("## [1] (kx,ky,kz) em unidades de 2pi/Param. =============== ##")
      print ("## [2] (kx,ky,kz) em unidades de 1/Angs. ================== ##")
      print ("## [3] (kx,ky,kz) em unidades de 1/nm. ==================== ##")  
   #----------------------------------
   if (soma_1 == 2 and soma_2 == 2 and escolha == -1):    
      print ("## [4] (k1,k2,k3) Coord. Diretas: K = k1*B1 + k2*B2 + k3*B3 ##")    
   #----------------------------------
   if (soma_2 == 2 and escolha == -1): 
      print ("##############################################################") 
      Dimensao = input (" "); Dimensao = int(Dimensao)
      print (" ")
   #----------------------------------
   if (soma_2 != 2):
      Dimensao = 4
   #----------------------------------   
   if (soma_1 != 2 and escolha == 1):
      Dimensao = 1
   #----------------------------------   
   if (soma_1 == 2 and soma_2 == 2 and escolha == 1):
      Dimensao = 4
   #----------------------------------   
     
   if (Dimensao < 4):
      if (dk[3] == 1 and dk[4] == 1): Plano_k = 1  #  Plano kxky
      if (dk[3] == 1 and dk[5] == 1): Plano_k = 2  #  Plano kxkz
      if (dk[4] == 1 and dk[5] == 1): Plano_k = 3  #  Plano kykz
   
   if (Dimensao == 4):
      if (dk[0] == 1 and dk[1] == 1): Plano_k = 1  #  Plano k1k2
      if (dk[0] == 1 and dk[2] == 1): Plano_k = 2  #  Plano k1k3
      if (dk[1] == 1 and dk[2] == 1): Plano_k = 3  #  Plano k2k3   

#-----------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------

if (escolha == 1):
   esc_fermi = 1
   rot_energ = 0
   esc = 0
   n_d = 101
   pulo = 0
   fator = 1.0
   transp = 1.0

if (esc_fermi == 0): dE_fermi = 0.0
if (esc_fermi == 1): dE_fermi = (Efermi)*(-1)     

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------
read_spin = 1
execute_python_file(filename = '_procar.py') 

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
                #------------------------------------------------------ 
                if (esc == 1):
                   temp_sn = sim_nao[ion_n]
                #------------------------------------------------------ 
                for orb_n in range(1,(n_orb+1)):
                    if (esc == 0 or (esc == 1 and temp_sn == "sim")):
                       tot_sx[wp][point_k][Band_n] = ( tot_sx[wp][point_k][Band_n] + Sx[wp][orb_n][point_k][Band_n][ion_n] )
                       tot_sy[wp][point_k][Band_n] = ( tot_sy[wp][point_k][Band_n] + Sy[wp][orb_n][point_k][Band_n][ion_n] )
                       tot_sz[wp][point_k][Band_n] = ( tot_sz[wp][point_k][Band_n] + Sz[wp][orb_n][point_k][Band_n][ion_n] )
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
# Copiando o codigo TESTE_SPIN.py para o diretório de saida -----------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

# Teste para saber se o arquivo Spin_Texture_Contour.py já se encontra no diretorio de saida
try: f = open(dir_files + '/output/Spin_Texture/Spin_Texture_Contour.py'); f.close(); os.remove(dir_files + '/output/Spin_Texture/Spin_Texture_Contour.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_spin_texture_contour.py'
destination = dir_files + '/output/Spin_Texture/Spin_Texture_Contour.py'
shutil.copyfile(source, destination)

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Spin_Texture_Contour.py possa ser executado isoladamente ---
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

file = open(dir_files + '/output/Spin_Texture/Spin_Texture_Contour.py', 'r')
lines = file.readlines()
file.close()

linha = 11

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'nk = {nk}  #  Numero de pontos-k do calculo \n')
linha += 1; lines.insert(linha, f'rot_energ = {rot_energ}  #  Escolha quanto a rotular as energias das Curvas de Nivel, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, f'fator = {fator}  #  Fator pelo qual o comprimento dos vetores de spin serao aumentados ou diminuidos \n')
linha += 1; lines.insert(linha, f'pulo = {pulo}  #  Numero de vetores de Spin que sao ignorados de forma intercalada ao longo do percurso da curva de nivel da banda \n')
linha += 1; lines.insert(linha, f'n_d = {n_d}  #  Dimensao-D (DxDxD) de interpolacao no plot \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'Plano_k = {Plano_k}  #  [1] Plano (kx,ky) ou (k1,k2); [2] Plano (kx,kz) ou (k1,k3); [3] Plano (ky,kz) ou (k2,k3) \n')
linha += 1; lines.insert(linha, f'transp = {transp}  #  Transparencia aplicada ao gradiente de cores do plot 2D das Curvas de Nivel \n')
linha += 1; lines.insert(linha, f'tipo_contour = {tipo_contour}  #  Forma de obtenção das energias das Curvas de Nivel: Onde [0] é automatico; [1] range de energia e [2] informado manualmente \n')
linha += 1; lines.insert(linha, f'n_contour = {n_contour}  #  Numero de Curvas de Nivel a serem obtidas \n')
linha += 1; lines.insert(linha, f'Efermi = {Efermi}  #  Valor da energia de Fermi obtida no arquivo OUTCAR \n')
linha += 1; lines.insert(linha, f'esc_fermi = {esc_fermi}  #  Escolha quanto aos valores de energia. onde: [0] adotar a saida do VASP e [1] adotar o nivel de Fermi como 0.0eV \n')
#--------------------------------
if (tipo_contour == 1):
   linha += 1; lines.insert(linha, f'energ_i = {energ_i}; energ_f = {energ_f}  #  Energia inicial e final do Range de energia das Curvas de Nivel \n')
if (tipo_contour == 2):
   linha += 1; lines.insert(linha, f'levels_n = {levels_n}  #  Valores das Curvas de Nivel especificadas manualmente \n')
if (tipo_contour < 2):
   linha += 1; lines.insert(linha, f'levels_n = [0.0, 0.0, 0.0, 0.0, 0.0]  #  Valores das Curvas de Nivel especificados manualmente \n')
#--------------------------------
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da banda sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Spin_Texture/Spin_Texture_Contour.py', 'w')
file.writelines(lines)
file.close()

#----------------------------------------------------------------------------
exec(open(dir_files + '/output/Spin_Texture/Spin_Texture_Contour.py').read())
#----------------------------------------------------------------------------
