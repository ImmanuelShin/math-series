import pytest
from series.series import fibonacci, lucas, sum_series

def test_fib_zero():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_fib_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected
  
def test_fib_two():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_fib_seven():
  actual = fibonacci(7)
  expected = 13
  assert actual == expected

def test_luc_one():
  actual = lucas(1)
  expected = 2
  assert actual == expected

def test_luc_two():
  actual = lucas(2)
  expected = 1
  assert actual == expected

def test_luc_seven():
  actual = lucas(7)
  expected = 18
  assert actual == expected

def test_sumf_seven():
  actual = sum_series(7)
  expected = 13
  assert actual == expected

def test_suml_seven():
  actual = sum_series(7, 2)
  expected = 18
  assert actual == expected