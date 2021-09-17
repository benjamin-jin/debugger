# debugger
Enable / Disable `print` for global level

# Usage Example
```python3
debug.debug("HI")             # "HI" is printed
debug.setLevels("info")       # set debugLevel as INFO
debug.debug("HI")             # "HI" is not printed
```

# Debug levels
> quiet : Do not print except `error`

> info : Print only `error` and `info` message

> verbose : Print only `error`, `info`, `warn` message

> debug : Print only `error`, `info` `warn`, `debug` message

# Syntax Sugar for `debug`
You may not need type `debug.debug(message)` for print `debug-level` message. Just write `debug(message)`.
