def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    country = locale.split('.')[0].split('_')[1]

    match country:
        case 'US':
            return 'Howdy pardner!'
        case 'GB':
            return 'Hello guvnah!'
        case 'AU':
            return "G'day mate!"
        case 'CA':
            return 'Hello der pal!'
        case _:
            return 'Hello.'
        
print(local_greet('en_US.TF-8'))
print(local_greet('en_GB.TF-8'))
print(local_greet('en_AU.TF-8'))
print(local_greet('en_CA.TF-8'))
print(local_greet('en_NZ.TF-8'))
###