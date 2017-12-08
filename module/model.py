import sys
sys.path.append('../')

class User():
#class User(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(80), unique=True)
    #email = db.Column(db.String(120), unique=True)

    def __init__(self, username):
        self.username = username
        #self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    # used for login plugin
    @property
    def is_active(self):
        return True
    @property
    def is_authenticated(self):
        return True
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            #return unicode(self.id)
            return "123"
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')


#class Post(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    body = db.Column(db.String(140))
#    timestamp = db.Column(db.DateTime)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#    def __repr__(self):
#        return '<Post %r>' % (self.body)
