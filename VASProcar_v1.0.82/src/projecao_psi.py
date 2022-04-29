
def execute_python_file(filename: str):
   return exec(open(main_dir + str(filename)).read(), globals())

#----------------------------------------------------------------
# Verificando se a pasta "Psi" existe, se não existe ela é criada
#----------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Psi'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Psi')
#-------------------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = 'informacoes.py')

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("################## Projecao dos estados Psi ##################")
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
      print(" ")

   print ("##############################################################")
   print ("Digite o peso/tamanho das esferas na projecao: ===============")
   print ("Digite um valor entre 0.0 e 1.0 ==============================")
   print ("##############################################################")
   peso_total = input (" "); peso_total = float(peso_total)
   print(" ")

   print ("##############################################################")
   print ("Digite o valor de transparencia a ser aplicado nas projecoes: ")
   print ("Esta opcao e util para verificar a sobreposicao de orbitais.  ")   
   print ("Digite um valor entre 0.0 e 1.0 ==============================")
   print ("==============================================================")
   print ("Dica: Quanto maior for a densidade de pontos-k, menor deve ser")
   print ("      o valor de transparencia utilizado, comece por 0.1 ==== ")
   print ("##############################################################")
   transp = input (" "); transp = float(transp)
   print(" ")   

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------

if (lorbit == 10): n_orb = 3
if (lorbit >= 11): n_orb = 9

ion_orb = [[[0]*(n_orb+1) for i in range(ni+1)] for j in range(5+1)]  #  ion_orb[n_psi][ni][n_orb]

psi = [[[[0.0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)] for k in range(5+1)]  #  psi[n_psi][n_procar][nk][nb]          
est_psi = [[[[0.0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)] for k in range(5+1)]  #  est_psi[n_psi][n_procar][nk][nb]
estado_psi = [[[[0.0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)] for k in range(5+1)]  #  estado_psi[n_psi][n_procar][nk][nb]
total = [[[0.0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]  #  total[n_procar][nk][nb] 

l_psi = ['null']*(5+1)
dpi = 2*3.1415926535897932384626433832795

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("Quantos estados Psi deseja analisar? =========================")
print (" ========= (Sao permitidos no maximo 5 estados Psi) ========= ")
print ("##############################################################")
n_psi = input (" "); n_psi = int(n_psi)
print(" ")

if (n_psi <= 0): n_psi = 1
if (n_psi > 5): n_psi = 5

for i in range(1,(n_psi+1)):
    print (f'Digite o rotulo do estado_Psi {i}: =============================')
    l_psi[i] = input ("rotulo: "); l_psi[i] = str(l_psi[i])
    print(" ")

if (n_psi <= 0): n_psi = 1
if (n_psi > 5): n_psi = 5

print ("##############################################################")
print ("Para definir um estado Psi, voce deve informar um determinado ")
print ("intervalo de ions, e tambem informar quais orbitais devem ser ")
print ("incluidos neste intervalo.                                    ")
print ("==============================================================")
print ("Para um dado estado Psi, voce pode informar quantos intervalos")
print ("de ions achar necessario.                                     ")
print ("==============================================================")
print ("Use a nomenclatura abaixo para designar os Orbitais:          ")
if (lorbit == 10):
   print ("s p d                                                         ")
if (lorbit >= 11):
   print ("s p d px py pz dxy dyz dz2 dxz dx2                            ")
print ("==============================================================")
print ("Exemplos:                                                     ")
if (lorbit == 10):
   print ("ion_inicial ion_final orbitais: 3 3  S P D                    ")
   print ("ion_inicial ion_final orbitais: 5 14 S P                      ")
if (lorbit >= 11):
   print ("ion_inicial ion_final orbitais: 15 27 S Px Py Pz Dxy          ")  
   print ("ion_inicial ion_final orbitais: 35 78 S Pz Dxy Dyz Dz2 Dxz Dx2")
   print ("ion_inicial ion_final orbitais: 5  9  S P D                   ")
   print ("##############################################################")
print(" ")

for i in range(1,(n_psi+1)):
    #--------------------------------------------------------------------------
    print ("##############################################################")
    print (f'Escolha os ions e orbitais compoem o estado Psi {i} ============')         
    print ("--------------------------------------------------------------")
    print (f'Quantos intervalos_de_ions deseja fornecer ao estado_psi {i}?   ')
    print ("##############################################################")   
    loop = input (" "); loop = int(loop)
    print (" ")

    for j in range (1,(loop+1)):
        #--------------------------------------------------------------------------
        print (f'Informe o {j} intervalo_de_ions do estado_psi_{i} ==============')
        print (" ")
        psi_io = input ("ion_inicial ion_final orbitais: ").split()
        print (" ")
        #----------------------
        loop_i = int(psi_io[0])
        loop_f = int(psi_io[1])
        #----------------------
        if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
           print (" ")
           print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
           print ("   ERRO: Os valores de ions informados estao incorretos   ")
           print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
           print (" ")
           exit()
        #----------------------   
        loop_o = len(psi_io) -2
        #----------------------
        
        for p in range(loop_i,(loop_f+1)):
            for t in range(1,(loop_o+1)):
                #------------------------
                if (lorbit == 10):                   
                   if (psi_io[t+1] == 's' or psi_io[t+1] == 'S'): ion_orb[i][p][1] = 1                    
                   if (psi_io[t+1] == 'p' or psi_io[t+1] == 'P'): ion_orb[i][p][2] = 1                      
                   if (psi_io[t+1] == 'd' or psi_io[t+1] == 'D'): ion_orb[i][p][3] = 1
                #------------------------      
                if (lorbit >= 11):                   
                   if (psi_io[t+1] == 's' or psi_io[t+1] == 'S'): ion_orb[i][p][1] = 1                      
                   if (psi_io[t+1] == 'p' or psi_io[t+1] == 'P'): ion_orb[i][p][2] = 1; ion_orb[i][p][3] = 1; ion_orb[i][p][4] = 1                      
                   if (psi_io[t+1] == 'd' or psi_io[t+1] == 'D'): ion_orb[i][p][5] = 1; ion_orb[i][p][6] = 1; ion_orb[i][p][7] = 1; ion_orb[i][p][8] = 1; ion_orb[i][p][9] = 1                      
                   if (psi_io[t+1] == 'px' or psi_io[t+1] == 'Px' or psi_io[t+1] == 'PX'): ion_orb[i][p][2] = 1                      
                   if (psi_io[t+1] == 'py' or psi_io[t+1] == 'Py' or psi_io[t+1] == 'PY'): ion_orb[i][p][3] = 1                      
                   if (psi_io[t+1] == 'pz' or psi_io[t+1] == 'Pz' or psi_io[t+1] == 'PZ'): ion_orb[i][p][4] = 1                      
                   if (psi_io[t+1] == 'dxy' or psi_io[t+1] == 'Dxy' or psi_io[t+1] == 'DXY'): ion_orb[i][p][5] = 1                      
                   if (psi_io[t+1] == 'dyz' or psi_io[t+1] == 'Dyz' or psi_io[t+1] == 'DYZ'): ion_orb[i][p][6] = 1                      
                   if (psi_io[t+1] == 'dz2' or psi_io[t+1] == 'Dz2' or psi_io[t+1] == 'DZ2'): ion_orb[i][p][7] = 1                      
                   if (psi_io[t+1] == 'dxz' or psi_io[t+1] == 'Dxz' or psi_io[t+1] == 'DXZ'): ion_orb[i][p][8] = 1                      
                   if (psi_io[t+1] == 'dx2' or psi_io[t+1] == 'Dx2' or psi_io[t+1] == 'DX2'): ion_orb[i][p][9] = 1 

temp = [0.0]*(n_orb)

print ("##############################################################")
print ("Confira os estados informados antes de prosseguir:            ")
print ("Onde [0] = NAO e [1] = SIM                                    ")
print ("##############################################################")

for i in range(1,(n_psi+1)):
    print (" ")
    print ("------------")
    print (f'Estado Psi {i}')
    print ("------------")
    for j in range(1,(ni+1)):
        for k in range (1,(n_orb+1)):
            temp[k-1] = ion_orb[i][j][k]
        if (lorbit == 10):
           print (f'ion {j}: orbitais S[{temp[0]}] P[{temp[1]}] D[{temp[2]}]')
        if (lorbit >= 11):
           print (f'ion {j}: orbitais S[{temp[0]}] Px[{temp[1]}] Py[{temp[2]}] Pz[{temp[3]}] Dxy[{temp[4]}] Dyz[{temp[5]}] Dz2[{temp[6]}] Dxz[{temp[7]}] Dx2[{temp[8]}]')   
          
print (" ")
print ("##############################################################")
print ("Atencao: Caso esteja tudo certo com os estados Psi informados ")
print ("         aperte [ENTER] para continuar.                       ")
print ("##############################################################")
confirmacao = input (" "); confirmacao = str(confirmacao)

if (escolha == 1):   
   Dimensao = 1
   peso_total = 1.0
   transp = 1.0
   dest_k = 1

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------
execute_python_file(filename = 'procar.py')

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------         
   
# color_SPD  = [0]*n_procar*nk*nb  # color_SPD[n_procar*nk*nb]
# color_P    = [0]*n_procar*nk*nb  # color_P[n_procar*nk*nb]
# color_D    = [0]*n_procar*nk*nb  # color_D[n_procar*nk*nb] 

#======================================================================
# Calculo do peso (% de contribuição) de cada estado PSi ==============
#======================================================================

for wp in range(1, (n_procar+1)):
    for k in range(1,(nk+1)):                                  
        for b in range (1,(nb+1)):
            for i in range (1,(ni+1)):                                       
                for o in range(1,(n_orb+1)):
                    total[wp][k][b] = total[wp][k][b] + orb[wp][o][k][b][i]
                    #-----------------------------------------------------------------------------------------------
                    for p in range(1,(n_psi+1)):
                        if (ion_orb[p][i][o] == 1):
                           psi[p][wp][k][b] = psi[p][wp][k][b] + orb[wp][o][k][b][i]                
            #----------------------------------------------------------           
            # Fim do Loop dos ions ------------------------------------
            #----------------------------------------------------------  
            for p in range (1,(n_psi+1)):
                if (total[wp][k][b] != 0.0):
                   psi[p][wp][k][b] = ( psi[p][wp][k][b]/total[wp][k][b] )*peso_total                 
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
execute_python_file(filename = 'label.py')



#======================================================================
#======================================================================
# Plot das Projeções dos estados Psi (GRACE) ==========================
#====================================================================== 
#======================================================================
                          
print (" ")          
print ("============================================")

#----------------------------------------------------------------
projection = open(dir_files + '/output/Psi/Estados_Psi.agr', 'w')    
#----------------------------------------------------------------

print ("Analisando a Projecao dos estados Psi")         

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
       for j in range(34):
           if (temp_r == '#' + str(j+1)): temp_r = r_grace[j]                  
       projection.write(f'@    xaxis  ticklabel {i}, "{temp_r}" \n')

projection.write(f'@    yaxis  tick major {escala_y:.2f} \n')
projection.write(f'@    yaxis  label "E-Ef (eV)" \n')

projection.write(f'@    legend loctype world \n')
projection.write(f'@    legend {x_inicial}, {y_final} \n')
projection.write(f'@    legend box fill pattern 4 \n')
projection.write(f'@    legend length 1 \n')

for j in range (1,(n_psi+1)):

    legend = l_psi[j]; color = cor_orb[j+6]  #  Cor do estado Psi
    grac = 's' + str(j-1)
          
    projection.write(f'@    {grac} type xysize \n')
    projection.write(f'@    {grac} symbol 1 \n')
    projection.write(f'@    {grac} symbol color {color} \n')
    projection.write(f'@    {grac} symbol fill color {color} \n')
    projection.write(f'@    {grac} symbol fill pattern 1 \n')
    projection.write(f'@    {grac} line type 0 \n')
    projection.write(f'@    {grac} line color {color} \n')   
    projection.write(f'@    {grac} legend  "{legend}" \n')
                     
number = 0

for j in range(nb+1+contador2):

    number += 1

    if (j <= (nb-1)): color = 1 # cor Preta
    if (j == nb):     color = 2 # cor Vermelha
    if (j > nb):      color = 7 # Cor Cinza
   
    projection.write(f'@    s{j + n_psi} type xysize \n')
    projection.write(f'@    s{j + n_psi} line type 1 \n')
    projection.write(f'@    s{j + n_psi} line color {color} \n') 

projection.write("@type xysize")
projection.write(" \n")
      
# Plot dos estados Psi ================================================

for j in range (1,(n_psi+1)):      
    for wp in range (1,(n_procar+1)):
        for point_k in range (1,(nk+1)):
            for Band_n in range (1,(nb+1)):
                #----------------------------------------------------------------     
                estado = psi[j][wp][point_k][Band_n]
                est_psi[j][wp][point_k][Band_n] = estado
                estado_psi[j][wp][point_k][Band_n] = ((dpi*estado)**2)*peso_total         
                #----------------------------------------------------------------          
                if (wp == 1 and point_k == 1 and Band_n == 1):    
                   projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} 0.0 \n')
                if (estado > 0.0):    
                   projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} {estado} \n')

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


    
#======================================================================
#======================================================================
# Plot das Projeções dos Orbitais (Matplotlib) ========================
#====================================================================== 
#======================================================================

# Gravando a informação das bandas para o Plot das Projeções ==========
    
#-------------------------------------------------------
bandas = open(dir_files + '/output/Psi/Bandas.dat', 'w')
#-------------------------------------------------------

for j in range (1,(n_procar+1)):
    for point_k in range (1,(nk+1)):
        bandas.write(f'{xx[j][point_k]}')
        for Band_n in range (1,(nb+1)):
            bandas.write(f' {Energia[j][point_k][Band_n]}')
        bandas.write(f' \n')
                
#-------------
bandas.close()
#-------------        

# Gravando a informação de cada estado Psi para o Plot das Projeções ==

#-------------------------------------------------
psi = open(dir_files + '/output/Psi/Psi.dat', 'w')
#-------------------------------------------------

for k in range (1,(nb+1)):
    for i in range (1,(n_procar+1)):
        for j in range (1,(nk+1)):
            psi.write(f'{xx[i][j]} {Energia[i][j][k]}')
            psi.write(f' {estado_psi[1][i][j][k]} {estado_psi[2][i][j][k]} {estado_psi[3][i][j][k]} {estado_psi[4][i][j][k]} {estado_psi[5][i][j][k]}')         
            psi.write(f' \n')
                
#----------
psi.close()
#----------

# Obtendo e gravando as cores no padrão RGB que designam cada orbital bem como cada combinação de orbitais para o Plot das Projeções ===:

#-------------------------------------------------------------
color_rgb = open(dir_files + '/output/Psi/color_rgb.dat', 'w')
#-------------------------------------------------------------

number = -1
           
for Band_n in range (1, (nb+1)):
    for wp in range (1, (n_procar+1)):
        for point_k in range (1, (nk+1)):       
           number += 1
           
           #---------------------------------------------------------------------------------------------------------------------------------------------         
           # Notação do Matplotlib para o padrão RGB de cores: cor = [red, green, blue] com cada componente variando de 0.0 a 1.0 -----------------------
           # c_red = [1, 0, 0]; c_green = [0, 1, 0]; c_blue = [0, 0, 1]; c_magenta = [1, 0, 1]; c_rosybrown = [0.737254902, 0.560784313, 0.560784313] ---           
           #---------------------------------------------------------------------------------------------------------------------------------------------

           #-----------------------------------------------------------------------------
           # Psi_1 = blue; Psi_2 = red; Psi_3 = green; Psi_4 = magenta; Psi_5 = rosybrown
           #-----------------------------------------------------------------------------               
           c_red    =  est_psi[2][wp][point_k][Band_n] + 0.737254902*(est_psi[5][wp][point_k][Band_n]) + est_psi[4][wp][point_k][Band_n]
           c_green  =  est_psi[3][wp][point_k][Band_n] + 0.560784313*(est_psi[5][wp][point_k][Band_n])
           c_blue   =  est_psi[1][wp][point_k][Band_n] + 0.560784313*(est_psi[5][wp][point_k][Band_n]) + est_psi[4][wp][point_k][Band_n]
           #--------------------------------
           if (c_red > 1.0):   c_red   = 1.0
           if (c_green > 1.0): c_green = 1.0
           if (c_blue > 1.0):  c_blue  = 1.0
           #-------------------------------------------------
           color_rgb.write(f' {c_red} {c_green} {c_blue} \n')            

#----------------
color_rgb.close()
#----------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Psi.py para o diretório de saida ------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

# Teste para saber se o arquivo Psi.py já se encontra no diretorio de saida
try: f = open(dir_files + '/output/Psi/Psi.py'); f.close(); os.remove(dir_files + '/output/Psi/Psi.py')
except: 0 == 0
   
source = main_dir + '/plot/plot_projecao_psi.py'
destination = dir_files + '/output/Psi/Psi.py'
shutil.copyfile(source, destination)

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Psi.py possa ser executado isoladamente ---
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

file = open(dir_files + '/output/Psi/Psi.py', 'r')
lines = file.readlines()
file.close()

linha = 4

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'n_psi = {n_psi}  #  Numero de estados Psi \n')
linha += 1; lines.insert(linha, f'l_psi = {l_psi}  #  Rotulos dos estados Psi \n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}  #  Numero de arquivos PROCAR a serem lidos \n')
linha += 1; lines.insert(linha, f'nk  = {nk}  #  Numero de pontos-k do calculo \n')
linha += 1; lines.insert(linha, f'nb = {nb}  #  Numero de bandas do calculo \n')
linha += 1; lines.insert(linha, f'energ_min = {energ_min}  #  Menor valor de energia das bandas \n')
linha += 1; lines.insert(linha, f'energ_max = {energ_max}  #  Maior valor de energia das bandas \n')
linha += 1; lines.insert(linha, f'lorbit = {lorbit}  #  Valor da variavel lorbit adotada no calculo \n')
linha += 1; lines.insert(linha, f'Dimensao = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'transp = {transp}  #  Transparencia aplicada ao plot das projecoes \n')
linha += 1; lines.insert(linha, f'dest_k = {dest_k}  #  [0] Nao destacar nem rotular nenhum ponto-k; [1] Destacar automaticamente os pontos-k informados no KPOINTS; [2] Destacar e rotular os pontos-k a sua escolha \n')
linha += 1; lines.insert(linha, f'dest_pk = {dest_pk}  #  Coordenadas dos pontos-k de interesse a serem destacados no plot da projeção \n')

if (dest_k == 2): 
   for i in range(contador2):
       for j in range(34):
           if (label_pk[i] == '#' + str(j+1)):
              label_pk[i] = r_matplot[j]    
   linha += 1; lines.insert(linha, f'label_pk = {label_pk}  #  Rotulos dos pontos-k de interesse a serem destacados no plot da projeção \n')

linha += 1; lines.insert(linha, f'save_png = {save_png}; save_pdf = {save_pdf}; save_eps = {save_eps}  #  Formato em que o plot da projeção sera salvo, onde [0] = NAO e [1] = SIM \n')                         
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Psi/Psi.py', 'w')
file.writelines(lines)
file.close()

#--------------------------------------------------
exec(open(dir_files + '/output/Psi/Psi.py').read())
#--------------------------------------------------
