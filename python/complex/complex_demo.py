import complex_pb2

complex_message = complex_pb2.ComplexMessage()

# Wrong
# one_dummy_message = complex_message.DummyMessage()
# one_dummy_message.id = 123
# one_dummy_message.name = "I am a dummy message"

one_dummy_message = complex_pb2.DummyMessage()
one_dummy_message.id = 333
one_dummy_message.name = "I am a dummy message"
print(one_dummy_message)
print("=" * 70)

complex_message.one_dummy.id = 123
complex_message.one_dummy.name = "hello ss"

print(complex_message)
print("=" * 70)

first_multiple_dummy = complex_message.multiple_dummy.add()
first_multiple_dummy.id = 456
first_multiple_dummy.name = "你好呀"
print(complex_message)
print("=" * 70)

complex_message.multiple_dummy.add(id=789, name="!!!!!!!")
print(complex_message)
print("=" * 70)

third_dummy_message = complex_pb2.DummyMessage()
third_dummy_message.id = 100
third_dummy_message.name = "baconyao latest"
# extend 是 reference type (copy一份)
complex_message.multiple_dummy.extend([third_dummy_message])
# 所以儘管下列 assign 新的值，依然不會改變已經被 extend 的值
third_dummy_message.id = 111
print(complex_message)
