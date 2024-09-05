import importlib.abc
import sys


class AbstractBaseFactoryFactory:
    def build():
        return None


class FactoryFactory(AbstractBaseFactoryFactory):
    def __init__(self, factory):
        self.factory = factory

    def build(self):
        return self.factory.get_bad_idea()
       

class FactoryBadIdea:
    def get_bad_idea(self):
        return "factory"


class StopItImportHook(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    BAD_IDEAS = (
        "tool",
        "helper",
        "util",
        FactoryFactory(FactoryBadIdea()).build(),
        "builder",
    )

    def find_module(self, fullname, path=None):
        if any(x in fullname.lower() for x in self.BAD_IDEAS):
            raise ImportError("stop it")
        return None

    def find_spec(self, fullname, path=None, target=None):
        return self.find_module(fullname)


sys.meta_path.insert(0, StopItImportHook())
