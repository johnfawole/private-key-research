# importing 3 vital modules from the Python Cryptography library
# read the actual documentation for better understanding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# the private key to be generated
private_key = ec.generate_private_key(ec.SECP384R1())

# serialization phase; encoding, formating, and choosing your preferred encryption algorithm
private_key_serialization = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    #@dev "Utila Cryptography" can be replaced with any word or phrase for a higher entropy
    encryption_algorithm=serialization.BestAvailableEncryption(b"Utila Cryptography")
)

# hashing with SHA-256, it will be useful for our next steps
first_hash = hashes.SHA256()
hasher = hashes.Hash(first_hash)
# actual updating of the serialized private key with hash
hasher.update(private_key_serialization)
hashed_private_key = hasher.finalize()

# turning into into a 32-byte
private_key_32_bytes = hashed_private_key[:32]
private_key_in_hex = private_key_32_bytes.hex()

# padding to optimization the length of the private key
padding_the_private_key = private_key_in_hex.zfill(64)

# this will publish our private key to the console
print(padding_the_private_key)