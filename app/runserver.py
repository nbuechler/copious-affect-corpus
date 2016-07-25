from app import app
import sys
from helpers.views import helpers
from corpus_storage.views import corpus_storage
from corpus_builder.views import corpus_builder

app.register_blueprint(helpers, url_prefix='/helpers')
app.register_blueprint(corpus_storage, url_prefix='/corpus_storage')
app.register_blueprint(corpus_builder, url_prefix='/corpus')

# Sets the port, or defaults to 80
if (len(sys.argv) > 1):
    port = int(sys.argv[1])
else:
    port=80

app.run(debug=True, host='0.0.0.0', port=port)
