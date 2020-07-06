import simple_pb2

# 實例一個 SimpleMessage
simple_message = simple_pb2.SimpleMessage()
simple_message.id = 123
simple_message.is_simple = True
simple_message.name = "ABC-測試簡單～"
print(simple_message)
print("=" * 50)

# 陣列
simple_list = simple_message.sample_list
print(simple_list)
# 填值進陣列
simple_list.append(3)
simple_list.append(4)
simple_list.append(5)
print(simple_list)
print("=" * 50)

# 寫檔 (一定要使用 wb，因為 protobuf 是 binary)
with open("simple.bin", "wb") as f:
    print("Write as Binary")
    byteAsString = simple_message.SerializeToString()
    f.write(byteAsString)

with open("simple.bin", "rb") as f:
    print("Read values")
    message_read = simple_pb2.SimpleMessage().FromString(f.read())

print(message_read)

print("=" * 50)
print(message_read.is_simple)
message_read.id = 456
print(message_read.id)
