import random

def generate_random_password(length):
  """
  Generates a random password with a specified length.
  
  Args:
    length: The desired length of the password.
    
  Returns:
    A randomly generated password string.
  """
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
  password = ''.join(random.choice(characters) for i in range(length))
  return password

# Example usage:
password_length = 12
random_password = generate_random_password(password_length)
print(f"Random Password: {random_password}")
