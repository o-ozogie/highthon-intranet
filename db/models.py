from db.connection import db
import datetime

class Status(db.Enum):
    WAIT_SETTLEMENT = 'wait_settlement'
    WAIT_CONFIRM = 'wait_confirm'
    CONFIRM = 'confirm'
    WAIT_REFUND = 'wait_refund'
    CANCELED = 'canceled'

class Major(db.Enum):
    REAL_LIFE = 'real-life'
    GAME = 'game'

class Position(db.Enum):
    DEVELOP = 'develop'
    DESIGN = 'design'

class Applicant(db.Document):
    phone_no = db.StringField(required=True, unique=True)
    name = db.StringField(required=True, max_length=10)
    grade = db.IntField(required=True, min=1, max=3)
    email = db.StringField(required=True, max_length=50)
    num_of_waiting = db.IntField()
    school = db.StringField(required=True,)
    account = db.StringField(required=True,)
    password = db.StringField(required=True,)
    status = db.EnumField(Status, default=Status.WAIT_SETTLEMENT)
    major = db.EnumField(Major)
    position = db.EnumField(Position)
    applicant_at = db.DateTimeField(default=datetime.utcnow)
    settlement_at = db.DateTimeField()

class Team(db.Document):
    service_name = db.StringField(required=True, unique=True)
    name = db.StringField()
    major = db.EnumField(Major)
    members = db.ListField()
    reviews = db.DictField()

class Reviewer(db.Document):
    name = db.StringField(required=True, unique=True)
    scret = db.StringField()

class ItemOfReview(db.Document):
    name = db.StringField()
    description = db.StringField()
    max_score = db.IntField()

class Admin(db.Document):
    email = db.StringField()
    password = db.StringField()
    name = db.StringField()

class Notice(db.Document):
    title = db.StringField()
    content = db.StringField()
    attached_files = db.ListField()
    created_at = db.DateTimeField(default=datetime.utcnow)

