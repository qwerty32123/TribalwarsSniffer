import typing

import sa
from sqlalchemy.orm import relationship, declarative_base

import db

from sqlalchemy import Column, JSON, INTEGER, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import TEXT,JSONB


class ResponseModel(db.Base):

    __tablename__ = 'responses'

    id = Column(Integer, primary_key=True, autoincrement=True)

    headers = Column(JSON, nullable=False)
    status_code = Column(INTEGER, nullable=False)
    body = Column(TEXT, nullable=True)
    cookies = Column(TEXT,nullable=True)

    request_id = Column(INTEGER,ForeignKey('requests.id'))


    def __init__(self, headers, status_code):
        self.headers = headers
        self.status_code = status_code

    def __repr__(self):
        return self._repr(id=self.id, status=self.status_code)

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













