# flatten the original data to one columns, since it initially has one column per language prompt.
def process_docs(dataset):
    language_columns = ["en", "zh", "it", "vi", "ar", "ko", "th", "bn", "sw", "jv"]

    new_rows = []
    for i, row in enumerate(dataset):
        # row should be a dict
        for lang in language_columns:
            prompt = row.get(lang, "")
            if not isinstance(prompt, str) or prompt.strip() == "":
                continue
            new_rows.append({"prompt": prompt, "id": f"{i}_{lang}"})
    return new_rows
