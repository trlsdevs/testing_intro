## Testing intro
The repo contain code for testing learning purpose only.\
All the test execution based TOX and Pytest

TOX - https://tox.wiki/en/latest/ \
Pytest  - https://docs.pytest.org/en/7.2.x/

This repo contain 3 tests sections
1. Unit tests - this section show by example to way to write and execution function based and class based unit tests 
2. Integration tests - this section show by example the tests in web framework such as Django \
   this section a Task app called "Manyana" and used a platform for the tests
3. E2E Test  -  


To execute and run the tests follow the next steps

### Unit tests
1. Enter to folder `cd unit_testing`
2. run `tox -e class` to execute class based tests
3. run `tox -e funct` to execute functions based tests.
4. run `tox -e all` to execute all tests.

### Unit tests
1. Enter to folder `cd integrations_testing`
2. run `tox -e app` to execute class based tests

### E2E tests
1. Enter to folder `cd e2e_testing`
2. run `tox -e screen` to execute screen compare test
3. run `tox -e app` to execute to do app E2E