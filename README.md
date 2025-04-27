# Digital-signature-verification-in-a-multi-client-environment
This project simulates the working of **digital signatures** in a **multi-client environment** using the **BLS (Boneh–Lynn–Shacham) signature scheme** from the `py_ecc.bls.ciphersuites` library.

It demonstrates:
- **Key generation** for multiple clients.
- **Digital signature creation** by clients.
- **Signature verification** by the server.
- **Simulated communication** between clients and server in a secure environment.

## Project Overview

This project explores the use of BLS digital signatures to ensure authentication and integrity in a system where multiple clients interact with a server.

Each client:
- Generates their own key pair (private and public keys).
- Signs a message using their private key.
- Sends the signed message to the server.

The server:
- Verifies the authenticity of each message using the corresponding public key.

## Features

- Key pair generation for multiple clients.
- Digital signature generation using BLS.
- Secure message signing.
- Signature verification to ensure message authenticity.
- Simulated multi-client to server interaction.

## Technologies Used

- Python 3
- `py_ecc` library (`py_ecc.bls.ciphersuites`)
- BLS signature scheme

## How to Run

1. Install dependencies:
   ```bash
   pip install py_ecc
   ```
2. Run the simulation:
   ```bash
   python digital_signature_simulation.py
   ```

## Note

The BLS signature scheme provides **short, efficient, and secure digital signatures** ideal for distributed and multi-client systems like blockchains and decentralized networks.


