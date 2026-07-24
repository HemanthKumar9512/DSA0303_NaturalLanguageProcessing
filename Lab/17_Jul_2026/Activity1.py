# Morphological Feature Identification

words = {
    "cities": {
        "Root": "city",
        "Prefix": "-",
        "Suffix": "-ies",
        "POS": "Noun",
        "Number": "Plural",
        "Tense": "-",
        "Degree": "-",
        "Morphological Tags": "NNS"
    },

    "geese": {
        "Root": "goose",
        "Prefix": "-",
        "Suffix": "Irregular",
        "POS": "Noun",
        "Number": "Plural",
        "Tense": "-",
        "Degree": "-",
        "Morphological Tags": "NNS"
    },

    "caught": {
        "Root": "catch",
        "Prefix": "-",
        "Suffix": "Irregular",
        "POS": "Verb",
        "Number": "-",
        "Tense": "Past",
        "Degree": "-",
        "Morphological Tags": "VBD"
    },

    "playing": {
        "Root": "play",
        "Prefix": "-",
        "Suffix": "-ing",
        "POS": "Verb",
        "Number": "-",
        "Tense": "Present Participle",
        "Degree": "-",
        "Morphological Tags": "VBG"
    },

    "happier": {
        "Root": "happy",
        "Prefix": "-",
        "Suffix": "-er",
        "POS": "Adjective",
        "Number": "-",
        "Tense": "-",
        "Degree": "Comparative",
        "Morphological Tags": "JJR"
    },

    "teachers": {
        "Root": "teach",
        "Prefix": "-",
        "Suffix": "-ers",
        "POS": "Noun",
        "Number": "Plural",
        "Tense": "-",
        "Degree": "-",
        "Morphological Tags": "NNS"
    },

    "children": {
        "Root": "child",
        "Prefix": "-",
        "Suffix": "Irregular",
        "POS": "Noun",
        "Number": "Plural",
        "Tense": "-",
        "Degree": "-",
        "Morphological Tags": "NNS"
    },

    "largest": {
        "Root": "large",
        "Prefix": "-",
        "Suffix": "-est",
        "POS": "Adjective",
        "Number": "-",
        "Tense": "-",
        "Degree": "Superlative",
        "Morphological Tags": "JJS"
    },

    "running": {
        "Root": "run",
        "Prefix": "-",
        "Suffix": "-ing",
        "POS": "Verb",
        "Number": "-",
        "Tense": "Present Participle",
        "Degree": "-",
        "Morphological Tags": "VBG"
    },

    "studies": {
        "Root": "study",
        "Prefix": "-",
        "Suffix": "-ies",
        "POS": "Verb",
        "Number": "Singular",
        "Tense": "Present",
        "Degree": "-",
        "Morphological Tags": "VBZ"
    }
}

print("="*110)
print(f"{'Word':<12}{'Root':<12}{'Prefix':<10}{'Suffix':<12}{'POS':<12}{'Number':<12}{'Tense':<20}{'Degree':<15}{'Tags'}")
print("="*110)

for word, info in words.items():
    print(f"{word:<12}{info['Root']:<12}{info['Prefix']:<10}{info['Suffix']:<12}{info['POS']:<12}{info['Number']:<12}{info['Tense']:<20}{info['Degree']:<15}{info['Morphological Tags']}")
