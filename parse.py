#!/usr/bin/env python
from __future__ import print_function
import fileinput, sys, re

variables = {}
arg1 = None

class Constant(object):
  def __init__(self, name, obj=None):
    self.name = name
    self.obj = obj

  def __getattr__(self, name):
    return self.obj

  def __str__(self):
    return self.name


def parse(line):

  lines = line.split(";;")
  for line in lines:
    if line == "" or line == "\n" or line is None: return None
    if line is not None:
      chunks = line.split(";")
      if len(chunks) > 1: 
        global arg1
        arg1 = chunks[1]
        if arg1[len(arg1)-1] == '\n':
          arg1 = arg1[0:len(arg1)-1]
          print("ARG1:", arg1)
        for i in range(1, len(chunks)):
          chunk = chunks[i]
          if chunk[len(chunk)-1] == '\n':
            chunk = chunk[0:len(arg1)-1]
      if (len(chunks) == 1):
        expr = chunks[0]
        print("EXPR:", expr)
        return madEval(expr)
      elif (len(chunks) > 1):
        evaluate(chunks[0], chunks[1], chunks[2])

def madEval(expr):
  temp = expr
  try:
    temp = eval(expr)
  except NameError:
    if variables is not None:
      regex = re.compile("[a-zA-Z]+")
      strings = regex.findall(expr)
      print("STRINGS:", strings)
      if strings != []:
        for string in strings:
          if string in variables.keys():
            print(string,"is a key")
            pattern = string+"([^a-zA-Z])"
            t = re.findall(pattern, temp)
            print("T:",t)
            if t is None or t == [] or t == '\n':
              t = re.findall(string+"\n", temp)
              replacement = str(variables[string])
              temp = re.sub(string, replacement, temp)
            else:
              replacement = str(variables[string])+t[0]
              temp = re.sub(pattern, replacement, temp)

        return eval(temp)
  return temp # hmmm

#def replaceVariables()

def evaluate(*args):
  print("ARG2:", args[2])
  num = madEval(args[2])
  if args[0] == "let" and len(args) == 3:
    if (re.search("[a-z]+", str(arg1)) != None):
      if (args[1] in variables.keys()):
        print("You told me \""+arg1+"\" meant", variables[arg1],"- did you lie?")
      else:
        constant = Constant(str(arg1), num)
        variables[str(constant)] = getattr(constant, "obj")
        print(constant, "means", variables[str(constant)])
    else:
      print("Illegal assignment:", "\""+arg1+"\"", "is not a sequence of letters!")
  elif (args[0] == "do" and len(args) == 3):
    do(args[1], int(num))
    #args[1]
  #print(args)
  print(variables)

def do(func, num):
  if num is 0: return
  if func is not None:
    madEval(func)
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
