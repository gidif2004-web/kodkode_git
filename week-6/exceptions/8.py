def load_config(path):
    try:
        with open(path, 'r') as f:
            line = f.readline
            int(line)
    except Exception as e:
        raise  RuntimeError("failed to loadconfig") from e
