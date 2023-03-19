from sqlalchemy import select

import db
from Request import RequestModel
from Response import ResponseModel
from Session import SessionModel

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:123@localhost:5432/tribalwars')
Session = sessionmaker(bind=engine)
session = Session()




from pprint import pprint

records = session.query(RequestModel).filter_by(session_id=7).filter(RequestModel.url.contains("signon"))
for p in records:
    pprint(vars(p))
