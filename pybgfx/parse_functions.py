class Function():
    def __init__(self, name, restype, args):
        self.name = name
        self.restype = restype
        self.args = args

functions = []
with open("functions.txt") as f:
    for line in f:
        return_type = line[0:line.find(" ")]
        function_name = line.split("(")[0].split(" ")[1]
        args = line[line.find("(")+1:-3].replace("const", "").replace("struct", "").split(",")

        arg_types = []
        for arg in args:
            arg_types.append(arg.strip().split(" ")[0])
        functions.append(Function(function_name, return_type, arg_types))

for func in functions:
    print("{} = _bind(\"{}\",".format(func.name.replace("bgfx_", ""), func.name))
    arg_string = ""
    for arg in func.args:
        arg_string += arg.replace("_s", "").replace("_t", "").replace("*", "") + ", "
    print("\targs=[{}],".format(arg_string))
    print("\treturns=None)")
    print("")