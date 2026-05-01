# private key = d
# public key = (n,e)



d=13
(n,e) = (77,37)
m = 2

encrypt = m**e % n
decrypt = m = encrypt**d % n

print(encrypt)
print(decrypt)


## breaking RSA (under certain conditions)

#bobs public encyptionkey is (n,e) = (629, 17)

(n,e) = (629, 17)

m = ord('A')
c = m**e % n
print(f'Bobs Ciphertext is {c}')
