import db
import Response
import Request

import Session



def run():
    pass

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()
