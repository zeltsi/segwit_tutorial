hash            = (bytes.fromhex('73c9fec091af7d5fa74650e758b40b4f9895404d1cb95193b6ec059a541dd44f'))[::-1]
# Yes, it's a real private key. You can have a go with it, but please try to recharge this address so that others might get to try it too
private_key     = bytes.fromhex("0c5453736c13e0cb4f364fa9bba7e614b82ac542c7c69bdd9f618730f195f7f1")
#
tx_out_count    = (1).to_bytes(1, byteorder="little", signed=False)

pk_script_one        = bytes.fromhex('a91487b16bf5c5e43bf1dbd69440556f4f5a1430b5fd87')
pk_script_bytes_one  = (len(pk_script_one)).to_bytes(1, byteorder="little", signed=False)
value_one            = int(0.0013 * 100000000).to_bytes(8, byteorder="little", signed=True)
tx_in_count          = (1).to_bytes(1, byteorder="little", signed=False)
index                = (1).to_bytes(4, byteorder="little", signed=False)
sequence             = bytes.fromhex('ffffffff')
lock_time            = (0).to_bytes(4, byteorder="little", signed=False)
amount               = (int(0.00135501 * 100000000).to_bytes(8, byteorder="little", signed=True))

tx_out = (
    value_one
    + pk_script_bytes_one
    + pk_script_one
)

import hashlib
import ecdsa
signing_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1) # Don't forget to specify the curve

version     = (1).to_bytes(4, byteorder="little", signed=False)
previous_output = hash + index

raw_tx = (
    version
    + tx_in_count
    + previous_output
    + bytes.fromhex('00') # sighash
    + sequence
    + tx_out_count
    + tx_out
    + lock_time
)

print("RAW: " + raw_tx.hex())

hash_type = bytes.fromhex('01000000')

def dSHA256(raw):
    hash_1 = hashlib.sha256(raw).digest()
    hash_2 = hashlib.sha256(hash_1).digest()
    return hash_2

hashPrevouts = dSHA256(previous_output)
hashSequence = dSHA256(sequence)
hashOutputs  = dSHA256(tx_out)

verifying_key = signing_key.get_verifying_key()

# Use this code block if the address you gave corresponds to the compressed public key
x_cor = bytes.fromhex(verifying_key.to_string().hex())[:32] # The first 32 bytes are the x cordinate
y_cor = bytes.fromhex(verifying_key.to_string().hex())[32:] # The last 32 bytes are the y cordinate
if int.from_bytes(y_cor, byteorder="big", signed=True) % 2 == 0: # We need to turn the y_cor into a number. 
    public_key = bytes.fromhex("02" + x_cor.hex())
else:
    public_key = bytes.fromhex("03" + x_cor.hex())


sha256_1 = hashlib.sha256(public_key)

ripemd160 = hashlib.new("ripemd160")
ripemd160.update(sha256_1.digest())

keyhash = ripemd160.digest()
redeemScript = bytes.fromhex(f'0014{keyhash.hex()}')
scriptcode = bytes.fromhex(f'76a914{keyhash.hex()}88ac') # This is the classic P2PKH scriptPubKey
hash_pre = (
    version
    + hashPrevouts
    + hashSequence
    + previous_output
    + (len(scriptcode).to_bytes(1, byteorder="little", signed=False))
    + scriptcode
    + amount
    + sequence
    + hashOutputs
    + lock_time
    + hash_type
)

sig_hash = dSHA256(hash_pre)
signature = signing_key.sign_digest(sig_hash, sigencode = ecdsa.util.sigencode_der_canonize) # The signature is alreasy specified in DER format!
witness = (
    (len(signature) + 1).to_bytes(1, byteorder="little", signed=False)
    + signature
    + bytes.fromhex("01")
    + (len(public_key)).to_bytes(1, byteorder="little", signed=False)
    + public_key
)

ser_tx = (
    version
    + bytes.fromhex('00') # marker
    + bytes.fromhex('01') # flag
    + tx_in_count
    + previous_output
    + (len(redeemScript)+1).to_bytes(1, byteorder="little", signed=False)
    + (len(redeemScript)).to_bytes(1, byteorder="little", signed=False)
    + redeemScript
    + sequence
    + tx_out_count
    + tx_out
    + (2).to_bytes(1, byteorder="little", signed=False)
    + witness
    + lock_time
)

print ("hashOutputs: "  + hashOutputs.hex())
print ("hashSequence: " + hashSequence.hex())
print ("hashPrevouts: " + hashPrevouts.hex())
print ("HASHED_PRE: "   + hash_pre.hex())
print ("Ser: "          + ser_tx.hex())