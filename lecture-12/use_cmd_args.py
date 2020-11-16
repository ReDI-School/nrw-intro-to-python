import sys

cmd_args = sys.argv

print(cmd_args)

if len(cmd_args) == 2:
    print("Hello", cmd_args[1])

if len(cmd_args) == 3:
    print("Hello", cmd_args[1], "and", cmd_args[2])

if len(cmd_args) >= 4:
    print("Hello "+ ", ".join(cmd_args[1:-2]) + ", " + cmd_args[-2] + " and " + cmd_args[-1])
