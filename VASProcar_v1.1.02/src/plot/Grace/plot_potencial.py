
for l in range(1,(3+1)):

    if (l == 1):      
       print ("Analisando a direcao-X ==================================")
       name = 'Potencial_x'; eixo = 'X '; t_grid = Grid_x; coord = ion_x
       dx = fator_x/20; x_inicial = (0.0 - dx); x_final = (fator_x + dx)
       dy = (max(Vx) - min(Vx))/20; y_inicial = (min(Vx) - dy); y_final = (max(Vx) + dy)    
       
    if (l == 2):
       print ("Analisando a direcao-Y ==================================")      
       name = 'Potencial_y'; eixo = 'Y '; t_grid = Grid_y; coord = ion_y
       dx = fator_y/20; x_inicial = (0.0 - dx); x_final = (fator_y + dx)
       dy = (max(Vy) - min(Vy))/20; y_inicial = (min(Vy) - dy); y_final = (max(Vy) + dy)
       
    if (l == 3):
       print ("Analisando a direcao-Z ==================================")      
       name = 'Potencial_z'; eixo = 'Z '; t_grid = Grid_z; coord = ion_z
       dx = fator_z/20; x_inicial = (0.0 - dx); x_final = (fator_z + dx)
       dy = (max(Vz) - min(Vz))/20; y_inicial = (min(Vz) - dy); y_final = (max(Vz) + dy)

    #----------------------------------------------------------------------
    potencial = open(dir_files + '/output/Potencial/' + name + '.agr', "w")
    #----------------------------------------------------------------------

    potencial.write("# Grace project file \n")
    potencial.write("# ============================================================== \n")
    potencial.write(f'# written using VASProcar version {version} - Python tools for VASP \n')
    potencial.write(f'# {url_1} \n')
    potencial.write(f'# {url_2} \n') 
    potencial.write("# ============================================================== \n")
    potencial.write("@version 50122 \n")
    potencial.write("@with g0 \n")
    potencial.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
    # potencial.write(f'@    view {fig_xmin}, {fig_ymin}, {fig_xmax}, {fig_ymax} \n')

    escala_x = (x_final - x_inicial)/5
    escala_y = (y_final - y_inicial)/5

    potencial.write(f'@    xaxis  tick major {escala_x:.2f} \n')
    if (Dimensao == 1):
       label = eixo + '(Angs.)'
       potencial.write(f'@    xaxis  label "{label}" \n') 
    if (Dimensao == 2):
       label = eixo + '(nm)'
       potencial.write(f'@    xaxis  label "{label}" \n') 
 
    potencial.write(f'@    yaxis  tick major {escala_y:.2f} \n')
    potencial.write(f'@    yaxis  label "Potencial Eletrostatico (V)" \n')

    #======================================================================

    if (destaque == 0): ni = 0
    if (destaque == 1): ni = ni

    for i in range(1,((ni+1)+1)):

        if (destaque == 1 and i <= ni): color = 7 # cor Cinza
        if (i > ni): color = 2  # cor Vermelha
   
        potencial.write(f'@    s{i-1} type xy \n')
        potencial.write(f'@    s{i-1} line type 1 \n')
        potencial.write(f'@    s{i-1} line color {color} \n')

        if (i <= ni):
           potencial.write(f'@    s{i-1} line linestyle 1 \n')        
           potencial.write(f'@    s{i-1} line linewidth 0.5 \n')
        if (i > ni):
           potencial.write(f'@    s{i-1} line linestyle 1 \n')        
           potencial.write(f'@    s{i-1} line linewidth 2.0 \n')

    potencial.write(f'@type xy \n')

    # Destacando as coordenadas dos ions da rede:
            
    if (destaque == 1): 
       for i in range (ni):
           potencial.write(f'{coord[i]} {y_inicial} \n')
           potencial.write(f'{coord[i]} {y_final} \n')     
           potencial.write(" \n")    
    
    # Plot do valor m??dio do potencial eletrostatico em uma dada dire????o:
    
    for i in range (t_grid):
       
        if (l == 1):
           X[i] = (float(i)/(float(Grid_x) - 1.0))*fator_x
           potencial.write(f'{X[i]} {Vx[i]} \n')

        if (l == 2):
           Y[i] = (float(i)/(float(Grid_y) - 1.0))*fator_y
           potencial.write(f'{Y[i]} {Vy[i]} \n')

        if (l == 3):
           Z[i] = (float(i)/(float(Grid_z) - 1.0))*fator_z
           potencial.write(f'{Z[i]} {Vz[i]} \n')           

    #----------------
    potencial.close()
    #----------------
    
