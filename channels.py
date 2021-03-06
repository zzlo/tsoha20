from db import db

def is_channel(channel_name):
    if len(channel_name) > 30:
        return False

    sql = "SELECT * FROM channels WHERE name=:channel_name"
    channel_name = channel_name.lower()
    result = db.session.execute(sql, {"channel_name":channel_name})
    channel = result.fetchone()
    if channel == None:
        return create_channel(channel_name)
    else:
        return True

def create_channel(channel_name):
    try:
        sql = "INSERT INTO channels (name) VALUES (:channel_name)"
        db.session.execute(sql, {"channel_name":channel_name})
        db.session.commit()
    except:
        return False
    return True

def get_channel_id(channel_name):
    sql = "SELECT id FROM channels WHERE name=:channel_name"
    channel_name = channel_name.lower()
    result = db.session.execute(sql, {"channel_name":channel_name})
    channel_id = result.fetchone()[0]
    return channel_id

is_channel("main")     