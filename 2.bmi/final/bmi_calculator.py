print("Bienvenue sur le calculateur de BMI \n ------------------")

weight = float(input('Votre poids en kg : '))
height = float(input('Votre taille en cm : '))

def formula_bmi(weight=weight, height=height):
    height = height / 100
    bmi = weight / height**2
    rounded_bmi = round(bmi, 2)
    return rounded_bmi


print(f"Votre BMI est de {formula_bmi()}.")
