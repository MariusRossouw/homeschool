# Navigate to your folder
cd "Great White Sharks"

# Create a virtual environment (only need to do this once)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Now install genanki (this is safe inside the venv)
pip install genanki

# Run your script
python create_shark_anki_decks.py