rules = [
    {"if": ["fever", "cough", "fatigue"], "then": "Flu"},
    {"if": ["fever", "cough", "shortness of breath"], "then": "COVID-19"},
    {"if": ["headache", "nausea", "sensitivity to light"], "then": "Migraine"},
    {"if": ["sore throat", "runny nose", "sneezing"], "then": "Common Cold"},
    {"if": ["chest pain", "shortness of breath", "dizziness"], "then": "Heart Attack"},
]

def diagnose(symptoms):
    matched_diseases = []
    symptoms_set = set(symptoms)

    for rule in rules:
        for symp in rule['if']:
            if symp in symptoms_set:
                matched_diseases.append(rule['then'])

    return matched_diseases

def main():
    print("Enter your symptoms separated by commas (e.g., fever, cough):")
    
    user_input = input("Symptoms: ").lower()
    symptoms = [s.strip() for s in user_input.split(",")]
    print(symptoms)

    diagnoses = diagnose(symptoms)

    if diagnoses:
        print("\nPossible diagnosis(es):")
        for disease in diagnoses:
            print(f"- {disease}")
    else:
        print("\nNo matching diagnosis found. Please consult a doctor.")

main()
