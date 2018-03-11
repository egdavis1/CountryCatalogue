##Programmer: Emma Davis
#Date Due: Dec. 3, 2016
#This program contains two classes.  The first class defines the countries sent to it by the second function.  The first
#class returns values to the second class as needed when it is called.

#This class defines the object country.
class Country:
    #Constructor method
    def __init__(self, name, pop, area, continent):
        self.name = name
        self.pop = pop
        self.area = area
        self.continent = continent
        self.popDensity = round(int(self.pop)/float(self.area), 2)

    #Returns a string version of the country
    def __repr__(self):
        self.pop = str(self.pop)
        self.area = str(self.area)
        self.popDensity = str(self.popDensity)
        self.continent = str(self.continent)
        self.string = self.name + ": " +  self.pop + ", " + self.area + ", " + self.popDensity + ", " + self.continent

        return self.string

    #Sets the population that the method is given
    def setPopulation(self, pop):
        self.pop = pop

    #Returns the name of the country
    def getName(self):
        return self.name

    #returns the area of the country
    def getArea(self):
        return self.area

    #returns the population of the country
    def getPopulation(self):
        return self.pop

    #returns the continent of the country
    def getContinent(self):
        return self.continent

    #returns the population density of the country
    def getPopDensity(self):
        self.popDensity = round(int(self.pop)/float(self.area), 2)
        return self.popDensity

#This class uses the Country class to define the countries.  It computes different comutations with the countries.
class CountryCatalogue:
    #Constructor method
    def __init__ (self, txtFile):
        #open the file with the countries and continents
        self.continent = open("continent.txt", "r")

        #define a dictionary
        cDictionary = {}

        #reads the first line of the file before doing anything as the first line is just a header
        self.continent.readline()

        #fills the dictionary of countries and continents
        for line in self.continent:
            #strips and splits the line
            line = line.strip()
            line = line.split(",")

            #sets the country to the key and the continent to the value
            cDictionary[line[0]] = line[1]

        #close the file
        self.continent.close()

        #opens the file that the class is sent
        self.data = open(txtFile, "r")
        #reads the first line without doing anything as the first line is a header
        self.data.readline()
        #creats a country object as a list
        self.country = []

        #loops through the lines of the file
        for line in self.data:
            #strips and replaces the commas with an empty string and splits the line
            line = line.strip()
            line = line.replace(",", "")
            line = line.split("|")

            #finds the countinent that the country is in from the dictionary by looping through the dictionary
            for element in cDictionary:
                #if the country in the dictionary is the same as the country
                if element == line[0]:
                    #sends the country with its
                    self.country.append(Country(line[0], line[1], line[2], cDictionary[element]))

        #close the file
        self.data.close()

    #method to add a country
    def addCountry(self):
        #ask for user input to add a country
        answer = input("Would you like to add a new country? (Y/N): ")

        #while an incorrect reponse is given
        while answer.upper() != "Y" and answer.upper() != "N":
            #print error message then ask for user input again
            print("Invalid answer. Please enter a Y or N.")
            answer = input("Would you like to add a new country? (Y/N): ")

        #if the user would like to add a new country
        if answer.upper() == "Y":
            #ask for user input of the name of the new country
            countryName = input("Enter the new country name: ")

            #goes through the countries to see if the inputed country is already in the list of countries
            for x in range(len(self.country)):
                while (self.country[x].getName()).lower() == countryName.lower():
                    #if the country is already in the catalogue then ask for a new country name
                    print("That country is already in the catalogue, please enter a different country.")
                    countryName = input("Enter the new country name: ")

            #ask for user input for additional information about the country
            countryPop = int(input("Enter " + countryName + "'s population: "))
            countryArea = int(input("Enter " + countryName + "'s area: "))

            #add the new country to the catalogue
            self.country.append(Country(countryName, countryPop, countryArea, ""))

    #method to delete a country from the catalogue
    def deleteCountry(self):
        #ask for user input for the country to be deleted, assume correct input
        deleteCountry = input("Enter a country to be deleted: ")

        #boolen variable: set to True if new country, set to False is the country is already in the catalogue
        newCountry = True

        #loop through the list of countries to see if the inputed country is in the catalogue
        for x in range(len(self.country) - 1):
            if (self.country[x].getName()).lower() == deleteCountry.lower():
                #if country is in the catalogue then delete it and print a confirmation message
                self.country.pop(x)
                print(deleteCountry, "was deleted.")

                #set the boolen variable to False as the country is not new
                newCountry = False

        #if the country is not in the catalogue then print a message saying the inputed country was not deleted
        if newCountry == True:
                print(deleteCountry, "was not in the catalogue. It was not deleted.")


    #method to find a country and display the information on it
    def findCountry(self):
        #ask for user input for the name of the country
        findCountry = input("Enter a country: ")
        notCountry = False

        #loop through the countries
        for x in range(len(self.country)):
            #see if the country is the same as the inputed country and if it is, then print the information on the country
            if (self.country[x].getName()).lower() == findCountry.lower():
                print(self.country[x].__repr__())
                notCountry = True

        #if the inputed country is not in the catalogue then print a message saying the country does not exist
        if not notCountry:
            print("Country does not exist")

    #method that displays all the countries in the catalogue that are in the continent entered by the user
    def filterCountriesByContinent(self):
        #get user input
        continent = input("Enter a continent: ")

        #loop through the country catalogue
        for x in range (len(self.country)):
            #if the country is in the specified continent then display the name of that country
            if (self.country[x].getContinent()).lower() == continent.lower():
                print(self.country[x].getName())
        print()

    #prints the whole catalogue
    def printCountryCatalogue(self):
        for element in self.country:
            print(element.__repr__())

    ##methods that gets user input for the name of the country then asks for the new population of that country then
    #displays the country's new population density
    def setPopulationOfASelectedCountry(self):
        newCountry = False
        #gets user input for the country
        popCountry = input("Enter a country: ")

        #loops through the countries
        for x in range (len(self.country)):
            #if the country is the country the user inputed
            if (self.country[x].getName()).lower() == popCountry.lower():
                #get the new population of the country then set it to that country
                pop = input("Enter the new population of " + popCountry + ": ")
                self.country[x].setPopulation(pop)

                #print the new population density of the country
                print("The new population density of", popCountry, "is: ", round(int(self.country[x].getPopulation())/float(self.country[x].getArea()), 2))
                newCountry = True

        #if the country was not in the catalogue then print a message
        if not newCountry:
            print(popCountry, "wasn't in the calalogue.")

    #method that finds and displays the name of the country that has the largest population
    def findCountryWithLargestPop(self):

        #sets the first country as the highest population
        highPop = int(self.country[0].getPopulation())
        countryNum = 0

        #loops through the countries
        for x in range(len(self.country)):
            ##if the country's population is greater than the highest population then set this country to be the country
            #with the highest population
            if int(self.country[x].getPopulation()) > highPop:
                highPop = int(self.country[x].getPopulation())
                countryNum = x

        #display the country with the largest population
        print("The country with the largest population is:", self.country[countryNum].getName())

    #method that finds and displays the name of the country with the smallest area
    def findCountryWithSmallestArea(self):
        #sets the first country's area to be the smallest area
        lowArea = float(self.country[0].getArea())
        countryNum = 0

        #loops through the countries
        for x in range(len(self.country)):
            #if the area of the country is smaller than the smallest area then set this country to have the smallest area
            if float(self.country[x].getArea()) < lowArea:
                lowArea = float(self.country[x].getArea())
                countryNum = x

        #display the country with the smallest area
        print("The country with the smallest area is:", self.country[countryNum].getName())
        print()

    ##method that gets the lower and upper bound for population density from the user then displays all of the countries
    #with a population density within that range
    def filterCountriesByPopDensity(self):
        #get user input for the lower and upper bound
        lowerBound = input("Enter the lower bound for a population density range: ")
        upperBound = input("Enter the upper bound for a population density range: ")

        print("The countries with population densities in range", lowerBound, "-", upperBound, " are:", end = " ")

        #loops through the countries and print if the countries population density is within the range then displays it
        for x in range(len(self.country)):
            if float(self.country[x].getPopDensity()) > int(lowerBound) and float(self.country[x].getPopDensity()) < int(upperBound):
                print(self.country[x].getName(), end = " ")
        print("\n")

    #method that finds and displays the name of the continent with the greatest population as well as the number of people
    def findMostPopulousContinent(self):
        #set each continents population to zero
        asiaPop = 0
        northAmericaPop = 0
        southAmeriaPop = 0
        africaPop = 0
        europePop = 0

        #loops through the countries
        for x in range(len(self.country)):
            #if the country is in Asia add the population of the country to the population of Asia
            if (self.country[x].getContinent()).lower() == "Asia".lower():
                asiaPop = asiaPop + int(self.country[x].getPopulation())

            #if the country is in North America add the population of the country to the population of North America
            elif (self.country[x].getContinent()).lower() == "North America".lower():
                northAmericaPop = northAmericaPop + int(self.country[x].getPopulation())

            #if the country is in South America add the population of the country to the population of South America
            elif (self.country[x].getContinent()).lower() == "South America".lower():
                southAmeriaPop = southAmeriaPop + int(self.country[x].getPopulation())

            #if the country is in Africa add the population of the country to the population of Africa
            elif(self.country[x].getContinent()).lower() == "Africa".lower():
                africaPop = africaPop + int(self.country[x].getPopulation())

            #if the country is in Europe add the population of the country to the population of Europe
            elif(self.country[x].getContinent()).lower() == "Europe".lower():
                europePop = europePop + int(self.country[x].getPopulation())

        #sets Asia to be the most populus continent and sets the population
        mostPopulusContinent = "Asia"
        mostPopulus = asiaPop

        #if the population in North America is bigger then set it to be the most populus continent
        if northAmericaPop > mostPopulus:
            mostPopulusContinent = "North America"
            mostPopulus = northAmericaPop

        #if the population in South America is bigger then set it to be the most populus continent
        elif southAmeriaPop > mostPopulus:
            mostPopulusContinent = "South America"
            mostPopulus = southAmeriaPop

        #if the population in Africa is bigger then set it to be the most populus continent
        elif africaPop > mostPopulus:
            mostPopulusContinent = "Africa"
            mostPopulus = africaPop

        #if the population in Europe is bigger then set it to be the most populus continent
        elif europePop > mostPopulus:
            mostPopulusContinent = "Europe"
            mostPopulus = europePop

        #display the most populus continent's name and the amount of people living in it
        print("The most populus continent is:", mostPopulusContinent, "with", mostPopulus, "people living in it.")

    #method that saves all the countries to a file given to it in alphabetical order
    def saveCountryCatalogue(self, fileName):
        #open the file
        writeFile = open(fileName, "w")
        sortedCountries = []

        #loops through the countries and adds them to the list of sorted countries
        for x in range(len(self.country)):
            sortedCountries.append(self.country[x].getName())

        #sorts the countries
        sortedCountries = sorted(sortedCountries)

        #loops through the sorted countries
        for x in range(len(self.country)):
            #loops through the countries
            for y in range(len(self.country)):
                #if the sorted country equals the country the creates a string of all the information on that country
                if sortedCountries[x] == self.country[y].getName():
                    string = str(self.country[y].getName()) + "|" + str(self.country[y].getContinent()) + "|" + str(self.country[y].getPopulation()) + "|" + str(self.country[y].getPopDensity()) + "\n"
                    #writes the string to the file
                    writeFile.write(string)

        #closes the file and prints a message to the screen
        writeFile.close()
        print("The cuntry catalogue has been save to", fileName, "file.")

