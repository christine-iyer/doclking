

import sys
import re
from collections import Counter
import random

def analyze_text(text):
    """
    Perform basic linguistic analysis on text.
    """
    # Word frequency analysis
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = Counter(words)
    
    # Basic statistics
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    print(f"📊 Text Analysis Results:")
    print(f"   Words: {len(words)}")
    print(f"   Unique words: {len(word_freq)}")
    print(f"   Sentences: {len(sentences)}")
    print(f"   Avg words per sentence: {len(words)/len(sentences):.1f}")
    
    print(f"\n🔥 Top 5 most common words:")
    for word, count in word_freq.most_common(5):
        print(f"   '{word}': {count} times")

def generate_markov_text(text, length=50):
    """
    Generate text using a simple Markov chain.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Build word pairs
    word_pairs = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        
        if current_word not in word_pairs:
            word_pairs[current_word] = []
        word_pairs[current_word].append(next_word)
    
    # Generate new text
    if not word_pairs:
        return "Not enough text to generate from!"
    
    current_word = random.choice(list(word_pairs.keys()))
    generated = [current_word]
    
    for _ in range(length - 1):
        if current_word in word_pairs:
            current_word = random.choice(word_pairs[current_word])
            generated.append(current_word)
        else:
            current_word = random.choice(list(word_pairs.keys()))
            generated.append(current_word)
    
    return ' '.join(generated)

def count_syllables(word):
    """
    Estimate syllable count (simple heuristic).
    """
    word = word.lower()
    vowels = "aeiouy"
    syllable_count = 0
    prev_was_vowel = False
    
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel:
            syllable_count += 1
        prev_was_vowel = is_vowel
    
    # Handle silent 'e'
    if word.endswith('e') and syllable_count > 1:
        syllable_count -= 1
    
    return max(1, syllable_count)

def find_rhymes(word, word_list):
    """
    Find potential rhymes (simple ending match).
    """
    word = word.lower()
    rhymes = []
    
    for w in word_list:
        w = w.lower()
        if w != word and len(w) > 2 and len(word) > 2:
            # Check if they end with same 2+ characters
            if word[-2:] == w[-2:] or word[-3:] == w[-3:]:
                rhymes.append(w)
    
    return rhymes[:5]  # Return first 5 matches

def main():
    """
    Main function for the Docling project.
    """
    print("🚀 Welcome to Docling - Linguistic Analysis Tool!")
    print("=" * 50)
    
    # Sample text for demonstration
    sample_text = """
    The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet.
    Language is a fascinating aspect of human communication. It evolves constantly and reflects culture.
    Computational linguistics combines computer science with linguistic analysis. Text processing enables
    many modern applications like search engines and chatbots.
    """
    
    print("🔍 Analyzing sample text...")
    analyze_text(sample_text)
    
    print(f"\n🎲 Generated text (Markov chain):")
    generated = generate_markov_text(sample_text, 20)
    print(f"   {generated}")
    
    print(f"\n🎵 Syllable counter demo:")
    test_words = ["gargantuan", "improbable", "stupendous", "linguistic", "extraordinary"]
    for word in test_words:
        syllables = count_syllables(word)
        print(f"   '{word}': {syllables} syllables")
    
    print(f"\n🎯 Rhyme finder demo (words that rhyme with 'cat'):")
    word_list = ["bat", "hat", "mat", "dog", "log", "rat", "sat", "flat", "chat"]
    rhymes = find_rhymes("cat", word_list)
    print(f"   Rhymes: {', '.join(rhymes) if rhymes else 'None found'}")
    
    print(f"\n✨ Try running this with your own text!")

if __name__ == "__main__":
    main()