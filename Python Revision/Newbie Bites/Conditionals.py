#Objective: Revise the use of conditionals in Python

def check_payday(date):
    if date == "payday":
        return("Time to pay the rent.")
    else:
        return("Keep calm and eat two minute noodles.")


#Expected Result: "Time to pay the rent."
print(check_payday("payday"))

#Expected Result: "Keep calm and eat two minute noodles."
print(check_payday("notPayday"))
