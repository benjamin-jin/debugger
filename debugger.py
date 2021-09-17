def helper(value: int):
  return f"\033[{value}m"

class colors:
  RESET       = helper(0)
  BOLD        = helper(1)
  UNDERLINE   = helper(4)

  RED         = helper(91)
  GREEN       = helper(92)
  YELLOW      = helper(93)
  BLUE        = helper(94)
  PURPLE      = helper(95)
  CYAN        = helper(96)


class debug:
  debugLevels = ["quiet","info","verbose", "debug"]
  level = "debug"
  @classmethod
  def setLevel(cls, level):
    if level in cls.debugLevels:
      cls.level = level

  def __init__(self, *args):
    text = self.make(args)
    if self.level == "debug":
      self.debug(text)
  @classmethod
  def info(cls, *args):
    if cls.debugLevels.index("info") <= cls.debugLevels.index(cls.level):
      if type(args) == str:
        return cls.print("info", args)
      else:
        return cls.print("info", cls.make(args))
  @classmethod
  def debug(cls, *args):
    if cls.debugLevels.index("debug") <= cls.debugLevels.index(cls.level):
      if type(args) == str:
        return cls.print("debug", args)
      else:
        return cls.print("debug", cls.make(args))
  @classmethod
  def warn(cls, *args):
    if cls.debugLevels.index("verbose") <= cls.debugLevels.index(cls.level):
      if type(args) == str:
        return cls.print("warn", args)
      else:
        return cls.print("warn", cls.make(args))

  @classmethod
  def error(cls, *args):
    if cls.debugLevels.index("quiet") <= cls.debugLevels.index(cls.level):
      if type(args) == str:
        return cls.print("error", args)
      else:
        return cls.print("error", cls.make(args))

  @classmethod
  def print(cls, level : str, text : str):
    message = f"{level.upper()} :: {text}"
    if level == "error":
      print(colors.RED + f"{message}" + colors.RESET)
    elif level == "warn":
      print(colors.YELLOW + f"{message}" + colors.RESET)
    elif level == "debug":
      print(colors.PURPLE + message + colors.RESET)
    else:
      print(colors.GREEN + message + colors.RESET)
    return 0

  @classmethod
  def make(cls, args):
    args = [str(each) for each in args]
    return " ".join(args)
  @classmethod
  def test(cls, target = True, expected = None, method = "==", text: str = ""):
    if type(target) != bool and expected != None:
      if method == "!=" or method.startswith("dif"):
        method = "!="
        condition = target != expected
      elif method == "in":
        try:
          condition = expected in target
        except TypeError:
          condition = None
          debug.error(f"target {target} is type of {type(target)}, which is not iterable")
      else:
        condition = target == expected
      text = f"{text} =>" if text != "" else f"Testing {target} {method} {expected} =>"
    else:
      condition = target
      text = "" if text == "" else f"{text} "
      text = f"Simple Testing : {text}=>"
    if condition != None:
      answer = "True" if condition else "False"
      cls.debug(f"{text} {answer}")