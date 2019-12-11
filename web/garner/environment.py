import os
from dotenv import load_dotenv

load_dotenv()


### Django Environment ###

ENVIRONMENT = os.environ.get('ENVIRONMENT')

### Plaid ###

PLAID_CLIENT_ID = os.environ.get('PLAID_CLIENT_ID')
PLAID_PUBLIC_KEY = os.environ.get('PLAID_PUBLIC_KEY')
PLAID_SECRET = os.environ.get('PLAID_SECRET')
PLAID_ENVIRONMENT = os.environ.get('PLAID_ENVIRONMENT')
