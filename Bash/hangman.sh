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
  if [[ "p" == *$guess1* ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/1
    guess2="$(echo $guess | sed s/./$guess1/1)"
    guess=$guess2
    continue 
  elif [[ "y" == *$guess1* ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/2
    guess3="$(echo $guess | sed s/./$guess1/2)"
    guess=$guess3
    continue
  elif [[ "t" == *$guess1* ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/3
    guess4="$(echo $guess | sed s/./$guess1/3)"
    guess=$guess4
    continue
  elif [[ "h" == *$guess1* ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/4
    guess5="$(echo $guess | sed s/./$guess1/4)"
    guess=$guess5
    continue
  elif [[ "o" == *$guess1* ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/5
    guess6="$(echo $guess | sed s/./$guess1/5)"
    guess=$guess6
    continue
  elif [[ "n" == *$guess1* ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/6
    guess7="$(echo $guess | sed s/./$guess1/6)"
    guess=$guess7
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