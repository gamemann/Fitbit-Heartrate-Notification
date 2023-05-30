def debug_message(cfg: dict, level: int = 1, message: str = "Debug Message"):
    if int(cfg["Debug"]) >= level:
        print("[%d] %s" % (level, message))