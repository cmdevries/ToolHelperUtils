import importlib.abc,sys
class AbstractBaseFactoryFactory:
	def build():0
class FactoryFactory(AbstractBaseFactoryFactory):
	def __init__(A,factory):A.factory=factory
	def build(A):return A.factory.get_bad_idea()
class FactoryBadIdea:
	def get_bad_idea(A):return'factory'
class StopItImportHook(importlib.abc.MetaPathFinder,importlib.abc.Loader):
	BAD_IDEAS='tool','helper','util',FactoryFactory(FactoryBadIdea()).build(),'builder'
	def find_module(A,fullname,path=None):
		if any(A in fullname.lower()for A in A.BAD_IDEAS):raise ImportError('stop it')
	def find_spec(A,fullname,path=None,target=None):return A.find_module(fullname)
sys.meta_path.insert(0,StopItImportHook())