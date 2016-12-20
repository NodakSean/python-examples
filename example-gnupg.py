"""
Encrypt a file using GPG, then FTP
it to a remote server.
"""

from gnupg import GPG
from ftplib import FPT

# Create instance and set gpg working directory
gpg = GPG(gnupghome=".gpg")

# import an existing public key
with open("mykey.asc", 'r') as fp:
    key_data = fp.read()
    import_status = gpg.import_keys(key_data)
    print("ok: {}".format(import_status.results["ok"]))
    print("text: {}".format(import_status.results["text"]))

# Encrypt a file using the public key.
with open("plain.txt", 'rb') as fp:
    encrypted_file = "encrypted.asc"
    encrypt_status = gpg.encrypt_file(
        fp,
        recipients=import_status.fingerprints,
        always_trust=True,
        output=encrypted_file)
    print("ok {}".format(encrypt_status.ok))
    print("text: {}".format(encrypt_status.text))
    print("stderr: {}".format(encrypt_status.stderr))

# FTP the file
with FTP("ftp.somehost.com") as ftp:
    ftp.connect("a_username", "a_password")
    fp = open(encrypted_file, 'rb')
    ftp.storbinary("STOR {}".format(encrypted_file), fp)
    ftp.quit()

fp.close()