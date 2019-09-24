# Greeklish to Greek converter
## Project for the course Natural Language Processing
### NTUA School of Electrical Engineering, 8th Semester
Greek is a complicated language in a way that the writer has to take many parameters into account while writing, like the spelling, punctuation, etc. Hence, it is a trend nowadays for greek people not to write greek while texting, but to use a different approach which is called <b>Greeklish</b>. 
* What is Greeklish? <br>
<t> Greeklish is a type of writing, in which the greek alphabet is replaced with the latin. In this way, the writer does not need to be concerned about the spelling and the punctuation and as a result the writing can be accelerated.<br><br>
Examples:<br>
ΚΑΛΗΜΕΡΑ &rarr; KALIMERA<br>
ΘΑΛΑΣΣΑ &rarr; THALASA or 8ALASSA<br>
ΓΕΙΑ ΣΟΥ &rarr; GIA SU<br>
---
In this project we had to create a converter that would take Greeklish texts as inputs and translate them to Greek texts. In order to complete this task we created a pipeline of <b>Finite State Machines (FSMs)</b>, in which every FSM had a different role. The approach followed was:<br>

* 1st Step: Training the FSM<br>
<t> The matching of letters from the latin alphabet to the greek one is an injective function. For instance, the letter Θ can be found in a form of 8 or TH. Hence, there can be more than one possible options for a match from latin to greek. In order to distinguish each case, the FSM should have weights on its edges so it can choose the most economic path. The weights were calculated from a training text and the values they got was the logarithm of the frequency of appearence of each matching between the greeklish and the greek text. The purpose of the logarithm was to simplify the calculations.

* 2nd Step: Architecture of the Converter<br>
<t> The final converter is created with a serial connection of the translator and an orthographer. At first, each word is inserted in the FSM and all the possible paths are selected along with the respective weights. Now, we have some possible translations for the word and we know how possible each translation could be valid. Then, those translations are inserted in the orthograpger, which is an FSM created from a dictionary of greek words. The word that generates the smaller cost is finally chosen and given as an output.
  
Implementation:<br>
<t> &rarr; Python3<br>
    &rarr; OpenFSM<br>
    &rarr; bash<br>
  
Further improvements:<br>
The model may be improved if <b>N-grams</b> are used so each letter translation is done taking into account the translation of the N previous letters. Those <b>N-grams</b> could also be applied between words, so the translation would be sensitive to context. Other machine learning techniques worth of examination is the use of Markov Models, LSTMs and BoG techniques.

Contributors:
* alexkaf
* manzar96
