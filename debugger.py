import datetime
import inspect
import traceback
import json
import os
from colors import *

_debugLevels = ["quiet","info","verbose", "debug"]
_currentLevel = "debug"
def setLevel(level : str) -> None:
  global _currentLevel
  if level in _debugLevels:
    _currentLevel = level
# API for debug print color

_data = {
  "INFO" : {
    "ansi" : {
      "fg" : "GREEN",
      "bg" : "",
      "style" : []
    },
    "prefixes" : ["{inspect}"],
    "postfixes" : []
  },
  "WARN" : {
    "ansi" : {
      "fg" : "YELLOW",
      "bg" : "",
      "style" : []
    },
    "prefixes" : ["{inspect}"],
    "postfixes" : []
  },
  "ERROR" : {
    "ansi" : {
      "fg" : "RED",
      "bg" : "",
      "style" : []
    },
    "prefixes" : [],
    "postfixes" : ["{trace}"]
  },
  "DEBUG" : {
    "ansi" : {
      "fg" : "BLUE",
      "bg" : "",
      "style" : []
    },
    "prefixes" : [],
    "postfixes" : []
  }
}
def saveConfigure(path : str = ".debug-setting.json") -> None:
  print(_data["DEBUG"]["prefixes"])
  with open(path, "w") as f:
    json.dump(_data, f, indent=4)
def loadConfigure(path : str = ".debug-setting.json") -> None:
  if os.path.isfile(path):
    with open(path) as f:
      data = json.load(f)
    for each in data:
      _data[each] = data[each]
# loadConfigure()
def setColorMap(input1, input2 = None):
  if type(input1) == dict:
    for each in input1.keys():
      setColorMap(each, input1[each])
  elif type(input1) == str and type(input2) == str:
    if input1.upper() in _data.keys() and input2.upper() in _colors.keys():
      _data[input1.upper()]["_colors"] = input2.upper()

# API for set commonMessage
# def setCommon(prefixes : list = list(), postfixes : list= list()) -> None:
#   for each in _data.keys():
#     _data[each]["prefixes"]  = prefixes  if len(prefixes) != 0 else _data[each]["prefixes"]
#     _data[each]["postfixes"] = postfixes if len(postfixes) != 0 else _data[each]["postfixes"]
# def editCommon(prefixes : list = list(), postfixes : list= list()) -> None:
#   for each in _data.keys():
#     _data[each]["prefixes"]  = _data[each]["prefxies"] + prefixes
#     _data[each]["postfixes"] = _data[each]["postfixes"] + postfixes
# def resetCommon() -> None:
#   for each in _data.keys():
#     _data[each]["prefixes"]  = list()
#     _data[each]["postfixes"] = list()

# def setprefixes(input1, input2 = None):
#   if type(input1) == dict:
#     for each in input1.keys():
#       setprefixes(each, input1[each])
#   elif type(input1) == str and type(input2) == str:
#     if input1.upper() in _data.keys():
#       _data[input1.upper()]["prefixes"] = _data[input1.upper()]["prefixes"].append(input2)
#       print(_data[input1.upper()]["prefixes"])
#   elif type(input2) == list:
#       _data[input1.upper()]["prefixes"] = input2

# def setpostfixes(input1, input2 = None):
#   if type(input1) == dict:
#     for each in input1.keys():
#       setpostfixes(each, input1[each])
#   elif type(input1) == str and type(input2) == str:
#     if input1.upper() in _data.keys():
#       _data[input1.upper()]["postfixes"] += input2
#   elif type(input1) == str and type(input2) == list:
#       _data[input1.upper()]["postfixes"] = input2

# Print Helper
def printHelper(level : str, text : str) -> None:
  prefixed = []
  for each in _data[level.upper()]["prefixes"]:
    if callable(each):
      prefixed.append(str(each()))
    else:
      prefixed.append(str(each))
  postfixed = []
  for each in _data[level.upper()]["postfixes"]:
    if callable(each):
      postfixed.append(str(each()))
    else:
      postfixed.append(str(each))
  messageFormat = [x for x in [" ".join(prefixed), text, " ".join(postfixed)] if x != ""]
  message = ": ".join(messageFormat)
  frame = inspect.getframeinfo(inspect.currentframe().f_back.f_back)
  message = message.replace("{level}", level.upper()).replace("{time}", str(datetime.datetime.now())).replace("{inspect}", "{}:{}".format(frame.filename,frame.lineno))
  message = message.replace("{trace}", traceback.format_exc())
  print(color(message, bg=_data[level.upper()]["ansi"]["bg"].lower(), style="+".join(_data[level.upper()]["ansi"]["style"]).lower(),fg=_data[level.upper()]["ansi"]["fg"].lower()))
  # print(_colors[_data[level.upper()]["_colors"].upper()] + message + _colors["RESET"])
# into string
def intoString(args) -> str:
  converted = []
  for each in args:
    if callable(each):
      converted.append(str(each()))
    else:
      converted.append(each)
  return " ".join(converted)

def debug(*args) -> None:
  if _debugLevels.index("debug") <= _debugLevels.index(_currentLevel):
    printHelper("debug", intoString(args))
def error(*args) -> None:
  if _debugLevels.index("quiet") <= _debugLevels.index(_currentLevel):
    printHelper("error", intoString(args))
def warn(*args) -> None:
  if _debugLevels.index("verbose") <= _debugLevels.index(_currentLevel):
    printHelper("warn", intoString(args))
def info(*args) -> None:
  if _debugLevels.index("info") <= _debugLevels.index(_currentLevel):
    printHelper("info", intoString(args))

#   def test(cls, target = True, expected = None, method = "==", text: str = ""):
#     if type(target) != bool and expected != None:
#       if method == "!=" or method.startswith("dif"):
#         method = "!="
#         condition = target != expected
#       elif method == "in":
#         try:
#           condition = expected in target
#         except TypeError:
#           condition = None
#           debug.error(f"target {target} is type of {type(target)}, which is not iterable")
#       else:
#         condition = target == expected
#       text = f"{text} =>" if text != "" else f"Testing {target} {method} {expected} =>"
#     else:
#       condition = target
#       text = "" if text == "" else f"{text} "
#       text = f"Simple Testing : {text}=>"
#     if condition != None:
#       answer = "True" if condition else "False"
#       cls.debug(f"{text} {answer}")