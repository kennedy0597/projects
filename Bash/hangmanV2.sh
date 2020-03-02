get_word(){
  echo "enter a random word"
  read -s word1
  letter1=($(echo $word1|sed 's/\(.\)/\1 /g'))
  ${letter1[0]}
}

get_word