# GreekCompiler

📘 Greek++ Compiler

A complete compiler for the custom programming language Greek++, implemented in Python.

📌 Overview

This project is a fully functional compiler for the programming language Greek++, designed and implemented entirely in Python.
Greek++ is a custom language with its own grammar, syntax rules, commands, and semantic constraints.

The compiler supports all major compilation stages, including:

Lexical Analysis (Lexer)

Syntax Analysis (Parser)

Semantic Checks

Intermediate Code Generation

Final Code Generation

This project demonstrates the full pipeline of a modern compiler architecture.

🧩 Features of the Greek++ Language

Greek++ includes its own custom-designed structure, commands, and rules, such as:

Variables and data declarations

Arithmetic and logical expressions

Conditional statements

Looping constructs

Functions / procedures

Input–output commands

Custom grammar rules following a formal BNF-like structure

(Αν θέλεις, μπορώ να προσθέσω και κανονική BNF γραμματική!)

🛠 Compiler Structure
✔ 1. Lexical Analyzer (Lexer)

Responsible for scanning the input program and splitting it into tokens:

keywords

identifiers

numbers

symbols

operators

It includes error handling for unknown tokens and invalid lexemes.

✔ 2. Syntax Analyzer (Parser)

Implements a grammar for Greek++ and constructs the parse tree.
It detects:

syntax errors

missing symbols

invalid statement structure

Supports recursive descent / LL parsing / (γράψε το είδος που χρησιμοποιείς).

✔ 3. Intermediate Code Generation

The compiler produces intermediate representations (IR) such as:

quadruples (quads)

three-address code

low-level instructions

This IR is used as the bridge between the parser and the final code generator.

✔ 4. Final Code Generation

The compiler translates intermediate code into target assembly-like code.
( RISC-V)

Handles register allocation, jumps, labels, and sequential execution.
