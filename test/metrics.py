import nltk
from nltk.metrics import edit_distance
from nltk.translate.bleu_score import corpus_bleu
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

reference_file = '/Users/eleanorewu/Latex-OCR/data/val/val-formulas.txt'
candidate_file = '/Users/eleanorewu/Latex-OCR/test/latexocr_output_parallel.txt'
reference_texts = load_text(reference_file)
candidate_texts = load_text(candidate_file)

if len(reference_texts) < len(candidate_texts):
    raise ValueError("The reference texts has less lines than candidate texts. Impossible.")
elif len(reference_texts) > len(candidate_texts):
    reference_texts = reference_texts[:len(candidate_texts)]


# Normalized Edit Distance
ned_scores = [edit_distance(word_tokenize(ref), word_tokenize(cand)) / max(len(word_tokenize(ref)), 1) 
              for ref, cand in zip(reference_texts, candidate_texts)]
average_ned = sum(ned_scores) / len(ned_scores)

# Token Accuracy
token_accuracies = [sum(1 for x, y in zip(word_tokenize(ref), word_tokenize(cand)) if x == y) / max(len(word_tokenize(ref)), 1) 
                    for ref, cand in zip(reference_texts, candidate_texts)]
average_token_accuracy = sum(token_accuracies) / len(token_accuracies)

# BLEU Score
reference_tokens = [[word_tokenize(ref)] for ref in reference_texts]
candidate_tokens = [word_tokenize(cand) for cand in candidate_texts]
bleu_score = corpus_bleu(reference_tokens, candidate_tokens)

print(f"BLEU score: {bleu_score}")
print(f"Normalized Edit Distances: {average_ned}")
print(f"Token Accuracies: {average_token_accuracy}")
