##############################################################
# Versao 1.001 (10/01/2022) ##################################
########################## Autores: ##########################
# Augusto de Lelis Araújo - INFIS/UFU (Uberlândia/MG) ########
# e-mail: augusto-lelis@outlook.com ##########################
# ---------------------------------------------------------- #
# Renan Maciel da Paixão - ????????????????????????????????? #
# e-mail: ?????????????????????.com ##########################
##############################################################

#---------------------------------------------
exec(open("_VASProcar/informacoes.py").read())
#---------------------------------------------
inform = open("saida/informacoes.txt", "a")
#------------------------------------------

#######################################################
########## Lendo os parâmetros de input ###############
#######################################################

#======================================================================
# Obtenção dos parâmetros de input por interação com usuário ==========
#======================================================================

if (leitura == 0 and escolha == -2):
   print ("##############################################################")
   print ("################### Projecao dos Orbitais ####################")
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
   print ("==============================================================")
   esc = input (" "); esc = int(esc)

   if (esc == 1):

      sim_nao = ["nao"]*(ni + 1)             # Inicialização do vetor sim_nao
      
      print ("Especifique os ions selecionados em intervalos ===============")
      print ("Quantos intervalos de ions ira fornecer abaixo? ==============")
      print ("##############################################################")
      loop = input (" "); loop = int(loop)
      for i in range (1,(loop+1)):
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
             sim_nao[i] = "sim"

   print (" ")

if (leitura == 0 and escolha == 2):   
   Dimensao = 1
   peso_total = 1.0
   esc = 0
   
#======================================================================
# Obtenção dos parâmetros de input por leitura do arquivo de input ====
#======================================================================

if (leitura == 1):
   #----------------------------------------------
   entrada = open("input/input_projecoes.txt", "r")
   #----------------------------------------------

   for i in range(6):
       VTemp = entrada.readline()
   Dimensao = int(VTemp)                          # Unidade de medida adotada no eixo-k (2pi/Param, 1/Angs ou 1/nm).

   for i in range(4):
       VTemp = entrada.readline()
   peso_total = float(VTemp)                      # Tamanho/peso das esferas nos graficos de projeções.

   for i in range(5):
       VTemp = entrada.readline()
   esc = int(VTemp)                               # Escolha se serão Plotados/Analisados todos os ions ou não, nas projeções.                                                   

   #-------------
   if (esc == 1):

      sim_nao = ["nao"]*(ni + 1)                  # Inicialização do vetor sim_nao

      for i in range(4):
          VTemp = entrada.readline()
      loop = int(VTemp)

      VTemp = entrada.readline()
      VTemp = entrada.readline()

      for j in range(loop):

          VTemp = entrada.readline().split()
          loop_i = int(VTemp[0]); loop_f = int(VTemp[1])

          if (loop_i > ni) or (loop_f > ni):
             print ("")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("ERRO: Corrija o arquivo de entrada (ions_selecionados.txt)")
             print ("      existe mais atomos definidos do que na rede")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("")       
       
          for i in range(loop_i, (loop_f + 1)):
              sim_nao[i] = "sim"

   #--------------
   entrada.close()
   #--------------                                                   

#======================================================================
# Extraindo os dados do arquivos PROCAR ===============================
#======================================================================

#----------------------------------------
exec(open("_VASProcar/procar.py").read())
#----------------------------------------

#======================================================================
# Obtenção de alguns parâmetros de ajusto do Grafico (GRACE) ==========
#======================================================================    

x_inicial = xx[1][1]
x_final   = xx[n_procar][nk]
y_inicial = energ_min
y_final   = energ_max

#======================================================================
# Destacando pontos-k de interesse na estrutura de Bandas =============
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
# Calculando o total de cada orbital bem como a soma dos orbitais para
# os ions selecionados ================================================
#======================================================================

if (lorbit >= 11): 
   soma_orb = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(9+1)] for k in range(n_procar+1)]  # soma_orb[n_procar][9][nk][nb]
if (lorbit == 10): 
   soma_orb = [[[[0]*(nb+1) for j in range(nk+1)] for l in range(3+1)] for k in range(n_procar+1)]  # soma_orb[n_procar][3][nk][nb]

tot = [[[0]*(nb+1) for j in range(nk+1)] for k in range(n_procar+1)]                                # tot[n_procar][nk][nb] 

#  soma_orb[n_procar][1][nk][nb] = Soma da contrinuição de cada ion para o orbital S
#  soma_orb[n_procar][2][nk][nb] = Soma da contrinuição de cada ion para o orbital Py ou P (lorbit = 10)
#  soma_orb[n_procar][3][nk][nb] = Soma da contrinuição de cada ion para o orbital Pz ou D (lorbit = 10)
#  soma_orb[n_procar][4][nk][nb] = Soma da contrinuição de cada ion para o orbital Px
#  soma_orb[n_procar][5][nk][nb] = Soma da contrinuição de cada ion para o orbital Dxy
#  soma_orb[n_procar][6][nk][nb] = Soma da contrinuição de cada ion para o orbital Dyz
#  soma_orb[n_procar][7][nk][nb] = Soma da contrinuição de cada ion para o orbital Dz2
#  soma_orb[n_procar][8][nk][nb] = Soma da contrinuição de cada ion para o orbital Dxz
#  soma_orb[n_procar][9][nk][nb] = Soma da contrinuição de cada ion para o orbital Dx2
#  tot = Soma de cada orbital (com a respectiva contribuição de cada ion)

for wp in range (1, (n_procar+1)):
    for point_k in range (1, (nk+1)):
        for Band_n in range (1, (nb+1)):
            for orb_n in range (1, (9+1)):               
                for ion_n in range (1, (ni+1)):
                    tot[wp][point_k][Band_n] = tot[wp][point_k][Band_n] + orb[wp][orb_n][point_k][Band_n][ion_n]                 
                    if (esc == 1):
                       temp_sn = sim_nao[ion_n]
                    if (esc == 0 or (esc == 1 and temp_sn == "sim")):
                       soma_orb[wp][orb_n][point_k][Band_n] = soma_orb[wp][orb_n][point_k][Band_n] + orb[wp][orb_n][point_k][Band_n][ion_n]

#=======================================================================
# Efetuando a normalização dos orbitais: O quanto cada orbital contribui
# para um dado estado em um dado ponto-k ===============================
#=======================================================================

for wp in range (1, (n_procar+1)):
    for point_k in range (1, (nk+1)):
        for Band_n in range (1, (nb+1)):
            for orb_n in range (1, (9+1)):
                if (tot[wp][point_k][Band_n] != 0.0):
                   soma_orb[wp][orb_n][point_k][Band_n] = ( soma_orb[wp][orb_n][point_k][Band_n]/tot[wp][point_k][Band_n] )*peso_total  

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

for t in range (wm,(wn+1)):                   # Loop para a analise das Projecoes
        
#-----------------------------------------------------------------------

    if (t == 1):
       projection = open("saida/Orbitais_S_P_D.agr", "w") 
    if (t == 4):
       projection = open("saida/Orbitais_Px_Py_Pz.agr", "w") 

#-----------------------------------------------------------------------

    if (t == 1):
       print ("Analisando a Projecao do Orbital S")
    if (t == 2):
       print (" ")
       print ("Analisando a Projecao do Orbital P")
    if (t == 3):
       print (" ")
       print ("Analisando a Projecao do Orbital D")
    if (t == 4):
       print (" ")
       print ("Analisando a Projecao do Orbital Px")
    if (t == 5):
       print (" ")
       print ("Analisando a Projecao do Orbital Py")
    if (t == 6):
       print (" ")
       print ("Analisando a Projecao do Orbital Pz")

#-----------------------------------------------------------------------

################### Plot das Texturas nos arquivos ".agr" ##############

    if (t == 1 or t == 4):

       projection.write("# Grace project file \n")
       projection.write("# \n")
       projection.write("@version 50122 \n")

       projection.write("@with box \n")
       projection.write("@    box on \n")
       if (t <= 3):
          projection.write("@    box 0.81, 0.95, 0.88, 0.83 \n")
       if (t > 3):
          projection.write("@    box 0.81, 0.95, 0.8875, 0.83 \n")
       projection.write("@box def \n")

       for i in range (1,(3+1)):

           projection.write("@with ellipse \n")
           projection.write("@    ellipse on \n")
          
           if (i == 1):
              projection.write("@    ellipse 0.815, 0.92, 0.835, 0.94 \n")
              color = cor[4]       # Cor (Azul) do Orbital S ou Px.
           if (i == 2):
              projection.write("@    ellipse 0.815, 0.88, 0.835, 0.9 \n")
              color = cor[5]       # Cor (Vermelho) do Orbital P ou Py.
           if (i == 3):
              projection.write("@    ellipse 0.815, 0.84, 0.835, 0.86 \n")
              color = cor[6]       # Cor (Verde) do Orbital D ou Pz.

           projection.write(f'@    ellipse color {color} \n')
           projection.write(f'@    ellipse fill color {color} \n')
           projection.write("@    ellipse fill pattern 1 \n")
           projection.write("@ellipse def \n")

       for i in range (1,(3+1)):

           projection.write("@with string \n")
           projection.write("@    string on \n")

           if (i == 1):
              if (t <= 3):
                 projection.write("@    string 0.8525, 0.92 \n")
                 projection.write("@    string color 1 \n")
                 projection.write(f'@    string def "S" \n')
              if (t > 3):
                 projection.write("@    string 0.8525, 0.92 \n")
                 projection.write("@    string color 1 \n")
                 projection.write(f'@    string def "Px" \n')                 

           if (i == 2):
              if (t <= 3):              
                 projection.write("@    string 0.8525, 0.88 \n")
                 projection.write("@    string color 1 \n")
                 projection.write(f'@    string def "P" \n')
              if (t > 3):              
                 projection.write("@    string 0.8525, 0.88 \n")
                 projection.write("@    string color 1 \n")
                 projection.write(f'@    string def "Py" \n')              

           if (i == 3):
              if (t <= 3):              
                 projection.write("@    string 0.8525, 0.84 \n")
                 projection.write("@    string color 1 \n")
                 projection.write(f'@    string def "D" \n')
              if (t > 3):              
                 projection.write("@    string 0.8525, 0.84 \n")
                 projection.write("@    string color 1 \n")
                 projection.write(f'@    string def "Pz" \n')

       projection.write("@with string \n")
       projection.write("@    string on \n")
       projection.write("@    string 0.1, 0.96 \n")
       projection.write(f'@    string def "E(eV)" \n')
       projection.write("@with string \n")
       projection.write("@    string on \n")

       if (Dimensao == 1):
          projection.write("@    string 0.66, 0.017 \n")
          projection.write(f'@    string def "(2pi/Param.)" \n')
       if (Dimensao == 2):
          projection.write("@    string 0.70, 0.017 \n")
          projection.write(f'@    string def "(1/Angs.)" \n')
       if (Dimensao == 3):
          projection.write("@    string 0.73, 0.017 \n")
          projection.write(f'@    string def "(1/nm)" \n')

       projection.write("@with g0 \n")
       projection.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
       projection.write("@    view 0.1, 0.075, 0.8, 0.95 \n")

       escala_x = (x_final - x_inicial)/5
       escala_y = (y_final - y_inicial)/5

       projection.write(f'@    xaxis  tick major {escala_x:.2f} \n')
       projection.write(f'@    yaxis  tick major {escala_y:.2f} \n')        

       for i in range (1,(3+1)):
          
           if (i == 1):
              grac='s0'; color = cor[4]        # Cor (Azul) do Orbital S ou Px.
           if (i == 2):
              grac='s1'; color = cor[5]        # Cor (Vermelho) do Orbital P ou Py.
           if (i == 3):
              grac='s2'; color = cor[6]        # Cor (Verde) do Orbital D ou Pz.

           projection.write(f'@    {grac} type xysize \n')
           projection.write(f'@    {grac} symbol 1 \n')
           projection.write(f'@    {grac} symbol color {color} \n')
           projection.write(f'@    {grac} symbol fill color {color} \n')
           projection.write(f'@    {grac} symbol fill pattern 1 \n')
           projection.write(f'@    {grac} line type 0 \n')
           projection.write(f'@    {grac} line color {color} \n')
        
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
                if (t == 2): # Orbital P = Px + Py + Pz 
                   orbital = soma_orb[wp][2][point_k][Band_n] + soma_orb[wp][3][point_k][Band_n] + soma_orb[wp][4][point_k][Band_n]
                if (t == 3): # Orbital D = Dxy + Dyz + Dz2 + Dxz + Dx2 
                   orbital = soma_orb[wp][5][point_k][Band_n] + soma_orb[wp][6][point_k][Band_n] + soma_orb[wp][7][point_k][Band_n] + soma_orb[wp][8][point_k][Band_n] + soma_orb[wp][9][point_k][Band_n]
                if (t == 4): # Orbital Px 
                   orbital = soma_orb[wp][4][point_k][Band_n]
                if (t == 5): # Orbital Py 
                   orbital = soma_orb[wp][2][point_k][Band_n]
                if (t == 6): # Orbital pz 
                   orbital = soma_orb[wp][3][point_k][Band_n]
                #------------------------------------------------------
                if (orbital > 0.0):    
                   projection.write(f'{xx[wp][point_k]} {y[wp][point_k][Band_n]} {orbital} \n')
          
    projection.write(" \n")
       

#======================================================================
# Plot da estrutura de Bandas =========================================
#======================================================================

    if (t == 3 or t == 6):
      
       # Plot da Estrutura de Bandas.
       for Band_n in range (1,(nb+1)):
           projection.write(" \n")
           for i in range (1,(n_procar+1)):
               for point_k in range (1,(nk+1)):
                   projection.write(f'{xx[i][point_k]} {y[i][point_k][Band_n]} 0.0 \n')

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
