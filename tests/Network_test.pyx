""" Create Fully Specified Network From Input Data """

# distutils: language=c++
# distutils: extra_compile_args=-std=c++11

from tests.cytest_wrapper import cytest
from aco_mtsp import Network

@cytest
def test_basic():
    assert Network.basicfunc(1) == 1
