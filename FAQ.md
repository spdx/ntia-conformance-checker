Q: I am having trouble installing the python modules. What gives?

A: It could be due to using an OS package manager (like `apt`) to install
`pipenv` rather than using `pip`. Please try using `pip`.
Additionally, please ensure that `pipenv` is available in your path.
See issue #49 for an example of related error output and further
information.