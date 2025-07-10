from werkzeug.security import check_password_hash, generate_password_hash

resultado = generate_password_hash('admin123', method='scrypt')
print(resultado)