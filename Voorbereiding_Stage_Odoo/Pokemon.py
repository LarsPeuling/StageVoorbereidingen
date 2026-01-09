import random

if __name__ == "__main__":
     
    #pokemon_power = int(input("Enter the power value of the pokemon: "))
    powers =[]
    intput = int(input("Enter number of pokemons you've captured: "))
    for i in range(intput):
        pokemon_power = random.randint(1,100)
        powers.append(pokemon_power)
        
    mini, maxi = 0,0
     
    print ("Powers of pokemons are: ", powers)
    for power in powers:
        if mini == 0 and maxi == 0:
            mini, maxi = powers[0], powers[0]
            print(mini, maxi)
        else:
            mini = min(mini, power)
            maxi = max(maxi, power)
            print(mini, maxi)