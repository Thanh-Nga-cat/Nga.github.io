def rsa_encrypt(message, p, q, e):
    n = p * q
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

message = "NguyenThiThanhNga"
p, q, e = 17, 23, 5

encrypted_text = rsa_encrypt(message, p, q, e)
print("Mã hóa thành công:", encrypted_text)
