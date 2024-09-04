import importlib.abc
import importlib.machinery
import sys


class StopItImportHook(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_module(self, fullname, path=None):
        print(f"{fullname=}")
        if "tools" in fullname.lower() or "helper" in fullname.lower() \
            or "utils" in fullname.lower():
            raise ValueError("stop it")
        return None

    def find_spec(self, fullname, path=None, target=None):
        return self.find_module(fullname)

sys.meta_path.insert(0, StopItImportHook())
