from app import jsonrpc
from app.lib import auth, log_db
from flask import g


@jsonrpc.method('Log.add(category=str, level=str, msg=str, tags=list) -> list', validate=True)
@auth.requires_rpc_auth
def addLog(category, level, msg, tags=[]):
    log_id = log_db.addLog(g.auth.username, category, level, msg, tags)
    return { "logId": format(log_id) }


@jsonrpc.method('Log.getAll(category=str) -> list', validate=True)
@auth.requires_rpc_auth
def getLogAll(category):
    logs = log_db.getLogAll(g.auth.username, category)
    return {"logList": log_db.prepareData(logs) }



@jsonrpc.method('Log.getCount(category=str) -> list', validate=True)
@auth.requires_rpc_auth
def getLogCount(category):
    log_count = log_db.getLogCount(g.auth.username, category)
    return { "logCount": int(log_count) }
