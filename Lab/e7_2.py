rules = [
    {"if": {"fever", "cough", "fatigue"}, "then": "Flu"},
    {"if": {"fever", "cough", "shortness of breath"}, "then": "COVID-19"},
    {"if": {"headache", "nausea", "sensitivity to light"}, "then": "Migraine"},
    {"if": {"sore throat", "runny nose", "sneezing"}, "then": "Common Cold"},
    {"if": {"chest pain", "shortness of breath", "dizziness"}, "then": "Heart Attack"},
]

def diagnose(symptoms):
    matched_diseases = []
    symptoms_set = set(symptoms)

    for rule in rules:
        if rule["if"].issubset(symptoms_set):
            matched_diseases.append(rule["then"])

    return matched_diseases

def main():
    print("=== Forward Chaining Medical Expert System ===")
    print("Enter your symptoms separated by commas (e.g., fever, cough):")

    user_input = input("Symptoms: ").lower()
    symptoms = [s.strip() for s in user_input.split(",")]

    diagnoses = diagnose(symptoms)

    if diagnoses:
        if len(diagnoses) > 1:
            print("\nMultiple possible diseases detected based on overlapping symptoms:")
        else:
            print("\nPossible diagnosis:")

        for disease in diagnoses:
            print(f"- {disease}")
    else:
        print("\nNo matching diagnosis found. Please consult a doctor.")

if __name__ == "__main__":
    main()
