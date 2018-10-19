## Data section
## =================

## [NOTE] Piaget's cognitive development theory IS NOT 
## just a collection of stage description. Please refer 
## to following link for a more detail introduction of 
## cognitive development theory. 
## https://en.wikipedia.org/wiki/Piaget%27s_theory_of_cognitive_development

piaget_theory = {
    "Sensorimotor": {
        "description": (
            "嬰兒透過感覺與動作經驗建構對於世界的知識，\n"
            "並藉著本能性反射與世界互動。\n"
            "此階段將發展出物體恆存概念。\n"),
        "label": "感覺運動期"
    },
    "Preoperational": {
        "description": (
            "幼兒已經能使用語言、符號等工具表徵外在事物。\n"
            "此階段幼兒的思考被認為有以自我為中心、不可逆轉、\n"
            "專注事物單面向等特性。\n"),
        "label": "前運思期"
    },
    "Concrete Operational": {
        "description": (
            "幼兒開始理解邏輯規則，並能按照具體經驗解決問題。\n"  
            "在認知發展理論中，此階段的幼兒已掌握可逆與保留概念，\n"
            "同時也能理解如何從別人的角度看世界。"
            ),
        "label": "具體運思期"
    },
    "Formal Operational": {
        "description": (
            "個體開始具備抽象概念思考和演繹推理的能力，\n"
            "並逐漸展現出後設認知及系統性解決問題的能力。\n"),
        "label": "形式運思期"
    }
}

## Input Section
## ===============

age_str = input("請輸入年齡(0-16):")
age = int(age_str)

## Program Section
## ================
if 0 <= age < 2:
    stage = "Sensorimotor"
elif 2 <= age < 7:
    stage = "Preoperational"
elif 7 <= age < 11:
    stage = "Concrete Operational"
elif 11 <= age <= 16:
    stage = "Formal Operational"
else:
    print("invalid age")
    exit()
stage_info = piaget_theory[stage]
stage_tw = stage_info["label"]
description = stage_info["description"]

## Output Section
## ==============
print("== " + stage_tw + " ==")
print("(" + stage + ")")
print(description)
