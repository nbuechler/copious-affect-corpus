# copious-affect-corpus
copious-affect-corpus is meant to maintain a growing corpus of human affects, right now its only semantic information

# First set of scope is to make a corpus
We shall see if it goes to a second round of scope.

# Tech stack
It will use Flask to do the api. It will probably also be structured in a way that it can be used in other projects, otherwise this wouldn't be MIT Licensed.

# Steps
* first, install virtualenv if not done so already -- https://virtualenv.pypa.io/en/latest/installation.html(https://virtualenv.pypa.io/en/latest/installation.html)
* then, run this command: $ virtualenv venv
* (make sure you get the'.'): $ . venv/bin/activate
* pip install -r requirements.txt

# Run Server

```
python app/runserver.py 5000
```

# Requirements

* Flask==0.10.1
* Flask-Cors==2.1.0
* itsdangerous==0.24
* Jinja2==2.8
* MarkupSafe==0.23
* six==1.10.0
* Werkzeug==0.11.3
* wheel==0.24.0
* nltk==3.2.1
* requests==2.10.0
* Flask-PyMongo==0.3.1
* pymongo==2.9.3


# List of affects for this to data
```
acceptance, admiration, affection, amusement, anger, anticipation, anxiety, appraisal, appreciation, arousal, arrogance, awe, blame, boredom, calmness, compassion, compromise, concern, confidence, confusion, contempt, contentment, curiosity, denial, depression, desire, despair, dimension, disappointment, disgust, dissonance, distress, dread, ecstasy, edginess, embarrassment, enjoyment, enthusiasm, envy, eroticism, excitement, exuberance, fear, grace, gratification, gratitude, grief, happiness, harmony, hate, hope, humility, indifference, interest, irritation, jealousy, joy, love, lunacy, lust, mania, melancholy, pain, panic, patience, perturbation, pity, pleasure, pride, rage, relief, remorse, reproach, resentment, resignation, sadness, satisfaction, shame, shock, stress, surprise, triumph, trust, wonder, worry
```

# CREDITS
```
To build a corpus ('Be Excellent to Each Other')
```

_Thesaurus service provided by words.bighugelabs.com (https://words.bighugelabs.com/api.php)_

# License

MIT
