pet = int(input())
vas = int(input())
tol = int(input())
s = {pet: "Петя", vas: "Вася", tol: "Толя"}
print(f"          {s[max(pet, vas, tol)]}          ")
print(f"  {s[pet + vas + tol - max(pet, vas, tol) - min(pet, vas, tol)]}                    ")
print(f"                  {s[min(pet, vas, tol)]}  ")
print("   II      I      III   ")