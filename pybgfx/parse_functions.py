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
    for i in range(0, len(func.args)):
        arg = func.args[i]
        arg_type = arg.replace("_s", "").replace("_t", "")
        if arg_type.startswith("bgfx") == False:
            arg_type = "c_" + arg_type
        if "*" in arg_type:
            arg_type = "POINTER(" + arg_type.replace("*", "") + ")"
        arg_string += arg_type
        if i < len(func.args) - 1:
            arg_string += ", "
    print("\targs=[{}],".format(arg_string))
    return_type = "None"
    if func.restype != "void":
        return_type = "c_" + func.restype.replace("_s", "").replace("_t", "")
    print("\treturns={})".format(return_type))
    print("")