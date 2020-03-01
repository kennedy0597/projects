#!/bin/bash
# this is a script for a hangman game

echo "Welcome to hangman"
echo "You have 5 tries"

welcome(){
    echo "enter your alphabet guess"
    echo "you have $try left"
}

function guessing(){
while [ $try != 0 ]; do
read guess1
  if [[ $word == *$guess1* ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/5
    continue 
  else
    echo wrong
    echo "$(($try - 1)) tries left" 
    try="$(($try - 1))"
    continue
  fi
done
echo "no mo tries"
}
try=5
word=python
guess=------

welcome
guessing