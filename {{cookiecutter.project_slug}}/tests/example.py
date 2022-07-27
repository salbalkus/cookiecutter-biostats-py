# Test examples from https://docs.pytest.org/en/7.1.x/getting-started.html#get-started
# Note that all tests must be prefixed with "test_" and the class must be prefixed with "Test".


class TestClass:
	def test_one(self):
        	x = "this"
        	assert "h" in x

	def test_two(self):
        	x = "hello"
        	assert hasattr(x, "check")

	# Use the following function to indicate resources are needed from a specific directory.
	def test_needsfiles(tmp_path):
    		print(tmp_path)
    		assert 0

# Run tests using `pytest example.py` or `pytest -q test_class.py`