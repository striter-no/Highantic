from src.highend.xml_parsing import *
import uuid

class BasicToolSpec:
    def __init__(self):
        self.basic_prompt = """
# Basic Rule

You are an AI that must be pedantic about your tasks and follow clear design rules. You will be punished very severely for not following the rules.

## UUID

In requests you will find the UUID field. Do not include this UUID in your responses.

## Formatting

Do not use the "```" from the examples in your response. That means that you should not use the ``` wrapping around your response. It is STRICTLY FORBIDDEN.

If the information in the example is in the form “$(information)”, then you replace the entire “$(information)” block with whatever you think you need in the current context.

If the information isn't wrapped in that design, then you're obligated to use it without changing it.

You SHOULD USE ONLY xml formatting, without Markdown, and you CAN use Markdown syntax INSIDE blocks/tags.

## Supplements

### Tools

You use a number of tools for your work. Formatting a response using a tool:

```example
<$(instrument_name)>
$(Output of the instrument...)
</$(instrument_name)>
```

Each tool should be used explicitly in those situations where it is necessary and specified in the **requirements**.

### WARNING

You need to use EACH tools STRICTLY SEPARETLY, NOT NESTED. There are examples:

WRONG, do NOT follow this:
```wrong-example
<tool1>
This is wrong Bla-bla...
<tool2>
This is wrong More bla-bla...
</tool2>
</tool1>
```

RIGHT, strictly follow this pattern:
```right-example
<tool1>
Bla-bla...
</tool1>
<tool2>
More bla-bla...
</tool2>
```

THEY ARE NO USAGE EXAMPLES FOR NESTED TOOLS. ONLY SUB-TOOLS can BE NESTED in MAIN tools.

#### Sub-tools

Each tool can have a number of sub-tools. Sub-tools are needed if any parameters are required for an additional tool.

Sub-tools will be specified in the description of the main parameter, and if they are NOT specified you are obliged NOT to use them.

When using sub-tools, you specify the main tool's response in the `main` sub-tag, and after the `main` tag, the sub-tool tags

A sub-tool can be of data type:

1. `undefined` - The data type is arbitrary
2. `number` - The number in the response is
3. `string` - In the response a string of text
4. `list[...]` - A list of the above data types (no limit to the number of elements)
5. `tuple[..., ...]` - A tuple of the above data types (limited number of elements)

Example of using a tool with sub-tools (`resolution` - data type `tuple[number, number]`):

```example
<$(image_gen)>
<main>$(Generate an image of a car)</main>
$(<resolution>1000, 1000</resolution)>)
<$(/image_gen)>
```

The content of the main body of the any tool MAY be empty

#### Tool Descriptions
"""

class SubTool:
    def __init__(
        self,
        name: str,
        description: str,
        data_type: str,
        use_requirements: str
    ):
        self.name = name
        self.description = description
        self.data_type = data_type
        self.use_requirements = use_requirements

class Tool:
    def __init__(
        self, 
        name: str,
        use_requirements: str,
        purposes: str,
        description: str,
        examples: list[str] = [],
        subtools: list[SubTool] = []
    ):
        self.name = name
        self.use_requirements = use_requirements
        self.purposes = purposes
        self.description = description
        self.examples = examples
        self.subtools = subtools

    # TODO: examples
    def compile(self):
        out  = f"- Tool name: `{self.name}`\n"

        out += f"\t- **Requirements for use**:\n"
        out += f"\t\t{self.use_requirements}\n"

        out += f"\t- **Purpose of use**:\n"
        out += f"\t\t{self.purposes}\n"

        out += f"\t- **General description**:\n"
        out += f"\t\t{self.description}\n"

        if self.subtools != []:
            out += "\t- **Sub-tools**:\n"
            for sbt in self.subtools:
                out += f"\t\t- Sub-tool: `{sbt.name}`\n"
                out += f"\t\t\tData-type: {sbt.data_type}\n"
                out += f"\t\t\tDescription: {sbt.description}\n"
                out += f"\t\t\tUse-requirements: {sbt.use_requirements}\n"
        else:
            out += "\t- **Sub-tools**:\n\t\tNo sub-tools specified.\n"

        return out

class Salt:
    @staticmethod
    def add_salt(input_text: str) -> str:
        return f"{input_text}\n# UUID SECTION:\n--UUID--\n{uuid.uuid4()}\n--end--"

class Compiler:
    @staticmethod
    def compile(base: BasicToolSpec, tools: list[Tool]) -> str:
        out = base.basic_prompt

        for tool in tools:
            out += tool.compile() + "\n"

        return out
    
class LLMParse:
    @staticmethod
    def parse(answer: str):
        xml_info = xml_parse(answer)

        return xml_info