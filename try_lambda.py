def execute_param_fn(args, hosei, fn):
    result = fn(args, hosei)
    return result

a = [1, 2, 3]
b = 4
print(execute_param_fn(a, b, lambda args, hosei: max(args) + hosei))
print(execute_param_fn(a, b, lambda args, hosei: min(args) - hosei))