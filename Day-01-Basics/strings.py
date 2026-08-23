message = 'hello world'
print(len(message))
print(message[0])
print(message[4])
print(message[5])
print(message[10])
print(message[0:5])
print(message[1:7])
print(message.upper())
print(message.count('l'))
print(message.count('o'))
print(message.find('world'))
print(message.find('hello'))
print(message.find('universe'))
new_message = message.replace('world','universe')
print(new_message)
greeting = 'Hello'
name = 'World'
message = '{}, {}' .format(greeting,name)
print(message)
message = f'{greeting},{name.upper()}.'
print(message)
print(dir(name))
print(help(str))