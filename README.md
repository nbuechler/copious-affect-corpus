# copious-affect-corpus -- Goals
copious-affect-corpus is meant to maintain a growing corpus of human affects, right now its only semantic information

* Appoximately 400 (IN PROGRESS) representational emotions are categorized, these do not absolutely map to the neurological emotion of a human
* One human maps the neurological emotion - the one that they experience chemically/electrically - to a representation. This is what we call it via an english word.
* Humans will often map one neurological emotion to their defined preset of many representational emotions. This might be why we confuse and sometimes argue with each other about emotions. Remember that a word is only a represetnation of an idea. Anger - the word - is not a neurological emotion. The set of neurological impulses is actually the neurological emotion and it might be represented by something like a set of words; e.g. Anger, Sadness, Fear, etc.

# First set of scope is to make the corpus
We shall see if it goes to a second round of scope. But for now, the first set of scope includes a corpus of ~400 r-emotions only mapping to semantic data.

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
See the emotions spreadsheet in _unique_corpra
```

# Also notes...
*dimensions are known as a special kind of category
*categories are thus the basis for an r-emotion
*multiple r-emotions correspond to a n-emotion (future scope)

# Future questions
*how do some emotions (r or n) relate to others (r or n)?
*if we idenity some sets of emotions, how do they relate to each other?
*can we find the emtional state of different things (people, articles, etc)?

# Tech notes
to export the mongo database:
```
for linux:
mongodump -d affect-corpus -o ./<dir name>

for windows:
in my case...
mongodump.exe -d affect-corpus -o ..\..\..\..\..\Users\<USER>\<dir_name>
```
to import the mongo database:

```
for linux:
mongorestore --db affect-corpus ./mongo_database_backup/affect-corpus/

for windows:
mongorestore.exe --db affect-corpus C:\<root_dir>\copious-affect-corpus\mongo_database_backup\affect-corpus
```

## Note on mongorestore from docs

```
mongorestore can create a new database or add data to an existing database. However, mongorestore performs inserts only and does not perform updates. That is, if restoring documents to an existing database and collection and existing documents have the same value _id field as the to-be-restored documents, mongorestore will not overwrite those documents.
```

# CREDITS
```
To build a corpus ('Be Excellent to Each Other')
```

_Thesaurus service provided by words.bighugelabs.com (https://words.bighugelabs.com/api.php)_

# License

MIT
