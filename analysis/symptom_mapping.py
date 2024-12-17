def map_symptoms_to_conditions(symptoms):
    """
    Map symptoms to common mental health conditions.
    :param symptoms: List of reported symptoms.
    :return: Matching conditions.
    """
    symptom_condition_map = {
        "fatigue": "Depression",
        "panic attacks": "Anxiety Disorder",
        "intrusive thoughts": "OCD",
        "hyperactivity": "ADHD",
        "nightmares": "PTSD"
    }
    
    conditions = set()
    for symptom in symptoms:
        condition = symptom_condition_map.get(symptom.lower())
        if condition:
            conditions.add(condition)
    
    return list(conditions)

# Example usage
if __name__ == "__main__":
    user_symptoms = ["Fatigue", "Panic Attacks", "Intrusive Thoughts"]
    print("Mapped Conditions:", map_symptoms_to_conditions(user_symptoms))
