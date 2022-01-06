Running the tests with pytest
```
(venv) Iqbals-MBP:stateless_examples afrobeard$ pytest test_matrix.py --hypothesis-show-statistics
================================================================================ test session starts =================================================================================
platform darwin -- Python 3.9.0, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /Users/afrobeard/PycharmProjects/rule_based_testing/stateless_examples
plugins: hypothesis-5.43.4
collected 3 items                                                                                                                                                                    

test_matrix.py ...                                                                                                                                                             [100%]
=============================================================================== Hypothesis Statistics ================================================================================

test_matrix.py::test_rotate_commutative:

  - during reuse phase (0.00 seconds):
    - Typical runtimes: ~ 2ms, ~ 53% in data generation
    - 1 passing examples, 0 failing examples, 0 invalid examples

  - during generate phase (0.21 seconds):
    - Typical runtimes: 0-2 ms, ~ 63% in data generation
    - 99 passing examples, 0 failing examples, 0 invalid examples

  - Stopped because settings.max_examples=100


test_matrix.py::test_shape_preserved:

  - during reuse phase (0.00 seconds):
    - Typical runtimes: ~ 1ms, ~ 47% in data generation
    - 1 passing examples, 0 failing examples, 0 invalid examples

  - during generate phase (0.19 seconds):
    - Typical runtimes: 0-1 ms, ~ 64% in data generation
    - 99 passing examples, 0 failing examples, 0 invalid examples

  - Stopped because settings.max_examples=100


test_matrix.py::test_quad_rotate:

  - during reuse phase (0.00 seconds):
    - Typical runtimes: ~ 1ms, ~ 39% in data generation
    - 1 passing examples, 0 failing examples, 0 invalid examples

  - during generate phase (0.20 seconds):
    - Typical runtimes: 0-1 ms, ~ 62% in data generation
    - 99 passing examples, 0 failing examples, 0 invalid examples

  - Stopped because settings.max_examples=100


================================================================================= 3 passed in 0.78s ==================================================================================
```