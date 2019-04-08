from app.api import bp

@bp.route('/users/<int:id>', methods = ['GET'])
def get_user_id(id):
    pass

@bp.route('/users', methods = ['GET'])
def get_users():
    pass

@bp.route('/users/<int:id>/sessions', methods = ['GET', 'POST'])
def get_sessions(id):
    pass

@bp.route('/users/<int:id>/events', methods = ['GET', 'POST'])
def get_events(id):
    pass

@bp.route('/users', methods = ['POST'])
def create_user():
    pass

@bp.route('/users/<int:id>', methods = ['PUT'])
def update_user(id):
    pass