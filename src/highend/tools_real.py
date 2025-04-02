import src.highend.gpt_chain as gchain
from functools import wraps

class ArgParser:
    @staticmethod
    def parse(
        arg: str,
        data_type: str
    ):
        data_type = data_type.lower().strip()
        if data_type == "undefined":
            return arg
        elif data_type == "number":
            return float(arg)
        elif data_type == "string":
            return str(arg)
        elif data_type.startswith("list["):
            return [ArgParser.parse(item, data_type[5:-1]) for item in arg.split(",")]
        elif data_type.startswith("tuple["):
            types = [i for i in data_type[6:-1].split(',')]
            return tuple(ArgParser.parse(arg.split(',')[i], types[i]) for i in range(len(arg.split(","))))

        raise ValueError(f"Unsupported data type: {data_type}")

class RealTools:
    def __init__(self):
        self.tool_callbacks = {}

    def callback(self, argument):
        def decorator(function):
            self.tool_callbacks[argument] = function
            
            @wraps(function)
            def wrapper(*args, **kwargs):
                retval = function(*args, **kwargs)
                return retval
            return wrapper
        return decorator
    
    def run(self, ans: str):
        parsed = gchain.LLMParse.parse(ans)
        print(parsed)

        for tool_name, tool_handler in self.tool_callbacks.items():
            if tool_name in parsed:
                tool_handler(parsed[tool_name])