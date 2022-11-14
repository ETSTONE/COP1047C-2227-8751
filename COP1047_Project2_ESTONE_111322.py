#COP1047 Project 2 
#EStone
#11/13/22



dogs_per_pack = 10 #10 dogs per pack
buns_per_pack = 8 #8 buns/rolls per pack

people = int(input("Enter the number of people attending the cookout: "))
dogs = int(input("Enter the number of hot dogs each person will eat: "))

#Each hot dog will always be served with a bun. NO QUESTIONS!
number_of_dogs = people * dogs

#If Else serves to ensure the counts are taken into consideration, we want to be as accurate as possible.
#using % to identify the remainder and // to provide the the even distrobution
if number_of_dogs % dogs_per_pack == 0:
    number_of_packs = number_of_dogs // dogs_per_pack
else:
    number_of_packs = number_of_dogs // dogs_per_pack + 1

if number_of_dogs % buns_per_pack == 0:
    number_of_bun_packs = number_of_dogs // buns_per_pack
else:
    number_of_bun_packs = number_of_dogs // buns_per_pack + 1

print("Minimum number of Hot Dog package(s): ", number_of_packs)
print("Minimum number of Hot Dog Bun/Roll(s) package(s) : ", number_of_bun_packs)
print("Number of individual Hot Dog(s) left over: ", number_of_packs * dogs_per_pack - number_of_dogs)
print("Number of individual Hot Dog Bun/Roll(s) left over: ", number_of_bun_packs * buns_per_pack - number_of_dogs)

## Could have imported a math library to use the ceil function to round up, but I wanted to do it the long way.