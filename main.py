import base64
import hashlib
import xml.etree.ElementTree as ET
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import argparse

def dotnet_password_derive_bytes_no_salt(password, length, count):
    iter_hash  = hashlib.sha1(password).digest()
    count -= 1    
    for i in range(count-1): 
        iter_hash = hashlib.sha1(iter_hash).digest()

    done_bytes = hashlib.sha1(iter_hash).digest()
    return(done_bytes[:length])

# Cloud.Base.aru.DRC = "9B80F6F2-BEF9-4C7F-8708-9932B806A5C4" in CloudBerry Backup version 7.8.5.15
CLOUDBERRY_AES_KEY = dotnet_password_derive_bytes_no_salt(b'9B80F6F2-BEF9-4C7F-8708-9932B806A5C4', 16, 100)


CIPHER_INSTANCE = AES.new(CLOUDBERRY_AES_KEY, AES.MODE_ECB)


def extract_from_enginesettings(path: str):
    tree = ET.parse(path)
    root = tree.getroot()
    network_shares = root.find("NetworkShares")


    for share in network_shares.findall("NetworkCredentialsSettings"):
        login = share.findtext("Login")
        share_path = share.findtext("Share")
        encrypted_password = share.findtext("Password")
        password =  unpad(CIPHER_INSTANCE.decrypt(base64.b64decode(encrypted_password)),16).decode()
        print(f"{share_path} {login} {password}")



def main():
    parser = argparse.ArgumentParser(
                    prog='Cloudberry Config Decryptor',
                    description='Decrypt passwords inside CloudBerry config files',
    )
    parser.add_argument('config', help="Path to the CloudBerry enginesettings.list file")

    args = parser.parse_args()    

    extract_from_enginesettings(args.config)


if __name__ == "__main__":
    main()
