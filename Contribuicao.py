##############################################################
# Versao 4.006 (02/09/2021) ##################################
########################## Autores: ##########################
# Augusto de Lelis Araújo - INFIS/UFU (Uberlândia/MG) ########
# e-mail: augusto-lelis@outlook.com ##########################
# ---------------------------------------------------------- #
# Renan Maciel da Paixão - ????????????????????????????????? #
# e-mail: ?????????????????????.com ##########################
##############################################################

#---------------------------------
exec(open("extraction.py").read())
#---------------------------------



############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### BLOCO 2: EXTRAÇÃO DOS RESULTADOS ###################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################



#######################################################
############ Lendo o arquivo de input #################
#######################################################

#-------------------------------------------
entrada = open("input_Contribuicao.txt", "r")
#-------------------------------------------

for i in range(7):
    VTemp = entrada.readline()
Band_i = int(VTemp)                            # Banda inicial a ser analisada.

for i in range(3):
    VTemp = entrada.readline()
Band_f = int(VTemp)                            # Banda final a ser analisada.

for i in range(3):
    VTemp = entrada.readline()
point_i = int(VTemp)                            # Ponto-k inicial a ser analisada.

for i in range(3):
    VTemp = entrada.readline()
point_f = int(VTemp)                            # Ponto-k final a ser analisada.

#--------------
entrada.close()
#--------------

#---------------------------
Band_antes   = (Band_i  -1)                    # Bandas que não serão analisadas
Band_depois  = (Band_f  +1)                    # Bandas que não serão analisadas
point_antes  = (point_i -1)                    # Pontos-k que não serão analisados
point_depois = (point_f +1)                    # Pontos-k que não serão analisados

#----------------------------------------------------
contrib_ions = open("Contribuicao_dos_ions.txt", "w")
contrib_orbitais = open("Contribuicao_Orbitais.txt", "w")
#---------------------------

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
tot = [0]*(ni+1)

#--------------------------------------------------------------

wp = 1      # Configurado por enquanto apenas para n_procar = 1
n_point_k = 0

#---------------------------
procar = open("PROCAR", "r")
#---------------------------

for i in range(3):
    VTemp = procar.readline()
      
######################## Loop dos Pontos_k ############################
                                                                      
for point_k in range(1, (nk+1)):                                     

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

            # if (point_k == point_f and Band_n == Band_depois):        # Criterio para interromper a execução do programa.
               # break

            if (Band_n > Band_antes and Band_n < Band_depois):        # Criterio para definir quais bandas serão analisadas.

               contrib_ions.write(f'Banda {Band_n} \n')
               contrib_ions.write("==================================================== \n")

               contrib_orbitais.write(f'Banda {Band_n:<3} \n')

               # if (Band_n == Band_i):
                  # contrib_ions.write("==================================================== \n")              
               
               if (lorbit >= 11): 
                  contrib_orbitais.write("============================================================================================================================================================== \n")
               if (lorbit == 10):
                  contrib_orbitais.write("================================================= \n")

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
                      # -------------------------------
                      VTemp = procar.readline().split()
                      # -------------------------------
                      ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                      dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); total = float(VTemp[10])
                      # -----------------------------------------------------------------------------------------------------------------------------------------
                      p = (px + py + pz); d = (dxy + dyz + dz2 + dxz + dx2)
                      # soma_s = (soma_s + s); soma_p = (soma_p + p); soma_d = (soma_d + d)
                      # soma_px = (soma_px + px); soma_py = (soma_py + py); soma_pz = (soma_pz + pz)
                      # soma_dxy = (soma_dxy + dxy); soma_dyz = (soma_dyz + dyz); soma_dz2 = (soma_dz2 + dz2); soma_dxz = (soma_dxz + dxz); soma_dx2 = (soma_dx2 + dx2)
                      # -----------------------------------------------------------------------------------------------------------------------------------------------
                      if (total != 0):
                         contrib_orbitais.write(f'{rotulo[ion_n]:>2}: ion {atomo[ion_n]:<3} | S = {s:.3f} | P = {p:.3f} | D = {d:.3f} | Px = {px:.3f} | Py = {py:.3f} | Pz = {pz:.3f} | Dxy = {dxy:.3f} | Dyz = {dyz:.3f} | Dz2 = {dz2:.3f} | Dxz = {dxz:.3f} | Dx2 = {dx2:.3f} |  \n')

                   if (lorbit == 10):
                      VTemp = procar.readline().split() 
                      ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); total = float(VTemp[4])
                      # soma_s = (soma_s + s); soma_p = (soma_p + p); soma_d = (soma_d + d)            

                      if (total != 0):
                         contrib_orbitais.write(f'ion {atomo[ion_n]:<3} | S = {s:.3f} | P = {p:.3f} | D = {d:.3f} \n')

                   tot[ion_n] = total
                   orb_total = orb_total + total
                   
#-----------------------------------------------------------------------

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

               if (lorbit >= 11):

                  VTemp = procar.readline().split()                            
                  soma_s = float(VTemp[1]); soma_py = float(VTemp[2]); soma_pz = float(VTemp[3]); soma_px = float(VTemp[4])
                  soma_p = (soma_px + soma_py + soma_pz)
                  soma_dxy = float(VTemp[5]); soma_dyz = float(VTemp[6]); soma_dz2 = float(VTemp[7]); soma_dxz = float(VTemp[8]); soma_dx2 = float(VTemp[9]); soma_total = float(VTemp[10])
                  soma_d = (soma_dxy + soma_dyz + soma_dz2 + soma_dxz + soma_dx2)                   

                  if (lorbit >= 11): 
                     contrib_orbitais.write("============================================================================================================================================================== \n")
                  if (lorbit == 10):
                     contrib_orbitais.write("================================================= \n")                

                  contrib_orbitais.write(f'Soma:       | S = {soma_s:.3f} | P = {soma_p:.3f} | D = {soma_d:.3f} | Px = {soma_px:.3f} | Py = {soma_py:.3f} | Pz = {soma_pz:.3f} | Dxy = {soma_dxy:.3f} | Dyz = {soma_dyz:.3f} | Dz2 = {soma_dz2:.3f} | Dxz = {soma_dxz:.3f} | Dx2 = {soma_dx2:.3f} |  \n')
 
               if (lorbit == 10):

                  VTemp = procar.readline().split()                             
                  soma_s = float(VTemp[1]); soma_p = float(VTemp[2]); soma_d = float(VTemp[3]); soma_total = float(VTemp[4])                
                

                  if (lorbit >= 11): 
                     contrib_orbitais.write("============================================================================================================================================================== \n")
                  if (lorbit == 10):
                     contrib_orbitais.write("================================================= \n")

                  contrib_orbitais.write(f'            | S = {soma_s:.3f} | P  = {soma_p:.3f} | D  = {soma_d:.3f} | \n')                  

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

                  contrib_ions.write("==================================================== \n")
                  contrib_ions.write(" \n")

                  if (lorbit >= 11): 
                     contrib_orbitais.write("============================================================================================================================================================== \n")
                  if (lorbit == 10):
                     contrib_orbitais.write("================================================= \n")

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
