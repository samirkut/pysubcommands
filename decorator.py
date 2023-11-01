import functools

registered_cmds = {}

def subcommand(*a, **kw):
    global registered_cmd

    def decorator(func):
        name = func.__name__
        if a:
            name = a[0]

        if "help" not in kw:
            kw["help"] = func.__doc__
        args = kw.pop('args', [])
        registered_cmds[name]={'func':func.__name__, 'kwargs':kw, 'args':args}

        @functools.wraps(func)
        def fn(*args, **kwargs):
            print(f"{name} invoked")
            value = func(*args, **kwargs)
            return value

        return fn
    
    return decorator

def register_subcommands(subparsers):
    for name, d in registered_cmds.items():
        subparser = subparsers.add_parser(f, **d['kwargs'])
        for arg in d['args']:
            subparser.add_argument(**arg)

