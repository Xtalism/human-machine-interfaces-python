try:
        name = (input('Enter your name: ')).lower()
        gender = (input('Enter your gender: ')).lower()
        name_letter = name [0]
        gender_letter = gender[0]

        women = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
        men = ['ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        if (gender_letter == 'f' and name_letter in women) or (gender_letter == 'm' and name_letter in men):
                print('You belong to group A')
        else:
                print('You belong to group B')

except ValueError:
        print('You must enter a string!')