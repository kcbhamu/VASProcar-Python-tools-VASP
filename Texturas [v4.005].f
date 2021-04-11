      program TEXTURAS
      ! Autor: Augusto de Lelis Araujo - INFIS/UFU (Uberlandia/MG)
      ! Versao 4.005 (18/10/2020)
      
      Character c1*15,c2*20,c3*19,grac*4,c9*18,c*3
      Character term1*15,term2*15,term3*15
      parameter(nk_max=1000,nb_max=5000,nproc_max=10)
      real xx(nk_max,nb_max)
      real y(nproc_max,nk_max,nb_max)
      real dest_pk(nk_max)
      integer Band_i,Band_f,Band_antes,Band_depois,ni,nb,nk,e,n_procar
      integer ion_i,ion_f,ion_antes,ion_depois,point_k,Band_n,ion_n,wp
      integer i,number,number1,cont,numeracao
      integer peso,nada,cond,esc,numeracao_2,t,int_crit,int_crit_2
      real s,p,d,py,pz,px,dxy,dyz,dz2,dxz,dx2,rest,nii,Band_nn
      real orb_tot,orb_sx,orb_sy,orb_sz,orb_S,orb_P,orb_D
      real tot,totsx,totsy,totsz,S_Max,S_Min,Stotal_Max
      real number2,massa,peso1,peso2,peso3,peso4,peso5,peso6,peso7,peso8
      real peso9,peso10,number3,x,xinicial,xfinal,yinicial,yfinal
      real delta_xi,delta_xf,delta_yi,delta_yf
!-----------------------------------------------------------------------
      real Parametro,A1x,A1y,A1z,A2x,A2y,A2z,A3x,A3y,A3z
      real B1x,B1y,B1z,B2x,B2y,B2z,B3x,B3y,B3z,ss1,ss2,ss3,ss
      real Coord_X,Coord_Y,Coord_Z,k_b1,k_b2,k_b3,dE
      real Coord_X_antes,Coord_Y_antes,Coord_Z_antes,comp,comp_antes
      real delta_X,delta_Y,delta_Z
!-----------------------------------------------------------------------
      integer ps
      parameter (ps=201)
      integer w,j,temp2,temp3
      real peso_1(ps),peso_x,peso_inicial,peso_final,peso_total
      real int_1(ps),int_2(ps),int_x,int_inicial,int_final
!-----------------------------------------------------------------------
      Character am*1,bm*1,cm*1,dm*1,g1m*3,h1m*3,n1m*6,m1m*6
      Character wx*5,em*6,fm*6,gm*4,hm*4,im*7,jm*7,km*7,lm*7,mm*6,nm*6
      Character aw*4,bw*4,cw*4,dw*6,ew*5,fw*4,gw*6,hw*5
      integer SO,n1,k1,k2,n1_valencia,n1_conducao,point_i,point_f
      real Efermi,criterio,energ_tot,resto_crit,criterio_2
      real n2,n3,menor_n2,maior_n2,GAP,resto_crit_2,raio
!-----------------------------------------------------------------------
      integer ww
      parameter (ww=500)
      integer ion_selec(ww)
      character sim_nao(ww)*3,temp_sn*3
!-----------------------------------------------------------------------
      integer num_tot,esc_2,criterio_1,wm,wn,wo
      real Sx_Max,Sy_Max,Sz_Max,Sx_Min,Sy_Min,Sz_Min
      real orb_Px,orb_Py,orb_Pz,energ_min,energ_max
      integer destacar_efermi,destacar_pontos_k,loop,temp_pk,ccontrol1
!-----------------------------------------------------------------------
      integer temp_xk,color,cc,controle,wr,interacao,contador2
      parameter (cc=9)
      integer cor(cc),loop_i,loop_f,n_point_k,r1,nk_total
      real mag_s_x,mag_s_y,mag_s_z,mag_p_x,mag_p_y,mag_p_z,n_eletrons
      real mag_d_x,mag_d_y,mag_d_z,mag_tot_x,mag_tot_y,mag_tot_z
      real dE1,dE2,dE3,dE4,dE5,dE6,dE7,dE8,dE9,dE10
      real r2,r3,r4,comprim,comprim_old,dif
      Character xk*13,wk*13,yk*3
!-----------------------------------------------------------------------

      interacao = 0 ! interacao = 0 (Leitura do arquivo de input)
                    ! interacao = 1 (input inserido manualmente)

!#######################################################################
!###################### Leitura do Arquivo PROCAR ######################
!#######################################################################

      if (interacao.EQ.0) then

        open(37,file ='input_Texturas.txt', ACCESS = 'SEQUENTIAL')

        read(37,*);read(37,*);read(37,*);read(37,*);read(37,*)
        read(37,*) Dimensao

        read(37,*);read(37,*)
        read(37,*) n_procar   ! Numero de arquivos PROCAR (maximo de 10)

        do i=1,6; read(37,*); end do
        read(37,*) e          ! Tamanho/Peso das esferas do grafico

        read(37,*); read(37,*)
        read(37,*) peso_total   ! ions analisados                       ! Digite 0 para Plotar todas as Bandas
                                                                        ! Digite 1 para Plotar Bandas selecionadas
        read(37,*); read(37,*); read(37,*); read(37,*)
        read(37,*) esc

        esc_b = 1
        destacar_efermi = 1
        destacar_pontos_k = 1

        close (37)

      !&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
      end if !&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
      !&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

!-----------------------------------------------------------------------

100   format(a15,i4,a20,i4,a19,i4)
102   format(a18,3f11.8)
104   format(a4,a4,a9,f14.8,a19)
70    format(7F16.9)
                                                                        !Obs.: Codigo das cores
      cor(1) = 1    ! Cor da componente Nula do Spin (Preto)            !Branco=0, Preto=1, Vermelho=2, Verde=3, Azul=4, Amarelo=5, Marrom=6, Cinza=7
      cor(2) = 2    ! Cor da componente Up do Spin   (Vermelho)         !Violeta=8, Cyan=9, Magenta=10, Laranja=11, Indigo=12, Marron=13, Turquesa=14
      cor(3) = 4    ! Cor da componente Down do Spin (Azul)
      cor(4) = 4    ! Cor do Orbital S (Azul)
      cor(5) = 2    ! Cor do Orbital P (Vermelho)
      cor(6) = 3    ! Cor do Orbital D (Verde)
      cor(7) = 4    ! Cor do Orbital Px (Azul)
      cor(8) = 2    ! Cor do Orbital Py (Vermelho)
      cor(9) = 3    ! Cor do Orbital Pz (Verde)

      peso_inicial = 0.0      ! Menor tamanho de esfera no XMGrace.

!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

      print *, "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
      print *, "Versao 4.005 (18/10/2020) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
      print *, "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

      print *, ""
      print *, "#######################################################"
      print *, "########## Analisando o arquivo OUTCAR ################"
      print *, "######## Buscando informacoes do Sistema ##############"
      print *, "#######################################################"
      print *, ""

!#######################################################################
!######### Procedimento para obter informacoes no arquivo PROCAR #######
!#######################################################################

      if (n_procar.EQ.1) then
      open(10,file ='PROCAR', ACCESS = 'SEQUENTIAL')
      else if (n_procar.NE.1) then
      open(10,file ='PROCAR.1', ACCESS = 'SEQUENTIAL')
      end if
      
      open(12,file ='OUTCAR', ACCESS = 'SEQUENTIAL')
      open(17,file='informacoes.txt',status='unknown')

      read(10,*)
      read(10,100)c1,nk,c2,nb,c3,ni                                     ! Leitura do n§ de pontos_k, bandas e ions.
      close (10)

!#######################################################################
!######### Procedimento para obter informacoes no arquivo OUTCAR #######
!#######################################################################

!-----------------------------------------------------------------------
! Verificacao se o calculo foi realizado com ou sem o acoplamento SO
!-----------------------------------------------------------------------

      em = "xxxxxx"
      fm = "ICHARG"                                                     ! ICHARG e uma palavra presente em uma linha anterior a linha que contem a informacao sobre a variavel ISPIN.

      do while (em.NE.fm)
      read(12,*)em
      end do

      read(12,*)wx,am,ispin                                             ! Leitura do valor associado a variavel ISPIN.

      if (ispin.EQ.2) then
      print *,""
      print *,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
      print *,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
      print *,""
      print *,"Este programa nao foi compilado para analisar um calculo"
      print *,"com polarizacao de Spin (ISPIN = 2)"
      print *,"********************************************************"
      print *,"Modifique o codifo fonte, ou refaca seu calculo"
      print *,"********************************************************"
      print *,""
      print *,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
      print *,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
      print *,""
      print *,""
      pause
      end if

      read(12,*)

      cm = "F"
      dm = "T"
      lm = "LSORBIT"

      read(12,*)km,am,bm                                                ! Leitura do valor associado a variavel LSORBIT.
        if (km.EQ.lm.AND.bm.EQ.cm) then
        SO = 1
      print *,"-------------------------------------------------------"
        print *, "LSORBIT = .FALSE. (Calculo sem acoplamento SO)"
      write(17,*)"----------------------------------------------------"
        write(17,*)"LSORBIT = .FALSE. (Calculo sem acoplamento SO)"
        else if (km.EQ.lm.AND.bm.EQ.dm) then
        SO = 2
      print *,"-------------------------------------------------------"
        print *,"LSORBIT = .TRUE. (Calculo com acoplamento SO)"
      write(17,*)"----------------------------------------------------"
        write(17,*)"LSORBIT = .TRUE. (Calculo com acoplamento SO)"
        end if

!-----------------------------------------------------------------------
! Verificacao do numero de eletrons do sistema.
!-----------------------------------------------------------------------

      g1m = "xxx"
      h1m = "VCA"                                                       ! VCA e uma palavra presente em uma linha anterior a linha que contem a informacao sobre a variavel NELECT.

      do while (g1m.NE.h1m)
      read(12,*)g1m
      end do

      read(12,*)m1m,am,n_eletrons                                       ! Leitura do valor associado a variavel NELECT.

!-----------------------------------------------------------------------

      print *,"-------------------------------------------------------"
      print *, "n. de Pontos K =",nk,"; n. de Bandas =",nb,"; n. de ions&
     & =",ni,""
      print *, "n. de eletrons =",n_eletrons,""
      write(17,*)"----------------------------------------------------"
      write(17,*)"n. de Pontos K =",nk,"; n. de Bandas =",nb,"; n. de io&
     &ns =",ni,""
      write(17,*)"n. de eletrons =",n_eletrons,""

!-----------------------------------------------------------------------
! Verificacao do LORBIT utilizado para a geracao do arquivo PROCAR.
!-----------------------------------------------------------------------

      gm = "xxxx"
      hm = "LELF"                                                       ! LELF e uma palavra presenta em uma linha anterior a linha que contem a informacao sobre a variavel LORBIT.

      do while (gm.NE.hm)
      read(12,*)gm
      end do

      nm = "LORBIT"

      read(12,*)mm,am,lorbit                                            ! Leitura do valor associado a variavel LORBIT.
      if (mm.EQ.nm) then
      print *, "-----------------------------------------------------"
      print *, "LORBIT =",lorbit," / ISPIN =",ispin," (sem polarizacao d&
     &e spin)"
      print *, "-----------------------------------------------------"
      write(17,*)"---------------------------------------------------"
      write(17,*)"LORBIT =",lorbit," / ISPIN =",ispin," (sem polarizacao&
     & de spin)"
      write(17,*)"---------------------------------------------------"
      end if

!-----------------------------------------------------------------------
! Busca da Energia de Fermi do sistema.
!-----------------------------------------------------------------------

      im = "xxxxxxx"
      jm = "average"                                                    ! average e uma palavra presente em uma linha um pouco anterior a linha que contem a informacao sobre a variavel E-fermi.

      do while (im.NE.jm)
      read(12,*)im
      end do

      read(12,*);read(12,*)

      nii = real(ni)                                                    ! Converte a variavel inteira (ni) para o tipo real
      criterio = (nii/5.0)
      int_crit = int(criterio)                                          ! Retorna a parte inteira do numero real (criterio)
      resto_crit = mod(criterio,1.0)                                    ! Retorna a parte fracionaria do numero real (criterio)

      if (int_crit.EQ.0.and.resto_crit.GT.0.0) then
      criterio_1 = 1
      do i=1,criterio_1
      read(12,*)
      end do
      else if(int_crit.NE.0.and.resto_crit.EQ.0.0)then
      criterio_1 = int_crit
      do i=1,criterio_1
      read(12,*)
      end do
      else if(int_crit.NE.0.and.resto_crit.GT.0.0)then
      criterio_1 = int_crit + 1
      do i=1,criterio_1
      read(12,*)
      end do
      end if

      read(12,*);read(12,*);read(12,*)

      jm = "E-fermi"

      read(12,*)im,am,Efermi                                            ! Leitura do valor associado a variavel E-fermi.
      if (im.EQ.jm) then
      print *, "Energia de fermi =",Efermi," eV"
      print *, "-----------------------------------------------------"
      write(17,*)"Energia de fermi =",Efermi," eV"
      write(17,*)"---------------------------------------------------"
      end if

!-----------------------------------------------------------------------
! Verificando quais bandas de energia correspondem as bandas de valencia
! e conducao, bem como do respectivo GAP de energia.
! Esta verificacao somente faz sentido para calculos realizados em um
! unico passo, visto que o arquivo CONTCAR analisado pode ou nao conter
! a regiao de menor GAP do sistema.
! Esta verificacao tambem nao faz sentido para sistemas metalicos.
!-----------------------------------------------------------------------

      read(12,*)
      read(12,*)

      menor_n2 = -1000.0
      maior_n2 = 1000.0

      do i=1,nk
      read(12,*)
      read(12,*)
        do j=1,nb
        read(12,*) n1,n2,n3
          if (n3.GT.0.0) then
            if (n2.GT.menor_n2) then
            menor_n2 = n2
            n1_valencia = n1
            k1=i
            end if
          else if (n3.EQ.0.0) then
            if (n2.LT.maior_n2) then
            maior_n2 = n2
            n1_conducao = n1
            k2=i
            end if
          end if
        end do
        read(12,*)
      end do

      GAP = (maior_n2 - menor_n2)

      print *, "Ultima Banda ocupada =",n1_valencia,""
      print *, "Primeira Banda vazia =",n1_conducao,""
      if (k1.EQ.k2) then
      print *, "GAP (direto) =",GAP," eV - Kpoint ",k1,""
      else if (k1.NE.k2) then
      print *, "GAP (indireto) =",GAP," eV  //  Kpoints",k1," e",k2,""
      end if
      print *, "------------------------------------------------------"
      write(17,*)"Ultima Banda ocupada =",n1_valencia,""
      write(17,*)"Primeira Banda vazia =",n1_conducao,""
      if (k1.EQ.k2) then
      write(17,*) "GAP (direto) =",GAP," eV - Kpoint ",k1,""
      else if (k1.NE.k2) then
      write(17,*)"GAP (indireto) =",GAP," eV  //  Kpoints",k1," e",k2,""
      end if
      write(17,*)"----------------------------------------------------"

!-----------------------------------------------------------------------
! Busca da Energia total do sistema.
!-----------------------------------------------------------------------

      aw = "xxxx"
      bw = "FREE"                                                       ! FREE e uma palavra presente em uma linha que fica duas linhas anteriores a linha que contem a informacao sobre a variavel (free energy TOTEN).

      do while (aw.NE.bw)
      read(12,*)aw
      end do

      read(12,*)

      cw = "free"
      dw = "energy"
      ew = "TOTEN"

      read(12,*)fw,gw,hw,am,energ_tot                                   ! Leitura do valor associado a variavel (free energy TOTEN).
      if (fw.EQ.cw.AND.gw.EQ.dw.AND.hw.EQ.ew) then
      print *, "free energy TOTEN =",energ_tot," eV"
      print *, "-----------------------------------------------------"
      write(17,*)"free energy TOTEN =",energ_tot," eV"
      write(17,*)"---------------------------------------------------"
      end if

!-----------------------------------------------------------------------
! Buscando os valores de Magnetizacao.
!-----------------------------------------------------------------------

      if (SO.EQ.2) then
      temp_xk = 4 + ni
!------------------------- Magentizacao (X): ---------------------------
      xk = "xxxxxxxxxxxxx" ; wk = "magnetization"
      do while (xk.NE.wk); read(12,*)xk; end do
      do i=1,temp_xk; read(12,*); end do
      read(12,*) yk,mag_s_x,mag_p_x,mag_d_x,mag_tot_x
!------------------------- Magentizacao (Y): ---------------------------
      xk = "xxxxxxxxxxxxx" ; wk = "magnetization"
      do while (xk.NE.wk); read(12,*)xk; end do
      do i=1,temp_xk; read(12,*); end do
      read(12,*) yk,mag_s_y,mag_p_y,mag_d_y,mag_tot_y
!------------------------- Magentizacao (Z): ---------------------------
      xk = "xxxxxxxxxxxxx" ; wk = "magnetization"
      do while (xk.NE.wk); read(12,*)xk; end do
      do i=1,temp_xk; read(12,*); end do
      read(12,*) yk,mag_s_z,mag_p_z,mag_d_z,mag_tot_z
!-----------------------------------------------------------------------
      print*,""
      print*,"################### Magnetizacao: #######################"
      print*,"Eixo X:  total =",mag_tot_x,""
      print*,"Eixo Y:  total =",mag_tot_y,""
      print*,"Eixo Z:  total =",mag_tot_z,""
      print*,"#########################################################"
      print*,""
!-----------------------------------------------------------------------
      write(17,*)""
      write(17,*)"################# Magnetizacao: #####################"
      write(17,*)"Eixo X:  total =",mag_tot_x,""
      write(17,*)"Eixo Y:  total =",mag_tot_y,""
      write(17,*)"Eixo Z:  total =",mag_tot_z,""
      write(17,*)"#####################################################"
      write(17,*)""
!-----------------------------------------------------------------------
      end if
!-----------------------------------------------------------------------
      
      close (12)    ! Fechamento do arquivo OUTCAR

!#######################################################################
!##################### Leitura do Arquivo CONTCAR ######################
!#######################################################################

      open (11,file ='CONTCAR', ACCESS = 'SEQUENTIAL')

      read(11,*)

      read(11,*)Parametro                                               ! Leitura do Parametro de rede do sistema.

      read(11,*)A1x,A1y,A1z                                             ! Leitura das coordenadas (X, Y e Z) do vetor primitivo (A1) da celula unitaria no espaco real.
      read(11,*)A2x,A2y,A2z                                             ! Leitura das coordenadas (X, Y e Z) do vetor primitivo (A2) da celula unitaria no espaco real.
      read(11,*)A3x,A3y,A3z                                             ! Leitura das coordenadas (X, Y e Z) do vetor primitivo (A3) da celula unitaria no espaco real.

!-----------------------------------------------------------------------
!------------ Correcao caso o Parametro de Rede nao tenha sido ---------
!----------- corretamente especificado no arquivo POSCAR/CONTCAR -------
!-----------------------------------------------------------------------

      if (Parametro.EQ.1.0) then
      Parametro = SQRT((A1x*A1x) + (A1y*A1y) + (A1z*A1z))
      A1x = A1x/Parametro; A1y = A1y/Parametro; A1z = A1z/Parametro
      A2x = A2x/Parametro; A2y = A2y/Parametro; A2z = A2z/Parametro
      A3x = A3x/Parametro; A3y = A3y/Parametro; A3z = A3z/Parametro
      end if

      if (Parametro.EQ.1.0) then
      Parametro = SQRT((A2x*A2x) + (A2y*A2y) + (A2z*A2z))
      A1x = A1x/Parametro; A1y = A1y/Parametro; A1z = A1z/Parametro
      A2x = A2x/Parametro; A2y = A2y/Parametro; A2z = A2z/Parametro
      A3x = A3x/Parametro; A3y = A3y/Parametro; A3z = A3z/Parametro
      end if
      
      if (Parametro.EQ.1.0) then
      Parametro = SQRT((A3x*A3x) + (A3y*A3y) + (A3z*A3z))
      A1x = A1x/Parametro; A1y = A1y/Parametro; A1z = A1z/Parametro
      A2x = A2x/Parametro; A2y = A2y/Parametro; A2z = A2z/Parametro
      A3x = A3x/Parametro; A3y = A3y/Parametro; A3z = A3z/Parametro
      end if
      
!-----------------------------------------------------------------------

      ss1 = A1x*((A2y*A3z) - (A2z*A3y))
      ss2 = A1y*((A2z*A3x) - (A2x*A3z))
      ss3 = A1z*((A2x*A3y) - (A2y*A3x))
      ss =  ss1 + ss2 + ss3                                             ! Eu apenas divide esta soma em tres partes, uma vez que ela e muito longa, e ultrapassava a extensao da linha.

      B1x = ((A2y*A3z) - (A2z*A3y))/ss                                  ! Para compreender estas operacoes sobre as componentes X, Y e Z dos vetores primitvos da rede
      B1y = ((A2z*A3x) - (A2x*A3z))/ss                                  ! cristalina (A1, A2 e A3), vc deve executar a operacao padrao de construcao dos vetores
      B1z = ((A2x*A3y) - (A2y*A3x))/ss                                  ! primitivos da rede rec¡proca com base nos vetores primitvos da rede cristalina.
      B2x = ((A3y*A1z) - (A3z*A1y))/ss                                  ! Tal operacao se encontra disponivel em qualquer livro de estado solido.
      B2y = ((A3z*A1x) - (A3x*A1z))/ss
      B2z = ((A3x*A1y) - (A3y*A1x))/ss
      B3x = ((A1y*A2z) - (A1z*A2y))/ss
      B3y = ((A1z*A2x) - (A1x*A2z))/ss
      B3z = ((A1x*A2y) - (A1y*A2x))/ss

      write(17,*)"*****************************************************"
      write(17,*)"******* Vetores Primitivos da Rede Reciproca ********"
      write(17,*)"*****************************************************"
      write(17,*)"****"
      write(17,*)"****  B1 = 2pi/Param.(",B1x,",",B1y,",",B1z,")"
      write(17,*)"****  B2 = 2pi/Param.(",B2x,",",B2y,",",B2z,")"
      write(17,*)"****  B3 = 2pi/Param.(",B3x,",",B3y,",",B3z,")"
      write(17,*)"****  Param. =",Parametro," Angs."
      write(17,*)"****"
      write(17,*)"*****************************************************"
      write(17,*)"*****************************************************"

      !*****************************************************************
      ! Dimensao = 1 >> k em unidades de 2pi/Param com Param em Angs. **
      ! DimensÆo = 2 >> k em unidades de 1/Angs. ***********************
      ! Dimensao = 3 >> K em unidades de 1/nm **************************
      !*****************************************************************
      if (Dimensao.EQ.1) then
      fator_zb = 1
      else if (Dimensao.EQ.2) then
      fator_zb = (2*3.1415926535897932384626433832795)/Parametro
      else if (Dimensao.EQ.3) then
      fator_zb = (10*2*3.1415926535897932384626433832795)/Parametro
      end if

      B1x = B1x*fator_zb
      B1y = B1y*fator_zb
      B1z = B1z*fator_zb
      B2x = B2x*fator_zb
      B2y = B2y*fator_zb
      B2z = B2z*fator_zb
      B3x = B3x*fator_zb
      B3y = B3y*fator_zb
      B3z = B3z*fator_zb

      !-----------------------------------------------------------------

      if (interacao.EQ.1) then

        print *, ""
        print *,"######################################################"
        print *,"Digite o numero de arquivos PROCAR (maximo de 10):"
        print *,"######################################################"
        print *, ""
        read *, n_procar
        print *, ""

        print *,"######################################################"
        print *,"Projecoes a serem analisadas:"

        print *,"------------------------------------------------------"
        print *,"Caso voce deseje Plotar apenas a Estrutura de Bandas"
        print *,"Digite 77"
        print *,"Obs.: A Estrutura de Bandas sempre e plotada para as"
        print *,"demais projecoes"

        if (SO.EQ.2) then
        print *,"------------------------------------------------------"
        print *,"Para analisar as Projecoes de Spin (Sx, Sy e Sz)"
        print *,"Digite 99"
        print *,"O Spin_UP sera representado pelas esferas em Vermelho"
        print *,"O Spin_DOWN sera representado pelas esferas em Azul"
        end if
      
        if (lorbit.EQ.10) then
        print *,"------------------------------------------------------"
        print*,"Para analisar as Projecoes dos Orbitais (S, P, D e Total&
     &)"
        print *,"Digite -99"
        end if
      
        if (lorbit.GT.10) then
        print *,"------------------------------------------------------"
        print *,"Para analisar as Projecoes dos Orbitais (S, P, D, Total&
     &, Px, Py e Pz)"
        print *,"Digite -99"
        end if

        if (SO.EQ.1) then
        print *,"------------------------------------------------------"
        print *,"######################################################"
        print *, ""
        end if
      
        if (SO.EQ.2) then
        print *,"------------------------------------------------------"
        print *,"Para analisar todas as Projecoes acima "
        print *,"Digite 100"
        print *,"------------------------------------------------------"
        print *,"######################################################"
        print *,""
        end if
      
        read *, e
        print *, ""
      
        if (e.NE.77) then
        print *,"######################################################"
        print *,"Digite o tamanho/peso das esferas do grafico:"
        print *,"######################################################"
        print *, ""
        read *, peso_total
        print *, ""
        end if

        print *,"######################################################"
        print *,"           O que vc deseja Plotar/Analisar:           "
        print *,"------------------------------------------------------"
        print *,"Para analisar todos os ions ================= Digite 0"
        print *,"Para analisar ions selecionados ============= Digite 1"
        !print *,"Plotar/Analisar Bandas, K_points e ions selecionados:"
        !print *,"Digite 2"
        print *,"------------------------------------------------------"
        print *,"######################################################"
        print *, ""
        read *, esc

        if (esc.NE.0.and.esc.NE.1.and.esc.NE.2) then
        esc=0
        end if
      
        !print*,"######################################################"
        !print*,"      Com relacao as Bandas, vc ainda pode escolher:  "
        !print*,"------------------------------------------------------"
        !print*,"Para Plotar todas as bandas selecionadas  === Digite 1"
        !print*,"Para Plotar as bandas com numeracao par   === Digite 2"
        !print*,"Para Plotar as bandas com numeracao impar === Digite 3"
        !print*,"------------------------------------------------------"
        !print*,"######################################################"
        !print *, ""
        !read *, esc_b
      
        !if (esc_b.NE.1.and.esc_b.NE.2.and.esc_b.NE.3) then
        !esc_b=1
        !end if
      
        esc_b = 1
        
        !print *, "######### Vc deseja destacar o n¡vel de Fermi: #####"
        !print *, "Para NAO, Digite 0 #################################"
        !print *, "Para SIM, Digite 1 #################################"
        !print *, "####################################################"
        !print *, ""
        destacar_efermi = 1
        print *, ""


        !print *, "######### Vc deseja destacar alguns Pontos-K: ######"
        !print *, "Digite 0 para NAO ##################################"
        !print *, "Digite 1 para SIM ##################################"
        !print *, "####################################################"
        !print *, ""
        !read *, destacar_pontos_k
        destacar_pontos_k = 1
        !print *, ""
        !if(destacar_pontos_k.LT.0.or.destacar_pontos_k.GT.1)then
        !print *, "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
        !print *, "Vc digitou um valor errado !!!"
        !print *, "Por favor, reinicie o programa e tente novamente"
        !print *, "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
        !print *, ""
          !if (interacao.NE.0) then
          !pause
          !end if
        !end if

      !&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
      end if !&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
      !&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

      !-----------------------------------------------------------------

      if (lorbit.EQ.10) then
        if (e.EQ.-99.or.e.EQ.100) then
        open (29,file = 'Temp_orb-S_Excluir.txt')
        open (30,file = 'Temp_orb-P_Excluir.txt')
        open (31,file = 'Temp_orb-D_Excluir.txt')
        end if
      end if

      if (lorbit.GT.10) then
        if (e.EQ.-99.or.e.EQ.100) then
        open (26,file = 'Temp_orb-Px_Excluir.txt')
        open (27,file = 'Temp_orb-Py_Excluir.txt')
        open (28,file = 'Temp_orb-Pz_Excluir.txt')
        open (29,file = 'Temp_orb-S_Excluir.txt')
        open (30,file = 'Temp_orb-P_Excluir.txt')
        open (31,file = 'Temp_orb-D_Excluir.txt')
        end if
      end if
        
      if (SO.EQ.2) then
        if (e.EQ.99.or.e.EQ.100) then
        open (33,file = 'Temp_Spin_Sx_Excluir.txt')
        open (34,file = 'Temp_Spin_Sy_Excluir.txt')
        open (35,file = 'Temp_Spin_Sz_Excluir.txt')
        end if
      end if
      
!-----------------------------------------------------------------------
        if (esc.EQ.0.or.esc.EQ.1) then                                  ! Para esc = 0 ou 1, todas as Bandas e K_Points sao plotados.
        Band_i = 1
        Band_f = nb
        point_i = 1
        point_f = nk
        end if
        
        if (esc.EQ.0) then
        ion_i = 1
        ion_f = ni                                                      ! Para esc = 0 ou 1, todas os ions sao analisados.
        end if

!-----------------------------------------------------------------------

        if (esc.EQ.1.or.esc.EQ.2) then

          do i = 1,ni
          sim_nao(i) = "nao"
          end do

          open(18,file ='ions_selecionados.txt', ACCESS = 'SEQUENTIAL')

          read(18,*)loop

          do j = 1,loop
          read(18,*)loop_i,loop_f
            do i = loop_i,loop_f
            sim_nao(i) = "sim"
            end do
          end do
          
          close(18)
          
        end if

!-----------------------------------------------------------------------

      print *, ""
      print *, "Rodando: ##############################################"
      print *, "####### Rodando: ######################################"
      print *, "############### Rodando: ##############################"
      print *, "####################### Rodando: ######################"
      print *, "############################### Rodando: ##############"
      print *, "####################################### Rodando: ######"
      print *, "############################################## Rodando:"
      print *, ""
      print *, ""

      Band_antes = Band_i -1     ! Bandas que nao serao plotadas.
      Band_depois = Band_f +1    ! Bandas que nao serao plotadas.
      point_antes = point_i -1   ! K_points que nao serao plotados.
      point_depois = point_f +1  ! K_points que nao serao plotados.
      ion_antes = ion_i -1       ! ions que nao serao analisados.
      ion_depois = ion_f +1      ! ions que nao serao analisados.
      
      energ_max = -1000
      energ_min = 1000

!-----------------------------------------------------------------------

      ! write(17,*)""
      write(17,*)"*****************************************************"
      write(17,*)"*********** Pontos-k na Zona de Brillouin ***********"
      write(17,*)"*****************************************************"
      write(17,*)""
      
      if (Dimensao.EQ.1) then
      write(17,*)"Ponto-k: Coord. Diretas Kx, Ky e Kz -- Separacao (2Pi/&
     &Param)"
      else if (Dimensao.EQ.2) then
      write(17,*)"Ponto-k: Coord. Diretas Kx, Ky e Kz -- Separacao (1/An&
     &gs.)"
      else if (Dimensao.Eq.3) then
      write(17,*)"Ponto-k: Coord. Diretas Kx, Ky e Kz -- Separacao (1/nm&
     &)"
      end if
      
      write(17,*)""

      n_point_k = 0

!-----------------------------------------------------------------------

!######################### Laco dos PROCAR #############################

      do wp = 1,n_procar

      if (wp.EQ.1.and.n_procar.EQ.1) then
      open (10,file ='PROCAR', ACCESS = 'SEQUENTIAL')
      else if (wp.EQ.1.and.n_procar.NE.1) then
      open (10,file ='PROCAR.1', ACCESS = 'SEQUENTIAL')
      else if (wp.EQ.2) then
      open (10,file ='PROCAR.2', ACCESS = 'SEQUENTIAL')
      else if (wp.EQ.3) then
      open (10,file ='PROCAR.3', ACCESS = 'SEQUENTIAL')
      else if (wp.EQ.4) then
      open (10,file ='PROCAR.4', ACCESS = 'SEQUENTIAL')
      else if (wp.EQ.5) then
      open (10,file ='PROCAR.5', ACCESS = 'SEQUENTIAL')
      else if (wp.EQ.6) then
      open (10,file ='PROCAR.6', ACCESS = 'SEQUENTIAL')
      else if (wp.EQ.7) then
      open (10,file ='PROCAR.7', ACCESS = 'SEQUENTIAL')
      else if (wp.EQ.8) then
      open (10,file ='PROCAR.8', ACCESS = 'SEQUENTIAL')
      else if (wp.EQ.9) then
      open (10,file ='PROCAR.9', ACCESS = 'SEQUENTIAL')
      else if (wp.EQ.10) then
      open (10,file ='PROCAR.10', ACCESS = 'SEQUENTIAL')
      end if

      read(10,*)
      read(10,*)
      read(10,*)
      
!######################## Laco dos Pontos_k ############################

      do point_k=1,nk
      
        if (point_k.GT.point_antes.and.point_k.LT.point_depois) then    ! Criterio para definir quais Pontos_k serao analisados ou ignorados.
      
        read(10,102)c9,k_b1,k_b2,k_b3
        read (10,*)
      
!############### Distancia de separacao entre os pontos-k ##############

        Coord_X = ((K_b1*B1x) + (K_b2*B2x) + (K_b3*B3x))
        Coord_Y = ((K_b1*B1y) + (K_b2*B2y) + (K_b3*B3y))
        Coord_Z = ((K_b1*B1z) + (K_b2*B2z) + (K_b3*B3z))

          if (wp.EQ.1.and.point_k.EQ.point_i) then
          comp = 0.0
          xx(wp,point_k) = comp
          else if(wp.NE.1.or.point_k.NE.point_i) then
          delta_X = Coord_X_antes - Coord_X
          delta_Y = Coord_Y_antes - Coord_Y
          delta_Z = Coord_Z_antes - Coord_Z
          comp = sqrt(delta_X**2 + delta_Y**2 + delta_Z**2)
          comp = comp + comp_antes
          xx(wp,point_k) = comp
          end if

        Coord_X_antes = Coord_X
        Coord_Y_antes = Coord_Y
        Coord_Z_antes = Coord_Z
        comp_antes = comp

112   format(i4,4f12.8)

      n_point_k = n_point_k + 1

      write(17,112)n_point_k,k_b1,k_b2,k_b3,comp

!#######################################################################

        if (n_procar.EQ.1) then
        print *, "Analisando o Ponto_k",point_k,""
        else if (n_procar.GT.1) then
        print *, "Analisando o Ponto_k",point_k," do PROCAR",wp,""
        end if

        if (point_k.EQ.nk) then
        print *, "==================================="
        end if

!########################## Laco das Bandas ############################

          do Band_n = 1,nb

          if (esc_b.EQ.1) then
          Band_nn = real(Band_n)                                        ! Converte a variavel inteira (Band_n) para o tipo real.
          criterio_2 = (Band_n/1.0)
          int_crit_2 = int(criterio_2)                                  ! Retorna a parte inteira do numero real (criterio_2).
          resto_crit_2 = mod(criterio_2,1.0)                            ! Retorna a parte fracionaria do numero real (criterio_2).
          end if
          if (esc_b.NE.1) then
          Band_nn = real(Band_n)                                        ! Converte a variavel inteira (Band_n) para o tipo real.
          criterio_2 = (Band_n/2.0)
          int_crit_2 = int(criterio_2)                                  ! Retorna a parte inteira do numero real (criterio_2).
          resto_crit_2 = mod(criterio_2,1.0)                            ! Retorna a parte fracionaria do numero real (criterio_2).
          end if

            if (esc_b.EQ.1) then ; rest = 0.0 ; end if
            if (esc_b.EQ.2) then ; rest = 0.0 ; end if
            if (esc_b.EQ.3) then ; rest = 0.5 ; end if

            if (Band_n.GT.Band_antes.and.Band_n.LT.Band_depois.and.resto&
     &_crit_2.EQ.rest) then

            read(10,104)c7,c10,c8,energ,c5

!######################### Ajuste das energias #########################

      if (wp.EQ.1) then
      dE  = (Efermi)*(-1)
      y(wp,point_k,Band_n) = energ + dE
      auto_valor = y(wp,point_k,Band_n)
      end if

      if (wp.EQ.2) then
        if (point_k.EQ.point_i.and.Band_n.EQ.Band_i) then !y(2,1,1)
        dE  = y(1,point_f,Band_i) - energ
        end if
      y(wp,point_k,Band_n) = energ + dE
      auto_valor = y(wp,point_k,Band_n)
      end if
      
      if (wp.EQ.3) then
        if (point_k.EQ.point_i.and.Band_n.EQ.Band_i) then !y(3,1,1)
        dE  = y(2,point_f,Band_i) - energ
        end if
      y(wp,point_k,Band_n) = energ + dE
      auto_valor = y(wp,point_k,Band_n)
      end if
      
      if (wp.EQ.4) then
        if (point_k.EQ.point_i.and.Band_n.EQ.Band_i) then !y(4,1,1)
        dE  = y(3,point_f,Band_i) - energ
        end if
      y(wp,point_k,Band_n) = energ + dE
      auto_valor = y(wp,point_k,Band_n)
      end if
      
      if (wp.EQ.5) then
        if (point_k.EQ.point_i.and.Band_n.EQ.Band_i) then !y(5,1,1)
        dE  = y(4,point_f,Band_i) - energ
        end if
      y(wp,point_k,Band_n) = energ + dE
      auto_valor = y(wp,point_k,Band_n)
      end if
      
      if (wp.EQ.6) then
        if (point_k.EQ.point_i.and.Band_n.EQ.Band_i) then !y(6,1,1)
        dE  = y(5,point_f,Band_i) - energ
        end if
      y(wp,point_k,Band_n) = energ + dE
      auto_valor = y(wp,point_k,Band_n)
      end if
      
      if (wp.EQ.7) then
        if (point_k.EQ.point_i.and.Band_n.EQ.Band_i) then !y(7,1,1)
        dE  = y(6,point_f,Band_i) - energ
        end if
      y(wp,point_k,Band_n) = energ + dE
      auto_valor = y(wp,point_k,Band_n)
      end if
      
      if (wp.EQ.8) then
        if (point_k.EQ.point_i.and.Band_n.EQ.Band_i) then !y(8,1,1)
        dE  = y(7,point_f,Band_i) - energ
        end if
      y(wp,point_k,Band_n) = energ + dE
      auto_valor = y(wp,point_k,Band_n)
      end if
      
      if (wp.EQ.9) then
        if (point_k.EQ.point_i.and.Band_n.EQ.Band_i) then !y(9,1,1)
        dE  = y(8,point_f,Band_i) - energ
        end if
      y(wp,point_k,Band_n) = energ + dE
      auto_valor = y(wp,point_k,Band_n)
      end if
      
      if (wp.EQ.10) then
        if (point_k.EQ.point_i.and.Band_n.EQ.Band_i) then !y(10,1,1)
        dE  = y(9,point_f,Band_i) - energ
        end if
      y(wp,point_k,Band_n) = energ + dE
      auto_valor = y(wp,point_k,Band_n)
      end if

!#######################################################################

              if (energ_max.LT.auto_valor) then                         ! Calculo do maior auto-valor de energia.
              energ_max = auto_valor
              end if

              if (energ_min.GT.auto_valor) then                         ! Calculo do menor auto-valor de energia.
              energ_min = auto_valor
              end if
              
              do i = 1,2
              read(10,*)
              end do
          
            orb_total = 0.0
            orb_sx = 0.0
            orb_sy = 0.0
            orb_sz  = 0.0
            orb_S  = 0.0
            orb_P  = 0.0
            orb_D = 0.0
            orb_Px = 0.0
            orb_Py = 0.0
            orb_Pz = 0.0
            
!########################### Laco dos ions #############################

!====================== Lendo o Orbital Total ==========================

              do ion_n=1,ni
!-----------------------------------------------------------------------
                if (esc.EQ.0) then
                  if (ion_n.GT.ion_antes.and.ion_n.LT.ion_depois) then  ! analisando os ions selecionados.
                    if (lorbit.GE.11) then
                    read (10,*) ion,s,py,pz,px,dxy,dyz,dz2,dxz,dx2,tot
                    p = px + py + pz
                    d = dxy + dyz + dz2 + dxz + dx2
                    else if (lorbit.EQ.10) then
                    read (10,*) ion,s,p,d,tot
                    end if
                    
                    orb_total = orb_total + tot

                    if (e.EQ.-99.or.e.EQ.100) then
                    orb_S = orb_S + s
                    orb_P = orb_P + p
                    orb_D = orb_D + d
                    end if

                    if (lorbit.GT.10) then
                      if (e.EQ.-99.or.e.EQ.100) then
                      orb_Px = orb_Px + px
                      orb_Py = orb_Py + py
                      orb_Pz = orb_Pz + pz
                      end if
                    end if

                  else   ! ions nao-selecionados.
                    if (lorbit.GE.11) then
                    read (10,*) ion,s,py,pz,px,dxy,dyz,dz2,dxz,dx2,tot
                    else if (lorbit.EQ.10) then
                    read (10,*) ion,s,p,d,tot
                    end if
                    orb_total = orb_total + tot
                    
                  end if
                  
                end if
!-----------------------------------------------------------------------
                if (esc.EQ.1.or.esc.EQ.2) then                          ! Lendo os ions selecionados no arquivo (ions_selecionados.txt).
                temp_sn = sim_nao(ion_n)
                  if (temp_sn.EQ."sim") then
                    if (lorbit.GE.11) then
                    read (10,*) ion,s,py,pz,px,dxy,dyz,dz2,dxz,dx2,tot
                    p = px + py + pz
                    d = dxy + dyz + dz2 + dxz + dx2
                    else if (lorbit.EQ.10) then
                    read (10,*) ion,s,p,d,tot
                    end if

                    orb_tot = orb_tot + tot                             ! orb_tot refere-se ao Orbital Total a ser plotado
                    orb_total = orb_total + tot                         ! orb_total refere-se a uma quantidade que sera utilizada na normalizacao dos orbitais.

                    if (e.EQ.-99.or.e.EQ.100) then
                    orb_S = orb_S + s
                    orb_P = orb_P + p
                    orb_D = orb_D + d
                    end if
             
                    if (lorbit.GT.10) then
                      if (e.EQ.-99.or.e.EQ.100) then
                      orb_Px = orb_Px + px
                      orb_Py = orb_Py + py
                      orb_Pz = orb_Pz + pz
                      end if
                    end if
                    
                  else if (temp_sn.EQ."nao") then                       ! ions nao-selecionados no arquivo (ions_selecionados.txt).
                    if (lorbit.GE.11) then
                    read (10,*) ion,s,py,pz,px,dxy,dyz,dz2,dxz,dx2,tot
                    else if (lorbit.EQ.10) then
                    read (10,*) ion,s,p,d,tot
                    end if
                    orb_total = orb_total + tot
                    
                  end if
                  
                end if
!-----------------------------------------------------------------------
              end do    ! Fim Parcial do laco dos ions.
!-----------------------------------------------------------------------
              read (10,*)

            if (SO.EQ.2) then                                           ! Condicao para calculo com acoplamento Spin-orbita
            
!===================== Lendo a componente Sx do Spin ===================
              do ion_n=1,ni
!-----------------------------------------------------------------------
                if (e.EQ.99.or.e.EQ.100)then
                  if (esc.EQ.0) then
                    if (ion_n.GT.ion_antes.and.ion_n.LT.ion_depois) then ! analisando os ions selecionados.
                      if (lorbit.GE.11) then
                      read(10,*)ion,s,py,pz,px,dxy,dyz,dz2,dxz,dx2,totsx
                      else if (lorbit.EQ.10) then
                      read (10,*) ion,s,p,d,totsx
                      end if
                    orb_sx = orb_sx + totsx
                    else
                    read (10,*)   ! ignorando os ions nao selecionados.
                    end if
                  end if
!-----------------------------------------------------------------------
                  if (esc.EQ.1.or.esc.EQ.2) then                        ! Lendo os ions selecionados no arquivo (ions_selecionados.txt).
                  temp_sn = sim_nao(ion_n)
                    if (temp_sn.EQ."sim") then
                      if (lorbit.GE.11) then
                      read(10,*)ion,s,py,pz,px,dxy,dyz,dz2,dxz,dx2,totsx
                      else if (lorbit.EQ.10) then
                      read (10,*) ion,s,p,d,totsx
                      end if
                    orb_sx = orb_sx + totsx
                    else if (temp_sn.EQ."nao") then
                    read (10,*)   ! ignorando os ions nao selecionados
                    end if
                  end if
!-----------------------------------------------------------------------
                else
                read (10,*)
                end if
!-----------------------------------------------------------------------
              end do    ! Fim Parcial do laco dos ions.
!-----------------------------------------------------------------------
            read (10,*)
          
!===================== Lendo a componente Sy do Spin ===================
              do ion_n=1,ni
!-----------------------------------------------------------------------
                if (e.EQ.99.or.e.EQ.100)then
                  if (esc.EQ.0) then
                    if (ion_n.GT.ion_antes.and.ion_n.LT.ion_depois) then   ! analisando os ions selecionados.
                      if (lorbit.GE.11) then
                      read(10,*)ion,s,py,pz,px,dxy,dyz,dz2,dxz,dx2,totsy
                      else if (lorbit.EQ.10) then
                      read (10,*) ion,s,p,d,totsy
                      end if
                    orb_sy = orb_sy + totsy
                    else
                    read (10,*)   ! ignorando os ions nao-selecionados.
                    end if
                  end if
!-----------------------------------------------------------------------
                  if (esc.EQ.1.or.esc.EQ.2) then                        ! Lendo os ions selecionados no arquivo (ions_selecionados.txt).
                  temp_sn = sim_nao(ion_n)
                    if (temp_sn.EQ."sim") then
                      if (lorbit.GE.11) then
                      read(10,*)ion,s,py,pz,px,dxy,dyz,dz2,dxz,dx2,totsy
                      else if (lorbit.EQ.10) then
                      read (10,*) ion,s,p,d,totsy
                      end if
                    orb_sy = orb_sy + totsy
                    else if (temp_sn.EQ."nao") then
                    read (10,*)   ! ignorando os ions nao selecionados.
                    end if
                  end if
!-----------------------------------------------------------------------
                else
                read (10,*)
                end if
!-----------------------------------------------------------------------
              end do    ! Fim Parcial do laco dos ions.
!-----------------------------------------------------------------------
            read (10,*)
          
!===================== Lendo a componente Sz do Spin ===================
              do ion_n=1,ni
!-----------------------------------------------------------------------
                if (e.EQ.99.or.e.EQ.100)then
                  if (esc.EQ.0) then
                    if (ion_n.GT.ion_antes.and.ion_n.LT.ion_depois) then ! analisando os ions selecionados.
                      if (lorbit.GE.11) then
                      read(10,*)ion,s,py,pz,px,dxy,dyz,dz2,dxz,dx2,totsz
                      else if (lorbit.EQ.10) then
                      read (10,*) ion,s,p,d,totsz
                      end if
                    orb_sz = orb_sz + totsz
                    else
                    read (10,*)   ! ignorando os ions nao selecionados.
                    end if
                  end if
!-----------------------------------------------------------------------
                  if (esc.EQ.1.or.esc.EQ.2) then                        ! Lendo os ions selecionados no arquivo (ions_selecionados.txt).
                  temp_sn = sim_nao(ion_n)
                    if (temp_sn.EQ."sim") then
                      if (lorbit.GE.11) then
                      read(10,*)ion,s,py,pz,px,dxy,dyz,dz2,dxz,dx2,totsz
                      else if (lorbit.EQ.10) then
                      read (10,*) ion,s,p,d,totsz
                      end if
                    orb_sz = orb_sz + totsz
                    else if (temp_sn.EQ."nao") then
                    read (10,*)   ! ignorando os ions nao selecionados.
                    end if
                  end if
!-----------------------------------------------------------------------
                else
                read (10,*)
                end if
!-----------------------------------------------------------------------
              end do    ! Fim Parcial do laco dos ions.
!-----------------------------------------------------------------------
            read (10,*)
!-----------------------------------------------------------------------
           end if
           
!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
!%%%%%%%%%%%%% Escrita das Texturas em um arquivo temporario %%%%%%%%%%%
!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

              if (e.EQ.-99.or.e.EQ.100) then
              orb_S = ((orb_S/orb_total) + peso_inicial)*peso_total
              write(29,*)comp,auto_valor,orb_S                          ! Escrita do Orbital_S em um arquivo temporario.
              orb_P = ((orb_P/orb_total) + peso_inicial)*peso_total
              write(30,*)comp,auto_valor,orb_P                          ! Escrita do Orbital_P em um arquivo temporario.
              orb_D = ((orb_D/orb_total) + peso_inicial)*peso_total
              write(31,*)comp,auto_valor,orb_D                          ! Escrita do Orbital_D em um arquivo temporario.
              end if

              if (lorbit.GT.10) then
                if (e.EQ.-99.or.e.EQ.100)then
                orb_Px = ((orb_Px/orb_total) + peso_inicial)*peso_total
                write(26,*)comp,auto_valor,orb_Px                       ! Escrita do Orbital_Px em um arquivo temporario.
                orb_Py = ((orb_Py/orb_total) + peso_inicial)*peso_total
                write(27,*)comp,auto_valor,orb_Py                       ! Escrita do Orbital_Py em um arquivo temporario.
                orb_Pz = ((orb_Pz/orb_total) + peso_inicial)*peso_total
                write(28,*)comp,auto_valor,orb_Pz                       ! Escrita do Orbital_Pz em um arquivo temporario.
                end if
              end if

! $$$$$$$$$$$ Aparentemente o valor dos spins nao estao normalizados como ocorre para os orbitais. $$$$$$$$$$$
! $$$$$$$$$$$ Verificar se esta normalizacao e necessaria. $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

              if (e.EQ.99.or.e.EQ.100) then
              orb_sx = (orb_sx + peso_inicial)*peso_total
              write(33,*)comp,auto_valor,orb_sx
              orb_sy = (orb_sy + peso_inicial)*peso_total
              write(34,*)comp,auto_valor,orb_sy
              orb_sz = (orb_sz + peso_inicial)*peso_total
              write(35,*)comp,auto_valor,orb_sz
              end if
              
 !============= Pulando as linhas referente a fase (LORBIT 12) ==========

              if (lorbit.EQ.12) then
              temp2=((2*ni)+2)
                do i=1,temp2
                read (10,*)
                end do
              else if (lorbit.NE.12) then
              read (10,*)
              end if
          
!==================== Bandas exclu¡das do calculo ======================

            else                                                        ! Continuacao do if que regula as Bandas que serao plotadas ou nao.

              if (lorbit.EQ.12) then                                    ! Valido somente para LORBIT = 12.
                if (SO.EQ.1) then                                       ! Para calculo sem acoplamento Spin-orbita.
                temp3 = 6 + 3*ni
                else if (SO.EQ.2) then                                  ! Para calculo com acoplamento Spin-orbita.
                temp3 = 9 + 6*ni
                end if
              end if

              if (lorbit.NE.12) then                                    ! Valido somente para LORBIT = 1O ou 11.
                if (SO.EQ.1) then                                       ! Para calculo sem acoplamento Spin-orbita.
                temp3 = 5 + ni
                else if (SO.EQ.2) then                                  ! Para calculo com acoplamento Spin-orbita.
                temp3 = 8 + 4*ni
                end if
              end if

            do i=1,temp3                                                ! Esta parte do codigo pula/exclu¡ as Bandas de energia
            read (10,*)                                                 ! em cada Ponto-k, que nao foram selecionadas para serem plotadas.
            end do
        
            end if
          
          end do  ! Fim do laco das Bandas.
        
!================== Ignorar linhas ao final de cada ponto-k ============

          if (point_k.LT.nk) then
          read (10,*)
          end if
        
!==================== Pontos-k exclu¡dos do calculo ====================

        else                                                            ! Continuacao do if que regula os Pontos-k que serao plotados ou nao.

            if (lorbit.EQ.12) then                                      ! Valido somente para LORBIT = 12.
              if (SO.EQ.1) then                                         ! Para calculo sem acoplamento Spin-orbita.
              temp3 = (6 + 3*ni)*nb + 3
              else if (SO.EQ.2) then
              temp3 = (9 + 6*ni)*nb + 3                                 ! Para calculo com acoplamento Spin-orbita.
              end if
            end if

            if (lorbit.NE.12) then                                      ! Valido somente para LORBIT = 10 ou 11.
              if (SO.EQ.1) then                                         ! Para calculo sem acoplamento Spin-orbita.
              temp3 = (5 + ni)*nb + 3
              else if (SO.EQ.2) then                                    ! Para calculo com acoplamento Spin-orbita.
              temp3 = (8 + 4*ni)*nb + 3
              end if
            end if

            do i=1,temp3                                                ! Esta parte do codigo pula/exclu¡ os K_points
            read (10,*)                                                 ! que nao foram selecionados para serem plotados.
            end do

        end if

      end do  ! Fim do laco dos Pontos-k

!===================== Fim do leitura do arquivo PROCAR ================
      close (10)

!========================== Fim do laco dos PROCAR =====================
      end do

!=============== Fim da escrita do arquivo "informacoes.txt" ===========
      close (17)
!========== ! Obtendo os pontos-k a serem destacados nos gr ficos ======

      open (18,file ='informacoes.txt', ACCESS = 'SEQUENTIAL')

      if (SO.EQ.1) then;
      do i = 1,33; read(18,*); end do
      end if

      if (SO.EQ.2) then;
      do i = 1,40; read(18,*); end do
      end if

      contador2 = 0

      nk_total = nk*n_procar

      do i = 1,nk_total
      read(18,*) r1,r2,r3,r4,comprim
        if (i.NE.1.and.i.NE.nk_total) then
        dif = comprim - comprim_old
          if (dif.EQ.0.0) then
          contador2 = contador2 + 1
          dest_pk(contador2) = comprim
          end if
        end if
      comprim_old = comprim
      end do

      close(18)
      
!-----------------------------------------------------------------------

      if (e.EQ.-99.or.e.EQ.100) then
      close(25)
      close(29)
      close(30)
      close(31)
      end if
        
      if (lorbit.GT.10) then
        if (e.EQ.-99.or.e.EQ.100) then
        close(26)
        close(27)
        close(28)
        end if
      end if
      
      if (SO.EQ.2) then
        if (e.EQ.99.or.e.EQ.100) then
        close(33)
        close(34)
        close(35)
        end if
      end if

!################# Parametros para ajustes dos Graficos ################

      open(2,file='Estrutura_de_Bandas.agr',status='unknown')

      xinicial = xx(1,point_k)
      xfinal = xx(n_procar,point_f)
      yinicial = energ_min
      yfinal = energ_max

      ! Parametros que ajustam os contornos do grafico:
      !delta_xi = ((xx(point_f))/100)*2.5                               ! Aumenta ou diminui a distancia do grafico com relacao a borda Esquerda.
      delta_xf = delta_xi                                               ! Aumenta ou diminui a distancia do grafico com relacao a borda Direita.
      !delta_yi = (sqrt(((energ_max - energ_min)/100)**2))*2.5          ! Aumenta ou diminui a distancia do grafico com relacao a borda Inferior.
      delta_yf = delta_yi                                               ! Aumenta ou diminui a distancia do grafico com relacao a borda Superior.

      xinicial = xinicial! - delta_xi
      xfinal = xfinal! + delta_xf
      yinicial = yinicial! - delta_yi
      yfinal = yfinal! + delta_yf

!########### Plot das Bandas no arquivo "Estrutura_de_Bandas.agr" ######

      write(2,*)"# Grace project file"
      write(2,*)"#"
      write(2,*)"@version 50122"
      write(2,*)"@with string"
      write(2,*)"@    string on"
      write(2,*)"@    string 0.055, 0.96"
      write(2,*)"@    string def ""E(eV)"""
      write(2,*)"@with string"
      write(2,*)"@    string on"

          if (Dimensao.EQ.1) then
          write(2,*)"@    string 0.506, 0.017"
          write(2,*)"@    string def ""(2pi/Param.)"""
          else if (Dimensao.EQ.2) then
          write(2,*)"@    string 0.541, 0.017"
          write(2,*)"@    string def ""(1/Angs.)"""
          else if (Dimensao.EQ.3) then
          write(2,*)"@    string 0.57, 0.017"
          write(2,*)"@    string def ""(1/nm)"""
          end if

      write(2,*)"@with g0"
      write(2,*) "@    world ",xinicial,", ",yinicial,", ",xfinal,","
     . ,yfinal,""
      write(2,*)"@    view 0.055000, 0.075000, 0.600000, 0.950000"
      escalax = (xfinal - xinicial)/5
      escalay = (yfinal - yinicial)/5
      write(2,*)"@    xaxis  tick major ",escalax,""
      write(2,*)"@    yaxis  tick major ",escalay,""

      !Plot da Estrutura de Bandas.
      
      do Band_n = Band_i,Band_f
        write(2,*)""
          do j = 1,n_procar
            do point_k = point_i,point_f
            write(2,*)xx(j,point_k),y(j,point_k,Band_n)
            end do
          end do
        end do

      !Destacando a Energia de Fermi, na Estrutura de Bandas.
      
      if (destacar_efermi.EQ.1) then
      write(2,*)""
      write(2,*)xx(1,point_i),0.0
      write(2,*)xx(n_procar,point_f),0.0
      end if

      !Destacando pontos-K de interesse na estrutura de Bandas
      if (destacar_pontos_k.EQ.1) then
        do loop = 1,contador2
        write(2,*)""
        write(2,*)dest_pk(loop),energ_min
        write(2,*)dest_pk(loop),energ_max
        print *, ""
        end do
      end if

!-----------------------------------------------------------------------
      close (2)    ! Fechamento do arquivo Estrutura_de_Bandas.agr
!-----------------------------------------------------------------------

!#######################################################################

!-----------------------------------------------------------------------
      if (e.NE.77) then                                                 !Lembrando que a opcao e = 77 faz com que somente a Estrutura de Bandas seja plotada.
!-----------------------------------------------------------------------

      print *, ""
      print *,"########################################################"
      print *,"############# Processando os Resultados ################"
      print *,"########################################################"
      print *, ""

!#######################################################################
!################# Agora sera escrito o arquivo de sa¡da ###############
!#######################################################################

        if(e.NE.99.and.e.NE.-99.and.e.NE.100)then; wm=1; wn=1;
        else if (e.EQ.99) then; wm=1; wn=3                              ! Spin (Sx, Sy e Sz)
        else if (e.EQ.-99.and.lorbit.EQ.10) then; wm=4; wn=6            ! Orbitais (S, P, D)
        else if (e.EQ.-99.and.lorbit.GT.10) then; wm=4; wn=9            ! Orbitais (S, P, D) e (Px, Py, Pz)
        else if (e.EQ.100.and.lorbit.EQ.10) then; wm=1; wn=6            ! Spin (Sx, Sy e Sz)  //  Orbitais (S, P, D)
        else if (e.EQ.100.and.lorbit.GT.10) then; wm=1; wn=9            ! Spin (Sx, Sy e Sz)  //  Orbitais (S, P, D) e (Px, Py, Pz)
        end if

        do t=wm,wn !Laco para a analise das Projecoes
        
!-----------------------------------------------------------------------
          if((e.EQ.99.and.t.EQ.1).or.(e.EQ.100.and.t.EQ.1)) then
          open (49,file = 'Textura_Spin_Sx.agr', ACCESS = 'SEQUENTIAL')
          else if((e.EQ.99.and.t.EQ.2).or.(e.EQ.100.and.t.EQ.2)) then
          open (49,file = 'Textura_Spin_Sy.agr', ACCESS = 'SEQUENTIAL')
          else if((e.EQ.99.and.t.EQ.3).or.(e.EQ.100.and.t.EQ.3)) then
          open (49,file = 'Textura_Spin_Sz.agr', ACCESS = 'SEQUENTIAL')
          end if

          if((e.EQ.-99.and.t.EQ.4).or.(e.EQ.100.and.t.EQ.4)) then
          open(49,file='Orbitais_S_P_D.agr', ACCESS = 'SEQUENTIAL')
          else if((e.EQ.-99.and.t.EQ.7).or.(e.EQ.100.and.t.EQ.7)) then
          open(49,file='Orbitais_Px_Py_Pz.agr', ACCESS = 'SEQUENTIAL')
          end if
!-----------------------------------------------------------------------

          if (e.EQ.99.and.t.EQ.1) then
          print *, "Analisando a Projecao Sx do Spin"
          else if (e.EQ.99.and.t.EQ.2) then
          print *, ""
          print *, "Analisando a Projecao Sy do Spin"
          else if (e.EQ.99.and.t.EQ.3) then
          print *, ""
          print *, "Analisando a Projecao Sz do Spin"
          end if
          
          if (e.EQ.-99.and.t.EQ.4) then
          print *, "Analisando a Projecao do Orbital S"
          else if (e.EQ.-99.and.t.EQ.5) then
          print *, ""
          print *, "Analisando a Projecao do Orbital P"
          else if (e.EQ.-99.and.t.EQ.6) then
          print *, ""
          print *, "Analisando a Projecao do Orbital D"
          else if (e.EQ.-99.and.t.EQ.7) then
          print *, ""
          print *, "Analisando a Projecao do Orbital Px"
          else if (e.EQ.-99.and.t.EQ.8) then
          print *, ""
          print *, "Analisando a Projecao do Orbital Py"
          else if (e.EQ.-99.and.t.EQ.9) then
          print *, ""
          print *, "Analisando a Projecao do Orbital Pz"
          end if

          if (e.EQ.100.and.t.EQ.1) then
          print *, "Analisando a Projecao Sx do Spin"
          else if (e.EQ.100.and.t.EQ.2) then
          print *, ""
          print *, "Analisando a Projecao Sy do Spin"
          else if (e.EQ.100.and.t.EQ.3) then
          print *, ""
          print *, "Analisando a Projecao Sz do Spin"
          else if (e.EQ.100.and.t.EQ.4) then
          print *, ""
          print *, "Analisando a Projecao do Orbital S"
          else if (e.EQ.100.and.t.EQ.5) then
          print *, ""
          print *, "Analisando a Projecao do Orbital P"
          else if (e.EQ.100.and.t.EQ.6) then
          print *, ""
          print *, "Analisando a Projecao do Orbital D"
          else if (e.EQ.100.and.t.EQ.7) then
          print *, ""
          print *, "Analisando a Projecao do Orbital Px"
          else if (e.EQ.100.and.t.EQ.8) then
          print *, ""
          print *, "Analisando a Projecao do Orbital Py"
          else if (e.EQ.100.and.t.EQ.9) then
          print *, ""
          print *, "Analisando a Projecao do Orbital Pz"
          end if

!-----------------------------------------------------------------------

!################## Plot das Texturas nos arquivos ".agr" ##############

      if((e.EQ.-99.or.e.EQ.99.or.e.EQ.100).and.(t.LE.4.or.t.EQ.7)) then

      write(49,*)"# Grace project file"
      write(49,*)"#"
      write(49,*)"@version 50122"
      write(49,*)"@with string"
      write(49,*)"@    string on"
      write(49,*)"@    string 0.055, 0.96"
      write(49,*)"@    string def ""E(eV)"""
      write(49,*)"@with string"
      write(49,*)"@    string on"

          if (Dimensao.EQ.1) then
          write(49,*)"@    string 0.506, 0.017"
          write(49,*)"@    string def ""(2pi/Param.)"""
          else if (Dimensao.EQ.2) then
          write(49,*)"@    string 0.541, 0.017"
          write(49,*)"@    string def ""(1/Angs.)"""
          else if (Dimensao.EQ.3) then
          write(49,*)"@    string 0.57, 0.017"
          write(49,*)"@    string def ""(1/nm)"""
          end if

      write(49,*)"@with g0"
      write(49,*) "@    world ",xinicial,", ",yinicial,", ",xfinal,","
     . ,yfinal,""
      write(49,*)"@    view 0.055000, 0.075000, 0.600000, 0.950000"
      escalax = (xfinal - xinicial)/5
      escalay = (yfinal - yinicial)/5
      write(49,*)"@    xaxis  tick major ",escalax,""
      write(49,*)"@    yaxis  tick major ",escalay,""

        do i=1,3

          if (i.EQ.1.and.t.LE.3) then; grac='s0';      color = cor(1)   ! Cor da componente Nula dos Spins Sx, Sy e Sz.
          else if (i.EQ.2.and.t.LE.3) then; grac='s1'; color = cor(2)   ! Cor da componente Up dos Spins Sx, Sy e Sz.
          else if (i.EQ.3.and.t.LE.3) then; grac='s2'; color = cor(3)   ! Cor da componente Down dos Spins Sx, Sy e Sz.
          end if
          
          if (i.EQ.1.and.t.GT.3) then; grac='s0';      color = cor(t)   ! Cor do Orbital S ou Px.
          else if (i.EQ.2.and.t.GT.3) then; grac='s1'; color = cor(t+1) ! Cor do Orbital P ou Py.
          else if (i.EQ.3.and.t.GT.3) then; grac='s2'; color = cor(t+2) ! Cor do Orbital D ou Pz.
          end if

          write(49,*) "@    ",grac," type xysize"
          write(49,*) "@    ",grac," symbol 1"
          write(49,*) "@    ",grac," symbol color",color,""
          write(49,*) "@    ",grac," symbol fill color",color,""
          write(49,*) "@    ",grac," symbol fill pattern 1"
          write(49,*) "@    ",grac," line type 0"
          write(49,*) "@    ",grac," line color",color,""
          
        end do
        
      write(49,*) "@type xysize"
      write(49,*)""
      
      end if

!-----------------------------------------------------------------------
        num_tot = n_procar*(nk*nb)
!-----------------------------------------------------------------------

        if (t.LE.3) then; controle=3                                    ! Loop para a leitura dos valores Nulo, Up e Down das componentes de Spin (Sx, Sy e Sz).
        else if (t.GT.3) then; controle=1                               ! Loop para a leitura dos valores nao-nulos dos Orbitais.
        end if

        do i=1,controle
          
      if ((e.EQ.99.and.t.EQ.1).or.(e.EQ.100.and.t.EQ.1)) then
      open (32,file = 'Temp_Spin_Sx_Excluir.txt', ACCESS='SEQUENTIAL')
      else if ((e.EQ.99.and.t.EQ.2).or.(e.EQ.100.and.t.EQ.2)) then
      open (32,file = 'Temp_Spin_Sy_Excluir.txt', ACCESS='SEQUENTIAL')
      else if ((e.EQ.99.and.t.EQ.3).or.(e.EQ.100.and.t.EQ.3)) then
      open (32,file = 'Temp_Spin_Sz_Excluir.txt', ACCESS='SEQUENTIAL')
      else if ((e.EQ.-99.and.t.EQ.4).or.(e.EQ.100.and.t.EQ.4)) then
      open (32,file = 'Temp_orb-S_Excluir.txt', ACCESS = 'SEQUENTIAL')
      else if ((e.EQ.-99.and.t.EQ.5).or.(e.EQ.100.and.t.EQ.5)) then
      open (32,file = 'Temp_orb-P_Excluir.txt', ACCESS = 'SEQUENTIAL')
      else if ((e.EQ.-99.and.t.EQ.6).or.(e.EQ.100.and.t.EQ.6)) then
      open (32,file = 'Temp_orb-D_Excluir.txt', ACCESS = 'SEQUENTIAL')
      else if ((e.EQ.-99.and.t.EQ.7).or.(e.EQ.100.and.t.EQ.7)) then
      open (32,file = 'Temp_orb-Px_Excluir.txt', ACCESS = 'SEQUENTIAL')
      else if ((e.EQ.-99.and.t.EQ.8).or.(e.EQ.100.and.t.EQ.8)) then
      open (32,file = 'Temp_orb-Py_Excluir.txt', ACCESS = 'SEQUENTIAL')
      else if ((e.EQ.-99.and.t.EQ.9).or.(e.EQ.100.and.t.EQ.9)) then
      open (32,file = 'Temp_orb-Pz_Excluir.txt', ACCESS = 'SEQUENTIAL')
      end if
      
!-----------------------------------------------------------------------

          if (t.LE.3) then
            do j=1,num_tot
            read(32,*) comp,auto_valor,raio
              if (i.EQ.1.and.raio.EQ.0.0) then
              write(49,*)comp,auto_valor,raio
              else if (i.EQ.2.and.raio.GT.0.0) then
              write(49,*)comp,auto_valor,raio
              else if (i.EQ.3.and.raio.LT.0.0) then
              write(49,*)comp,auto_valor,raio
              end if
            end do
          else if (t.GT.3) then
            do j=1,num_tot
            read(32,*) comp,auto_valor,raio
              if (raio.GT.0.0) then
              write(49,*)comp,auto_valor,raio
              end if
            end do
          end if
          
        write(49,*)""
      
        close (32)
        
      end do

!-----------------------------------------------------------------------
      if (t.LE.3.or.t.EQ.6.or.t.EQ.9)then
      
      !Plot da Estrutura de Bandas.
      do Band_n = Band_i,Band_f
      write(49,*)""
        do i=1,n_procar
          do point_k = point_i,point_f
          write(49,*)xx(i,point_k),y(i,point_k,Band_n),0.0
          end do
        end do
      end do
      
!-----------------------------------------------------------------------
      !Destacando a Energia de Fermi, no plot das Texturas.
      write(49,*)""
      if (destacar_efermi.EQ.1) then
      write(49,*)xx(1,point_i),0.0,0.0
      write(49,*)xx(n_procar,point_f),0.0,0.0
      end if
!-----------------------------------------------------------------------
      !Destacando alguns pontos-K de interesse, na Estrutura de Bandas.
      if (n_procar.EQ.1) then
        if (destacar_pontos_k.GT.0.and.destacar_pontos_k.LT.11) then
          do loop = 1,destacar_pontos_k
          write(49,*)""
          temp_pk = dest_pk(loop)
          write(49,*)xx(1,temp_pk),energ_min,0.0
          write(49,*)xx(1,temp_pk),energ_max,0.0
          end do
        end if
      end if
!-----------------------------------------------------------------------
      !Destacando pontos-K de interesse na estrutura de Bandas
      if (destacar_pontos_k.EQ.1) then
        do loop = 1,contador2
        write(49,*)""
        write(49,*)dest_pk(loop),energ_min,0.0
        write(49,*)dest_pk(loop),energ_max,0.0
        print *, ""
        end do
      end if
!-----------------------------------------------------------------------
      close (49)
      close (11)    ! Fechamento do arquivo CONTCAR

      end if ! Fim do laco para a escrita da Estrutura de Bandas
!-----------------------------------------------------------------------
      end do ! Fim do laco para a analise das Projecoes
!-----------------------------------------------------------------------
      end if ! Fim do laco para (e.NE.77)
!-----------------------------------------------------------------------
      
      end program TEXTURAS                                              ! Autor: Augusto de Lelis Araujo - INFIS_UFU
