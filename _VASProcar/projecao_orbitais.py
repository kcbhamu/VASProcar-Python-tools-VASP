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

#---------------------------------------------------------------------
# Verificando se a pasta "Orbitais" existe, se não existe ela é criada
#---------------------------------------------------------------------
if os.path.isdir("saida/Orbitais"):
   0 == 0
else:
   os.mkdir("saida/Orbitais")
#----------------------------

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
print ("############### Projecao dos Orbitais (S,P,D): ###############")
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
             print (" ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("   ERRO: Os valores de ions informados estao incorretos   ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print (" ")
          for i in range(loop_i, (loop_f + 1)):
              sim_nao[i] = "sim"          

   print (" ")

if (escolha == 2):   
   Dimensao = 1
   peso_total = 1.0
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
   
soma_orb = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(n_orb+1)] for k in range(n_procar+1)]                    # soma_orb[n_procar][n_orb][nk][nb]
total = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                                                 # tot[n_procar][nk][nb]
 
#  orb      = [procar.py] Parcela do Orbital (S, P ou D) referente a cada ion "ni".
#  soma_orb = Soma do Orbital (S, P ou D) sobre todos os ions "ni" selecionados.
#  tot      = Soma sobre todos os orbitais e todos os ions.

orbital_S   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_P   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_D   = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Px  = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Py  = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Pz  = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Dxy = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Dyz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Dz2 = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Dxz = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]
orbital_Dx2 = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]

dpi = 2*3.1415926535897932384626433832795

#======================================================================
# Calculo do peso (% de contribuição) de cada orbital =================
#====================================================================== 

for wp in range(1, (n_procar+1)):
    for point_k in range(1, (nk+1)):                                  
        for Band_n in range (1, (nb+1)):
            for ion_n in range (1, (ni+1)):            
                #------------------------------------------------------                
                if (esc == 1):
                   temp_sn = sim_nao[ion_n]
                #------------------------------------------------------                              
                for orb_n in range(1,(n_orb+1)):
                    total[wp][point_k][Band_n] = total[wp][point_k][Band_n] + orb[wp][orb_n][point_k][Band_n][ion_n]
                    if (esc == 0 or (esc == 1 and temp_sn == "sim")):
                       soma_orb[wp][orb_n][point_k][Band_n] = soma_orb[wp][orb_n][point_k][Band_n] + orb[wp][orb_n][point_k][Band_n][ion_n]                    
            #----------------------------------------------------------           
            # Fim do Loop dos ions ------------------------------------
            #----------------------------------------------------------  
            for orb_n in range (1, (n_orb+1)):
                if (total[wp][point_k][Band_n] != 0.0):
                   soma_orb[wp][orb_n][point_k][Band_n] = ( soma_orb[wp][orb_n][point_k][Band_n]/total[wp][point_k][Band_n] )*peso_total                   
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
# Plot das Projeções dos Orbitais (GRACE) =============================
#====================================================================== 
#======================================================================
                          
if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

# Rotulo dos Orbitais ================================================= 

t_orb = [0]*(12)
t_orb[1] = 'S'; t_orb[2] = 'P'; t_orb[3] = 'D'; t_orb[4] = 'Px'; t_orb[5] = 'Py'; t_orb[6] = 'Pz'
t_orb[7] = 'Dxy'; t_orb[8] = 'Dyz'; t_orb[9] = 'Dz2'; t_orb[10] = 'Dxz'; t_orb[11] = 'Dx2'

#======================================================================

print (" ")          
print ("============================================")

for i in range (1,(loop+1)):     # Loop para a analise das Projecoes
        
#-----------------------------------------------------------------------

    if (i == 1):
       #----------------------------------------------------------
       projection = open("saida/Orbitais/Orbitais_S_P_D.agr", "w")
       #----------------------------------------------------------
       print ("Analisando a Projecao dos Orbitais (S, P, D)")        
       s = 1; t = (3+1)
       
    if (i == 2):
       #------------------------------------------------------
       projection = open("saida/Orbitais/Orbitais_P.agr", "w")     
       #------------------------------------------------------
       print ("Analisando a Projecao dos Orbitais (Px, Py, Pz)") 
       s = 4; t = (6+1)
       
    if (i == 3):
       #------------------------------------------------------
       projection = open("saida/Orbitais/Orbitais_D.agr", "w")
       #------------------------------------------------------
       print ("Analisando a Projecao dos Orbitais (Dxy, Dyz, Dz2, Dxz, Dx2)") 
       s = 7; t = (11+1)   

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
    if (Dimensao == 2 and dest_k != 2): projection.write(f'@    xaxis  label "1/Angs." \n') 
    if (Dimensao == 3 and dest_k != 2): projection.write(f'@    xaxis  label "1/nm" \n')

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
       
    for j in range (s,t):
          
        if (j == (s+0)): grac='s0'; color = cor_orb[j]        # Cor dos Orbitais (S,Px,Dxy)
        if (j == (s+1)): grac='s1'; color = cor_orb[j]        # Cor dos Orbitais (P,Py,Dyz)
        if (j == (s+2)): grac='s2'; color = cor_orb[j]        # Cor dos Orbitais (D,Pz,Dz2)
        if (j == (s+3)): grac='s3'; color = cor_orb[j]        # Cor do Orbital Dxz
        if (j == (s+4)): grac='s4'; color = cor_orb[j]        # Cor do Orbital Dx2
           
        projection.write(f'@    {grac} type xysize \n')
        projection.write(f'@    {grac} symbol 1 \n')
        projection.write(f'@    {grac} symbol color {color} \n')
        projection.write(f'@    {grac} symbol fill color {color} \n')
        projection.write(f'@    {grac} symbol fill pattern 1 \n')
        projection.write(f'@    {grac} line type 0 \n')
        projection.write(f'@    {grac} line color {color} \n')
        projection.write(f'@    {grac} legend  "{t_orb[j]}" \n')

    for j in range(nb+1+contador2):

        if (j <= (nb-1)): color = 1 # cor Preta
        if (j == nb):     color = 2 # cor Vermelha
        if (j > nb):      color = 7 # Cor Cinza
   
        projection.write(f'@    s{j+(t-s)} type xysize \n')
        projection.write(f'@    s{j+(t-s)} line type 1 \n')
        projection.write(f'@    s{j+(t-s)} line color {color} \n') 

    projection.write("@type xysize")
    projection.write(" \n")
      
# Plot dos Orbitais ===================================================

    for j in range (s,t):

        for wp in range (1, (n_procar+1)):
            for point_k in range (1, (nk+1)):
                for Band_n in range (1, (nb+1)):
                    #------------------------------------------------------
                    if (j == 1): # Orbital S
                       orbital = soma_orb[wp][1][point_k][Band_n]
                       orbital_S[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    #-------------------- lorbit = 10 ---------------------
                    if (j == 2 and lorbit == 10): # Orbital P
                       orbital = soma_orb[wp][2][point_k][Band_n]
                       orbital_P[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 3 and lorbit == 10): # Orbital D
                       orbital = soma_orb[wp][3][point_k][Band_n]
                       orbital_D[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    #-------------------- lorbit >= 11 --------------------                     
                    if (j == 2 and lorbit >= 11): # Orbital P = Px + Py + Pz
                       orbital = soma_orb[wp][2][point_k][Band_n] + soma_orb[wp][3][point_k][Band_n] + soma_orb[wp][4][point_k][Band_n]
                       orbital_P[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 3 and lorbit >= 11): # Orbital D = Dxy + Dyz + Dz2 + Dxz + Dx2
                       orbital = soma_orb[wp][5][point_k][Band_n] + soma_orb[wp][6][point_k][Band_n] + soma_orb[wp][7][point_k][Band_n] + soma_orb[wp][8][point_k][Band_n] + soma_orb[wp][9][point_k][Band_n]
                       orbital_D[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    #------------------------------------------------------
                    if (j == 4): # Orbital Px 
                       orbital = soma_orb[wp][4][point_k][Band_n]
                       orbital_Px[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 5): # Orbital Py 
                       orbital = soma_orb[wp][2][point_k][Band_n]
                       orbital_Py[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 6): # Orbital pz 
                       orbital = soma_orb[wp][3][point_k][Band_n]
                       orbital_Pz[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    #------------------------------------------------------
                    if (j == 7): # Orbital Dxy 
                       orbital = soma_orb[wp][5][point_k][Band_n]
                       orbital_Dxy[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 8): # Orbital Dyz 
                       orbital = soma_orb[wp][6][point_k][Band_n]
                       orbital_Dyz[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 9): # Orbital Dz2 
                       orbital = soma_orb[wp][7][point_k][Band_n]
                       orbital_Dz2[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 10): # Orbital Dxz 
                       orbital = soma_orb[wp][8][point_k][Band_n]
                       orbital_Dxz[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    if (j == 11): # Orbital Dx2 
                       orbital = soma_orb[wp][9][point_k][Band_n]
                       orbital_Dx2[wp][point_k][Band_n] = ((dpi*orbital)**2)*peso_total
                    #------------------------------------------------------                       
                    if (wp == 1 and point_k == 1 and Band_n == 1):    
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} 0.0 \n')
                    if (orbital > 0.0):    
                       projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} {orbital} \n')

        projection.write(" \n")
       
# Plot da estrutura de Bandas =========================================
    
    for Band_n in range (1,(nb+1)):
        projection.write(" \n")
        for i in range (1,(n_procar+1)):
            for point_k in range (1,(nk+1)):
                projection.write(f'{xx[i][point_k]} {Energia[i][point_k][Band_n]} 0.0 \n')

# Destacando a energia de Fermi na estrutura de Bandas ================

    projection.write(" \n")
    projection.write(f'{xx[1][1]} 0.0 0.0 \n')
    projection.write(f'{xx[n_procar][nk]} 0.0 0.0 \n')

# Destacando pontos-k de interesse na estrutura de Bandas =============

    if (dest_k > 0):
       for loop in range (contador2):
           projection.write(" \n")
           projection.write(f'{dest_pk[loop]} {energ_min} 0.0 \n')
           projection.write(f'{dest_pk[loop]} {energ_max} 0.0 \n')

    #-----------------
    projection.close()
    #-----------------

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(".... Quase concluido ....")
print(".........................")
    
#======================================================================
#======================================================================
# Plot das Projeções dos Orbitais (Matplotlib) ========================
#====================================================================== 
#======================================================================

# Gravando a informação das bandas para o Plot das Projeções ==========
    
#-------------------------------------------------
bandas = open("saida/Orbitais/Bandas.dat", "w")
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

# Gravando a informação de cada orbital para o Plot das Projeções

#-------------------------------------------------
orbital = open("saida/Orbitais/Orbitais.dat", "w")
#-------------------------------------------------

for k in range (1,(nb+1)):
    for i in range (1,(n_procar+1)):
        for j in range (1,(nk+1)):
            orbital.write(f'{xx[i][j]} {Energia[i][j][k]}')
            orbital.write(f' {orbital_S[i][j][k]} {orbital_P[i][j][k]} {orbital_D[i][j][k]}')
            if (lorbit > 10):
               orbital.write(f' {orbital_Px[i][j][k]} {orbital_Py[i][j][k]} {orbital_Pz[i][j][k]}')
               orbital.write(f' {orbital_Dxy[i][j][k]} {orbital_Dyz[i][j][k]} {orbital_Dz2[i][j][k]} {orbital_Dxz[i][j][k]} {orbital_Dx2[i][j][k]}')             
            orbital.write(f' \n')
                
#--------------
orbital.close()
#--------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo orbitais.py para o diretório de saida -------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

import shutil

# Teste para saber se o arquivo orbitais.py já se encontra no diretorio de saida
try: f = open('saida/Orbitais/orbitais.py'); f.close(); os.remove('saida/Orbitais/orbitais.py')
except: 0 == 0
   
source = Diretorio + '/plot_projecao_orbitais.py'
destination = 'saida/Orbitais/plot_projecao_orbitais.py'
shutil.copyfile(source, destination)
os.rename('saida/Orbitais/plot_projecao_orbitais.py', 'saida/Orbitais/orbitais.py')

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código orbitais.py possa ser executado isoladamente ---
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

file = open('saida/Orbitais/orbitais.py', 'r')
lines = file.readlines()
file.close()

linha = 14

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}; nk  = {nk}; nb = {nb}; energ_min = {energ_min}; energ_max = {energ_max}; lorbit = {lorbit} \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
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

file = open('saida/Orbitais/orbitais.py', 'w')
file.writelines(lines)
file.close()

#----------------------------------------------
executavel = 'saida/Orbitais/orbitais.py'
exec(open(executavel).read())
#----------------------------------------------

#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
