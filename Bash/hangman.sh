#!/bin/bash
# this is a script for a hangman game

echo "Welcome to hangman"
echo "You have 5 tries"

welcome(){
    echo "enter your alphabet guess"
    echo "you have $try left"
}

get_word(){
  echo "enter a random word"
  read -s word1
  letter=($(echo $word1|sed 's/\(.\)/\1 /g'))
}

function guessing(){
while [[ $try != 0 ]]; do
read guess1
  if [[ ${letter[0]} == $guess1 ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/1
    guess2="$(echo $guess | sed s/./$guess1/1)"
    guess=$guess2
    continue 
  elif [[ ${letter[1]} == $guess1 ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/2
    guess3="$(echo $guess | sed s/./$guess1/2)"
    guess=$guess3
    continue
  elif [[ ${letter[2]} == $guess1 ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/3
    guess4="$(echo $guess | sed s/./$guess1/3)"
    guess=$guess4
    continue
  elif [[ ${letter[3]} == $guess1 ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/4
    guess5="$(echo $guess | sed s/./$guess1/4)"
    guess=$guess5
    continue
  elif [[ ${letter[4]} == $guess1 ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/5
    guess6="$(echo $guess | sed s/./$guess1/5)"
    guess=$guess6
    continue
  elif [[ ${letter[5]} == $guess1 ]]; then
    echo "correct guess"
    echo $guess | sed s/./$guess1/6
    guess7="$(echo $guess | sed s/./$guess1/6)"
    guess=$guess7
    continue
  elif [[ $guess = $word1 ]]; then
    echo "Congratulations, you guessed correctly with $try tries left"
    break 
  else
    echo wrong
    echo "$(($try - 1)) tries left" 
    try="$(($try - 1))"
    continue
  fi
done
}
try=5
guess=------

get_word
welcome
guessing