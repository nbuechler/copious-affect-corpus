# copious-affect-corpus
A growing corpora of affects, where an affect is a word, sound, or another sensation that indicates the presence of an emotion, specifically what I call an R-EMOTION (see below).

# About the project
#### Affect
Affect is the measurable observation of an emotion.

	> e.g. A particularly relevant affect is natural language

	> Suggestion:  Learn about Affective Computing

Affects are defined by the observed reality (via some kind of sign) of a person.

	> Suggestion:  Learn about Semiotics

	Examples of affect include a facial expression, natural language sentence (Syntagam), tone, body temperature and/or another aspect of their person.

#### 'Representational' Emotions (R-EMOTION)
Linguistic labels (signifier/signified pairs) used to define an emotion.

	> Affects can be recorded and observed in sets of multiple R-EMOTION s.

	> e.g. A particularly popular set: Paul Ekman's Big 6

	> Suggestion:  Learn about EmotionML, see: https://www.w3.org/TR/emotion-voc/xml

#### 'Inferential' Emotions (I-EMOTION)
I-EMOTION s are an interpretation of how culture (as an emergent quality of human systems) constructs signifier/signified pairs of emotion where I-EMOTION s represent these as a vector of multiple R-EMOTION s.

	> Suggestion:  Learn about Anthropology

	> Suggestion:  Learn about Complexity Theory

	> Important: R-EMOTION s are symbolic and are not the same as 'Inferential' Emotions (I-EMOTION).

# History

* Appoximately 400 representational emotions are categorized by speedy-affect-scorer, these do not absolutely map to the inferential emotion of a human, which will be described later
* A representation of an emotion is a label like 'Love' which reminds us humans of signifier/signified pairs (see semiotics)
* Usually, one human maps their signifier/signified pairs to single a representation
* This project introduces the newer concept of an 'Inferential Emotion'
* The emotion that humans experience via the 'lens of culture' are not representational but rather inferential - and to best understand the meaning we ought to rely more on a scientific process rather than a simple signifier/signified pairs (label) that acts as a representation.
* One-to-one relationships of 'Inferential Emotion' to 'Representational Emotions' are not common with culture due to the 'Complexity of Culture'. Humans might sometimes confuse and argue with each other about emotions due to this complexity, and their lack of understanding of emergence (see complexity theory). Remember, a label/word is only a representation (sign) of an idea. 'Anger' - the word/label - is not an inferential emotion (in all but a one case, where culture is homogeneously angry). The inferential emotion therefore might be represented by something like a set of words; e.g. A combination of n-set of labels (Anger, Sadness, Fear, etc.)


# Scope
The scope includes a corpus of ~400 r-emotions only mapping to semantic data.

# Future Scope
* Find other forms of affect to tie to r-emotions; i.e. other forms of affect include, facial expressions and sound/tone

# Goals
This project aims to maintain a growing corpus of human affects, right now its only semantic information but it could include physical, visual, or other information as this grows.

# Tech stack
It will use Flask to do the api. It will probably also be structured in a way that it can be used in other projects, otherwise this wouldn't be MIT Licensed.

# Steps
* first, install virtualenv if not done so already -- https://virtualenv.pypa.io/en/latest/installation.html(https://virtualenv.pypa.io/en/latest/installation.html)
* then, run this command: $ virtualenv venv
* (make sure you get the'.'): $ . venv/bin/activate
* IMPORTANT: For windows 10 it is: . venv/Scripts/activate (on the git bash)
* pip install -r requirements.txt

# Run Server

```
python app/runserver.py 5000
```

# High level documentation for using the api

* Use corpus_buidler to build the raw corpora (affect-corpus).

* Then, use corpus_storage to build the processed corpora (affect-synopsis), like so:

<pre>
  <code>
    (root)/corpus_storage/save_complete_object/all/
  </code>
</pre>

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
See the pne of the 'emotion_list' spreadsheets in the directory at the root of this project: _unique_corpra

# Also notes...
* categories are thus the basis for grouping sets of r-emotion s
* multiple r-emotions correspond to a i-emotion (inferential emotion)

# Future questions
* how do some emotions (r or i) relate to others (r or i)?
* if we idenity some sets of emotions, how do they relate to each other?
* can we find the emtional state of different things (people, articles, etc)?

# Tech notes
to export the mongo database:

_for linux:_
```
mongodump -d affect-corpus -o ./<dir name>
```

for windows:
*(in my case...)*
```
mongodump.exe -d affect-corpus -o ..\..\..\..\..\Users\<USER>\<dir_name>
```

to import the mongo database:

_for linux:_
```
mongorestore --db affect-corpus ./mongo_database_backup/affect-corpus/
```

_for windows:_
```
mongorestore.exe --db affect-corpus C:\<root_dir>\copious-affect-corpus\mongo_database_backup\affect-corpus
```

# Note on mongorestore from docs
mongorestore can create a new database or add data to an existing database. However, mongorestore performs inserts only and does not perform updates. That is, if restoring documents to an existing database and collection and existing documents have the same value _id field as the to-be-restored documents, mongorestore will not overwrite those documents.

# Note on neo4j restore
I added a tar compressed file on (10.27.16) and instructions for restoring the neo4j database to a state where the R-Emotions are linked to their respective affect-words (saves about 2 hours in the energetic-etl project)

Source:
http://stackoverflow.com/questions/25567744/backup-neo4j-community-edition-offline-in-unix-mac-or-linux


# CREDITS
_To build a corpus ('Be Excellent to Each Other')_

Thesaurus service provided by words.bighugelabs.com:
https://words.bighugelabs.com/api.php

# License
MIT
