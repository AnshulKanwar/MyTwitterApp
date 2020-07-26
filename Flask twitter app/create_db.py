from Twitter import create_app, db
from Twitter.Models import User, Tweet

app = create_app()
app.app_context().push()
db.create_all()
