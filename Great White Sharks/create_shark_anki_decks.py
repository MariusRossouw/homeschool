import genanki
import random

# Create unique model IDs for different card types
BASIC_MODEL_ID = random.randrange(1 << 30, 1 << 31)
MULTIPLE_CHOICE_MODEL_ID = random.randrange(1 << 30, 1 << 31)
FILL_BLANK_MODEL_ID = random.randrange(1 << 30, 1 << 31)

# Basic card model (front/back)
basic_model = genanki.Model(
    BASIC_MODEL_ID,
    'Basic Great White Shark Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div style="font-size: 24px; text-align: center;">{{Question}}</div>',
            'afmt': '{{FrontSide}}<hr><div style="font-size: 20px; text-align: center; color: #0066cc;">{{Answer}}</div>',
        },
    ])

# Multiple choice model
multiple_choice_model = genanki.Model(
    MULTIPLE_CHOICE_MODEL_ID,
    'Multiple Choice Model',
    fields=[
        {'name': 'Question'},
        {'name': 'ChoiceA'},
        {'name': 'ChoiceB'},
        {'name': 'ChoiceC'},
        {'name': 'ChoiceD'},
        {'name': 'Correct'},
    ],
    templates=[
        {
            'name': 'Multiple Choice',
            'qfmt': '''
                <div style="font-size: 20px; margin-bottom: 20px;">{{Question}}</div>
                <div style="font-size: 18px; margin: 10px;">A) {{ChoiceA}}</div>
                <div style="font-size: 18px; margin: 10px;">B) {{ChoiceB}}</div>
                <div style="font-size: 18px; margin: 10px;">C) {{ChoiceC}}</div>
                <div style="font-size: 18px; margin: 10px;">D) {{ChoiceD}}</div>
            ''',
            'afmt': '''
                {{FrontSide}}
                <hr>
                <div style="font-size: 22px; color: green; margin-top: 20px;">
                    ✓ Correct Answer: {{Correct}}
                </div>
            ''',
        },
    ])

# Fill in the blank model
fill_blank_model = genanki.Model(
    FILL_BLANK_MODEL_ID,
    'Fill in the Blank Model',
    fields=[
        {'name': 'Sentence'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Fill Blank',
            'qfmt': '<div style="font-size: 22px;">Fill in the blank:<br><br>{{Sentence}}</div>',
            'afmt': '{{FrontSide}}<hr><div style="font-size: 20px; color: #0066cc;">{{Answer}}</div>',
        },
    ])

# Cards for Yentl (9-year-old boy)
yentl_cards_data = {
    'basic': [
        ("What does 'apex' mean?", "The highest point of something"),
        ("What does 'formidable' mean?", "Causing fear or respect"),
        ("What does 'daunting' mean?", "Frightening or intimidating"),
        ("What does 'ominous' mean?", "A sign that something unpleasant might happen; threatening"),
        ("What does 'minute' (my-newt) mean?", "Very small or detailed"),
        ("What does 'lore' mean?", "Traditional knowledge or stories passed down about a subject"),
        ("What is a noun?", "A word that names a person, place, or thing"),
        ("What is a pronoun?", "A word that replaces a noun (like he, she, it, they)"),
        ("What are the five senses?", "Smell, vision, hearing, touch, and taste"),
        ("What are the five oceans?", "Pacific, Atlantic, Indian, Southern, and Arctic"),
        ("Which ocean do great white sharks avoid?", "The Arctic Ocean (too cold)"),
        ("What is an apex predator?", "An animal at the top of the food chain with no natural predators"),
        ("How do great white sharks use their sense of smell?", "They can smell a single drop of blood from miles away"),
        ("Why do great white sharks have good hearing?", "To hear low-frequency sounds like struggling fish from over a mile away"),
        ("What is the scientific name for great white sharks?", "Carcharodon carcharias"),
    ],
    'multiple_choice': [
        {
            'question': "What does 'apex predator' mean?",
            'choices': ["An animal that lives in caves", "An animal at the top of the food chain", "An animal that only eats plants", "An animal that lives in the Arctic"],
            'correct': "B) An animal at the top of the food chain"
        },
        {
            'question': "Which ocean is the largest?",
            'choices': ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
            'correct': "C) Pacific Ocean"
        },
        {
            'question': "How fast can great white sharks swim?",
            'choices': ["Up to 15 mph", "Up to 25 mph", "Up to 35 mph", "Up to 45 mph"],
            'correct': "C) Up to 35 mph"
        },
        {
            'question': "Which sense helps sharks detect vibrations in the water?",
            'choices': ["Smell", "Touch", "Taste", "Vision"],
            'correct': "B) Touch"
        },
        {
            'question': "What does 'formidable' mean?",
            'choices': ["Very small", "Causing fear or respect", "Traditional stories", "The highest point"],
            'correct': "B) Causing fear or respect"
        },
        {
            'question': "In the sentence 'The shark swims and it hunts,' what is 'it'?",
            'choices': ["A noun", "A pronoun", "A verb", "An adjective"],
            'correct': "B) A pronoun"
        },
        {
            'question': "How long can great white sharks live?",
            'choices': ["20 years", "40 years", "70 years or more", "100 years"],
            'correct': "C) 70 years or more"
        },
        {
            'question': "What makes great white sharks different from most fish?",
            'choices': ["They are cold-blooded", "They are warm-blooded", "They don't have teeth", "They can't swim"],
            'correct': "B) They are warm-blooded"
        },
    ],
    'fill_blank': [
        ("Great white sharks are _____ predators, meaning they are at the top of the food chain.", "apex"),
        ("The _____ reputation of sharks comes from old stories and movies.", "ominous"),
        ("Sharks have _____ abilities that cause fear or respect.", "formidable"),
        ("Swimming in the deep ocean can seem _____.", "daunting"),
        ("Scientists study every _____ detail of shark behavior.", "minute"),
        ("Traditional _____ about sharks often made them sound like monsters.", "lore"),
        ("In the sentence 'The shark hunts, and it eats,' the word 'it' is a _____.", "pronoun"),
        ("The word 'shark' is a _____ because it names a thing.", "noun"),
        ("Great white sharks can smell using their sense of _____.", "smell"),
        ("The _____ Ocean is the largest ocean on Earth.", "Pacific"),
    ]
}

# Cards for Evah (7-year-old girl)
evah_cards_data = {
    'basic': [
        ("What does 'apex' mean?", "The highest point of something"),
        ("What does 'formidable' mean?", "Causing fear or respect"),
        ("What does 'daunting' mean?", "Frightening or intimidating"),
        ("What does 'ominous' mean?", "Threatening; a sign something bad might happen"),
        ("What does 'minute' (my-newt) mean?", "Very small or detailed"),
        ("What does 'lore' mean?", "Traditional stories passed down about something"),
        ("What is a noun?", "A word that names a person, place, or thing (like shark, ocean, or Luna)"),
        ("What is a pronoun?", "A word that replaces a noun (like she, he, it, or they)"),
        ("What are the five senses?", "Smell, vision, hearing, touch, and taste"),
        ("Name all five oceans", "Pacific, Atlantic, Indian, Southern, and Arctic"),
        ("Which ocean is too cold for great white sharks?", "The Arctic Ocean"),
        ("What is an apex predator?", "An animal at the highest point of the food chain"),
        ("Can great white sharks smell really well?", "Yes! They can smell one drop of blood from miles away"),
        ("Do sharks lose their teeth?", "Yes, but new ones grow in! Sharks can go through thousands of teeth"),
    ],
    'multiple_choice': [
        {
            'question': "What does 'apex' mean?",
            'choices': ["Very small", "The highest point", "Scary stories", "A type of ocean"],
            'correct': "B) The highest point"
        },
        {
            'question': "Which ocean is the biggest?",
            'choices': ["Atlantic", "Pacific", "Indian", "Arctic"],
            'correct': "B) Pacific"
        },
        {
            'question': "How many senses do great white sharks have?",
            'choices': ["Three", "Four", "Five", "Six"],
            'correct': "C) Five"
        },
        {
            'question': "What does 'formidable' mean?",
            'choices': ["Very small", "Causing fear or respect", "Old stories", "An ocean"],
            'correct': "B) Causing fear or respect"
        },
        {
            'question': "In 'Luna found a tooth, and she kept it,' what is 'she'?",
            'choices': ["A noun", "A pronoun", "A shark", "An ocean"],
            'correct': "B) A pronoun"
        },
        {
            'question': "Which word is a noun?",
            'choices': ["She", "He", "Shark", "They"],
            'correct': "C) Shark"
        },
        {
            'question': "What does 'ominous' mean?",
            'choices': ["Happy", "Threatening or scary", "Beautiful", "Friendly"],
            'correct': "B) Threatening or scary"
        },
        {
            'question': "How many oceans are there on Earth?",
            'choices': ["Three", "Four", "Five", "Six"],
            'correct': "C) Five"
        },
    ],
    'fill_blank': [
        ("Great white sharks are _____ predators at the top of the food chain.", "apex"),
        ("Old scary stories about sharks are called _____.", "lore"),
        ("Sharks seem _____ because they cause fear or respect.", "formidable"),
        ("The big ocean can seem _____ or frightening.", "daunting"),
        ("Dark clouds look _____, like something bad might happen.", "ominous"),
        ("Luna looked at every _____ detail of the tooth.", "minute"),
        ("The word 'shark' is a _____ because it names something.", "noun"),
        ("The word 'it' is a _____ that replaces a noun.", "pronoun"),
        ("Sharks use their five _____ to survive: smell, vision, hearing, touch, and taste.", "senses"),
        ("The _____ Ocean is the biggest ocean.", "Pacific"),
    ]
}

def create_deck(name, deck_id, cards_data):
    """Create an Anki deck with various card types"""
    deck = genanki.Deck(deck_id, name)
    
    # Add basic cards
    for question, answer in cards_data['basic']:
        note = genanki.Note(
            model=basic_model,
            fields=[question, answer]
        )
        deck.add_note(note)
    
    # Add multiple choice cards
    for mc in cards_data['multiple_choice']:
        note = genanki.Note(
            model=multiple_choice_model,
            fields=[
                mc['question'],
                mc['choices'][0],
                mc['choices'][1],
                mc['choices'][2],
                mc['choices'][3],
                mc['correct']
            ]
        )
        deck.add_note(note)
    
    # Add fill in the blank cards
    for sentence, answer in cards_data['fill_blank']:
        note = genanki.Note(
            model=fill_blank_model,
            fields=[sentence, answer]
        )
        deck.add_note(note)
    
    return deck

# Create decks for both children with proper Anki hierarchy naming
yentl_deck_id = random.randrange(1 << 30, 1 << 31)
evah_deck_id = random.randrange(1 << 30, 1 << 31)

# Using :: creates a parent::child relationship in Anki
yentl_deck = create_deck("Yentl::Great White Sharks", yentl_deck_id, yentl_cards_data)
evah_deck = create_deck("Evah::Great White Sharks", evah_deck_id, evah_cards_data)

# Save the decks as separate .apkg files
genanki.Package(yentl_deck).write_to_file('yentl_great_white_sharks.apkg')
genanki.Package(evah_deck).write_to_file('evah_great_white_sharks.apkg')

print("✓ Anki decks created successfully!")
print("\nFiles created:")
print("  - yentl_great_white_sharks.apkg (for Yentl, age 9)")
print("  - evah_great_white_sharks.apkg (for Evah, age 7)")
print("\nIn Anki, these will appear as:")
print("  - Yentl::Great White Sharks")
print("  - Evah::Great White Sharks")
print("\nTo use these decks:")
print("1. Install Anki from https://apps.ankiweb.net/")
print("2. Open Anki")
print("3. Click 'File' → 'Import'")
print("4. Select each .apkg file")
print("5. The decks will be organized under 'Yentl' and 'Evah' parent folders")
print("6. Start studying!")