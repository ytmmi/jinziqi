#主界面前
label before_main_menu:
    show mianyueshe
    pause 2.0
    hide mianyueshe
    #转场
    with fade
    return

label start:
    # B站 by 云兔mmi
    # $ persistent._clear(progress=False) # 为了做测试，每次运行前都会将所有持久化数据清除，在正式作品中需要将其注释掉
    scene qipan
    python:
        quick_menu = False
    window hide
    show screen caidan_x
    show screen huihe_suomin
    show screen cexiao_1
    show screen cexiao_2
    if huihe==0:
        call screen xiaoqipan_y
    elif huihe==1:
        call screen xiaoqipan_f
    return


label ju_y:
    show screen daqipan
    call screen xiaoqipan_y
    return
label ju_f:
    show screen daqipan
    call screen xiaoqipan_f
    return

screen huihe_suomin:
    if huihe==0:
        text("回合 圆") xycenter(0.5,60)
    elif huihe==1:
        text("回合 方") xycenter(0.5,60)


screen daqipan:
    #大棋盘
    frame:
        background None
        xycenter(0.5,0.5)
        grid 3 3:
            hbox:
                if huihe==0:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_y1")]                 
                elif huihe==1:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_f1")]
                    
            hbox:
                if huihe==0:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_y2")]                 
                elif huihe==1:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_f2")]
            hbox:
                if huihe==0:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_y3")]                 
                elif huihe==1:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_f3")]
                    
            hbox:
                if huihe==0:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_y4")]                 
                elif huihe==1:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_f4")]
            hbox:
                if huihe==0:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_y5")]                 
                elif huihe==1:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_f5")]
                    
            hbox:
                if huihe==0:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_y6")]                 
                elif huihe==1:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_f6")]
            hbox:
                if huihe==0:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_y7")]                 
                elif huihe==1:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_f7")]
                    
            hbox:
                if huihe==0:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_y8")]                 
                elif huihe==1:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_f8")]
            hbox:
                if huihe==0:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_y9")]                 
                elif huihe==1:
                    imagebutton:
                        auto "images/da_qipan_wu_%s.png"
                        action [Jump("panduan_f9")]

screen daqipan_ju:
    #大棋盘 局
    frame:
        background None
        xycenter(0.5,0.5)
        grid 3 3:
            hbox:
                if daqipan_1_1_suxin==0:
                    add "images/da_qipan_wu_idle.png"
                elif daqipan_1_1_suxin==1:
                    if daqipan_1_1==1:
                        add "images/suzi_yuan/y1_idle.png"
                    elif daqipan_1_1==2:
                        add "images/suzi_yuan/y2_idle.png"
                    elif daqipan_1_1==3:
                        add "images/suzi_yuan/y3_idle.png"
                    elif daqipan_1_1==4:
                        add "images/suzi_yuan/y4_idle.png"
                    elif daqipan_1_1==5:
                        add "images/suzi_yuan/y5_idle.png"
                    elif daqipan_1_1==6:
                        add "images/suzi_yuan/y6_idle.png"
                    elif daqipan_1_1==7:
                        add "images/suzi_yuan/y7_idle.png"
                    elif daqipan_1_1==8:
                        add "images/suzi_yuan/y8_idle.png"
                    elif daqipan_1_1==9:
                        add "images/suzi_yuan/y9_idle.png"
                elif daqipan_1_1_suxin==2:
                    if daqipan_1_1==1:
                        add "images/suzi_fan/f1_idle.png"
                    elif daqipan_1_1==2:
                        add "images/suzi_fan/f2_idle.png"
                    elif daqipan_1_1==3:
                        add "images/suzi_fan/f3_idle.png"
                    elif daqipan_1_1==4:
                        add "images/suzi_fan/f4_idle.png"
                    elif daqipan_1_1==5:
                        add "images/suzi_fan/f5_idle.png"
                    elif daqipan_1_1==6:
                        add "images/suzi_fan/f6_idle.png"
                    elif daqipan_1_1==7:
                        add "images/suzi_fan/f7_idle.png"
                    elif daqipan_1_1==8:
                        add "images/suzi_fan/f8_idle.png"
                    elif daqipan_1_1==9:
                        add "images/suzi_fan/f9_idle.png"
            hbox:
                if daqipan_1_2_suxin==0:
                    add "images/da_qipan_wu_idle.png"
                elif daqipan_1_2_suxin==1:
                    if daqipan_1_2==1:
                        add "images/suzi_yuan/y1_idle.png"
                    elif daqipan_1_2==2:
                        add "images/suzi_yuan/y2_idle.png"
                    elif daqipan_1_2==3:
                        add "images/suzi_yuan/y3_idle.png"
                    elif daqipan_1_2==4:
                        add "images/suzi_yuan/y4_idle.png"
                    elif daqipan_1_2==5:
                        add "images/suzi_yuan/y5_idle.png"
                    elif daqipan_1_2==6:
                        add "images/suzi_yuan/y6_idle.png"
                    elif daqipan_1_2==7:
                        add "images/suzi_yuan/y7_idle.png"
                    elif daqipan_1_2==8:
                        add "images/suzi_yuan/y8_idle.png"
                    elif daqipan_1_2==9:
                        add "images/suzi_yuan/y9_idle.png"
                elif daqipan_1_2_suxin==2:
                    if daqipan_1_2==1:
                        add "images/suzi_fan/f1_idle.png"
                    elif daqipan_1_2==2:
                        add "images/suzi_fan/f2_idle.png"
                    elif daqipan_1_2==3:
                        add "images/suzi_fan/f3_idle.png"
                    elif daqipan_1_2==4:
                        add "images/suzi_fan/f4_idle.png"
                    elif daqipan_1_2==5:
                        add "images/suzi_fan/f5_idle.png"
                    elif daqipan_1_2==6:
                        add "images/suzi_fan/f6_idle.png"
                    elif daqipan_1_2==7:
                        add "images/suzi_fan/f7_idle.png"
                    elif daqipan_1_2==8:
                        add "images/suzi_fan/f8_idle.png"
                    elif daqipan_1_2==9:
                        add "images/suzi_fan/f9_idle.png"
            hbox:
                if daqipan_1_3_suxin==0:
                    add "images/da_qipan_wu_idle.png"
                elif daqipan_1_3_suxin==1:
                    if daqipan_1_3==1:
                        add "images/suzi_yuan/y1_idle.png"
                    elif daqipan_1_3==2:
                        add "images/suzi_yuan/y2_idle.png"
                    elif daqipan_1_3==3:
                        add "images/suzi_yuan/y3_idle.png"
                    elif daqipan_1_3==4:
                        add "images/suzi_yuan/y4_idle.png"
                    elif daqipan_1_3==5:
                        add "images/suzi_yuan/y5_idle.png"
                    elif daqipan_1_3==6:
                        add "images/suzi_yuan/y6_idle.png"
                    elif daqipan_1_3==7:
                        add "images/suzi_yuan/y7_idle.png"
                    elif daqipan_1_3==8:
                        add "images/suzi_yuan/y8_idle.png"
                    elif daqipan_1_3==9:
                        add "images/suzi_yuan/y9_idle.png"
                elif daqipan_1_3_suxin==2:
                    if daqipan_1_3==1:
                        add "images/suzi_fan/f1_idle.png"
                    elif daqipan_1_3==2:
                        add "images/suzi_fan/f2_idle.png"
                    elif daqipan_1_3==3:
                        add "images/suzi_fan/f3_idle.png"
                    elif daqipan_1_3==4:
                        add "images/suzi_fan/f4_idle.png"
                    elif daqipan_1_3==5:
                        add "images/suzi_fan/f5_idle.png"
                    elif daqipan_1_3==6:
                        add "images/suzi_fan/f6_idle.png"
                    elif daqipan_1_3==7:
                        add "images/suzi_fan/f7_idle.png"
                    elif daqipan_1_3==8:
                        add "images/suzi_fan/f8_idle.png"
                    elif daqipan_1_3==9:
                        add "images/suzi_fan/f9_idle.png"
            hbox:
                if daqipan_2_1_suxin==0:
                    add "images/da_qipan_wu_idle.png"
                elif daqipan_2_1_suxin==1:
                    if daqipan_2_1==1:
                        add "images/suzi_yuan/y1_idle.png"
                    elif daqipan_2_1==2:
                        add "images/suzi_yuan/y2_idle.png"
                    elif daqipan_2_1==3:
                        add "images/suzi_yuan/y3_idle.png"
                    elif daqipan_2_1==4:
                        add "images/suzi_yuan/y4_idle.png"
                    elif daqipan_2_1==5:
                        add "images/suzi_yuan/y5_idle.png"
                    elif daqipan_2_1==6:
                        add "images/suzi_yuan/y6_idle.png"
                    elif daqipan_2_1==7:
                        add "images/suzi_yuan/y7_idle.png"
                    elif daqipan_2_1==8:
                        add "images/suzi_yuan/y8_idle.png"
                    elif daqipan_2_1==9:
                        add "images/suzi_yuan/y9_idle.png"
                elif daqipan_2_1_suxin==2:
                    if daqipan_2_1==1:
                        add "images/suzi_fan/f1_idle.png"
                    elif daqipan_2_1==2:
                        add "images/suzi_fan/f2_idle.png"
                    elif daqipan_2_1==3:
                        add "images/suzi_fan/f3_idle.png"
                    elif daqipan_2_1==4:
                        add "images/suzi_fan/f4_idle.png"
                    elif daqipan_2_1==5:
                        add "images/suzi_fan/f5_idle.png"
                    elif daqipan_2_1==6:
                        add "images/suzi_fan/f6_idle.png"
                    elif daqipan_2_1==7:
                        add "images/suzi_fan/f7_idle.png"
                    elif daqipan_2_1==8:
                        add "images/suzi_fan/f8_idle.png"
                    elif daqipan_2_1==9:
                        add "images/suzi_fan/f9_idle.png"
            hbox:
                if daqipan_2_2_suxin==0:
                    add "images/da_qipan_wu_idle.png"
                elif daqipan_2_2_suxin==1:
                    if daqipan_2_2==1:
                        add "images/suzi_yuan/y1_idle.png"
                    elif daqipan_2_2==2:
                        add "images/suzi_yuan/y2_idle.png"
                    elif daqipan_2_2==3:
                        add "images/suzi_yuan/y3_idle.png"
                    elif daqipan_2_2==4:
                        add "images/suzi_yuan/y4_idle.png"
                    elif daqipan_2_2==5:
                        add "images/suzi_yuan/y5_idle.png"
                    elif daqipan_2_2==6:
                        add "images/suzi_yuan/y6_idle.png"
                    elif daqipan_2_2==7:
                        add "images/suzi_yuan/y7_idle.png"
                    elif daqipan_2_2==8:
                        add "images/suzi_yuan/y8_idle.png"
                    elif daqipan_2_2==9:
                        add "images/suzi_yuan/y9_idle.png"
                elif daqipan_2_2_suxin==2:
                    if daqipan_2_2==1:
                        add "images/suzi_fan/f1_idle.png"
                    elif daqipan_2_2==2:
                        add "images/suzi_fan/f2_idle.png"
                    elif daqipan_2_2==3:
                        add "images/suzi_fan/f3_idle.png"
                    elif daqipan_2_2==4:
                        add "images/suzi_fan/f4_idle.png"
                    elif daqipan_2_2==5:
                        add "images/suzi_fan/f5_idle.png"
                    elif daqipan_2_2==6:
                        add "images/suzi_fan/f6_idle.png"
                    elif daqipan_2_2==7:
                        add "images/suzi_fan/f7_idle.png"
                    elif daqipan_2_2==8:
                        add "images/suzi_fan/f8_idle.png"
                    elif daqipan_2_2==9:
                        add "images/suzi_fan/f9_idle.png"
            hbox:
                if daqipan_2_3_suxin==0:
                    add "images/da_qipan_wu_idle.png"
                elif daqipan_2_3_suxin==1:
                    if daqipan_1_3==1:
                        add "images/suzi_yuan/y1_idle.png"
                    elif daqipan_2_3==2:
                        add "images/suzi_yuan/y2_idle.png"
                    elif daqipan_2_3==3:
                        add "images/suzi_yuan/y3_idle.png"
                    elif daqipan_2_3==4:
                        add "images/suzi_yuan/y4_idle.png"
                    elif daqipan_2_3==5:
                        add "images/suzi_yuan/y5_idle.png"
                    elif daqipan_2_3==6:
                        add "images/suzi_yuan/y6_idle.png"
                    elif daqipan_2_3==7:
                        add "images/suzi_yuan/y7_idle.png"
                    elif daqipan_2_3==8:
                        add "images/suzi_yuan/y8_idle.png"
                    elif daqipan_2_3==9:
                        add "images/suzi_yuan/y9_idle.png"
                elif daqipan_2_3_suxin==2:
                    if daqipan_2_3==1:
                        add "images/suzi_fan/f1_idle.png"
                    elif daqipan_2_3==2:
                        add "images/suzi_fan/f2_idle.png"
                    elif daqipan_2_3==3:
                        add "images/suzi_fan/f3_idle.png"
                    elif daqipan_2_3==4:
                        add "images/suzi_fan/f4_idle.png"
                    elif daqipan_2_3==5:
                        add "images/suzi_fan/f5_idle.png"
                    elif daqipan_2_3==6:
                        add "images/suzi_fan/f6_idle.png"
                    elif daqipan_2_3==7:
                        add "images/suzi_fan/f7_idle.png"
                    elif daqipan_2_3==8:
                        add "images/suzi_fan/f8_idle.png"
                    elif daqipan_2_3==9:
                        add "images/suzi_fan/f9_idle.png"
            hbox:
                if daqipan_3_1_suxin==0:
                    add "images/da_qipan_wu_idle.png"
                elif daqipan_3_1_suxin==1:
                    if daqipan_3_1==1:
                        add "images/suzi_yuan/y1_idle.png"
                    elif daqipan_3_1==2:
                        add "images/suzi_yuan/y2_idle.png"
                    elif daqipan_3_1==3:
                        add "images/suzi_yuan/y3_idle.png"
                    elif daqipan_3_1==4:
                        add "images/suzi_yuan/y4_idle.png"
                    elif daqipan_3_1==5:
                        add "images/suzi_yuan/y5_idle.png"
                    elif daqipan_3_1==6:
                        add "images/suzi_yuan/y6_idle.png"
                    elif daqipan_3_1==7:
                        add "images/suzi_yuan/y7_idle.png"
                    elif daqipan_3_1==8:
                        add "images/suzi_yuan/y8_idle.png"
                    elif daqipan_3_1==9:
                        add "images/suzi_yuan/y9_idle.png"
                elif daqipan_3_1_suxin==2:
                    if daqipan_3_1==1:
                        add "images/suzi_fan/f1_idle.png"
                    elif daqipan_3_1==2:
                        add "images/suzi_fan/f2_idle.png"
                    elif daqipan_3_1==3:
                        add "images/suzi_fan/f3_idle.png"
                    elif daqipan_3_1==4:
                        add "images/suzi_fan/f4_idle.png"
                    elif daqipan_3_1==5:
                        add "images/suzi_fan/f5_idle.png"
                    elif daqipan_3_1==6:
                        add "images/suzi_fan/f6_idle.png"
                    elif daqipan_3_1==7:
                        add "images/suzi_fan/f7_idle.png"
                    elif daqipan_3_1==8:
                        add "images/suzi_fan/f8_idle.png"
                    elif daqipan_3_1==9:
                        add "images/suzi_fan/f9_idle.png"
            hbox:
                if daqipan_3_2_suxin==0:
                    add "images/da_qipan_wu_idle.png"
                elif daqipan_3_2_suxin==1:
                    if daqipan_1_2==1:
                        add "images/suzi_yuan/y1_idle.png"
                    elif daqipan_3_2==2:
                        add "images/suzi_yuan/y2_idle.png"
                    elif daqipan_3_2==3:
                        add "images/suzi_yuan/y3_idle.png"
                    elif daqipan_3_2==4:
                        add "images/suzi_yuan/y4_idle.png"
                    elif daqipan_3_2==5:
                        add "images/suzi_yuan/y5_idle.png"
                    elif daqipan_3_2==6:
                        add "images/suzi_yuan/y6_idle.png"
                    elif daqipan_3_2==7:
                        add "images/suzi_yuan/y7_idle.png"
                    elif daqipan_3_2==8:
                        add "images/suzi_yuan/y8_idle.png"
                    elif daqipan_3_2==9:
                        add "images/suzi_yuan/y9_idle.png"
                elif daqipan_3_2_suxin==2:
                    if daqipan_3_2==1:
                        add "images/suzi_fan/f1_idle.png"
                    elif daqipan_3_2==2:
                        add "images/suzi_fan/f2_idle.png"
                    elif daqipan_3_2==3:
                        add "images/suzi_fan/f3_idle.png"
                    elif daqipan_3_2==4:
                        add "images/suzi_fan/f4_idle.png"
                    elif daqipan_3_2==5:
                        add "images/suzi_fan/f5_idle.png"
                    elif daqipan_3_2==6:
                        add "images/suzi_fan/f6_idle.png"
                    elif daqipan_3_2==7:
                        add "images/suzi_fan/f7_idle.png"
                    elif daqipan_3_2==8:
                        add "images/suzi_fan/f8_idle.png"
                    elif daqipan_3_2==9:
                        add "images/suzi_fan/f9_idle.png"
            hbox:
                if daqipan_3_3_suxin==0:
                    add "images/da_qipan_wu_idle.png"
                elif daqipan_3_3_suxin==1:
                    if daqipan_3_3==1:
                        add "images/suzi_yuan/y1_idle.png"
                    elif daqipan_3_3==2:
                        add "images/suzi_yuan/y2_idle.png"
                    elif daqipan_3_3==3:
                        add "images/suzi_yuan/y3_idle.png"
                    elif daqipan_3_3==4:
                        add "images/suzi_yuan/y4_idle.png"
                    elif daqipan_3_3==5:
                        add "images/suzi_yuan/y5_idle.png"
                    elif daqipan_3_3==6:
                        add "images/suzi_yuan/y6_idle.png"
                    elif daqipan_3_3==7:
                        add "images/suzi_yuan/y7_idle.png"
                    elif daqipan_3_3==8:
                        add "images/suzi_yuan/y8_idle.png"
                    elif daqipan_3_3==9:
                        add "images/suzi_yuan/y9_idle.png"
                elif daqipan_3_3_suxin==2:
                    if daqipan_3_3==1:
                        add "images/suzi_fan/f1_idle.png"
                    elif daqipan_3_3==2:
                        add "images/suzi_fan/f2_idle.png"
                    elif daqipan_3_3==3:
                        add "images/suzi_fan/f3_idle.png"
                    elif daqipan_3_3==4:
                        add "images/suzi_fan/f4_idle.png"
                    elif daqipan_3_3==5:
                        add "images/suzi_fan/f5_idle.png"
                    elif daqipan_3_3==6:
                        add "images/suzi_fan/f6_idle.png"
                    elif daqipan_3_3==7:
                        add "images/suzi_fan/f7_idle.png"
                    elif daqipan_3_3==8:
                        add "images/suzi_fan/f8_idle.png"
                    elif daqipan_3_3==9:
                        add "images/suzi_fan/f9_idle.png"

screen xiaoqipan_y:
    #小棋盘 圆方
    frame:
        background None
        xsize 250
        ysize 250
        xycenter(201,364)
        grid 3 3:
            spacing 9 
            hbox:
                if huihe==0:
                    if xiaoqipan_y_gai_1==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_y_xuanze_1",1),
                                    SetVariable("xiaoqipan_y_xuanze_2",0),
                                    SetVariable("xiaoqipan_y_xuanze_3",0),
                                    SetVariable("xiaoqipan_y_xuanze_4",0),
                                    SetVariable("xiaoqipan_y_xuanze_5",0),
                                    SetVariable("xiaoqipan_y_xuanze_6",0),
                                    SetVariable("xiaoqipan_y_xuanze_7",0),
                                    SetVariable("xiaoqipan_y_xuanze_8",0),
                                    SetVariable("xiaoqipan_y_xuanze_9",0),
                                    SetVariable("cuandi_y",1),
                                    ShowTransient("xiaoqipan_y_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
                    
            hbox:
                if huihe==0:
                    if xiaoqipan_y_gai_2==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_y_xuanze_1",0),
                                    SetVariable("xiaoqipan_y_xuanze_2",1),
                                    SetVariable("xiaoqipan_y_xuanze_3",0),
                                    SetVariable("xiaoqipan_y_xuanze_4",0),
                                    SetVariable("xiaoqipan_y_xuanze_5",0),
                                    SetVariable("xiaoqipan_y_xuanze_6",0),
                                    SetVariable("xiaoqipan_y_xuanze_7",0),
                                    SetVariable("xiaoqipan_y_xuanze_8",0),
                                    SetVariable("xiaoqipan_y_xuanze_9",0),
                                    SetVariable("cuandi_y",2),
                                    ShowTransient("xiaoqipan_y_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==0:
                    if xiaoqipan_y_gai_3==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_y_xuanze_1",0),
                                    SetVariable("xiaoqipan_y_xuanze_2",0),
                                    SetVariable("xiaoqipan_y_xuanze_3",1),
                                    SetVariable("xiaoqipan_y_xuanze_4",0),
                                    SetVariable("xiaoqipan_y_xuanze_5",0),
                                    SetVariable("xiaoqipan_y_xuanze_6",0),
                                    SetVariable("xiaoqipan_y_xuanze_7",0),
                                    SetVariable("xiaoqipan_y_xuanze_8",0),
                                    SetVariable("xiaoqipan_y_xuanze_9",0),
                                    SetVariable("cuandi_y",3),
                                    ShowTransient("xiaoqipan_y_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==0:
                    if xiaoqipan_y_gai_4==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_y_xuanze_1",0),
                                    SetVariable("xiaoqipan_y_xuanze_2",0),
                                    SetVariable("xiaoqipan_y_xuanze_3",0),
                                    SetVariable("xiaoqipan_y_xuanze_4",4),
                                    SetVariable("xiaoqipan_y_xuanze_5",0),
                                    SetVariable("xiaoqipan_y_xuanze_6",0),
                                    SetVariable("xiaoqipan_y_xuanze_7",0),
                                    SetVariable("xiaoqipan_y_xuanze_8",0),
                                    SetVariable("xiaoqipan_y_xuanze_9",0),
                                    SetVariable("cuandi_y",4),
                                    ShowTransient("xiaoqipan_y_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==0:
                    if xiaoqipan_y_gai_5==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_y_xuanze_1",0),
                                    SetVariable("xiaoqipan_y_xuanze_2",0),
                                    SetVariable("xiaoqipan_y_xuanze_3",0),
                                    SetVariable("xiaoqipan_y_xuanze_4",0),
                                    SetVariable("xiaoqipan_y_xuanze_5",5),
                                    SetVariable("xiaoqipan_y_xuanze_6",0),
                                    SetVariable("xiaoqipan_y_xuanze_7",0),
                                    SetVariable("xiaoqipan_y_xuanze_8",0),
                                    SetVariable("xiaoqipan_y_xuanze_9",0),
                                    SetVariable("cuandi_y",5),
                                    ShowTransient("xiaoqipan_y_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==0:
                    if xiaoqipan_y_gai_6==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_y_xuanze_1",0),
                                    SetVariable("xiaoqipan_y_xuanze_2",0),
                                    SetVariable("xiaoqipan_y_xuanze_3",0),
                                    SetVariable("xiaoqipan_y_xuanze_4",0),
                                    SetVariable("xiaoqipan_y_xuanze_5",0),
                                    SetVariable("xiaoqipan_y_xuanze_6",1),
                                    SetVariable("xiaoqipan_y_xuanze_7",0),
                                    SetVariable("xiaoqipan_y_xuanze_8",0),
                                    SetVariable("xiaoqipan_y_xuanze_9",0),
                                    SetVariable("cuandi_y",6),
                                    ShowTransient("xiaoqipan_y_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==0:
                    if xiaoqipan_y_gai_7==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_y_xuanze_1",0),
                                    SetVariable("xiaoqipan_y_xuanze_2",0),
                                    SetVariable("xiaoqipan_y_xuanze_3",0),
                                    SetVariable("xiaoqipan_y_xuanze_4",0),
                                    SetVariable("xiaoqipan_y_xuanze_5",0),
                                    SetVariable("xiaoqipan_y_xuanze_6",0),
                                    SetVariable("xiaoqipan_y_xuanze_7",1),
                                    SetVariable("xiaoqipan_y_xuanze_8",0),
                                    SetVariable("xiaoqipan_y_xuanze_9",0),
                                    SetVariable("cuandi_y",7),
                                    ShowTransient("xiaoqipan_y_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==0:
                    if xiaoqipan_y_gai_8==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_y_xuanze_1",0),
                                    SetVariable("xiaoqipan_y_xuanze_2",0),
                                    SetVariable("xiaoqipan_y_xuanze_3",0),
                                    SetVariable("xiaoqipan_y_xuanze_4",0),
                                    SetVariable("xiaoqipan_y_xuanze_5",0),
                                    SetVariable("xiaoqipan_y_xuanze_6",0),
                                    SetVariable("xiaoqipan_y_xuanze_7",0),
                                    SetVariable("xiaoqipan_y_xuanze_8",1),
                                    SetVariable("xiaoqipan_y_xuanze_9",0),
                                    SetVariable("cuandi_y",8),
                                    ShowTransient("xiaoqipan_y_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==0:
                    if xiaoqipan_y_gai_9==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_y_xuanze_1",0),
                                    SetVariable("xiaoqipan_y_xuanze_2",0),
                                    SetVariable("xiaoqipan_y_xuanze_3",0),
                                    SetVariable("xiaoqipan_y_xuanze_4",0),
                                    SetVariable("xiaoqipan_y_xuanze_5",0),
                                    SetVariable("xiaoqipan_y_xuanze_6",0),
                                    SetVariable("xiaoqipan_y_xuanze_7",0),
                                    SetVariable("xiaoqipan_y_xuanze_8",0),
                                    SetVariable("xiaoqipan_y_xuanze_9",1),
                                    SetVariable("cuandi_y",9),
                                    ShowTransient("xiaoqipan_y_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass

screen xiaoqipan_f:
    #小棋盘 方方
    frame:
        background None
        xsize 250
        ysize 250
        xycenter(1089,364)
        grid 3 3:
            spacing 9 
            hbox:
                if huihe==1:
                    if xiaoqipan_f_gai_1==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_f_xuanze_1",1),
                                    SetVariable("xiaoqipan_f_xuanze_2",0),
                                    SetVariable("xiaoqipan_f_xuanze_3",0),
                                    SetVariable("xiaoqipan_f_xuanze_4",0),
                                    SetVariable("xiaoqipan_f_xuanze_5",0),
                                    SetVariable("xiaoqipan_f_xuanze_6",0),
                                    SetVariable("xiaoqipan_f_xuanze_7",0),
                                    SetVariable("xiaoqipan_f_xuanze_8",0),
                                    SetVariable("xiaoqipan_f_xuanze_9",0),
                                    SetVariable("cuandi_f",1),
                                    ShowTransient("xiaoqipan_f_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
                        
            hbox:
                if huihe==1:
                    if xiaoqipan_f_gai_2==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_f_xuanze_1",0),
                                    SetVariable("xiaoqipan_f_xuanze_2",1),
                                    SetVariable("xiaoqipan_f_xuanze_3",0),
                                    SetVariable("xiaoqipan_f_xuanze_4",0),
                                    SetVariable("xiaoqipan_f_xuanze_5",0),
                                    SetVariable("xiaoqipan_f_xuanze_6",0),
                                    SetVariable("xiaoqipan_f_xuanze_7",0),
                                    SetVariable("xiaoqipan_f_xuanze_8",0),
                                    SetVariable("xiaoqipan_f_xuanze_9",0),
                                    SetVariable("cuandi_f",2),
                                    ShowTransient("xiaoqipan_f_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==1:
                    if xiaoqipan_f_gai_3==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_f_xuanze_1",0),
                                    SetVariable("xiaoqipan_f_xuanze_2",0),
                                    SetVariable("xiaoqipan_f_xuanze_3",1),
                                    SetVariable("xiaoqipan_f_xuanze_4",0),
                                    SetVariable("xiaoqipan_f_xuanze_5",0),
                                    SetVariable("xiaoqipan_f_xuanze_6",0),
                                    SetVariable("xiaoqipan_f_xuanze_7",0),
                                    SetVariable("xiaoqipan_f_xuanze_8",0),
                                    SetVariable("xiaoqipan_f_xuanze_9",0),
                                    SetVariable("cuandi_f",3),
                                    ShowTransient("xiaoqipan_f_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==1:
                    if xiaoqipan_f_gai_4==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_f_xuanze_1",0),
                                    SetVariable("xiaoqipan_f_xuanze_2",0),
                                    SetVariable("xiaoqipan_f_xuanze_3",0),
                                    SetVariable("xiaoqipan_f_xuanze_4",1),
                                    SetVariable("xiaoqipan_f_xuanze_5",0),
                                    SetVariable("xiaoqipan_f_xuanze_6",0),
                                    SetVariable("xiaoqipan_f_xuanze_7",0),
                                    SetVariable("xiaoqipan_f_xuanze_8",0),
                                    SetVariable("xiaoqipan_f_xuanze_9",0),
                                    SetVariable("cuandi_f",4),
                                    ShowTransient("xiaoqipan_f_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==1:
                    if xiaoqipan_f_gai_5==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_f_xuanze_1",0),
                                    SetVariable("xiaoqipan_f_xuanze_2",0),
                                    SetVariable("xiaoqipan_f_xuanze_3",0),
                                    SetVariable("xiaoqipan_f_xuanze_4",0),
                                    SetVariable("xiaoqipan_f_xuanze_5",1),
                                    SetVariable("xiaoqipan_f_xuanze_6",0),
                                    SetVariable("xiaoqipan_f_xuanze_7",0),
                                    SetVariable("xiaoqipan_f_xuanze_8",0),
                                    SetVariable("xiaoqipan_f_xuanze_9",0),
                                    SetVariable("cuandi_f",5),
                                    ShowTransient("xiaoqipan_f_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==1:
                    if xiaoqipan_f_gai_6==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_f_xuanze_1",0),
                                    SetVariable("xiaoqipan_f_xuanze_2",0),
                                    SetVariable("xiaoqipan_f_xuanze_3",0),
                                    SetVariable("xiaoqipan_f_xuanze_4",0),
                                    SetVariable("xiaoqipan_f_xuanze_5",0),
                                    SetVariable("xiaoqipan_f_xuanze_6",1),
                                    SetVariable("xiaoqipan_f_xuanze_7",0),
                                    SetVariable("xiaoqipan_f_xuanze_8",0),
                                    SetVariable("xiaoqipan_f_xuanze_9",0),
                                    SetVariable("cuandi_f",6),
                                    ShowTransient("xiaoqipan_f_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==1:
                    if xiaoqipan_f_gai_7==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_f_xuanze_1",0),
                                    SetVariable("xiaoqipan_f_xuanze_2",0),
                                    SetVariable("xiaoqipan_f_xuanze_3",0),
                                    SetVariable("xiaoqipan_f_xuanze_4",0),
                                    SetVariable("xiaoqipan_f_xuanze_5",0),
                                    SetVariable("xiaoqipan_f_xuanze_6",0),
                                    SetVariable("xiaoqipan_f_xuanze_7",1),
                                    SetVariable("xiaoqipan_f_xuanze_8",0),
                                    SetVariable("xiaoqipan_f_xuanze_9",0),
                                    SetVariable("cuandi_f",7),
                                    ShowTransient("xiaoqipan_f_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==1:
                    if xiaoqipan_f_gai_8==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_f_xuanze_1",0),
                                    SetVariable("xiaoqipan_f_xuanze_2",0),
                                    SetVariable("xiaoqipan_f_xuanze_3",0),
                                    SetVariable("xiaoqipan_f_xuanze_4",0),
                                    SetVariable("xiaoqipan_f_xuanze_5",0),
                                    SetVariable("xiaoqipan_f_xuanze_6",0),
                                    SetVariable("xiaoqipan_f_xuanze_7",0),
                                    SetVariable("xiaoqipan_f_xuanze_8",1),
                                    SetVariable("xiaoqipan_f_xuanze_9",0),
                                    SetVariable("cuandi_f",8),
                                    ShowTransient("xiaoqipan_f_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass
            hbox:
                if huihe==1:
                    if xiaoqipan_f_gai_9==0:
                        imagebutton:
                            auto "images/gai_xiao_wu_%s.png"
                            action[SetVariable("xiaoqipan_f_xuanze_1",0),
                                    SetVariable("xiaoqipan_f_xuanze_2",0),
                                    SetVariable("xiaoqipan_f_xuanze_3",0),
                                    SetVariable("xiaoqipan_f_xuanze_4",0),
                                    SetVariable("xiaoqipan_f_xuanze_5",0),
                                    SetVariable("xiaoqipan_f_xuanze_6",0),
                                    SetVariable("xiaoqipan_f_xuanze_7",0),
                                    SetVariable("xiaoqipan_f_xuanze_8",0),
                                    SetVariable("xiaoqipan_f_xuanze_9",1),
                                    SetVariable("cuandi_f",9),
                                    ShowTransient("xiaoqipan_f_xuanze"),
                                    ShowTransient("daqipan")]
                    else:
                        pass

screen xiaoqipan_y_gai:
    #小棋盘 圆方 盖
    frame:
        background None
        xsize 250
        ysize 250
        xycenter(201,364)
        grid 3 3:
            spacing 9 
            hbox:
                if xiaoqipan_y_gai_1==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_y_gai_2==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_y_gai_3==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_y_gai_4==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_y_gai_5==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_y_gai_6==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_y_gai_7==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_y_gai_8==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_y_gai_9==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
screen xiaoqipan_f_gai:
    #小棋盘 方方 盖
    frame:
        background None
        xsize 250
        ysize 250
        xycenter(1089,364)
        grid 3 3:
            spacing 9 
            hbox:
                if xiaoqipan_f_gai_1==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_f_gai_2==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_f_gai_3==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_f_gai_4==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_f_gai_5==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_f_gai_6==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_f_gai_7==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_f_gai_8==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"
            hbox:
                if xiaoqipan_f_gai_9==0:
                    add "images/gai_xiao_wu_idle.png"
                else:
                    add "images/gai_xiao_idle.jpg"

screen xiaoqipan_y_xuanze:
    #小棋盘 圆方 选择时
    frame:
        background None
        xsize 250
        ysize 250
        xycenter(201,364)
        grid 3 3:
            spacing 9 
            hbox:
                if xiaoqipan_y_xuanze_1==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_y_xuanze_1 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_y_xuanze_2==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_y_xuanze_2 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_y_xuanze_3==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_y_xuanze_3 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_y_xuanze_4==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_y_xuanze_4 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_y_xuanze_5==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_y_xuanze_5 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_y_xuanze_6==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_y_xuanze_6 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_y_xuanze_7==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_y_xuanze_7 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_y_xuanze_8==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_y_xuanze_8 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_y_xuanze_9==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_y_xuanze_9 !=0:
                    add "images/gai_xiao_bantou_idle.png"         

screen xiaoqipan_f_xuanze:
    #小棋盘 方方 选择时
    frame:
        background None
        xsize 250
        ysize 250
        xycenter(1089,364)
        grid 3 3:
            spacing 9 
            hbox:
                if xiaoqipan_f_xuanze_1==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_f_xuanze_1 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_f_xuanze_2==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_f_xuanze_2 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_f_xuanze_3==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_f_xuanze_3 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_f_xuanze_4==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_f_xuanze_4 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_f_xuanze_5==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_f_xuanze_5 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_f_xuanze_6==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_f_xuanze_6 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_f_xuanze_7==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_f_xuanze_7 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_f_xuanze_8==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_f_xuanze_8 !=0:
                    add "images/gai_xiao_bantou_idle.png"
            hbox:
                if xiaoqipan_f_xuanze_9==0:
                    add "images/gai_xiao_wu_idle.png"
                elif xiaoqipan_f_xuanze_9 !=0:
                    add "images/gai_xiao_bantou_idle.png"