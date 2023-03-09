import dis

# Load the bytecode from the compiled module
with open('hidden_4.pyc', 'rb') as f:
    magic = f.read(4)
    timestamp = f.read(4)
    code = f.read()

# Disassemble the bytecode
instructions = list(dis.get_instructions(code))

# Extract the names from the disassembled instructions
names = set()
for inst in instructions:
    if inst.opname == 'LOAD_CONST' and isinstance(inst.argval, str) and not inst.argval.startswith('__'):
        names.add(inst.argval)

# Print the names in alphabetical order
for name in sorted(names):
    print(name)
