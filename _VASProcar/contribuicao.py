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

if (leitura == 0):
   print ("##############################################################")
   print ("##### Contribuicao dos Orbitais e ions para os estados #######")
   print ("##############################################################")
   print ("Quais Bandas e Pontos-k deseja analisar? =====================")
   print ("Ponto-k inicial a ser analisado: =============================")
   point_i = input (" "); point_i = int(point_i)
   print(" ")
   print ("Ponto-k final a ser analisado: ===============================")
   point_f = input (" "); point_f = int(point_f)
   print(" ")
   print ("Banda inicial a ser analisada: ===============================")
   Band_i = input (" "); Band_i = int(Band_i)
   print(" ")
   print ("Banda final a ser analisada: =================================")
   Band_f = input (" "); Band_f = int(Band_f)
   print(" ")

###########################################################################

if (leitura == 1):
   #--------------------------------------------------
   entrada = open("input/input_contribuicao.txt", "r")
   #--------------------------------------------------

   for i in range(7):
       VTemp = entrada.readline()
   point_i = int(VTemp)                           

   for i in range(3):
       VTemp = entrada.readline()
   point_f = int(VTemp)                          
   
   for i in range(3):
       VTemp = entrada.readline()
   Band_i = int(VTemp)                               
   
   for i in range(3):
       VTemp = entrada.readline()
   Band_f = int(VTemp)                               
   
   #--------------
   entrada.close()
   #--------------

###########################################################################

Band_antes   = (Band_i  -1)                    # Bandas que não serão analisadas
Band_depois  = (Band_f  +1)                    # Bandas que não serão analisadas
point_antes  = (point_i -1)                    # Pontos-k que não serão analisados
point_depois = (point_f +1)                    # Pontos-k que não serão analisados

#----------------------------------------------------------
contrib_ions = open("saida/Contribuicao_ions.txt", "w")
contrib_orbitais = open("saida/Contribuicao_Orbitais.txt", "w")
#--------------------------------------------------------------
  
contrib_ions.write("================================================================  \n")
contrib_ions.write(f'Observação: Os ions são listados na ordem de maior contribuição. \n')
contrib_ions.write(f'            ions com contribuição nula não serão listados.       \n')
contrib_ions.write("================================================================  \n")
contrib_ions.write(" \n")

contrib_orbitais.write("================================================================ \n")
contrib_orbitais.write(f'Observação: ions sem contribuição orbital não serão listados.   \n')
contrib_orbitais.write("================================================================ \n")
contrib_orbitais.write(" \n")  

################# Inicialização de Vetores e Matrizes: #################

xx = [[0]*(nk+1) for i in range(n_procar+1)]
kx = [[0]*(nk+1) for i in range(n_procar+1)]
ky = [[0]*(nk+1) for i in range(n_procar+1)]
kz = [[0]*(nk+1) for i in range(n_procar+1)]
separacao = [[0]*(nk+1) for i in range(n_procar+1)]
atomo = [0]*(ni+1)

s = [0]*(ni+1); p = [0]*(ni+1); d = [0]*(ni+1)
px = [0]*(ni+1); py = [0]*(ni+1); pz = [0]*(ni+1)
dxy = [0]*(ni+1); dyz = [0]*(ni+1); dz2 = [0]*(ni+1); dxz = [0]*(ni+1); dx2 = [0]*(ni+1)
tot = [0]*(ni+1); soma_s = [0]*(ni+1); soma_p = [0]*(ni+1); soma_d = [0]*(ni+1) 

#---------------------------------------------------------------------------------------

wp = 1      # Configurado por enquanto apenas para n_procar = 1
n_point_k = 0

linha_1 = "================================================="
linha_2 = "========================================================================================================================================================================="

#---------------------------
procar = open("PROCAR", "r")
#---------------------------

for i in range(3):
    VTemp = procar.readline()
      
######################## Loop dos Pontos_k ############################
                                                                      
for point_k in range(1, (nk+1)):

    if (point_k == 1):
           print("Analisando o arquivo PROCAR")  

    if (point_k > point_antes and point_k < point_depois):            # Criterio para definir quais pontos-k serão analisados.            

        VTemp = procar.readline().split()
        k_b1 = float(VTemp[3])
        k_b2 = float(VTemp[4])
        k_b3 = float(VTemp[5]) 
        VTemp = procar.readline()

        print(f'Analisando o ponto-k {point_k}')

        contrib_ions.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contrib_ions.write(f'Ponto-k {point_k}: Coord. Diretas ({k_b1}, {k_b2}, {k_b3}) \n')
        contrib_ions.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contrib_ions.write(" \n")

        contrib_orbitais.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contrib_orbitais.write(f'Ponto-k {point_k}: Coord. Diretas ({k_b1}, {k_b2}, {k_b3}) \n')
        contrib_orbitais.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contrib_orbitais.write(" \n")       

########################## Loop das Bandas ############################

        for Band_n in range (1, (nb+1)):

            if (Band_n > Band_antes and Band_n < Band_depois):          # Criterio para definir quais bandas serão analisadas.

               contrib_ions.write(f'Banda {Band_n} \n')
               contrib_ions.write(f'{linha_1}=== \n')

               contrib_orbitais.write(f'Banda {Band_n:<3} \n')             
               
               if (lorbit >= 11): 
                  contrib_orbitais.write(f'{linha_2} \n')
               if (lorbit == 10):
                  contrib_orbitais.write(f'{linha_1} \n')

               for i in range(3):
                   VTemp = procar.readline()

               orb_total = 0.0; soma = 0.0
               soma_s = 0.0; soma_p = 0.0; soma_d = 0.0
               soma_px = 0.0; soma_py = 0.0; soma_pz = 0.0
               soma_dxy = 0.0; soma_dyz = 0.0; soma_dz2 = 0.0; soma_dxz = 0.0; soma_dx2 = 0.0

            
############################ Loop dos ions #############################

#====================== Lendo o Orbital Total ==========================

               for ion_n in range (1, (ni+1)):
                   # ------------------
                   atomo[ion_n] = ion_n
                   # ------------------
                   if (lorbit >= 11):
                      VTemp = procar.readline().split()
                      # -------------------------------
                      ion = int(VTemp[0])
                      s[ion_n] = float(VTemp[1]); py[ion_n] = float(VTemp[2]); pz[ion_n] = float(VTemp[3]); px[ion_n] = float(VTemp[4])
                      dxy[ion_n] = float(VTemp[5]); dyz[ion_n] = float(VTemp[6]); dz2[ion_n] = float(VTemp[7]); dxz[ion_n] = float(VTemp[8]); dx2[ion_n] = float(VTemp[9])
                      # -------------------------------                    
                      p[ion_n] = px[ion_n] + py[ion_n] + pz[ion_n]
                      d[ion_n] = dxy[ion_n] + dyz[ion_n] + dz2[ion_n] + dxz[ion_n] + dx2[ion_n]
                      tot[ion_n] = s[ion_n] + p[ion_n] + d[ion_n]

                   if (lorbit == 10):
                      VTemp = procar.readline().split()
                      # -------------------------------
                      ion = int(VTemp[0]); s[ion_n] = float(VTemp[1]); p[ion_n] = float(VTemp[2]); d[ion_n] = float(VTemp[3])
                      # -------------------------------
                      tot[ion_n] = s[ion_n] + p[ion_n] + d[ion_n]

                   orb_total = orb_total + tot[ion_n]
                   
#-----------------------------------------------------------------------

               for ion_n in range (1, (ni+1)):
                   if (lorbit >= 11):
                      s[ion_n] = (s[ion_n]/orb_total)*100; p[ion_n] = (p[ion_n]/orb_total)*100; d[ion_n] = (d[ion_n]/orb_total)*100
                      px[ion_n] = (px[ion_n]/orb_total)*100; py[ion_n] = (py[ion_n]/orb_total)*100; pz[ion_n] = (pz[ion_n]/orb_total)*100
                      dxy[ion_n] = (dxy[ion_n]/orb_total)*100; dyz[ion_n] = (dyz[ion_n]/orb_total)*100; dz2[ion_n] = (dz2[ion_n]/orb_total)*100
                      dxz[ion_n] = (dxz[ion_n]/orb_total)*100; dx2[ion_n] = (dx2[ion_n]/orb_total)*100 
                      #-------------------------
                      soma_s = soma_s + s[ion_n]; soma_p = soma_p + p[ion_n]; soma_d = soma_d + d[ion_n]
                      soma_px = soma_px + px[ion_n]; soma_py = soma_py + py[ion_n]; soma_pz = soma_pz + pz[ion_n]
                      soma_dxy = soma_dxy + dxy[ion_n]; soma_dyz = soma_dyz + dyz[ion_n]; soma_dz2 = soma_dz2 + dz2[ion_n]
                      soma_dxz = soma_dxz + dxz[ion_n]; soma_dx2 = soma_dx2 + dx2[ion_n]
                      #-------------------------
                      if (tot[ion_n] != 0):
                         contrib_orbitais.write(f'{rotulo[ion_n]:>2}: ion {atomo[ion_n]:<3} | S = {s[ion_n]:5,.2f}% | P = {p[ion_n]:5,.2f}% | D = {d[ion_n]:5,.2f}% | Px = {px[ion_n]:5,.2f}% | Py = {py[ion_n]:5,.2f}% | Pz = {pz[ion_n]:5,.2f}% | Dxy = {dxy[ion_n]:5,.2f}% | Dyz = {dyz[ion_n]:5,.2f}% | Dz2 = {dz2[ion_n]:5,.2f}% | Dxz = {dxz[ion_n]:5,.2f}% | Dx2 = {dx2[ion_n]:5,.2f}% |  \n')

                   if (lorbit == 10):
                      s[ion_n] = (s[ion_n]/orb_total)*100; p[ion_n] = (p[ion_n]/orb_total)*100; d[ion_n] = (d[ion_n]/orb_total)*100
                      #-------------------------
                      soma_s = soma_s + s[ion_n]; soma_p = soma_p + p[ion_n]; soma_d = soma_d + d[ion_n]
                      #-------------------------
                      if (tot[ion_n] != 0):
                         contrib_orbitais.write(f'ion {atomo[ion_n]:<3} | S = {s[ion_n]:5,.2f}% | P = {p[ion_n]:5,.2f}% | D = {d[ion_n]:5,.2f}% \n')                    
                   
#-----------------------------------------------------------------------                   

               if (lorbit >= 11):

                  VTemp = procar.readline().split()                                             

                  if (lorbit >= 11): 
                     contrib_orbitais.write(f'{linha_2} \n')
                  if (lorbit == 10):
                     contrib_orbitais.write(f'{linha_1} \n')                

                  contrib_orbitais.write(f'Soma:       | S = {soma_s:5,.2f}% | P = {soma_p:5,.2f}% | D = {soma_d:5,.2f}% | Px = {soma_px:5,.2f}% | Py = {soma_py:5,.2f}% | Pz = {soma_pz:5,.2f}% | Dxy = {soma_dxy:5,.2f}% | Dyz = {soma_dyz:5,.2f}% | Dz2 = {soma_dz2:5,.2f}% | Dxz = {soma_dxz:5,.2f}% | Dx2 = {soma_dx2:5,.2f}% |  \n')
 
               if (lorbit == 10):

                  VTemp = procar.readline().split()                                           

                  if (lorbit >= 11): 
                     contrib_orbitais.write(f'{linha_2} \n')
                  if (lorbit == 10):
                     contrib_orbitais.write(f'{linha_1} \n')

                  contrib_orbitais.write(f'            | S = {soma_s:5,.2f}% | P  = {soma_p:5,.2f}% | D  = {soma_d:5,.2f}% | \n')                  

#----------------------------------------------------------------------

               for j in range (1,(ni+1)):
                   rotulo_temp[j] = rotulo[j]

               nj = (ni - 1)
               
               for k in range (1,(nj+1)):
                   w = (ni - k)
                   for l in range (1,(w+1)):
                       if (tot[l] < tot[l+1]):
                          tp1 = tot[l]
                          tot[l] = tot[l+1]
                          tot[l+1] = tp1                        
                          #--------------------
                          tp2 = atomo[l]
                          atomo[l] = atomo[l+1]
                          atomo[l+1] = tp2                   
                          #--------------------
                          tp4 = rotulo_temp[l]
                          rotulo_temp[l] = rotulo_temp[l+1]
                          rotulo_temp[l+1] = tp4                          

               for ion_n in range (1,(ni+1)):
                   tot[ion_n] = (tot[ion_n]/orb_total)*100
                   soma = soma + tot[ion_n]                

                   if (tot[ion_n] != 0):
                      contrib_ions.write(f'{rotulo_temp[ion_n]:>2}: ion {atomo[ion_n]:<3} | Contribuicao: {tot[ion_n]:>6,.3f}% | Soma: {soma:>7,.3f}% \n')

#----------------------------------------------------------------------                  

               if (SO == 2):                                          # Condição para cálculo com acoplamento Spin-órbita
                  #-----------------------------
                  for ion_n in range (1,(ni+1)):
                      VTemp = procar.readline()
                  VTemp = procar.readline()                           # Pulando a linha que contém a soma do Sx de todos os ions
                  #-----------------------------
                  for ion_n in range (1,(ni+1)):
                      VTemp = procar.readline()
                  VTemp = procar.readline()                           # Pulando a linha que contém a soma do Sy de todos os ions
                  #-----------------------------
                  for ion_n in range (1,(ni+1)):
                      VTemp = procar.readline()
                  VTemp = procar.readline()                           # Pulando a linha que contém a soma do Sz de todos os ions                    
                  #-----------------------------

#============ Pulando as linhas referente a fase (LORBIT 12) =========

               if (lorbit == 12):
                  temp2 = ((2*ni)+2)
                  for i in range (1,(temp2+1)):
                      VTemp = procar.readline()
               if (lorbit != 12):
                  VTemp = procar.readline()

               if (Band_n < (Band_f+1)):

                  contrib_ions.write(f'{linha_1}=== \n')
                  contrib_ions.write(" \n")

                  if (lorbit >= 11): 
                     contrib_orbitais.write(f'{linha_2} \n')
                  if (lorbit == 10):
                     contrib_orbitais.write(f'{linha_1} \n')

                  contrib_orbitais.write(" \n")  

#=================== Bandas excluidas do cálculo =====================

            if (Band_n <= Band_antes or Band_n >= Band_depois):       # Continuação do if que regula as Bandas que serão plotadas ou não.

               if (lorbit == 12):                                     # Válido somente para LORBIT = 12
                  if (SO == 1):                                       # Para cálculo sem acoplamento Spin-órbita.
                     temp3 = (6 + 3*ni)
                  if (SO == 2):                                       # Para cálculo com acoplamento Spin-órbita.
                     temp3 = (9 + 6*ni)
              
               if (lorbit != 12):                                     # Válido somente para LORBIT = 1O ou 11
                  if (SO == 1):                                       # Para cálculo sem acoplamento Spin-órbita.
                     temp3 = (5 + ni)
                  if (SO == 2):                                       # Para cálculo com acoplamento Spin-órbita.
                     temp3 = (8 + 4*ni)
          
               for i in range (1,(temp3+1)):                          # Esta parte do código pula/exclui as Bandas de energia em cada ponto-K, 
                   VTemp = procar.readline()                          # que não foram selecionadas para serem plotadas             
          
         #------------------------
         # Fim do loop das Bandas.
         #------------------------
        
#================== Ignorar linha ao final de cada K-point =============

        if (point_k < nk):
           VTemp = procar.readline()
       
#==================== K_points excluídos do cálculo ====================

    if (point_k <= point_antes or point_k >= point_depois):            # Continuação do if que regula os K_points que serão analisados ou não.

       if (lorbit == 12):                                              # Válido somente para LORBIT = 12
          if (SO == 1):                                                
              temp3 = ((6 + 3*ni)*nb + 3)                              # Para cálculo sem acoplamento Spin-órbita.
          if (SO == 2):
              temp3 = ((9 + 6*ni)*nb + 3)                              # Para cálculo com acoplamento Spin-órbita.
            
       if (lorbit != 12):                                              # Válido somente para LORBIT = 10 ou 11
          if (SO == 1):             
             temp3 = ((5 + ni)*nb + 3)                                 # Para cálculo sem acoplamento Spin-órbita.
          if (SO == 2):        
             temp3 = ((8 + 4*ni)*nb + 3)                               # Para cálculo com acoplamento Spin-órbita.
            
       for i in range (1,(temp3+1)):                                   # Esta parte do código pula/exclui os K_points que não foram selecionados para serem plotados.
           VTemp = procar.readline()          

    if (point_k >= point_depois):
       print(" ")
       print("======================= Concluido =======================")
       break
            
#--------------------------
# Fim do loop dos K_points.
#--------------------------

#-------------
procar.close()
contrib_ions.close()
contrib_orbitais.close()
inform.close()
#-------------

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################
