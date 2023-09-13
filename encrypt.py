from flask import Flask
from cryptography.fernet import Fernet
from flask import Flask, render_template, request

application = Flask(__name__)

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt the text
def encrypt_text(text):
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

# Decrypt the text
def decrypt_text(encrypted_text):
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the text to encrypt from the form
        plaintext = request.form['textToEncrypt']
        
        # Encrypt the text
        encrypted_data = encrypt_text(plaintext)

        # Decrypt the text (for demonstration purposes)
        decrypted_data = decrypt_text(encrypted_data)

        return render_template('index.html', encrypted_data=encrypted_data, decrypted_data=decrypted_data)

    return render_template('index.html', encrypted_data=None, decrypted_data=None)

if __name__ == '__main__':
    application.run(debug=True)