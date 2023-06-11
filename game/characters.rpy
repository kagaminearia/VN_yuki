# 此文件用于定义角色以及对应图片

#ctc
image ctc_blink:
    xalign 0.981 yalign 0.965 
    "GUI/arrow.png"
    alpha 1.0
    linear 0.75
    alpha 0.0
    linear 0.75
    repeat

#文本音效
#init python:
#    def male_voice(event, interact=True, **kwargs):
#        if not interact:
#            return

#        if event == "show_done":
#            renpy.sound.play("audio/male.mp3")
#        elif event == "slow_done":
#            renpy.sound.stop()

# 角色名
define y = Character('景雪', color="#ffffff", ctc="ctc_blink",ctc_position = "fixed")
define m = Character('米勒克尔', color="#ffffff", ctc="ctc_blink",ctc_position = "fixed")
define www = Character('？？？', color="#ffffff", ctc="ctc_blink",ctc_position = "fixed")

#define ruby = Character("露比", image="ruby", ctc="ctc_blink",ctc_position = "fixed")
#define m = Character("大臣", ctc="ctc_blink",ctc_position = "fixed", callback=male_voice)#文本音效callback
define narrator = Character(None,ctc="ctc_blink", ctc_position="fixed")


# 角色立绘
#image ruby smile = "images/ruby smile.png"
#image ruby concerned = "ruby_concerned.png"

#image side ruby smile = "side_ruby_smile.png"
#image side ruby = "others/side_ruby.png"

#image imgframe = "others/imgframe.png"

transform center_yk_b:
    xalign 0.5
    yalign 0.06

transform center_yk:
    xalign 0.5
    yalign 0.005

transform left_yk:
    xalign 0.25
    yalign 0.8

transform right_yk:
    xalign 0.75
    yalign 0.8

transform left_long:
    xalign 0.2
    yalign 1.0

transform right_long:
    xalign 0.8
    yalign 1.0