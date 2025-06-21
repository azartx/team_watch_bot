import os

TG_SHORT_GROUP_ID="-1002823803500"

# TODO: move group id to env vars
def getTargerGroupId() -> str:
    return os.getenv(TG_SHORT_GROUP_ID)