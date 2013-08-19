#!/usr/bin/env python
from __future__ import print_function
import fileinput, sys, re

variables = {}

class Constant(object):
  def __init__(self, name, obj=None):
    self.name = name
    self.obj = obj

  def __getattr__(self, name):
    return self.obj

  def __str__(self):
    return self.name


def parse(line):

  if line == "" or line == "\n" or line is None: return None
  if line is not None:
    chunks = line.split(";")
    if variables is not None:
      #for var in variables.keys():
      for i in range(len(chunks)):
        regex = re.compile("[a-z]+")
        strings = regex.findall(chunks[i])
#        print("STRINGS: ", strings)
        for string in strings:
#          print("STRING", string)
          if string in variables.keys():
            pattern = string+"([^a-z])"
            temp = re.findall(pattern, chunks[i])
            if temp is None or temp == []:
              temp = re.findall(string, chunks[i])
#            print(temp, chunks[i], variables[string])
            chunks[i] = re.sub(pattern, variables[string]+temp[0], chunks[i])
            #temp = chunks[i].replace(var, variables[var])
            #chunks[i] = 
    if (len(chunks) == 1):
      expr = chunks[0]
      return eval(expr)
    elif (len(chunks) > 1):
      evaluate(chunks[0], chunks[1], chunks[2])

def evaluate(*args):
  num = str(eval(args[2]))
  if args[0] == "let" and len(args) == 3:
    if (args[1] in variables.keys()):
      print("You told me \"", args[1], "\" meant", variables[args[1]],"- did you lie?")
    else:
      constant = Constant(args[1], num)
      variables[str(constant)] = getattr(constant, "obj")
      print(constant, " means ", variables[str(constant)])
  elif (args[0] == "do" and len(args) == 3):
    do(args[1], int(num))
  #print(args)

def do(func, num):
  if num is 0: return
  if func is not None:
    eval(func)
    do(func, num-1)


def repl(prompt='madison> '):
  while True:
    myInput = parse(raw_input(prompt))
    if myInput is not None: print(str(myInput))

def read(f):
  for line in f:
      myInput = parse(line)
      if myInput is not None: print(str(myInput))


def main():
  if (len(sys.argv) > 1):
    myFile = fileinput.input(sys.argv[1]);
    read(myFile)
  else:
    repl()
  
main()
