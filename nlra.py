import spacy

nlp = spacy.load("en_core_web_sm")

functional_keywords = ["shall", "must", "should", "will", "provide", "enable"]
nonfunctional_keywords = ["fast", "secure", "reliable", "usable", "scalable", "efficient"]

def classify_requirement(sentence):
    text = sentence.text.lower()
    if any(word in text for word in functional_keywords):
        return "Functional Requirement"
    elif any(word in text for word in nonfunctional_keywords):
        return "Non-Functional Requirement"
    else:
        return "Candidate Requirement"

def detect_ambiguity(sentence):
    ambiguous_terms = ["fast", "user-friendly", "secure", "reliable", "efficient", "etc"]
    return [word for word in ambiguous_terms if word in sentence.text.lower()]

def analyze_text(text):
    doc = nlp(text)
    requirements = []
    for sent in doc.sents:
        req_type = classify_requirement(sent)
        ambiguities = detect_ambiguity(sent)
        requirements.append({
            "sentence": sent.text.strip(),
            "type": req_type,
            "ambiguities": ambiguities
        })
    return requirements

if __name__ == "__main__":
    print("=== Natural Language Requirements Assistant ===")
    user_input = input("Paste project text: ")
    results = analyze_text(user_input)

    print("\n--- Results ---")
    for i, req in enumerate(results, start=1):
        print(f"R{i}: {req['sentence']}")
        print(f"   → Type: {req['type']}")
        if req['ambiguities']:
            print(f"   ⚠ Ambiguous terms: {', '.join(req['ambiguities'])}")
