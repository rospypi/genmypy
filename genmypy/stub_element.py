import collections

from ._typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import DefaultDict, Iterator, List, Optional, Sequence, Set, Tuple

INDENT_SIZE = 4
FUNCTION_PARAM_MULTILINE_THRESHOLD = 70


def _indent(depth):
    # type: (int) -> str
    return " " * INDENT_SIZE * depth


def _format(content, depth):
    # type: (str, int) -> str
    return "{}{}".format(_indent(depth), content)


class ModuleElement:
    def __init__(self):
        # type: () -> None
        self.statements = []  # type: List[StatementElementBase]

    def add_element(self, statement):
        # type: (StatementElementBase) -> None
        self.statements.append(statement)

    def generate(self):
        # type: () -> Iterator[str]
        for statement in self.statements:
            for line in statement.generate(0):
                yield line


class StatementElementBase(object):
    def generate(self, indent):
        # type: (int) -> Iterator[str]
        raise NotImplementedError()


def _generate_imports(items, indent):
    # type: (DefaultDict[str, Set[Optional[str]]], int) -> Tuple[List[str], List[str]]
    imports = []  # type: List[str]
    from_imports = []  # type: List[str]
    for module, elements in sorted(items.items()):
        if None in elements:
            imports.append(_format("import {}".format(module), indent))

        names = [e for e in elements if e is not None]
        if len(names) == 0:
            continue

        joined = ", ".join(sorted(names))
        from_imports.append(_format("from {} import {}".format(module, joined), indent))

    return imports, from_imports


class ImportsElement(StatementElementBase):
    def __init__(self):
        # type: () -> None
        self._system_modules = collections.defaultdict(
            set
        )  # type: DefaultDict[str, Set[Optional[str]]]
        self._third_party_modules = collections.defaultdict(
            set
        )  # type: DefaultDict[str, Set[Optional[str]]]

    def add_system_module(self, module, name):
        # type: (str, Optional[str]) -> None
        self._system_modules[module].add(name)

    def add_third_party_module(self, module, name):
        # type: (str, Optional[str]) -> None
        self._third_party_modules[module].add(name)

    def generate(self, indent):
        # type: (int) -> Iterator[str]
        imports, from_imports = _generate_imports(self._system_modules, indent)
        for line in imports:
            yield line
        for line in from_imports:
            yield line

        if len(self._system_modules) > 0:
            yield ""

        imports, from_imports = _generate_imports(self._third_party_modules, indent)
        for line in imports:
            yield line
        for line in from_imports:
            yield line


class EmptyLinesElement(StatementElementBase):
    def __init__(self, lines=1):
        # type: (int) -> None
        self.lines = lines

    def generate(self, indent):
        # type: (int) -> Iterator[str]
        # NOTE: Do not use _format(...) for empty lines
        for _ in range(self.lines):
            yield ""


class CommentElement(StatementElementBase):
    def __init__(self, comment):
        # type: (str) -> None
        self.comment = comment

    def generate(self, indent):
        # type: (int) -> Iterator[str]
        for line in self.comment.splitlines():
            yield _format("# {}".format(line), indent)


class ClassElement(StatementElementBase):
    def __init__(self, name, base=None):
        # type: (str, Optional[str]) -> None
        self.name = name
        self.base = base
        self.members = []  # type: List[StatementElementBase]

    def add(self, member):
        # type: (StatementElementBase) -> None
        self.members.append(member)

    def generate(self, indent):
        # type: (int) -> Iterator[str]
        if self.base is not None:
            yield _format("class {}({}):".format(self.name, self.base), indent)
        else:
            yield _format("class {}:".format(self.name), indent)

        for m in self.members:
            for line in m.generate(indent + 1):
                yield line


class FieldElement(StatementElementBase):
    def __init__(self, name, type):
        # type: (str, str) -> None
        self.name = name
        self.type = type

    def generate(self, indent):
        # type: (int) -> Iterator[str]
        yield _format("{}: {}".format(self.name, self.type), indent)


class FunctionElement(StatementElementBase):
    def __init__(self, name, return_type, params=None):
        # type: (str, str, Optional[Sequence[ParameterElement]]) -> None
        self.name = name
        self.return_type = return_type
        self.params = []  # type: List[ParameterElement]

        if params is not None:
            self.params.extend(params)

    def add_parameter(self, param):
        # type: (ParameterElement) -> None
        self.params.append(param)

    def generate(self, indent):
        # type: (int) -> Iterator[str]
        param_expression = ""

        params = [p.generate_expression() for p in self.params]
        total_length = sum(len(e) for e in params)
        if total_length > FUNCTION_PARAM_MULTILINE_THRESHOLD:
            param_defs = ",\n".join(_format(p, indent + 1) for p in params)
            param_expression = "\n{},\n{}".format(param_defs, _format("", indent))
        else:
            param_expression = ", ".join(params)

        generated = _format(
            "def {}({}) -> {}: ...".format(
                self.name,
                param_expression,
                self.return_type,
            ),
            indent,
        )
        for line in generated.splitlines():
            yield line


class ClassMethodElement(FunctionElement):
    def __init__(self, name, return_type, params=None):
        # type: (str, str, Optional[Sequence[ParameterElement]]) -> None
        super(ClassMethodElement, self).__init__(name, return_type)
        self.add_parameter(ParameterElement("self", None))
        if params is not None:
            for p in params:
                self.add_parameter(p)


class ParameterElement:
    def __init__(self, name, type, has_default=False):
        # type: (str, Optional[str], bool) -> None
        self.name = name
        self.type = type
        self.has_default = has_default

    def generate_expression(self):
        # type: () -> str
        ret = str(self.name)
        if self.type is not None:
            ret = "{}: {}".format(ret, self.type)

        if self.has_default:
            ret = "{} = ...".format(ret)

        return ret
