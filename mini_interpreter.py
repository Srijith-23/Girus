def mini_interpreter(code):
    variables = {}

    lines = code.strip().split(';')
    for line in lines:
        line = line.strip()
        if line.startswith("let"):
            _, var, eq, val = line.split()
            variables[var] = int(val)
        elif line.startswith("if"):
            cond, then = line[3:].split('then')
            var, op, num = cond.strip().split()
            num = int(num)
            if op == '==':
                if variables[var] == num:
                    print("=>", then.strip())
            elif op == '!=':
                if variables[var] != num:
                    print("=>", then.strip())

# 🧪 Test
code = """
let x = 5;
if x == 5 then print("x is five");
if x != 3 then print("x is not three");
"""
mini_interpreter(code)
# Output:
# => print("x is five")
# => print("x is not three")
