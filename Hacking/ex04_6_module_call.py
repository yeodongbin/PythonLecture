import sys
import ex04_5_modHero

querySkill = input("select weapon: ")

i=0

for each_item in modHero.skill:                            #(2)
    if(each_item == querySkill):
        modHero.printItem(querySkill, i)                   #(3)
    i = i+1
        
print("----------------------------------------")
print("\n")
