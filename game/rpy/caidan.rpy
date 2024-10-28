screen caidan_x:
    frame:
        xycenter(1200,80)
        background None
        textbutton"{alpha=0}{size=40}反{/alpha}":
            action ShowTransient("caidan")

screen guize_suomin:
    zorder 101 #层级
    modal True #禁止该界面与下层界面进行交互
    frame:
        xycenter(0.5,0.5)
        xysize(568,410)
        background "images/guize_suomin.png"
        frame:
            background None
            xsize 568
            xmargin 10
            ymargin 10
            #内边距
            text ("1 任意一方大的数字可以覆盖小的数字，反之不可。\n\n2 当一方棋子连成一条三点的线，则此方获胜。\n\n3 落子顺序为从小到大(非强制)。"):
                line_spacing 3
                language "unicode" #断行方法
                layout "tex"
                
        frame:
            xysize(568,82)
            ycenter 0.9
            background None
            frame:
                xycenter (0.5,0.5)
                background None
                textbutton"{size=35}返回{/alpha}":
                    text_color "#595951"
                    text_hover_color "#ffffff"
                    action Hide("guize_suomin")

screen caidan:
    zorder 100 #层级
    modal True #禁止该界面与下层界面进行交互
    frame:
        xycenter(0.5,0.5)
        xysize(568,410)
        background "images/caidan.png"
        
        vbox:
            hbox:
                frame:
                    xysize(568,82)
                    background None
                    frame:
                        xycenter (0.5,0.5)
                        background None
                        text "{size=40}菜单{/alpha}":
                            bold True
            hbox:
                frame:
                    xysize(568,82)
                    background None
                    frame:
                        xycenter (0.5,0.5)
                        background None
                        textbutton"{size=35}规则说明{/alpha}":
                            text_color "#595951"
                            text_hover_color "#ffffff"
                            action ShowTransient("guize_suomin")
            hbox:
                frame:
                    xysize(568,82)
                    background None
                    frame:
                        xycenter (0.5,0.5)
                        background None
                        textbutton"{size=35}重新开始{/alpha}":
                            text_color "#595951"
                            text_hover_color "#ffffff"
                            action Jump("congxinkaisi")
            hbox:
                frame:
                    xysize(568,82)
                    background None
                    frame:
                        xycenter (0.5,0.5)
                        background None
                        textbutton"{size=35}主界面{/alpha}":
                            text_color "#595951"
                            text_hover_color "#ffffff"
                            action MainMenu()
            hbox:
                frame:
                    xysize(568,82)
                    background None
                    frame:
                        xycenter (0.5,0.5)
                        background None
                        textbutton"{size=35}返回{/alpha}":
                            text_color "#595951"
                            text_hover_color "#ffffff"
                            action Hide("caidan")


screen cexiao_1:
    frame:
        xycenter(1200,630)
        background None
        textbutton"{alpha=0}{size=45}反{/alpha}":
            action Rollback()
screen cexiao_2:
    frame:
        xycenter(85,630)
        background None
        textbutton"{alpha=0}{size=45}反{/alpha}":
            action Rollback()


label congxinkaisi:
    python:
        #小棋盘 圆方 选择时 的变量
        xiaoqipan_y_xuanze_1=0
        xiaoqipan_y_xuanze_2=0
        xiaoqipan_y_xuanze_3=0
        xiaoqipan_y_xuanze_4=0
        xiaoqipan_y_xuanze_5=0
        xiaoqipan_y_xuanze_6=0
        xiaoqipan_y_xuanze_7=0
        xiaoqipan_y_xuanze_8=0
        xiaoqipan_y_xuanze_9=0
        # 小棋盘 圆方 盖 的变量
        xiaoqipan_y_gai_1=0
        xiaoqipan_y_gai_2=0
        xiaoqipan_y_gai_3=0
        xiaoqipan_y_gai_4=0
        xiaoqipan_y_gai_5=0
        xiaoqipan_y_gai_6=0
        xiaoqipan_y_gai_7=0
        xiaoqipan_y_gai_8=0
        xiaoqipan_y_gai_9=0
        #小棋盘 方方 选择时 的变量
        xiaoqipan_f_xuanze_1=0
        xiaoqipan_f_xuanze_2=0
        xiaoqipan_f_xuanze_3=0
        xiaoqipan_f_xuanze_4=0
        xiaoqipan_f_xuanze_5=0
        xiaoqipan_f_xuanze_6=0
        xiaoqipan_f_xuanze_7=0
        xiaoqipan_f_xuanze_8=0
        xiaoqipan_f_xuanze_9=0
        # 小棋盘 方方 盖 的变量
        xiaoqipan_f_gai_1=0
        xiaoqipan_f_gai_2=0
        xiaoqipan_f_gai_3=0
        xiaoqipan_f_gai_4=0
        xiaoqipan_f_gai_5=0
        xiaoqipan_f_gai_6=0
        xiaoqipan_f_gai_7=0
        xiaoqipan_f_gai_8=0
        xiaoqipan_f_gai_9=0
        #大棋盘的变量
        daqipan_1_1=0
        daqipan_1_2=0
        daqipan_1_3=0
        daqipan_2_1=0
        daqipan_2_2=0
        daqipan_2_3=0
        daqipan_3_1=0
        daqipan_3_2=0
        daqipan_3_3=0
        #大棋盘的圆方方 0为空1为圆2为方
        daqipan_1_1_suxin=0
        daqipan_1_2_suxin=0
        daqipan_1_3_suxin=0
        daqipan_2_1_suxin=0
        daqipan_2_2_suxin=0
        daqipan_2_3_suxin=0
        daqipan_3_1_suxin=0
        daqipan_3_2_suxin=0
        daqipan_3_3_suxin=0

        huihe=0
        #传递值
        cuandi_y=0
        cuandi_f=0
    jump start
    return