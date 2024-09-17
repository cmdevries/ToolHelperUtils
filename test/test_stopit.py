import pytest
def test():
	import tool_helper_utils
	with pytest.raises(ImportError)as A:import helper
	with pytest.raises(ImportError)as A:import tool_helper_utils.foobar.best_tools