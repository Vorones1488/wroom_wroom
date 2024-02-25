from datetime import datetime

from sqlalchemy import MetaData, Table, Integer, String, TIMESTAMP, ForeignKey, Column, JSON, Text

metadata = MetaData()

# Здесь хронятся модели баз данных пользователя
# нужно изменить на декларативный тиль 2.0

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('family', String),
    Column('email', String, nullable=False),
    Column('password', String, nullable=False),
    Column('address', Text, nullable=False),
    Column('phone_number', Integer),
    Column('data_time', TIMESTAMP, default=datetime.utcnow),
    Column('user_status', JSON, nullable=False)
)

order = Table(
    'order',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('users.id'), nullable=False),
    Column('amount', Integer, nullable=False)



)
