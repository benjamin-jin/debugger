# Python Debugger
When developping programs in Python, you may use `print` for debug your program. However, when to release your program you need to delete those `print` lines.

With this debugger, you do not need to remove all the debug lines.
```
setLevel("debug")
debug("hi")         # hi printed out

setLevel("info")
debug("hi")         # hi does not print out
```

# Debug Levels
- quite   : Does not print anything except error
- info    : Print `info` and `error`
- verobse : print `info`, `warn` and `error`
- debug   : print `debug`, `info`, `warn` and `error`

