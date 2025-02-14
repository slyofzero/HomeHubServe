def to_dict(object):
    return {column.name: getattr(object, column.name) for column in object.__table__.columns}