

from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

alphabet = list('abcdefghijklmnopqrstuvwxyz')

found = False
for letter1 in alphabet:
    for letter2 in alphabet:
        find_me = letter1 + letter2
        secret_password = find_me + 'bcmpda'
        
        if unzip_with_7z(zip_file_path, dest_path, secret_password):
            print(f"Success! Password was: {secret_password}")
            print(f"File extracted to: {dest_path}")
            print("\nExtracted files:")
            for item in os.listdir(dest_path):
                print(f"  - {item}")
            found = True
            break
    
    if found:
        break