favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Ruby',
    'phil': 'Python'
}

print('Sarah\'s favorite languages is ' + favorite_languages['sarah'].title() + '.')

for name, language in favorite_languages.items():
    print(name.title() + '\'s favorite language is ' + language.title())

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print('Hi ' + name.title() +
              ', I see your favorite language is ' +
              favorite_languages[name].title() + '!')

print('\nThe following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward':['ruby', 'go'],
    'phil': ['python', 'haskell']
}


for name, languages in favorite_languages.items():
    print('\n' + name.title() + '\'s favorite languages are:')
    for language in languages:
        print('\t' + language.title())