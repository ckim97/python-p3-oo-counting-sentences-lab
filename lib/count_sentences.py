#!/usr/bin/env python3
import re

class MyString(str):
  def __init__(self, value=""):
    super().__init__()
    self.value = value
  

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith(".")
    
  def is_question(self):
    return self.value.endswith("?")
    

  def is_exclamation(self):
    return self.value.endswith("!")
   
    
  def count_sentences(self):
    # re solution
    sentence_list = re.split("[?!.]", self.value)
    actual_sentences = [sentence for sentence in sentence_list if sentence != '']
    return len(actual_sentences)





    # count = 0
    # prev_char = ""
    
    # for char in self.value:
    #   if char in [".", "!", "?"] and prev_char.isalpha():
    #     count += 1
    #   prev_char = char
      
    # return count



    # split solution 
    # transformed_sentence = self.value.replace("!", ".").replace("?", ".")
    # sentence_list = transformed_sentence.split(".")
    # actual_sentences = [sentence for sentence in sentence_list if sentence != '']
    # return len(actual_sentences)
  

    

