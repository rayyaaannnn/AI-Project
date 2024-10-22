u_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l_alpha = 'abcdefghijklmnopqrstuvwxyz'

a = input('Enter any alphabet: ')

if  a in u_alpha:
    print('You entered',a,'in uppercase.')
elif  a in l_alpha:
    print('The alphabet',a,'in lowercase.')

