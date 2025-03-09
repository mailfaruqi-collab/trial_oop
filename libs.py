class UserDatabase:
    def __init__(self):
        """Initialize the user database."""
        self.users = []
        self.counter = 1  # To generate unique IDs

    def add_user(self, name, latitude, longitude, vehicle_type):
        """Add a new user to the database."""
        user = {
            "id": self.counter,
            "name": name,
            "latitude": latitude,
            "longitude": longitude,
            "vehicle_type": vehicle_type
        }
        self.users.append(user)
        self.counter += 1

    def get_users(self):
        """Retrieve all users."""
        return self.users

    def remove_user(self, user_id):
        """Remove a user by ID."""
        self.users = [user for user in self.users if user["id"] != user_id]