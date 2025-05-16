
import sys

print("sys.argv =", sys.argv)

print("Number of arguments:", len(sys.argv))

for i, arg in enumerate(sys.argv):

    print(f"Argument {i}: {arg}")
