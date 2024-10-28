label panduan_y1:
    call panduan_y_caifen from _call_panduan_y_caifen
    #要改的部分
    if daqipan_1_1<cuandi_y:
        python:
            daqipan_1_1=cuandi_y
            huihe=1
            daqipan_1_1_suxin=1
        call gai_y from _call_gai_y
        show screen xiaoqipan_y_gai
        show screen daqipan_ju
        call screen xiaoqipan_f
    else:
        call screen xiaoqipan_y

label panduan_y2:
    call panduan_y_caifen from _call_panduan_y_caifen_1
    #要改的部分
    if daqipan_1_2<cuandi_y:
        python:
            daqipan_1_2=cuandi_y
            huihe=1
            daqipan_1_2_suxin=1
        call gai_y from _call_gai_y_1
        show screen xiaoqipan_y_gai
        show screen daqipan_ju
        call screen xiaoqipan_f
    else:
        call screen xiaoqipan_y

label panduan_y3:
    call panduan_y_caifen from _call_panduan_y_caifen_2
    #要改的部分
    if daqipan_1_3<cuandi_y:
        python:
            daqipan_1_3=cuandi_y
            huihe=1
            daqipan_1_3_suxin=1
        call gai_y from _call_gai_y_2
        show screen xiaoqipan_y_gai
        show screen daqipan_ju
        call screen xiaoqipan_f
    else:
        call screen xiaoqipan_y

label panduan_y4:
    call panduan_y_caifen from _call_panduan_y_caifen_3
    #要改的部分
    if daqipan_2_1<cuandi_y:
        python:
            daqipan_2_1=cuandi_y
            huihe=1
            daqipan_2_1_suxin=1
        call gai_y from _call_gai_y_3
        show screen xiaoqipan_y_gai
        show screen daqipan_ju
        call screen xiaoqipan_f
    else:
        call screen xiaoqipan_y

label panduan_y5:
    call panduan_y_caifen from _call_panduan_y_caifen_4
    #要改的部分
    if daqipan_2_2<cuandi_y:
        python:
            daqipan_2_2=cuandi_y
            huihe=1
            daqipan_2_2_suxin=1
        call gai_y from _call_gai_y_4
        show screen xiaoqipan_y_gai
        show screen daqipan_ju
        call screen xiaoqipan_f
    else:
        call screen xiaoqipan_y

label panduan_y6:
    call panduan_y_caifen from _call_panduan_y_caifen_5
    #要改的部分
    if daqipan_2_3<cuandi_y:
        python:
            daqipan_2_3=cuandi_y
            huihe=1
            daqipan_2_3_suxin=1
        call gai_y from _call_gai_y_5
        show screen xiaoqipan_y_gai
        show screen daqipan_ju
        call screen xiaoqipan_f
    else:
        call screen xiaoqipan_y

label panduan_y7:
    call panduan_y_caifen from _call_panduan_y_caifen_6
    #要改的部分
    if daqipan_3_1<cuandi_y:
        python:
            daqipan_3_1=cuandi_y
            huihe=1
            daqipan_3_1_suxin=1
        call gai_y from _call_gai_y_6
        show screen xiaoqipan_y_gai
        show screen daqipan_ju
        call screen xiaoqipan_f
    else:
        call screen xiaoqipan_y

label panduan_y8:
    call panduan_y_caifen from _call_panduan_y_caifen_7
    #要改的部分
    if daqipan_3_2<cuandi_y:
        python:
            daqipan_3_2=cuandi_y
            huihe=1
            daqipan_3_2_suxin=1
        call gai_y from _call_gai_y_7
        show screen xiaoqipan_y_gai
        show screen daqipan_ju
        call screen xiaoqipan_f
    else:
        call screen xiaoqipan_y

label panduan_y9:
    call panduan_y_caifen from _call_panduan_y_caifen_8
    #要改的部分
    if daqipan_3_3<cuandi_y:
        python:
            daqipan_3_3=cuandi_y
            huihe=1
            daqipan_3_3_suxin=1
        call gai_y from _call_gai_y_8
        show screen xiaoqipan_y_gai
        show screen daqipan_ju
        call screen xiaoqipan_f
    else:
        call screen xiaoqipan_y

label panduan_f1:
    call panduan_f_caifen from _call_panduan_f_caifen
    #要改的部分
    if daqipan_1_1<cuandi_f:
        python:
            daqipan_1_1=cuandi_f
            huihe=0
            daqipan_1_1_suxin=2
        call gai_f from _call_gai_f
        show screen xiaoqipan_f_gai
        show screen daqipan_ju
        call screen xiaoqipan_y
    else:
        call screen xiaoqipan_f
label panduan_f2:
    call panduan_f_caifen from _call_panduan_f_caifen_1
    #要改的部分
    if daqipan_1_2<cuandi_f:
        python:
            daqipan_1_2=cuandi_f
            huihe=0
            daqipan_1_2_suxin=2
        call gai_f from _call_gai_f_1
        show screen xiaoqipan_f_gai
        show screen daqipan_ju
        call screen xiaoqipan_y
    else:
        call screen xiaoqipan_f

label panduan_f3:
    call panduan_f_caifen from _call_panduan_f_caifen_2
    #要改的部分
    if daqipan_1_3<cuandi_f:
        python:
            daqipan_1_3=cuandi_f
            huihe=0
            daqipan_1_3_suxin=2
        call gai_f from _call_gai_f_2
        show screen xiaoqipan_f_gai
        show screen daqipan_ju
        call screen xiaoqipan_y
    else:
        call screen xiaoqipan_f

label panduan_f4:
    call panduan_f_caifen from _call_panduan_f_caifen_3
    #要改的部分
    if daqipan_2_1<cuandi_f:
        python:
            daqipan_2_1=cuandi_f
            huihe=0
            daqipan_2_1_suxin=2
        call gai_f from _call_gai_f_3
        show screen xiaoqipan_f_gai
        show screen daqipan_ju
        call screen xiaoqipan_y
    else:
        call screen xiaoqipan_f

label panduan_f5:
    call panduan_f_caifen from _call_panduan_f_caifen_4
    #要改的部分
    if daqipan_2_2<cuandi_f:
        python:
            daqipan_2_2=cuandi_f
            huihe=0
            daqipan_2_2_suxin=2
        call gai_f from _call_gai_f_4
        show screen xiaoqipan_f_gai
        show screen daqipan_ju
        call screen xiaoqipan_y
    else:
        call screen xiaoqipan_f

label panduan_f6:
    call panduan_f_caifen from _call_panduan_f_caifen_5
    #要改的部分
    if daqipan_2_3<cuandi_f:
        python:
            daqipan_2_3=cuandi_f
            huihe=0
            daqipan_2_3_suxin=2
        call gai_f from _call_gai_f_5
        show screen xiaoqipan_f_gai
        show screen daqipan_ju
        call screen xiaoqipan_y
    else:
        call screen xiaoqipan_f

label panduan_f7:
    call panduan_f_caifen from _call_panduan_f_caifen_6
    #要改的部分
    if daqipan_3_1<cuandi_f:
        python:
            daqipan_3_1=cuandi_f
            huihe=0
            daqipan_3_1_suxin=2
        call gai_f from _call_gai_f_6
        show screen xiaoqipan_f_gai
        show screen daqipan_ju
        call screen xiaoqipan_y
    else:
        call screen xiaoqipan_f

label panduan_f8:
    call panduan_f_caifen from _call_panduan_f_caifen_7
    #要改的部分
    if daqipan_3_2<cuandi_f:
        python:
            daqipan_3_2=cuandi_f
            huihe=0
            daqipan_3_2_suxin=2
        call gai_f from _call_gai_f_7
        show screen xiaoqipan_f_gai
        show screen daqipan_ju
        call screen xiaoqipan_y
    else:
        call screen xiaoqipan_f

label panduan_f9:
    call panduan_f_caifen from _call_panduan_f_caifen_8
    #要改的部分
    if daqipan_3_3<cuandi_f:
        python:
            daqipan_3_3=cuandi_f
            huihe=0
            daqipan_3_3_suxin=2
        call gai_f from _call_gai_f_8
        show screen xiaoqipan_f_gai
        show screen daqipan_ju
        call screen xiaoqipan_y
    else:
        call screen xiaoqipan_f

label gai_y:
    python:
        if cuandi_y==1:
            xiaoqipan_y_gai_1=1
        elif cuandi_y==2:
            xiaoqipan_y_gai_2=1
        elif cuandi_y==3:
            xiaoqipan_y_gai_3=1
        elif cuandi_y==4:
            xiaoqipan_y_gai_4=1
        elif cuandi_y==5:
            xiaoqipan_y_gai_5=1
        elif cuandi_y==6:
            xiaoqipan_y_gai_6=1
        elif cuandi_y==7:
            xiaoqipan_y_gai_7=1
        elif cuandi_y==8:
            xiaoqipan_y_gai_8=1
        elif cuandi_y==9:
            xiaoqipan_y_gai_9=1
        else:
            pass
    return
label gai_f:
    python:
        if cuandi_f==1:
            xiaoqipan_f_gai_1=1
        elif cuandi_f==2:
            xiaoqipan_f_gai_2=1
        elif cuandi_f==3:
            xiaoqipan_f_gai_3=1
        elif cuandi_f==4:
            xiaoqipan_f_gai_4=1
        elif cuandi_f==5:
            xiaoqipan_f_gai_5=1
        elif cuandi_f==6:
            xiaoqipan_f_gai_6=1
        elif cuandi_f==7:
            xiaoqipan_f_gai_7=1
        elif cuandi_f==8:
            xiaoqipan_f_gai_8=1
        elif cuandi_f==9:
            xiaoqipan_f_gai_9=1
        else:
            pass
    return

label panduan_y_caifen:
    python:
        xiaoqipan_y_xuanze_1=0
        xiaoqipan_y_xuanze_2=0
        xiaoqipan_y_xuanze_3=0
        xiaoqipan_y_xuanze_4=0
        xiaoqipan_y_xuanze_5=0
        xiaoqipan_y_xuanze_6=0
        xiaoqipan_y_xuanze_7=0
        xiaoqipan_y_xuanze_8=0
        xiaoqipan_y_xuanze_9=0
    hide screen daqipan
    hide screen xiaoqipan_y_xuanze
    return

label panduan_f_caifen:
    python:
        xiaoqipan_f_xuanze_1=0
        xiaoqipan_f_xuanze_2=0
        xiaoqipan_f_xuanze_3=0
        xiaoqipan_f_xuanze_4=0
        xiaoqipan_f_xuanze_5=0
        xiaoqipan_f_xuanze_6=0
        xiaoqipan_f_xuanze_7=0
        xiaoqipan_f_xuanze_8=0
        xiaoqipan_f_xuanze_9=0
    hide screen daqipan
    hide screen xiaoqipan_f_xuanze
    return