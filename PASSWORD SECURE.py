def secure_password(password, replacements):
    for char, secure_char in replacements:
        password = password.replace(char, secure_char)
    return password

# Example usage
existing_password = "myPassword123"
replacement_chars = [("a", "@"), ("s", "$"), ("o", "0")]

secured_password = secure_password(existing_password, replacement_chars)
print("Original Password:", existing_password)
print("Secured Password:", secured_password)
