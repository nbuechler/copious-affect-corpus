from app import app
import sys
from helpers.views import helpers

app.register_blueprint(helpers, url_prefix='/helpers')

from helpers.corpus_builder import corpus
app.register_blueprint(corpus, url_prefix='/corpus')

# Sets the port, or defaults to 80
if (len(sys.argv) > 1):
    port = int(sys.argv[1])
else:
    port=80

app.run(debug=True, host='0.0.0.0', port=port)
