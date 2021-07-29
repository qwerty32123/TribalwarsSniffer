import typing

import sa
from sqlalchemy.orm import relationship

import db

from sqlalchemy.dialects.postgresql import FLOAT,JSONB,TEXT

from sqlalchemy import Column, String, JSON, INTEGER, ForeignKey, Integer


class RequestModel(db.Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True,autoincrement=True)
    headers = Column(JSON,nullable=False)
    method = Column(String,nullable=False)
    size = Column(INTEGER,nullable=False)
    timestamp_end = Column(FLOAT,nullable=False)
    timestamp_start = Column(FLOAT,nullable=False)
    body = Column(TEXT,nullable=True)
    url = Column(TEXT,nullable=False)
    cookies = Column(TEXT,nullable=True)
    session_id =  Column(INTEGER,ForeignKey('sessions.id'))




    response = relationship('ResponseModel')


    def __init__(self,method,url):
        self.method = method
        self.url = url




    def __repr__(self):
        return self._repr(id=self.id,method=self.method,
                          url=self.url)

    def _repr(self, **fields: typing.Dict[str, typing.Any]) -> str:
        '''
        Helper for __repr__
        '''
        field_strings = []
        at_least_one_attached_attribute = False
        for key, field in fields.items():
            try:
                field_strings.append(f'{key}={field!r}')
            except sa.orm.exc.DetachedInstanceError:
                field_strings.append(f'{key}=DetachedInstanceError')
            else:
                at_least_one_attached_attribute = True
        if at_least_one_attached_attribute:
            return f"<{self.__class__.__name__}({','.join(field_strings)})>"
        return f"<{self.__class__.__name__} {id(self)}>"
