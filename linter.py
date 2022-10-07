from cuda_lint import Linter
from cuda_lint.util import STREAM_STDERR

class QuickLintJs(Linter):
    syntax = ('JavaScript', 'JavaScript Babel')
    name = "quick-lint-js"
    cmd = "quick-lint-js -"
    regex = (
        r"^(?P<filename>.+?):(?P<line>\d+):(?P<col>\d+):\s"
        r"(?P<message>((?P<error>error:)|(?P<warning>warning:)).+)\s\[(?P<code>\w+)]"
    )
    error_stream = STREAM_STDERR
    