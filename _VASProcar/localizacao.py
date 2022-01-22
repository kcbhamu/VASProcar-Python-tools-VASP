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

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================

#---------------------------------------------
exec(open("_VASProcar/informacoes.py").read())
#---------------------------------------------

#----------------------------------------------------------------------

ABC = [0]*(ni+1)            # Inicilização do vetor ABC

for i in range (1,(ni+1)):  # Por padrão todos os ions pertencem a Região C
    ABC[i] = "C"

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("################## Localizacao dos Estados: ##################")
print ("##############################################################") 
print (" ")

if (escolha == -5):

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

if (escolha == 5):

   Dimensao = 1
   peso_total = 1.0
   
print ("##############################################################")
print ("Defina as regioes (A, B, C) a serem destacadas na projecao: ==")
print ("Defina intervalos de ions que compoem as regioes =============")
print ("Por padrao todos os ions pertencem inicialmente a Regiao C ===")
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
    print ("Qual a letra (A, B ou C) que rotula a Regiao do intervalo? ===")
    loop_cha = input (" ")
    if (loop_cha == "a"):
       loop_cha = "A"
    if (loop_cha == "b"):
       loop_cha = "B"
    if (loop_cha == "c"):
       loop_cha = "C"   
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

#*****************************************************************
# Dimensao = 1 >> k em unidades de 2pi/Param com Param em Angs. **
# Dimensao = 2 >> k em unidades de 1/Angs. ***********************
# Dimensao = 3 >> K em unidades de 1/nm **************************
#*****************************************************************
Dimensao = 1

#----------------------------------------
exec(open("_VASProcar/procar.py").read())
#----------------------------------------

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------

Prop = [[[[0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)] for k in range(3+1)]   # Prop[3][wp][nk][nb]
# Prop[1][wp][nk][nb] = Proporção de contribuição da Região A
# Prop[2][wp][nk][nb] = Proporção de contribuição da Região B
# Prop[3][wp][nk][nb] = Proporção de contribuição da Região C
   
atomo = [0]*(ni+1)
Contrib = [0]*(ni+1)
Reg = [0]*(ni+1)
u = [0]*(4+1)

#######################################################################
########################### Loop dos PROCAR ###########################
#######################################################################

#----------------------------------------------------------------------
contribuicao = open("saida/Contribuicao_Regioes.txt", "w")
#----------------------------------------------------------------------

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
            Soma = 0.0
            Soma_A = 0.0
            Soma_B = 0.0
            Soma_C = 0.0
            
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

            #----------------------------------------------------------           
            # Fim do Loop dos ions ------------------------------------
            #----------------------------------------------------------

            if (orb_total != 0.0):
               Prop[1][wp][point_k][Band_n] = (Regiao_A/orb_total)*peso_total   # Proporção de contribuição da Região A
               Prop[2][wp][point_k][Band_n] = (Regiao_B/orb_total)*peso_total   # Proporção de contribuição da Região B
               Prop[3][wp][point_k][Band_n] = (Regiao_C/orb_total)*peso_total   # Proporção de contribuição da Região C

            if (orb_total == 0.0):
               Prop[1][wp][point_k][Band_n] = 0.0
               Prop[2][wp][point_k][Band_n] = 0.0
               Prop[3][wp][point_k][Band_n] = 0.0
      
            #-----------------------------------------------------------------------

            if (orb_total != 0.0):
               Soma_A = (Soma_A/orb_total)*100
               Soma_B = (Soma_B/orb_total)*100
               Soma_C = (Soma_C/orb_total)*100
               
            if (orb_total == 0.0):
               Soma_A = 0.0
               Soma_B = 0.0
               Soma_C = 0.0

            if (Soma_A != 0):
               contribuicao.write(f'Regiao A = {Soma_A:7,.3f}% \n')
            if (Soma_B != 0):
               contribuicao.write(f'Regiao B = {Soma_B:7,.3f}% \n')
            if (Soma_C != 0):
               contribuicao.write(f'Regiao C = {Soma_C:7,.3f}% \n')

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
# Obtendo o nº pontos-k a serem destacados na estrutura de Bandas =====
#======================================================================

#------------------------------------------
inform = open("saida/informacoes.txt", "r")
#------------------------------------------

palavra = 'Pontos-k |'                          

for line in inform:   
    if palavra in line: 
       break

VTemp = inform.readline()
VTemp = inform.readline()
       
nk_total = nk*n_procar

contador2 = 0
dest_pk = [0]*(100)                    # Inicialização do vetor dest_pk de dimensão 100.

for i in range (1, (nk_total+1)):
    VTemp = inform.readline().split()
    r1 = int(VTemp[0]); r2 = float(VTemp[1]); r3 = float(VTemp[2]); r4 = float(VTemp[3]); comprimento = float(VTemp[4])
    if (i != 1) and (i != (nk_total+1)):  
       dif = comprimento - comprimento_old     
       if(dif == 0.0):
         contador2 += 1
         dest_pk[contador2] = comprimento
          
    comprimento_old = comprimento

#-------------
inform.close()
#-------------

print (" ")          
print ("=========================================================")
print (" ")

#======================================================================
# Plot das Projeções da Localização (GRACE) ===========================
#====================================================================== 

projection = open("saida/Localizacao__estados.agr", "w")

projection.write("# Grace project file \n")
projection.write("# \n")
projection.write("@version 50122 \n")
projection.write("@with string \n")
projection.write("@    string on \n")
projection.write(f'@    string {fig_xmin}, {fig_ymax + 0.01} \n')
projection.write(f'@    string def "E(eV)" \n')
projection.write("@with string \n")
projection.write("@    string on \n")

if (Dimensao == 1):
   projection.write(f'@    string {fig_xmax - 0.14}, {fig_ymin - 0.058} \n')
   projection.write(f'@    string def "(2pi/Param.)" \n')
if (Dimensao == 2):
   projection.write(f'@    string {fig_xmax - 0.10}, {fig_ymin - 0.058} \n')
   projection.write(f'@    string def "(1/Angs.)" \n')
if (Dimensao == 3):
   projection.write(f'@    string {fig_xmax - 0.07}, {fig_ymin - 0.058} \n')
   projection.write(f'@    string def "(1/nm)" \n')

projection.write("@with g0 \n")
projection.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
projection.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

escala_x = (x_final - x_inicial)/5
escala_y = (y_final - y_inicial)/5

projection.write(f'@    xaxis  tick major {escala_x:.2f} \n')
projection.write(f'@    yaxis  tick major {escala_y:.2f} \n')
projection.write(f'@    legend {fig_xmax + 0.025}, {fig_ymax} \n') 
              
for i in range (1,(3+1)):
    if (i == 1):
       grac='s0'; color = cor_A; legenda = 'A'
    if (i == 2):
       grac='s1'; color = cor_B; legenda = 'B'
    if (i == 3):
       grac='s2'; color = cor_C; legenda = 'C'

    projection.write(f'@    {grac} type xysize \n')
    projection.write(f'@    {grac} symbol 1 \n')
    projection.write(f'@    {grac} symbol color {color} \n')
    projection.write(f'@    {grac} symbol fill color {color} \n')
    projection.write(f'@    {grac} symbol fill pattern 1 \n')
    projection.write(f'@    {grac} line type 0 \n')
    projection.write(f'@    {grac} line color {color} \n')
    projection.write(f'@    {grac} legend  "{legenda}" \n')

for j in range(nb+1+contador2):

    if (j <= (nb-1)): color = 1
    if (j == nb):     color = 2
    if (j > nb):      color = 7
   
    projection.write(f'@    s{j+3} type xysize \n')
    projection.write(f'@    s{j+3} symbol 0 \n')
    projection.write(f'@    s{j+3} symbol color {color} \n')
    projection.write(f'@    s{j+3} symbol fill color {color} \n')
    projection.write(f'@    s{j+3} symbol fill pattern 0 \n')
    projection.write(f'@    s{j+3} line type 1 \n')
    projection.write(f'@    s{j+3} line color {color} \n')    
           
projection.write("@type xysize \n")
# projection.write(" \n")

#-----------------------------------------------------------------------

wm = 1
wn = 3

for t in range (wm,(wn+1)):

    if (t == 1):
       print ("Analisando a Localizacao dos Estados (Regiao A)")
    if (t == 2):
       print (" ")
       print ("Analisando a Localizacao dos Estados (Regiao B)")
    if (t == 3):
       print (" ")
       print ("Analisando a Localizacao dos Estados (Regiao C)")

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

#======================================================================
# Plot da estrutura de Bandas =========================================
#======================================================================

for Band_n in range (1,(nb+1)):
    projection.write(" \n")
    for wp in range (1,(n_procar+1)):
        for point_k in range (1,(nk+1)):
            projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} 0.0 \n')

#======================================================================
# Destacando a energia de Fermi na estrutura de Bandas ================
#======================================================================

projection.write(" \n")
projection.write(f'{xx[1][1]} 0.0 0.0 \n')
projection.write(f'{xx[n_procar][nk]} 0.0 0.0 \n')

#======================================================================
# Destacando pontos-k de interesse na estrutura de Bandas =============
#======================================================================

for loop in range (1,(contador2+1)):
    projection.write(" \n")
    projection.write(f'{dest_pk[loop]} {energ_min} 0.0 \n')
    projection.write(f'{dest_pk[loop]} {energ_max} 0.0 \n')

#-----------------------------------------------------------------------
projection.close()
#-----------------------------------------------------------------------

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################

