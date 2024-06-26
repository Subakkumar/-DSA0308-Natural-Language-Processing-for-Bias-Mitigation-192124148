import numpy as np

# Define the PCFG
non_terminals = ['S', 'NP', 'VP', 'PP']
terminals = ['the', 'dog', 'chased', 'the', 'cat']
rules = [
    ('S', 'NP VP'),
    ('NP', 'the dog'),
    ('VP', 'chased the cat'),
    ('PP', 'the cat')
]

# Define the probability distribution
probabilities = np.random.dirichlet(np.ones(len(rules)), size=1)

# Implement the parsing algorithm
def parse(sentence):
    # Initialize the parse tree
    parse_tree = {}

    # Iterate over the sentence
    for i, word in enumerate(sentence):
        # If the word is a terminal, add it to the parse tree
        if word in terminals:
            parse_tree[word] = word
        # If the word is a non-terminal, apply the rules of the grammar
        else:
            # Iterate over the rules of the grammar
            for rule in rules:
                # If the rule matches the word, apply it to the parse tree
                if rule[0] == word:
                    # Apply the rule to the parse tree
                    parse_tree[word] = rule[1]
                    break

    # Return the parse tree
    return parse_tree

# Compute the probability of the parse tree
def compute_probability(parse_tree):
    # Initialize the probability
    probability = 1

    # Iterate over the rules of the grammar
    for rule in rules:
        # If the rule is in the parse tree, compute its probability
        if rule[0] in parse_tree:
            # Compute the probability of the rule
            probability *= probabilities[rule[0]]

    # Return the probability
    return probability

# Test the parser
sentence = ['the', 'dog', 'chased', 'the', 'cat']
parse_tree = parse(sentence)
print(parse_tree)
print(compute_probability(parse_tree))
