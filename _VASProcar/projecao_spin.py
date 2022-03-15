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

#-----------------------------------------------------------------
# Verificando se a pasta "Spin" existe, se não existe ela é criada
#-----------------------------------------------------------------
if os.path.isdir("saida/Spin"):
   0 == 0
else:
   os.mkdir("saida/Spin")
#------------------------

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
print ("######### Plot 2D das Componentes de Spin (Sx|Sy|Sz) #########")
print ("##############################################################") 
print (" ")

if (escolha == -2):
   
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
      print(" ")

   print ("##############################################################")
   print ("Digite o peso/tamanho das esferas na projecao: ===============")
   print ("Digite um valor entre 0.0 e 1.0 ==============================")
   print ("##############################################################")
   peso_total = input (" "); peso_total = float(peso_total)
   print(" ")

   print ("##############################################################")
   print ("Digite o valor de transparencia a ser aplicado nas projecoes: ")
   print ("Esta opcao e util para verificar sobreposicoes.               ")   
   print ("Digite um valor entre 0.0 e 1.0 ==============================")
   print ("==============================================================")
   print ("Dica: Quanto maior for a densidade de pontos-k, menor deve ser")
   print ("      o valor de transparencia utilizado, comece por 0.1 ==== ")
   print ("##############################################################")
   transp = input (" "); transp = float(transp)
   print(" ")    

   print ("##############################################################")
   print ("O que vc deseja Plotar/Analisar? =============================")
   print ("Digite 0 para analisar todos os ions da rede =================")
   print ("Digite 1 para analisar ions selecionados =====================")
   print ("##############################################################")
   esc = input (" "); esc = int(esc)

   if (esc == 1):

      sim_nao = ["nao"]*(ni + 1)             # Inicialização do vetor sim_nao
      
      print (" ")
      print ("##############################################################")
      print ("Especifique os ions selecionados em intervalos ===============")
      print ("Quantos intervalos de ions ira fornecer abaixo? ==============")
      print ("##############################################################")
      loop = input (" "); loop = int(loop)
      for i in range (1,(loop+1)):
          print (" ")
          print (f'{i} intervalo: ==============================================')
          print ("Digite o ion inicial do intervalo ============================")
          loop_i = input (" "); loop_i = int(loop_i)
          print ("Digite o ion final do intervalo ==============================")
          loop_f = input (" "); loop_f = int(loop_f)
          if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
             print ("")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("   ERRO: Os valores de ions informados estao incorretos   ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("")
          for i in range(loop_i, (loop_f + 1)):
              sim_nao[i] = "sim"                              # Escolha se serão Plotados/Analisados todos os ions ou não, nas projeções.

   print(" ")

if (escolha == 2):   
   Dimensao = 1
   peso_total = 1.0
   transp = 1.0
   esc = 0
   dest_k = 1
   
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

soma_sx = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(3+1)] for k in range(n_procar+1)]  # soma_sx[n_procar][3][nk][nb]
soma_sy = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(3+1)] for k in range(n_procar+1)]  # soma_sy[n_procar][3][nk][nb]
soma_sz = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(3+1)] for k in range(n_procar+1)]  # soma_sz[n_procar][3][nk][nb]    

tot_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sx[n_procar][nk][nb]
tot_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sy[n_procar][nk][nb]
tot_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                            # tot_sz[n_procar][nk][nb]

total_sx = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sx[n_procar][nk][nb]
total_sy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sy[n_procar][nk][nb]
total_sz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                          # total_sz[n_procar][nk][nb]

#  soma_sx[n_procar][1][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital S de Sx
#  soma_sx[n_procar][2][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Py ou P (lorbit = 10) de Sx
#  soma_sx[n_procar][3][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Pz ou D (lorbit = 10) de Sx
#  soma_sx[n_procar][4][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Px de Sx
#  soma_sx[n_procar][5][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dxy de Sx
#  soma_sx[n_procar][6][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dyz de Sx
#  soma_sx[n_procar][7][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dz2 de Sx
#  soma_sx[n_procar][8][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dxz de Sx
#  soma_sx[n_procar][9][nk][nb] = Soma da contrinuição de cada ion (selecionado) para o orbital Dx2 de Sx
#  tot_sx   = Soma de todos os orbitais (para ions selecionados) de Sx
#  total_sx = Soma de todos os orbitais (para todos os ions) de Sx

dpi = 2*3.1415926535897932384626433832795

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
# Plot das Projeções das Componentes de Spin (Sx,Sy,Sz) (GRACE) =======
#====================================================================== 
#======================================================================

print (" ")          
print ("================================")

for t in range (1,(3+1)):            # Loop para a analise das Projecoes
        
#-----------------------------------------------------------------------

    if (t == 1):
       #-----------------------------------------------
       projection = open("saida/Spin/Spin_Sx.agr", "w")
       #-----------------------------------------------
       print ("Analisando a Projecao Sx do Spin")
       letras = 'Sx'
    if (t == 2):
       #-----------------------------------------------
       projection = open("saida/Spin/Spin_Sy.agr", "w")
       #-----------------------------------------------
       print ("Analisando a Projecao Sy do Spin")
       letras = 'Sy'
    if (t == 3):
       #-----------------------------------------------
       projection = open("saida/Spin/Spin_Sz.agr", "w")
       #-----------------------------------------------
       print ("Analisando a Projecao Sz do Spin")
       letras = 'Sz'

# Escrita do arquivo ".agr" do GRACE ===================================

    projection.write("# Grace project file \n")
    projection.write("# written using VASProcar (https://github.com/Augusto-Dlelis/VASProcar-Tools-Python) \n")
    projection.write("# \n")
    projection.write("@version 50122 \n")   
    projection.write("@with g0 \n")
    projection.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
    projection.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    projection.write(f'@    xaxis  tick major {escala_x:.2f} \n')

    palavra = '"\\f{Symbol}2p/\\f{Times-Italic}a"'
    if (Dimensao == 1 and dest_k != 2): projection.write(f'@    xaxis  label {palavra} \n')
    if (Dimensao == 2 and dest_k != 2): projection.write(f'@    xaxis  label "(1/Angs.)" \n') 
    if (Dimensao == 3 and dest_k != 2): projection.write(f'@    xaxis  label "(1/nm)" \n')

    if (dest_k == 2):
       projection.write(f'@    xaxis  tick spec type both \n')
       projection.write(f'@    xaxis  tick spec {contador2} \n')
       for i in range (contador2):
           projection.write(f'@    xaxis  tick major {i}, {dest_pk[i]} \n')
           temp_r = label_pk[i]
           for j in range(30):
               if (temp_r == '[' + str(j+1) + ']'): temp_r = r_grace[j]                  
           projection.write(f'@    xaxis  ticklabel {i}, "{temp_r}" \n')
    
    projection.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    projection.write(f'@    yaxis  label "E-Ef (eV)" \n')
    
    projection.write(f'@    legend {fig_xmax + leg_x}, {fig_ymax + leg_y} \n')   

    for i in range (1,(3+1)):

        if (i == 1):
           grac='s0'; color = cor_spin[2]; legenda = letras + ' \\f{Symbol}\\c-\\C'   # Cor (Vermelho) da componente Up dos Spins Sx, Sy e Sz.
        if (i == 2):
           grac='s1'; color = cor_spin[3]; legenda = letras + ' \\f{Symbol}\\c/\\C'   # Cor (Azul) da componente Down dos Spins Sx, Sy e Sz.
        if (i == 3):
           grac='s2'; color = cor_spin[1]; legenda = ''                                    # Cor (Preto) da componente Nula dos Spins Sx, Sy e Sz.

        projection.write(f'@    {grac} type xysize \n')
        projection.write(f'@    {grac} symbol 1 \n')
        projection.write(f'@    {grac} symbol color {color} \n')
        projection.write(f'@    {grac} symbol fill color {color} \n')
        projection.write(f'@    {grac} symbol fill pattern 1 \n')
        projection.write(f'@    {grac} line type 0 \n')
        projection.write(f'@    {grac} line color {color} \n')
        if (i <= 3): projection.write(f'@    {grac} legend  "{legenda}" \n')

    for j in range(nb+1+contador2):

        if (j <= (nb-1)): color = 1 # cor Preta
        if (j == nb):     color = 2 # cor Vermelha
        if (j > nb):      color = 7 # Cor Cinza        
   
        projection.write(f'@    s{j+3} type xysize \n')
        projection.write(f'@    s{j+3} line type 1 \n')
        projection.write(f'@    s{j+3} line color {color} \n')         
           
    projection.write("@type xysize")
    projection.write(" \n")
                          
# Plot das Componentes de Spin (Sx,Sy,Sz) =============================

    for i in range (1,(3+1)):                                          # Busca em loop pelas componente up, down e nula (Sx,Sy,Sz)
      
#-----------------------------------------------------------------------

        for wp in range (1, (n_procar+1)):
            for point_k in range (1, (nk+1)):
                for Band_n in range (1, (nb+1)):
                    #----------------------------------
                    if (t == 1):
                       si = tot_sx[wp][point_k][Band_n]
                    if (t == 2):
                       si = tot_sy[wp][point_k][Band_n]
                    if (t == 3):
                       si = tot_sz[wp][point_k][Band_n]
                    #-------------------------------------------------------------------------------
                    if (wp == 1 and point_k == 1 and Band_n == 1):    
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} 0.0 \n')                       
                    if (i == 1 and si > 0.0):
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} {si} \n')
                    if (i == 2 and si < 0.0):
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} {si} \n')
                    if (i == 3 and si == 0.0):
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} {si} \n')
        #-------------------------------------------------------------------------------------------
        projection.write(" \n")  

# Plot da estrutura de Bandas =========================================
    
    for Band_n in range (1,(nb+1)):
        projection.write(" \n")
        for i in range (1,(n_procar+1)):
            for point_k in range (1,(nk+1)):
                projection.write(f'{xx[i][point_k]} {Energia[i][point_k][Band_n]} 0.0 \n')
                
# Destacando a energia de Fermi no plot das Texturas ==================

    projection.write(" \n")
    projection.write(f'{xx[1][1]} 0.0 0.0 \n')
    projection.write(f'{xx[n_procar][nk]} 0.0 0.0 \n')

# Destacando pontos-k de interesse no plot das Texturas ===============

    if (dest_k > 0):
       for loop in range (contador2):
           projection.write(" \n")
           projection.write(f'{dest_pk[loop]} {energ_min} 0.0 \n')
           projection.write(f'{dest_pk[loop]} {energ_max} 0.0 \n')

    #-----------------
    projection.close()
    #-----------------

#======================================================================
#======================================================================
# Plot das Projeções da Localização (Matplotlib) ======================
#====================================================================== 
#======================================================================

# Gravando a informação das bandas para o Plot das Projeções ==========
    
#-------------------------------------------------
bandas = open("saida/Spin/Bandas.dat", "w")
#-------------------------------------------------

for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        bandas.write(f'{xx[j][point_k]}')
        for Band_n in range (1,(nb+1)):
            bandas.write(f' {Energia[j][point_k][Band_n]}')
        bandas.write(f' \n')
                
#-------------
bandas.close()
#-------------

# Gravando a informação das componentes de Spin para o Plot das Projeções

#--------------------------------------
spin = open("saida/Spin/Spin.dat", "w")
#--------------------------------------

for k in range (1,(nb+1)):
    for i in range (1,(n_procar+1)):
        for j in range (1,(nk+1)):
            spin.write(f'{xx[i][j]} {Energia[i][j][k]}')
            #---------------------------------------------------------------------------------------
            if (tot_sx[i][j][k] > 0):  spin.write(f' {((dpi*tot_sx[i][j][k])**2)*peso_total}')
            if (tot_sx[i][j][k] <= 0): spin.write(f' 0.0')
            if (tot_sx[i][j][k] < 0):  spin.write(f' {((dpi*tot_sx[i][j][k])**2)*peso_total}')
            if (tot_sx[i][j][k] >= 0): spin.write(f' 0.0')             
            #---------------------------------------------------------------------------------------
            if (tot_sy[i][j][k] > 0):  spin.write(f' {((dpi*tot_sy[i][j][k])**2)*peso_total}')
            if (tot_sy[i][j][k] <= 0): spin.write(f' 0.0')
            if (tot_sy[i][j][k] < 0):  spin.write(f' {((dpi*tot_sy[i][j][k])**2)*peso_total}')
            if (tot_sy[i][j][k] >= 0): spin.write(f' 0.0') 
            #---------------------------------------------------------------------------------------
            if (tot_sz[i][j][k] > 0):  spin.write(f' {((dpi*tot_sz[i][j][k])**2)*peso_total}')
            if (tot_sz[i][j][k] <= 0): spin.write(f' 0.0')
            if (tot_sz[i][j][k] < 0):  spin.write(f' {((dpi*tot_sz[i][j][k])**2)*peso_total}')
            if (tot_sz[i][j][k] >= 0): spin.write(f' 0.0')
            spin.write(f' \n')    
                
#-----------
spin.close()
#-----------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Spin.py para o diretório de saida -----------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

import shutil

# Teste para saber se o arquivo Spin.py já se encontra no diretorio de saida
try: f = open('saida/Spin/Spin.py'); f.close(); os.remove('saida/Spin/Spin.py')
except: 0 == 0
   
source = Diretorio + '/plot/plot_projecao_spin.py'
destination = 'saida/Spin/Spin.py'
shutil.copyfile(source, destination)

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Spin.py possa ser executado isoladamente ---
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

file = open('saida/Spin/Spin.py', 'r')
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
linha += 1; lines.insert(linha, f'transp = {transp}  #  Transparencia aplicada ao plot das projecoes \n')
linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da projeção sera salvo, onde [0] = NAO e [1] = SIM \n')
linha += 1; lines.insert(linha, f'dest_k = {dest_k}  #  [0] Nao destacar nem rotular nenhum ponto-k; [1] Destacar automaticamente os pontos-k informados no KPOINTS; [2] Destacar e rotular os pontos-k a sua escolha \n')
linha += 1; lines.insert(linha, f'dest_pk = {dest_pk}  #  Coordenadas dos pontos-k de interesse a serem destacados no plot da projeção \n')

if (dest_k == 2): 
   for i in range(contador2):
       for j in range(30):
           if (label_pk[i] == '[' + str(j+1) + ']'):
              label_pk[i] = r_matplot[j]    
   linha += 1; lines.insert(linha, f'label_pk = {label_pk}  #  Rotulos dos pontos-k de interesse a serem destacados no plot da projeção \n')
                         
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open('saida/Spin/Spin.py', 'w')
file.writelines(lines)
file.close()

#--------------------------------
executavel = 'saida/Spin/Spin.py'
exec(open(executavel).read())
#--------------------------------

#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
