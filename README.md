# What is This?

A quick experiment on the latest state of IronPython/C# integration. Uses IronPython 2. (Binaries/releases for IronPython 3 are not yet available.)

The goal of this code was to evaluate: if I make a project that uses IronPython for all the script files, is there a way to achieve unit-testing on those Python scripts? (If not, we should just use Python integration as an interface, but keep everything in .NET code.)

# What Works?

Calling Python code from C#, and calling C# code (namespaces/methods) from Python; passing objects back and forth; writing Python tests for Python code.

# Notes on Testing

For the tests to work, a number of things happened:

- Downloaded and unzipped the latest IronPython 2.7.10 binaries into `ipy` (deleting the non-.NET-Core.3.1 files)
- From the console, go into the `SturdyParakeet` directory
- Run the command `dotnet ../ipy/netcoreapp3.1/ipy.dll test_hello_you.py`

This invokes .NET to run the .NET Core version of Iron Python, which takes in the file to execute, and runs it. Note that `unittest` is provided via `Lib`, which ships with IronPython.