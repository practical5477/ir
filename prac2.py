documents = {
    1: "apple banana orange",
    2: "apple banana",
    3: "banana orange",
    4: "apple"
}

# Function to build an inverted index using dictionaries
def build_index(docs):
    index = {}  # Initialize an empty dictionary to store the inverted index
    for doc_id, text in docs.items():  # Iterate through each document and its text
        terms = set(text.split())
        # Split the text into individual terms
        for term in terms:  # Iterate through each term in the document
            if term not in index:
                index[term] = {doc_id}  # If the term is not in the index, create a new set with document ID
            else:
                index[term].add(doc_id)  # If the term exists, add the document ID to its set
    return index  # Return the built inverted index

# Building the inverted index
inverted_index = build_index(documents)

# Function for Boolean AND operation using inverted index
def boolean_and(operands, index):
    if not operands:  # If there are no operands, return all document IDs
        return list(range(1, len(documents) + 1))
    result = index.get(operands[0], set())  # Get the set of document IDs for the first operand
    for term in operands[1:]:  # Iterate through the rest of the operands
        result = result.intersection(index.get(term, set()))  # Compute intersection with sets of document IDs
    return list(result)  # Return the resulting list of document IDs

# Function for Boolean OR operation using inverted index
def boolean_or(operands, index):
    result = set()  # Initialize an empty set to store the resulting document IDs
    for term in operands:  # Iterate through each term in the query
        result = result.union(index.get(term, set()))  # Union of sets of document IDs for each term
    return list(result)  # Return the resulting list of document IDs

# Function for Boolean NOT operation using inverted index
def boolean_not(operand, index, total_docs):
    operand_set = set(index.get(operand, set()))  # Get the set of document IDs for the operand
    all_docs_set = set(range(1, total_docs + 1))  # Create a set of all document IDs
    return list(all_docs_set.difference(operand_set))  # Return documents not in the operand set

# Example queries
query1 = ["apple", "banana"]  # Query for documents containing both "apple" and "banana"
query2 = ["apple", "orange"]  # Query for documents containing "apple" or "orange"

# Performing Boolean Model queries using inverted index
result1 = boolean_and(query1, inverted_index)  # Get documents containing both terms
result2 = boolean_or(query2, inverted_index)  # Get documents containing either of the terms
result3 = boolean_not("orange", inverted_index, len(documents))  # Get documents not containing "orange"

# Printing results
print("Documents containing 'apple' and 'banana':", result1)
print("Documents containing 'apple' or 'orange':", result2)
print("Documents not containing 'orange':", result3)
