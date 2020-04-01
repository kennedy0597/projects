#!/bin/bash

main(){
  while [[ $try != 0 ]]; do
    echo "enter your alphabet guess"
    if [[ "$guess" != *"$word"* ]]; then
    read guess1
      if [[ "$word" == *"$guess1"* ]]; then
        echo "correct guess"
        guess+=$guess1
        echo "${word//[^[:space:]$guess]/*}" 
        continue
      else
        echo "Wrong"
        echo "$(($try - 1)) tries left" 
        try="$(($try - 1))"
        continue  
      fi
    else 
      echo "Congratulations! $word was the secret word"  
      break
    fi 
  done
}

welcome(){
  echo "welcome to hangman"
  echo "Enter a secret word and ask your friends to guess!"
  echo "you have $try tries"
  echo "Good Luck!"
}

get_word(){
  echo "enter a random word"
  read -s word
}


try=7
guess=""
welcome
get_word
main