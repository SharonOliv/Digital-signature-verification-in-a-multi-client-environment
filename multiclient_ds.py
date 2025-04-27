from py_ecc.bls.ciphersuites import G2ProofOfPossession as bls

# Simulate multiple clients
class Client:
    def __init__(self, client_id):
        self.client_id = client_id
        self.sk = bls.KeyGen(bytes(f"seed_{client_id}", 'utf-8'))
        self.pk = bls.SkToPk(self.sk)

    def sign_message(self, message: bytes):
        signature = bls.Sign(self.sk, message)
        print(f"[Client{self.client_id}] Signing message: {message.decode()}")
        print(f"[Client{self.client_id}] Signature (hex): {signature.hex()[:64]}...")  # Truncated for readability
        return signature

    def get_public_key(self):
        return self.pk

    def __repr__(self):
        return f"Client{self.client_id}"

# Verifier
class Verifier:
    @staticmethod
    def verify_signature(pk, message, signature):
        print(f"→ Verifying signature with public key {pk.hex()[:64]}...")  # Truncated
        is_valid = bls.Verify(pk, message, signature)
        print(f"Result: {'Valid ' if is_valid else 'Invalid '}")
        return is_valid

# Take message input
message = input("Enter the message to be signed: ").encode()

# Create multiple clients
clients = [Client(i) for i in range(1, 6)]

# Clients sign the message
signatures = []
print("\nSigning Phase:\n")
for client in clients:
    sig = client.sign_message(message)
    signatures.append((client, client.get_public_key(), sig))

# Verify each signature
print("\nVerification Phase:\n")
verifier = Verifier()
for client, pk, sig in signatures:
    print(f"\nVerifying signature from {client}:")
    verifier.verify_signature(pk, message, sig)
