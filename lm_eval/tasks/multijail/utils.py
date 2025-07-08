from datasets import Dataset


def process_docs(dataset):
    """Flatten the MultiJail dataset by extracting prompts from multiple language columns."""
    language_columns = ["en", "zh", "it", "vi", "ar", "ko", "th", "bn", "sw", "jv"]

    new_rows = []
    for i, row in enumerate(dataset):
        # row should be a dict
        for lang in language_columns:
            prompt = row.get(lang, "")
            if not isinstance(prompt, str) or prompt.strip() == "":
                continue
            new_rows.append({"prompt": prompt, "id": f"{i}_{lang}"})

    # Convert the list back to a Dataset object
    dataset_out = Dataset.from_list(new_rows)
    return dataset_out
