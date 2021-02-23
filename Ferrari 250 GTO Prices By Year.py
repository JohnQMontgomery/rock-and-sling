def main():

    #Ferrari 250 GTO Prices by Year
    year_1962_1964 = 18500 #less than 1965
    year_1965_1968 = 6000  #less than 1969
    year_1969_1971 = 12000 #less than 1972
    year_1972_1975 = 48000 #less than 1976
    year_1976_1980 = 200000 #less than 1981
    year_1981_1985 = 650000 #less than 1986
    year_1986_2012 = 35000000 #less than 2013
    year_2013_2014 = 52000000 #less than 2015
        
    year = int(input('Enter Ferrari 250 GTO Model Year: '))

    if year <= 1961:
        print('Please enter a model year between 1962-2014.')
        price = 0

    elif year >= 2015:
        print('Please enter a model year between 1962-2014.')
        price = 0

    elif year <= 1964:
        price = year_1962_1964

    elif year <= 1968:
        price = year_1965_1968

    elif year <= 1971:
        price = year_1969_1971

    elif year <= 1975:
        price = year_1972_1975

    elif year <= 1980:
        price = year_1976_1980

    elif year <= 1985:
        price = year_1981_1985

    elif year <= 2012:
        price = year_1986_2012

    else:
        price = year_2013_2014
        
    print('Annual Price: $%d' % price) 
      
    restart = input('Would you like a different model year? ').lower()
    if restart == 'yes':
        main()

    else:
        exit()

main()
   

