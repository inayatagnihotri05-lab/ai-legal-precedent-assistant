import json

def load_case(file_path):
    """
    Loads a structured small-case file.
    This function performs NO legal reasoning.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    case = load_case("data/sample_small_case.json")

    print("\n--- CASE SUMMARY (NON-BINDING) ---\n")
    print("Case Title:", case["case_title"])
    print("Jurisdiction:", case["jurisdiction"])
    print("Case Type:", case["case_type"])

    print("\nFacts of the Case:")
    for fact in case["facts_of_the_case"]:
        print("-", fact)

    print("\nRelief Sought:")
    for relief in case["relief_sought"]:
        print("-", relief)

    print("\nNote:", case["notes"])
