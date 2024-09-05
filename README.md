# ToolHelperUtils

This package creates an intentionally broken import interceptor for symbols containing anti-patterns

```python
>>> import tool_helper_utils
>>> import helper
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/chris/Code/ToolHelperUtils/tool_helper_utils/__init__.py", line 20, in find_spec
    return self.find_module(fullname)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/chris/Code/ToolHelperUtils/tool_helper_utils/__init__.py", line 16, in find_module
    raise ImportError("stop it")
ImportError: stop it
>>> import tool_helper_utils.foobar.abstract.factory.pattern.best_util_builder_yet
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/chris/Code/ToolHelperUtils/tool_helper_utils/__init__.py", line 20, in find_spec
    return self.find_module(fullname)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/chris/Code/ToolHelperUtils/tool_helper_utils/__init__.py", line 16, in find_module
    raise ImportError("stop it")
ImportError: stop it
```
