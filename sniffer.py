"""Send a reply from the proxy without sending any data to the remote server."""
import json

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from Request import RequestModel
from Response import ResponseModel
from Session import SessionModel

from mitmproxy import http

from CookieParser import format_cookies



class SaveTribalwarsRequests:
    def __init__(self):
        self.server = 'www.tribalwars.com'
        self.world = 'en120'
        self.user = 'zumodorslok'
        self.version = 1.0
        self.session_object =  SessionModel(server=self.server, world=self.world, version=self.version, user=self.user)
        self.engine = create_engine('postgresql://postgres:123@localhost:5432/tribalwars')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


        self.session.expire_on_commit = False


        self.Base = declarative_base()


        self.session.add(self.session_object)

        self.session.commit()
    # def createSession(self):
    #
    #     with Session(self.engine) as session:
    #         http_session =
    #         session.add(http_session)
    #         # We add created object to our DB
    #         session.flush()
    #         # At this point, the object  has been pushed to the DB,
    #         # and has been automatically assigned a unique primary key id
    #         session.refresh(http_session)
    #         print(http_session.id)
    #         # refresh updates given object in the session with its state in the DB
    #         # (and can also only refresh certain attributes - search for documentation)
    #         self.session_object = http_session

    def response(self, flow: http.HTTPFlow) -> None:

        try:
            if flow.request.headers['x-ig-client-version'] and self.session_object.version == None:
                self.session_object.version = flow.request.headers['x-ig-client-version']

                self.session.commit()
        except KeyError:
            pass

        request_url = flow.request.url

        Request = RequestModel(method=flow.request.method, url=request_url)
        request_headers = dict(flow.request.headers.items())
        request_headers = json.dumps(request_headers)
        Request.headers = request_headers


        Request.cookies = str(dict(flow.request.cookies))
        Request.body = ""
        if len(flow.request.text) >= 1:
            Request.body = flow.request.text

        Request.timestamp_start = flow.request.timestamp_start
        Request.timestamp_end = flow.request.timestamp_end
        Request.size = len(flow.request.content)

        response_headers = dict(flow.response.headers.items())


        response_headers = json.dumps(response_headers)

        Response = ResponseModel(headers=response_headers,
                                 status_code=flow.response.status_code)

        Response.body = ""
        if len(flow.response.text) >= 1:
            Response.body = flow.response.text.replace("\x00", "\uFFFD")

        Response.cookies = str(dict(flow.response.cookies))

        self.session.add(Response)

        self.session.commit()

        Request.response = [Response]
        self.session.add(Request)
        self.session.commit()

        self.session_object.requests.extend([Request])

        self.session.commit()


addons = [SaveTribalwarsRequests()]



































