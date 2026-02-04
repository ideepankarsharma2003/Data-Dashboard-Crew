from crewai_tools import BaseTool
import pandas as pd
import json
import io
import contextlib

class PythonInterpreterTool(BaseTool):
    name: str = "python_interpreter"
    description: str = (
        "Executes Python code for data analysis. "
        "The code MUST assign the final output to a variable named `result` "
        "which must be JSON-serializable."
    )

    def _run(self, code: str) -> str:
        local_vars = {}
        stdout = io.StringIO()

        try:
            with contextlib.redirect_stdout(stdout):
                exec(code, {"pd": pd, "json": json}, local_vars)

            if "result" not in local_vars:
                return "ERROR: Python code must define a `result` variable."

            return json.dumps(local_vars["result"])
        except Exception as e:
            return f"PYTHON_EXEC_ERROR: {str(e)}"
