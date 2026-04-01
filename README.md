# August Cipher & Custom Hash Implementation

## 1. Theory

### August Cipher
The August Cipher is a monoalphabetic substitution cipher based on the Caesar Cipher. 
* **Key:** Fixed shift of `1`.
* **Encryption:** Each letter is replaced by the next letter in the alphabet (A → B, B → C).
* **Decryption:** Each letter is replaced by the preceding letter (B → A, C → B).
* **Constraints:** Non-alphabetic characters (numbers, spaces, punctuation) are preserved without modification.

### Custom Hash Function
The hashing function produces a **32-bit hash value**. It uses:
1. **Polynomial Bases:** A rotating set of prime bases (`17, 29, 13, 37`) to ensure that character position affects the outcome and reduce the likelihood of collisions.
2. **Bitwise Operations:** Shifting (`<<`) and XOR (`^`) operations are applied to avoid collisions between similar strings.
3. **Fixed-Size Output:** The result is masked to **32 bits** and formatted as an **8-character hexadecimal string**, allowing the receiver to precisely identify the hash at the end of any transmitted message.
4. **Deterministic Output:** The same input always produces the same hash value.

---

## 2. How to Run

1. **Clone the repository:**
   * Open your terminal and run:
   ```bash
   git clone https://github.com/Sr1v1dhya/Cryptography-CIA.git

2. **Navigate to the project directory:**
    ```bash
    cd Cryptography-CIA

3. **Run the test script:**
    * Ensure you have Python 3 installed, then execute:
    ```bash
    python3 august.py

---

## 3. Worked Examples

### Example 1: 
* **Original Message:** `AUGUSTCIPHER`
* **Key:** `1`
* **Ciphertext:** `BVHVTUDJQIFS`
* **Hash (Hex):** `34763a36`
* **Final Transmitted Message:** `BVHVTUDJQIFS34763a36`

### Example 2: 
* **Original Message:** `SNUCHENNAI`
* **Key:** `1`
* **Ciphertext:** `TOVDIFOOBJ`
* **Hash (Hex):** `f662faa4`
* **Final Transmitted Message:** `TOVDIFOOBJf662faa4`

---

## 4. Test Script: Encrypt → Hash → Decrypt Round-Trip

This includes a simulation of the "Sender-Receiver" communication model.

### The Sender
The `sender()` function takes the raw plaintext and performs the following:
1. Calls `Augustencrypt()` to shift the characters by 1.
2. Passes the resulting ciphertext into the `hash()` function.
3. Appends the 8-character hex hash to the end of the ciphertext to create the final "packet."

### Transmission
The message is treated as a single string. Because the hash is fixed at 8 characters, no special delimiters are needed between the data and the hash.

### The Receiver
The `receiver()` function simulates the arrival of the message:
1. **Slicing:** It uses Python slicing (`message[:-8]` and `message[-8:]`) to separate the suspected ciphertext from the hash.
2. **Integrity Check:** It re-computes the hash of the received ciphertext.
3. **Verification:**
    * If `computed_hash == received_hash`, the console prints **"Message verified"** and proceeds to decrypt.
    * If they do not match (indicating the message was tampered with during transmission), it prints **"Message tampered"**.

---
