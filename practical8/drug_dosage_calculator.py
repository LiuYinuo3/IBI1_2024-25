w=float(input("the weight of the child is (kg):"))
c=input("the concentration of the drug is (120mg/5ml or 250mg/5ml):")
def volume(w,c):
    if w< 10 or w> 100:
        return "error: the weigh must be between 10 and 100kg"
    if c not in ["120mg/5ml", "250mg/5ml"]:
        return "error: the concentration must be 120 mg/5 ml or 250 mg/5 ml"
    required_mg = 15 * w
    if c == "120mg/5ml":
        volume = required_mg / 60
        return volume
    if c == "250mg/5ml":
        volume = required_mg / 50
        return volume
print("the volume of paracetamol required is:", volume(w,c),"ml")
#an example of using the function
print("example: if the weight is 20kg and the strength is 120mg/5ml, the recommended volume required is", volume(20,"120mg/5ml"), "ml")

