import bcrypt

# Function to hash a password
def hash_password(plain_password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password using the salt
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed_password


def verify_password(plain_password, hashed_password):
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)


if __name__=="__main__":

    password = input("mettre son mdp: ")

    hashed = hash_password(password)
    print(f"Mot de passe haché {hashed}")

    hashed2 = hash_password("mdp2")
    print(f"Mot de passe haché 2 {hashed2}")

    password_test = input("mettre son mdp de test: ")

    is_correct = verify_password(password_test, hashed)
    print(f"Password validation: {is_correct}")


    #==================================================

    #hashed_test = b'$2b$12$mI5ymyJmWdL9PtAPgL9I2OvPs0ie/IJoRYLla5I1s0LZ8sWRb0D3G'
    #password = input("mettre son mdp: ")
    #is_correct = verify_password(password, hashed_test)
    #print(f"Password validation: {is_correct}")