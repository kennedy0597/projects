#!/bin/bash
# this is a script for a hangman game

echo "Welcome to hangman"
echo "You have 5 tries"

message(){
    echo "enter your alphabet guess"
    echo "you have $try left"
}

read guess1

try=5
word=python
guess=------
if [[ $word == *$guess1* ]]; then
  echo "correct guess"
  echo $guess
else 
  echo wrong
  $(($try - 1))
fi