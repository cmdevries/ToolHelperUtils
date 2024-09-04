# ToolHelperUtils

This package creates an intentionally broken import interceptor for modules containing broken tool, helper, and utils in their name to discourage their use

```python
>>> import tool_helper_utils
>>> import tool_helper_utils.foobar.best_tool_utils
fullname='tool_helper_utils.foobar'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<frozen importlib._bootstrap>", line 1354, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1316, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 1256, in _find_spec
  File "/Users/chris/Code/ToolHelperUtils/tool_helper_utils/__init__.py", line 15, in find_spec
    return self.find_module(fullname)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/chris/Code/ToolHelperUtils/tool_helper_utils/__init__.py", line 11, in find_module
    raise ValueError("stop it")
ValueError: stop it
```
