def far_to_cel(temp):
    return (5/9) * (temp - 32)

def solve(numheads, numlegs):
    rabbit = (numlegs - 2*numheads) / 2
    chicken = numheads - rabbit
    return (int(rabbit), int(chicken))

def convert_to_gram(ounces):
    return ounces * 28.3495231


print("Let's cook rabbits and chickens for the dinner!")

numheads = int(input("How many heads of animals do you have?: "))
numlegs = int(input("How many legs of animals do you have?: "))

rabbit, chicken = solve(numheads, numlegs)

print("Now we have the amount of rabbits and chickens.\n Let's cook it!")

temp = int(input("Write the temperature you are gonna cook the chicken in: "))

print("Looks like it is in Fahrenheits. Let's convert it to Celcius!")

temp = int(far_to_cel(temp))
weight = int(input("What the weight of the animals in ounces?: "))

print("Yo, let's convert it to grams")

weight = int(convert_to_gram(weight))

print(f"So your animals' weight is {weight}, you are going to cook it at {temp} degrees Celcius and you have {rabbit} rabbits & {chicken} chickens")
