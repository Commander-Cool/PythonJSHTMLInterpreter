#!/usr/bin/env python 

import graphics
def interpret (trees):
	for tree in trees:
		nodetype = tree[0]
		if (nodetype == "word-element"):
			graphics.word(tree[1])
		elif (nodetype=="tag-element"):
			tagname = tree[1]
			tagargs = tree[2]
			subtrees = tree[3]
			closetagname = tree[4]
			if (tagname <> closetagname):
				graphics.warning("unbalanced tags")
			else:
				graphics.begintag(tagname,tagargs)
				interpret(subtrees)
				graphics.endtag()

def evaljsMath(tree):
	nodetype = tree[0]
	if (nodetype == "number"):
		return int(tree[1])
	elif (nodetype == "binop"):
		left_child = tree[1]
		operator = tree[2]
		right_child = tree[3]
		if (operator == "+"):
			return left_value + right_value
		elif (operator == "-"):
			return left_value - right_value

def envLookup(environment,varName):
	return environment.get(varName,None)

def evalExpression(tree,environment):
	nodetype = tree[0]
	if (nodetype =="number"):
		return int(tree[1])
	elif (nodetype == "binop"):
		left_value = evalExpression(tree[2],environment)
		operator = tree[2]
		right_value = evalExpression(tree[2],environment)
		if (operator == "+"):
			return left_value + right_value
		elif (operator = "-"):
			return left_value - right_value
		elif (nodetype == "identifier"):
			varName = tree[1]
			return envLookup(environment,varName)

def evalStmts(tree,environment):
	stmt = tree[0]
	if (stmt == "assign"):
		varName = tree[1]
		right_child = tree[2]
		new_value = evalExpression(right_child, environment)
		environmentUpdate(environment, varName, new_value)
	elif (stmt == "if-then-else"):
		conditional_exp = tree[1]
		then_stmts = tree[2]
		else_stmts = tree[3]
		if (evalExpression(conditional_exp,environment)):
			evalStmts(then_stmts,environment)
		else:
			evalStmts(else_stmts,environment)

