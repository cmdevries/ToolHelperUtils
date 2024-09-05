import importlib.abc
import sys


class StopItImportHook(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    BAD_IDEAS = (
        "tool",
        "helper",
        "util",
        "factory",
        "builder",
    )

    def find_module(self, fullname, path=None):
        if any(x in fullname.lower() for x in BAD_IDEAS):
            raise ImportError("stop it")
        return None

    def find_spec(self, fullname, path=None, target=None):
        return self.find_module(fullname)


sys.meta_path.insert(0, StopItImportHook())
