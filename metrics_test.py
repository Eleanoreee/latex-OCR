import math
from transformers import pipeline
from nltk.metrics import edit_distance
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
from nltk.tokenize import word_tokenize

# Load reference and candidate texts
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

reference_file = '/Users/eleanorewu/im2latex_formulas.lst'
candidate_file = '/Users/eleanorewu/czb/testing/latexocr_output_parallel.txt'
reference_texts = load_text(reference_file)
candidate_texts = load_text(candidate_file)

# Perplexity
def calculate_perplexity(texts):
    lm = pipeline("text-generation", model="gpt2")
    perplexities = []
    for text in texts:
        perplexities.append(math.exp(lm(text, return_dict=True)['logits']))
    return perplexities
perplexities = calculate_perplexity(candidate_texts)
average_perplexity = sum(perplexities) / len(perplexities)

# NED score
ned_scores = [edit_distance(word_tokenize(ref), word_tokenize(cand)) / len(word_tokenize(ref)) for ref, cand in zip(reference_texts, candidate_texts)]
average_edit_distance = sum(ned_scores) / len(ned_scores)
average_ned = sum(ned_scores) / len(ned_scores)

# Token Accuracy
token_accuracies = [sum(1 for x, y in zip(word_tokenize(ref), word_tokenize(cand)) if x == y) / len(word_tokenize(ref)) for ref, cand in zip(reference_texts, candidate_texts)]
average_token_accuracy = sum(token_accuracies) / len(token_accuracies)

# BLEU Score
weights = (0.25, 0.25, 0.25, 0.25)
bleu_score = corpus_bleu([[word_tokenize(ref)] for ref in reference_texts], [word_tokenize(cand) for cand in candidate_texts], weights=weights)

# Extract Match Score
extract_match_scores = [sentence_bleu([word_tokenize(ref)], word_tokenize(cand)) for ref, cand in zip(reference_texts, candidate_texts)]
average_extract_match_score = sum(extract_match_scores) / len(extract_match_scores)

print(f"BLEU score: {bleu_score}")
print(f"Normalized Edit Distances: {average_ned}")
print(f"Token Accuracies: {average_token_accuracy}")
print(f"Perplexity: {average_perplexity}")
print(f"Edit Distance: {average_edit_distance}")
print(f"Extract Match Score: {average_extract_match_score}")