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

#---------------------------------------------
exec(open("_VASProcar/informacoes.py").read())
#---------------------------------------------

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("############### Projecao dos Orbitais (S,P,D): ###############")
print ("##############################################################") 
print (" ")

if (escolha == -2):
   
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

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------

#---------------------------------------------
exec(open("_VASProcar/procar.py").read())
#---------------------------------------------     

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------
   
soma_orb = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(n_orb+1)] for k in range(n_procar+1)]                    # soma_orb[n_procar][n_orb][nk][nb]
total = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                                                 # tot[n_procar][nk][nb]
 
#  orb      = [procar.py] Parcela do Orbital (S, P ou D) referente a cada ion "ni".
#  soma_orb = Soma do Orbital (S, P ou D) sobre todos os ions "ni" selecionados.
#  tot      = Soma sobre todos os orbitais e todos os ions.

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

#======================================================================
# Plot das Projeções dos Orbitais (GRACE) =============================
#====================================================================== 
                          
if (lorbit == 10):              # Orbitais (S, P, D)
   wm = 1; wn = 3            
if (lorbit >= 11):              # Orbitais (S, P, D) e (Px, Py, Pz)
   wm = 1; wn = 6                   

print (" ")          
print ("==================================")
print (" ")

for t in range (wm,(wn+1)):     # Loop para a analise das Projecoes
        
#-----------------------------------------------------------------------

    if (t == 1):
       #-------------------------------------------------
       projection = open("saida/Orbitais_S_P_D.agr", "w")
       #-------------------------------------------------
       print ("Analisando a Projecao do Orbital S")
    if (t == 2):
       print (" ")
       print ("Analisando a Projecao do Orbital P")
    if (t == 3):
       print (" ")
       print ("Analisando a Projecao do Orbital D")
    if (t == 4):
       #----------------------------------------------------
       projection = open("saida/Orbitais_Px_Py_Pz.agr", "w")
       #----------------------------------------------------
       print (" ")
       print ("Analisando a Projecao do Orbital Px")
    if (t == 5):
       print (" ")
       print ("Analisando a Projecao do Orbital Py")
    if (t == 6):
       print (" ")
       print ("Analisando a Projecao do Orbital Pz")

#-----------------------------------------------------------------------
# Escrita do arquivo ".agr" do GRACE -----------------------------------
#-----------------------------------------------------------------------

    if (t == 1 or t == 4):

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
              if (t == 1): legenda = 'S'
              if (t == 4): legenda = 'Px' 
              grac='s0'; color = cor[4]        # Cor (Azul) do Orbital S ou Px.
           if (i == 2):
              if (t == 1): legenda = 'P'
              if (t == 4): legenda = 'Py'
              grac='s1'; color = cor[5]        # Cor (Vermelho) do Orbital P ou Py.
           if (i == 3):
              if (t == 1): legenda = 'D'
              if (t == 4): legenda = 'Pz'
              grac='s2'; color = cor[6]        # Cor (Verde) do Orbital D ou Pz.

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

       projection.write("@type xysize")
       projection.write(" \n")
      
#======================================================================
# Plot dos Orbitais ===================================================
#======================================================================

    for wp in range (1, (n_procar+1)):
        for point_k in range (1, (nk+1)):
            for Band_n in range (1, (nb+1)):
                #------------------------------------------------------
                if (t == 1): # Orbital S
                   orbital = soma_orb[wp][1][point_k][Band_n]
                if (t == 2 and lorbit == 10): # Orbital P
                   orbital = soma_orb[wp][2][point_k][Band_n]
                if (t == 2 and lorbit >= 11): # Orbital P = Px + Py + Pz
                   orbital = soma_orb[wp][2][point_k][Band_n] + soma_orb[wp][3][point_k][Band_n] + soma_orb[wp][4][point_k][Band_n]
                if (t == 3 and lorbit == 10): # Orbital D
                   orbital = soma_orb[wp][3][point_k][Band_n]
                if (t == 3 and lorbit >= 11): # Orbital P = Dxy + Dyz + Dz2 + Dxz + Dx2
                   orbital = soma_orb[wp][5][point_k][Band_n] + soma_orb[wp][6][point_k][Band_n] + soma_orb[wp][7][point_k][Band_n] + soma_orb[wp][8][point_k][Band_n] + soma_orb[wp][9][point_k][Band_n]
                if (t == 4): # Orbital Px 
                   orbital = soma_orb[wp][4][point_k][Band_n]
                if (t == 5): # Orbital Py 
                   orbital = soma_orb[wp][2][point_k][Band_n]
                if (t == 6): # Orbital pz 
                   orbital = soma_orb[wp][3][point_k][Band_n]
                #------------------------------------------------------
                if (wp == 1 and point_k == 1 and Band_n == 1):    
                   projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} 0.0 \n')
                if (orbital > 0.0):    
                   projection.write(f'{xx[wp][point_k]} {Energia[wp][point_k][Band_n]} {orbital} \n')
          
    projection.write(" \n")
       

#======================================================================
# Plot da estrutura de Bandas =========================================
#======================================================================

    if (t == 3 or t == 6):
      
       for Band_n in range (1,(nb+1)):
           projection.write(" \n")
           for i in range (1,(n_procar+1)):
               for point_k in range (1,(nk+1)):
                   projection.write(f'{xx[i][point_k]} {Energia[i][point_k][Band_n]} 0.0 \n')

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

       #-----------------
       projection.close()
       #-----------------

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
