import datetime
import typing

from sa.annotation import sa
from sqlalchemy.orm import relationship

import db

from sqlalchemy import Column, String, Integer, ForeignKey,DateTime


class SessionModel(db.Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True,autoincrement=True)
    server = Column(String, nullable=False)
    world = Column(String,nullable=False)
    user = Column(String,nullable=False)
    version = Column(String,nullable=False)
    session_date = Column(DateTime, default=datetime.datetime.utcnow)
    requests = relationship('RequestModel')



    def __init__(self,server,world,user,version):

        self.server = server
        self.world = world
        self.user = user
        self.version = version



    def __repr__(self):
        return self._repr(id=self.id,server=self.server,
                          world=self.world,user=self.user,version=self.version)

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