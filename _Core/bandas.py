
#-------------------------------------
bandas = open("saida/Bandas.agr", "w")
#-------------------------------------

# Instruções para o GRACE ler o arquivo "Estrutura_de_Bandas.agr" #####

bandas.write("# Grace project file \n")
bandas.write("# \n")
bandas.write("@version 50122 \n")
bandas.write("@with string \n")
bandas.write("@    string on \n")
bandas.write("@    string 0.1, 0.96 \n")
bandas.write(f'@    string def "E(eV)" \n')
bandas.write("@with string \n")
bandas.write("@    string on \n")

if (Dimensao == 1):
   bandas.write("@    string 0.66, 0.017 \n")
   bandas.write(f'@    string def "(2pi/Param.)" \n')
if (Dimensao == 2):
   bandas.write("@    string 0.70, 0.017 \n")
   bandas.write(f'@    string def "(1/Angs.)" \n')
if (Dimensao == 3):
   bandas.write("@    string 0.73, 0.017 \n")
   bandas.write(f'@    string def "(1/nm)" \n')

bandas.write("@with g0 \n")
bandas.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
bandas.write("@    view 0.1, 0.075, 0.8, 0.95 \n")

escala_x = (x_final - x_inicial)/5
escala_y = (y_final - y_inicial)/5
bandas.write(f'@    xaxis  tick major {escala_x:.2f} \n')
bandas.write(f'@    yaxis  tick major {escala_y:.2f} \n')

##################### Plot da Estrutura de Bandas #####################
      
for Band_n in range (Band_i,(Band_f+1)):
    bandas.write(" \n")
    for j in range (1,(n_procar+1)):
        for point_k in range (1,(nk+1)):
            bandas.write(f'{xx[j][point_k]} {y[j][point_k][Band_n]} \n')

# Destacando a Energia de Fermi na Estrutura de Bandas.
      
if (destacar_efermi == 1):
   bandas.write(" \n")
   bandas.write(f'{xx[1][1]} 0.0 \n')
   bandas.write(f'{xx[n_procar][point_f]} 0.0 \n')

# Destacando pontos-k de interesse na estrutura de Bandas.

if (n_procar == 1):
   if (destacar_pontos_k == 1):
      for loop in range (1,(contador2+1)):
          bandas.write(" \n")
          bandas.write(f'{dest_pk[loop]} {energ_min} \n')
          bandas.write(f'{dest_pk[loop]} {energ_max} \n')

# Destacando alguns pontos-k de interesse na Estrutura de Bandas.

if (n_procar > 1):
   wr = n_procar + 1
   for loop in range (1,(wr+1)):
       bandas.write(" \n")
       if (loop != wr):
          bandas.write(f'{xx[loop][1]} {energ_min} \n')
          bandas.write(f'{xx[loop][1]} {energ_max} \n')
       if (loop == wr):
          bandas.write(f'{xx[n_procar][nk]} {energ_min} \n')
          bandas.write(f'{xx[n_procar][nk]} {energ_max} \n')        

#-------------
bandas.close()
#-------------
