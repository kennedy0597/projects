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
if $try != 0; then
  if [[ $word == *$guess1* ]]; then
    echo "correct guess"
    echo $guess | sed -r 's/[-]+/'$guess1'/g' 
  else 
    echo wrong
    echo "$(($try - 1)) tries left" 
  fi
else
  echo "no more tries"
fi