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

#----------------------------------------------------------------------------
# Verificando se a pasta "Localizacao" existe, se não existe ela é criada ---
#----------------------------------------------------------------------------
if os.path.isdir("saida/Localizacao"):
   0 == 0
else:
   os.mkdir("saida/Localizacao")
#-------------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================

#-----------------------------------------
executavel = Diretorio + '/informacoes.py'
exec(open(executavel).read())
#-----------------------------------------

#----------------------------------------------------------------------

ABC = [0]*(ni+1)            # Inicilização do vetor ABC

for i in range (1,(ni+1)):  # Por padrão todos os ions pertencem a Região E
    ABC[i] = "E"

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("################## Localizacao dos Estados: ##################")
print ("##############################################################") 
print (" ")

if (escolha == -5):

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

if (escolha == 5):
   Dimensao = 1
   peso_total = 1.0
   transp = 1.0
   dest_k = 1
   
print ("##############################################################")
print ("Defina as regioes (A, B, C, D ou E) a serem destacadas: ======")
print ("Defina intervalos de ions que compoem as regioes =============")
print ("Por padrao todos os ions pertencem inicialmente a Regiao E ===")
print ("==============================================================")
print ("Quantos intervalos de ions ira fornecer abaixo? ==============")
print ("##############################################################")
loop = input (" "); loop = int(loop)
print(" ")

for i in range (1,(loop+1)):
    print (f'{i} intervalo: =================================================')
    print ("Digite o ion inicial do intervalo ============================")
    loop_i = input (" "); loop_i = int(loop_i)
    print ("Digite o ion final do intervalo ==============================")
    loop_f = input (" "); loop_f = int(loop_f)
    print ("Qual letra (A, B, C, D ou E) rotula a Regiao do intervalo? ===")
    loop_cha = input (" ")
    if (loop_cha == "a"): loop_cha = "A"
    if (loop_cha == "b"): loop_cha = "B"
    if (loop_cha == "c"): loop_cha = "C"
    if (loop_cha == "d"): loop_cha = "D"
    if (loop_cha == "e"): loop_cha = "E"        
    print(" ")     

    if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
       print ("")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       print ("   ERRO: Os valores de ions informados estao incorretos   ")
       print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
       print ("")
    for j in range (loop_i, (loop_f+1)):
        ABC[j] = loop_cha  

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

Prop = [[[[0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)] for k in range(5+1)]   # Prop[5][wp][nk][nb]
# Prop[1][wp][nk][nb] = Proporção de contribuição da Região A
# Prop[2][wp][nk][nb] = Proporção de contribuição da Região B
# Prop[3][wp][nk][nb] = Proporção de contribuição da Região C
# Prop[4][wp][nk][nb] = Proporção de contribuição da Região D
# Prop[5][wp][nk][nb] = Proporção de contribuição da Região E
   
atomo = [0]*(ni+1)
Contrib = [0]*(ni+1)
Reg = [0]*(ni+1)
u = [0]*(4+1)

num_A = 0
num_B = 0
num_C = 0
num_D = 0
num_E = 0

dpi = 2*3.1415926535897932384626433832795

#######################################################################
########################### Loop dos PROCAR ###########################
#######################################################################

#---------------------------------------------------------------------
contribuicao = open("saida/Localizacao/Contribuicao_Regioes.txt", "w")
#---------------------------------------------------------------------

for wp in range(1, (n_procar+1)):    
      
    if (n_procar > 1):
       contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
       contribuicao.write(f'PROCAR {wp} \n')
       contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
       contribuicao.write(" \n")
      
    ###################################################################
    ###################### Loop dos Pontos_k ##########################
    ###################################################################

    for point_k in range(1, (nk+1)):                                  
        
        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contribuicao.write(f'Ponto-k {point_k}: Coord. Diretas ({kb1[wp][point_k]}, {kb2[wp][point_k]}, {kb3[wp][point_k]}) \n')
        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contribuicao.write(" \n")      

        ###############################################################
        ################### Loop dos Bandas ###########################
        ###############################################################

        for Band_n in range (1, (nb+1)):

            contribuicao.write("================================================================= \n")
            contribuicao.write(f'Banda {Band_n} \n')
            contribuicao.write("================================================================= \n")          

            orb_total = 0.0
            Regiao_A = 0.0
            Regiao_B = 0.0
            Regiao_C = 0.0
            Regiao_D = 0.0
            Regiao_E = 0.0
            Soma = 0.0
            Soma_A = 0.0
            Soma_B = 0.0
            Soma_C = 0.0
            Soma_D = 0.0
            Soma_E = 0.0
            
            ###########################################################
            ################ Loop dos ions ############################
            ###########################################################

            for ion_n in range (1, (ni+1)):
               
                #----------------------
                atomo[ion_n] = ion_n
                temp_sm = ABC[ion_n]
                Reg[ion_n] = ABC[ion_n]
                #----------------------

                if (temp_sm == "A"):
                   Contrib[ion_n]  =  tot[wp][point_k][Band_n][ion_n]
                   Soma_A          =  Soma_A     +  Contrib[ion_n]
                   Regiao_A        =  Regiao_A   +  tot[wp][point_k][Band_n][ion_n]
                   orb_total       =  orb_total  +  tot[wp][point_k][Band_n][ion_n]  
                  
                if (temp_sm == "B"):
                   Contrib[ion_n]  =  tot[wp][point_k][Band_n][ion_n]
                   Soma_B          =  Soma_B     +  Contrib[ion_n]
                   Regiao_B        =  Regiao_B   +  tot[wp][point_k][Band_n][ion_n]
                   orb_total       =  orb_total  +  tot[wp][point_k][Band_n][ion_n]  

                if (temp_sm == "C"):
                   Contrib[ion_n]  =  tot[wp][point_k][Band_n][ion_n]
                   Soma_C          =  Soma_C     +  Contrib[ion_n]
                   Regiao_C        =  Regiao_C   +  tot[wp][point_k][Band_n][ion_n]
                   orb_total       =  orb_total  +  tot[wp][point_k][Band_n][ion_n]                 

                if (temp_sm == "D"):
                   Contrib[ion_n]  =  tot[wp][point_k][Band_n][ion_n]
                   Soma_D          =  Soma_D     +  Contrib[ion_n]
                   Regiao_D        =  Regiao_D   +  tot[wp][point_k][Band_n][ion_n]
                   orb_total       =  orb_total  +  tot[wp][point_k][Band_n][ion_n] 

                if (temp_sm == "E"):
                   Contrib[ion_n]  =  tot[wp][point_k][Band_n][ion_n]
                   Soma_E          =  Soma_E     +  Contrib[ion_n]
                   Regiao_E        =  Regiao_E   +  tot[wp][point_k][Band_n][ion_n]
                   orb_total       =  orb_total  +  tot[wp][point_k][Band_n][ion_n] 

            #----------------------------------------------------------           
            # Fim do Loop dos ions ------------------------------------
            #----------------------------------------------------------

            if (Regiao_A != 0.0): num_A = 1
            if (Regiao_B != 0.0): num_B = 1
            if (Regiao_C != 0.0): num_C = 1
            if (Regiao_D != 0.0): num_D = 1
            if (Regiao_E != 0.0): num_E = 1

            if (orb_total != 0.0):
               Prop[1][wp][point_k][Band_n] = (Regiao_A/orb_total)*peso_total   # Proporção de contribuição da Região A
               Prop[2][wp][point_k][Band_n] = (Regiao_B/orb_total)*peso_total   # Proporção de contribuição da Região B
               Prop[3][wp][point_k][Band_n] = (Regiao_C/orb_total)*peso_total   # Proporção de contribuição da Região C
               Prop[4][wp][point_k][Band_n] = (Regiao_D/orb_total)*peso_total   # Proporção de contribuição da Região D
               Prop[5][wp][point_k][Band_n] = (Regiao_E/orb_total)*peso_total   # Proporção de contribuição da Região E

            if (orb_total == 0.0):
               Prop[1][wp][point_k][Band_n] = 0.0
               Prop[2][wp][point_k][Band_n] = 0.0
               Prop[3][wp][point_k][Band_n] = 0.0
               Prop[4][wp][point_k][Band_n] = 0.0
               Prop[5][wp][point_k][Band_n] = 0.0
      
            #-----------------------------------------------------------------------

            if (orb_total != 0.0):
               Soma_A = (Soma_A/orb_total)*100
               Soma_B = (Soma_B/orb_total)*100
               Soma_C = (Soma_C/orb_total)*100
               Soma_D = (Soma_D/orb_total)*100
               Soma_E = (Soma_E/orb_total)*100
               
            if (orb_total == 0.0):
               Soma_A = 0.0
               Soma_B = 0.0
               Soma_C = 0.0
               Soma_D = 0.0
               Soma_E = 0.0

            if (Soma_A != 0):
               contribuicao.write(f'Regiao A = {Soma_A:7,.3f}% \n')
            if (Soma_B != 0):
               contribuicao.write(f'Regiao B = {Soma_B:7,.3f}% \n')
            if (Soma_C != 0):
               contribuicao.write(f'Regiao C = {Soma_C:7,.3f}% \n')
            if (Soma_D != 0):
               contribuicao.write(f'Regiao D = {Soma_D:7,.3f}% \n')
            if (Soma_E != 0):
               contribuicao.write(f'Regiao E = {Soma_E:7,.3f}% \n')   

            contribuicao.write("=================== \n")
            
            ##################################################################
            ##################################################################
            ##################################################################

            for j in range (1,(ni+1)):
               rotulo_temp[j] = rotulo[j]

            nj = (ni - 1)
                     
            for k in range (1,(nj+1)):
                wy = (ni - k)
                for l in range (1,(wy+1)):
                    if (Contrib[l] < Contrib[l+1]):
                     tp1 = Contrib[l]
                     Contrib[l] = Contrib[l+1]
                     Contrib[l+1] = tp1
                     #--------------------
                     tp2 = atomo[l]
                     atomo[l] = atomo[l+1]
                     atomo[l+1] = tp2
                     #--------------------                    
                     tp3 = Reg[l]
                     Reg[l] = Reg[l+1]
                     Reg[l+1] = tp3
                     #--------------------
                     tp4 = rotulo_temp[l]
                     rotulo_temp[l] = rotulo_temp[l+1]
                     rotulo_temp[l+1] = tp4                     

            for ion_n in range (1,(ni+1)):
                if (orb_total != 0):
                   Contrib[ion_n] = (Contrib[ion_n]/orb_total)*100
                Soma = Soma + Contrib[ion_n]
                
                if (Reg[ion_n] == "A"):
                   palavra = "(Regiao A)"
                if (Reg[ion_n] == "B"):
                   palavra = "(Regiao B)"
                if (Reg[ion_n] == "C"):
                   palavra = "(Regiao C)"
                if (Reg[ion_n] == "D"):
                   palavra = "(Regiao D)"
                if (Reg[ion_n] == "E"):
                   palavra = "(Regiao E)"   

                contribuicao.write(f'{rotulo_temp[ion_n]:>2}: ion {atomo[ion_n]:<3} | Contribuicao: {Contrib[ion_n]:6,.3f}% | Soma: {Soma:>7,.3f}% | {palavra} \n')

            contribuicao.write(" \n")

        #----------------------------------------------------------
        # Fim do Loop das Bandas ----------------------------------
        #----------------------------------------------------------      
    #----------------------------------------------------------
    # Fim do Loop dos pontos-k --------------------------------
    #----------------------------------------------------------    
#----------------------------------------------------------
# Fim do Loop dos arquivos PROCAR -------------------------
#----------------------------------------------------------

#-------------------    
contribuicao.close()
#-------------------

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

print (" ")          
print ("===============================================")

#======================================================================
#======================================================================
# Plot das Projeções da Localização (GRACE) ===========================
#====================================================================== 
#======================================================================

projection = open("saida/Localizacao/Localizacao_estados.agr", "w")

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
              
for i in range (1,(5+1)):
    if (i == 1):
       grac='s0'; color = cor_A; legenda = 'A'
    if (i == 2):
       grac='s1'; color = cor_B; legenda = 'B'
    if (i == 3):
       grac='s2'; color = cor_C; legenda = 'C'
    if (i == 4):
       grac='s3'; color = cor_D; legenda = 'D'
    if (i == 5):
       grac='s4'; color = cor_E; legenda = 'E'   

    projection.write(f'@    {grac} type xysize \n')
    projection.write(f'@    {grac} symbol 1 \n')
    projection.write(f'@    {grac} symbol color {color} \n')
    projection.write(f'@    {grac} symbol fill color {color} \n')
    projection.write(f'@    {grac} symbol fill pattern 1 \n')
    projection.write(f'@    {grac} line type 0 \n')
    projection.write(f'@    {grac} line color {color} \n')

    if (i == 1 and num_A == 1):
       projection.write(f'@    {grac} legend  "{legenda}" \n')
    if (i == 2 and num_B == 1):
       projection.write(f'@    {grac} legend  "{legenda}" \n')
    if (i == 3 and num_C == 1):
       projection.write(f'@    {grac} legend  "{legenda}" \n')
    if (i == 4 and num_D == 1):
       projection.write(f'@    {grac} legend  "{legenda}" \n')
    if (i == 5 and num_E == 1):
       projection.write(f'@    {grac} legend  "{legenda}" \n')   

for j in range(nb + 1 + contador2):
    #-----------------------------------------------------
    if (j <= (nb-1)): color = 1 # cor Preta
    if (j == nb):     color = 2 # cor Vermelha
    if (j > nb):      color = 7 # Cor Cinza  
    #-----------------------------------------------------
    projection.write(f'@    s{j+5} type xysize \n')
    projection.write(f'@    s{j+5} line type 1 \n')
    projection.write(f'@    s{j+5} line color {color} \n')    
    #-----------------------------------------------------       
projection.write("@type xysize \n")

for t in range (1,(5+1)):

    if (t == 1 and num_A == 1):
       print ("Analisando a Localizacao dos Estados (Regiao A)")
    if (t == 2 and num_B == 1):
       print ("Analisando a Localizacao dos Estados (Regiao B)")
    if (t == 3 and num_C == 1):
       print ("Analisando a Localizacao dos Estados (Regiao C)")
    if (t == 4 and num_D == 1):
       print ("Analisando a Localizacao dos Estados (Regiao D)")
    if (t == 5 and num_E == 1):
       print ("Analisando a Localizacao dos Estados (Regiao E)")   

#-----------------------------------------------------------------------
    num_tot = n_procar*(nk*nb)
#-----------------------------------------------------------------------

    for Band_n in range (1,(nb+1)):
        for wp in range (1,(n_procar+1)):
            for point_k in range (1,(nk+1)):
                if (wp == 1 and point_k == 1 and Band_n == 1):    
                   projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} 0.0 \n')
                projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} {Prop[t][wp][point_k][Band_n]} \n')

    projection.write(" \n")

# Plot das Bandas =====================================================

for Band_n in range (1,(nb+1)):
    projection.write(" \n")
    for wp in range (1,(n_procar+1)):
        for point_k in range (1,(nk+1)):
            projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} 0.0 \n')

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
       
#-----------------------------------------------------------------------
projection.close()
#-----------------------------------------------------------------------

#======================================================================
#======================================================================
# Plot das Projeções da Localização (Matplotlib) ======================
#====================================================================== 
#======================================================================

# Gravando a informação das bandas para o Plot das Projeções ==========
    
#-------------------------------------------------
bandas = open("saida/Localizacao/Bandas.dat", "w")
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

# Gravando a informação da contribuição de cada região para o Plot das Projeções

#-------------------------------------------------
Localizacao = open("saida/Localizacao/Localizacao.dat", "w")
#-------------------------------------------------

for k in range (1,(nb+1)):
    for i in range (1,(n_procar+1)):
        for j in range (1,(nk+1)):
            Localizacao.write(f'{xx[i][j]} {Energia[i][j][k]}')
            for l in range (1,(5+1)):
                Localizacao.write(f' {((dpi*Prop[l][i][j][k])**2)*peso_total}')
            Localizacao.write(f' \n')
                
#------------------
Localizacao.close()
#------------------

# Obtendo e gravando as cores no padrão RGB que designam cada região bem como cada combinação de região para o Plot das Projeções ===:

#-------------------------------------------------------
color_rgb = open("saida/Localizacao/color_rgb.dat", "w")
#-------------------------------------------------------

number = -1
for k in range (1, (nb+1)):
    for i in range (1, (n_procar+1)):
        for j in range (1, (nk+1)):       
           number += 1
           
           #---------------------------------------------------------------------------------------------------------------------------------------------         
           # Notação do Matplotlib para o padrão RGB de cores: cor = [red, green, blue] com cada componente variando de 0.0 a 1.0 -----------------------
           # c_red = [1, 0, 0]; c_green = [0, 1, 0]; c_blue = [0, 0, 1]; c_rosybrown = [0.737254902, 0.560784313, 0.560784313]; c_magenta = [1, 0, 1] ---           
           #---------------------------------------------------------------------------------------------------------------------------------------------

           #-----------------------------------------------------------------------------
           # Reg_A = blue; Reg_B = red; Reg_C = green; Reg_D = rosybrown; Reg_E = magenta
           #-----------------------------------------------------------------------------
           # Reg_A = Prop[1][i][j][k]; Reg_B = Prop[2][i][j][k]; Reg_C = Prop[3][i][j][k]
           # Reg_D = Prop[4][i][j][k]; Reg_E = Prop[5][i][j][k] 
           #-----------------------------------------------------------------------------
           
           c_red    =  Prop[2][i][j][k] + 0.737254902*(Prop[4][i][j][k]) + Prop[5][i][j][k] 
           c_green  =  Prop[3][i][j][k] + 0.560784313*(Prop[4][i][j][k])
           c_blue   =  Prop[1][i][j][k] + 0.560784313*(Prop[4][i][j][k]) + Prop[5][i][j][k]
           #--------------------------------
           if (c_red > 1.0):   c_red   = 1.0
           if (c_green > 1.0): c_green = 1.0
           if (c_blue > 1.0):  c_blue  = 1.0
           #------------------------------------------------
           color_rgb.write(f'{c_red} {c_green} {c_blue} \n')            

#----------------
color_rgb.close()
#----------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Localizacao.py para o diretório de saida ----------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

import shutil

# Teste para saber se o arquivo Localizacao.py já se encontra no diretorio de saida
try: f = open('saida/Localizacao/Localizacao.py'); f.close(); os.remove('saida/Localizacao/Localizacao.py')
except: 0 == 0
   
source = Diretorio + '/plot/plot_projecao_localizacao.py'
destination = 'saida/Localizacao/Localizacao.py'
shutil.copyfile(source, destination)

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Localizacao.py possa ser executado isoladamente ---
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

file = open('saida/Localizacao/Localizacao.py', 'r')
lines = file.readlines()
file.close()

linha = 14

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'n_procar = {n_procar}; nk  = {nk}; nb = {nb}; energ_min = {energ_min}; energ_max = {energ_max} \n')
linha += 1; lines.insert(linha, f'num_A = {num_A}; num_B = {num_B}; num_C = {num_C}; num_D = {num_D}; num_E = {num_E} \n')
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

file = open('saida/Localizacao/Localizacao.py', 'w')
file.writelines(lines)
file.close()

#----------------------------------------------
executavel = 'saida/Localizacao/Localizacao.py'
exec(open(executavel).read())
#----------------------------------------------

#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################
