# Frequency analysis of the modern Russian language based on comments in the VK

## Code

1. scraping_text.py - data scraping.
2. data_cleaning.py - remove commas, emojis and duplicate comments.
3. plotting_graph.py - frequency analysis and plotting graph, where the y axis is the frequency of occurrence of the symbol, and x is the letter.
4. encryption.py - encrypt text by the method of frequency analysis and decryption using frequency analysis.
5. syllables_splitting.py - splitting words into syllables. To split words into syllables, I use rusyllab/rusyllab.py. It's from https://github.com/Koziev/rusyllab.
6. check_syllable.py - each incorrect word( you need to select it manually) is split into syllables and we search for the most similar syllables for each syllable.

## Results

Frequency of occurrence of symbols in the form of a graph:

![frequency_graph](https://user-images.githubusercontent.com/42088646/109300893-34939e00-7848-11eb-8120-6bb2b6b152d4.png)

Frequency of occurrence of characters in the form of a table:


![frequency_table](https://user-images.githubusercontent.com/42088646/109301889-9c96b400-7849-11eb-8750-540992ea6a48.png)

Frequency of syllable occurrence:

![syllables](https://user-images.githubusercontent.com/42088646/109302134-f26b5c00-7849-11eb-9024-4bef0d4ddaa1.png)

## Article

https://habr.com/ru/post/513926/
