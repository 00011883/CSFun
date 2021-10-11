print(f"{'='*10}\n {' '*2}WIUT \n{'='*10}")

print(f"{'='*10}\n WIUT BIS \n{'='*10}")

decor = input("Enter decoration symbol: ")
faculty = input("Enter your faculty abbreviation: ")

print(f"{decor*10}\n WIUT {faculty}\n{decor*10}")

# Homework

csf_cw1 = float(input("Enter your result for CW1: "))
csf_cw2 = float(input("Enter your result for CW2: "))

result = csf_cw1 * .4 + csf_cw2 * .6

print(f"Your result is: {round(result,2)}")