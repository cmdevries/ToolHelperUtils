# ToolHelperUtils

This package creates intentionally broken tools, helpers, and utils packages
to discourage their use.

```python
>>> import helpers
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "ToolHelperUtils/helpers/__init__.py", line 4, in <module>
    f()
  File "ToolHelperUtils/helpers/__init__.py", line 2, in f
    f()
  File "ToolHelperUtils/helpers/__init__.py", line 2, in f
    f()
  File "ToolHelperUtils/helpers/__init__.py", line 2, in f
    f()
  [Previous line repeated 990 more times]
RecursionError: maximum recursion depth exceeded
```
