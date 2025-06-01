users = {
    'student': 'linux123',
    'admin': 'shellcoach'
}

def authenticate(username, password):
    return users.get(username) == password

def register_user(username, password):
    if username in users:
        return False
    users[username] = password
    return True
