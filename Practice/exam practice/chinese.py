trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}



def speak_Chinese(number):
    '''
    number: an integer, 0<=number<=999

    Returns: a string that is the number in Chinese
    '''
    if number <= 10:
        x = str(number)
        return trans[x]
    elif 11 <= number <= 19:
        x = str(number - 10)
        return trans['10'] + " " + trans[x]
    elif (20 <= number <= 99) and (number % 10 != 0):
        number = str(number)
        a = number[0]
        b = number[1]
        return trans[a] + " " + trans['10'] + " " + trans[b]
    elif (20 <= number <= 99) and (number % 10 == 0):
        number = str(number)
        a = number[0]
        return trans[a] + " " + trans['10']
    elif number % 100 == 0:
        number = str(number)
        a = number[0]
        return trans[a] + " " + trans['100']
    elif (number > 100) and (number % 100 != 0) and (number % 10 != 0):
        number = str(number)
        a = number[0]
        b = number[1]
        c = number[2]
        if b == '0':
            return trans[a] + " " +  trans['100'] + " " + trans[b] + " " + trans[c]
        else:
            return trans[a] + " " + trans['100'] + " " + trans[b] + " " + trans['10'] + " " + trans[c]
    elif (number > 100) and (number % 10 == 0):
        number = str(number)
        a = number[0]
        b = number[1]
        return trans[a] + " " + trans['100'] + " " + trans[b] + " " + trans['10']
    else:
        print('Number is too large, choose a number 1-999')
            

            
        
            


# For testing
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')


if __name__ == '__main__':
    main()
