#!/bin/env python3
import sys
import os

# sys.path.insert(0, f"{os.path.dirname(__file__)}/..")
# from printDebugging import *
from printDebugging import *
def do_print():
  debug(f"DEBUG-{getLevel()}")
  info(f"INFO-{getLevel()}")
  warn(f"WARN-{getLevel()}")
  error(f"ERROR-{getLevel()}")

# All Prints
# QUIET
setLevel(DEBUG)
do_print()
setDefault()
saveConfigure()
do_print()
# do_print()
# # INFO
# setLevel("INFO")
# do_print()
# # VERBOSE
# setLevel("VERBOSE")
# do_print()
# # DEBUG
# setLevel(DEBUG)
# do_print()
# print()
# set_color("purple", INFO, "bg")
# do_print()
# set_color("purple", DEBUG)
# do_print()
# set_color("purple", WARN)
# add_style("underline+bold", WARN)
# do_print()
# reset_style(WARN)
# set_color("underline+bold", "ERROR", "style")
# do_print()
# reset_style()
# do_print()
# reset_background()
# do_print()
# set_color("purple", DEBUG, "bg")
# set_color("purple", WARN, "bg")

# do_print()
# reset_background("WARN")
# do_print()
# reset_background()
# import datetime
# add_postfixes(["postfixes :: ", traceback.format_exc], ERROR)
# # add_prefixes(["current time :: ", datetime.datetime.now])
# do_print()
# reset_prefixes()
# do_print()
# reset_postfixes()
# do_print()
# set_prefixes("common prefix", "INFO")
# do_print()
# saveConfigure()
# # import traceback
# set_postfixes(datetime.datetime.now,"ERROR")

# do_print()
# saveConfigure()
# print(DebugLevel.INFO)

# print(getLevel())
# # setLevel(INFO)
# print(getLevel())
# debug("?")
# # error("?")
import traceback
set_postfixes(traceback.format_exc, ERROR)
try:
  0 / 0
except:
  error("Expected")