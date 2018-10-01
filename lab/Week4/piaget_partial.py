## Data Section
## =============
# [TODO] Please prepare the data in piaget_theory. An empty dict would result in KeyError in the following code.
piaget_theory = {

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