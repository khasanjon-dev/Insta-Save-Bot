from sqlalchemy.orm import Session

from utils.db_api.db.session import get_db
from utils.db_api.models import Users


class DataBase:
    @staticmethod
    def create_or_update(data: dict):
        session: Session = next(get_db())
        user = session.query(Users).filter_by(telegram_id=data['telegram_id']).count()
        if user:
            session.query(Users).filter(Users.telegram_id == data['telegram_id']). \
                update(data, synchronize_session=False)
        else:
            user = Users(**data)
            session.add(user)

        session.commit()
        session.close()


db = DataBase()
