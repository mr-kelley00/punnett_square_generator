# Punnett Square Generator, Ryan Kelley, 11:52AM, 10/17/22, v0.3

# String Variables to store parent alleles. 
parent0_allele0 = input("Please enter the first allele for Parent #0.  [If there is only one dominant allele, enter it first.]\n")
parent0_allele1 = input("Please enter the second allele for Parent #0.\n")
parent1_allele0 = input("Please enter the first allele for Parent #1. [If there is only one dominant allele, enter it first.]\n")
parent1_allele1 = input("Please enter the second allele for Parent #1.\n")

# String Variables to store the offspring alleles. 
# Need to check that Dominant Recessive order is maintained using .isUpper()
offspring_allele0 = parent0_allele0
offspring_allele1 = parent1_allele0
offspring_allele2 = parent0_allele1
offspring_allele3 = parent1_allele1
offspring_allele4 = parent0_allele0
offspring_allele5 = parent1_allele0
offspring_allele6 = parent0_allele1
offspring_allele7 = parent1_allele1


# Display the Punnett Square
# Turn into a function in future version. 

print(f"             {parent0_allele0}                  {parent0_allele1}         ")
print(f"     +=================+=================+")
print(f"     +                 |                 +")
print(f"     +                 |                 +")
print(f"{parent1_allele0}    +       {offspring_allele0}{offspring_allele1}        |     {offspring_allele2}{offspring_allele3}          +")
print(f"     +                 |                 +")
print(f"     +                 |                 +")
print(f"     +=================+=================+")
print(f"     +                 |                 +")
print(f"     +                 |                 +")
print(f"{parent1_allele1}    +       {offspring_allele0}{offspring_allele1}        |     {offspring_allele2}{offspring_allele3}          +")
print(f"     +                 |                 +")
print(f"     +                 |                 +")
print(f"     +=================+=================+")