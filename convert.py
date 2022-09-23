import base58
byte_array = base58.b58decode("private_key_hash")
json_string = "[" + ",".join(map(lambda b: str(b), byte_array)) + "]"
print(json_string)