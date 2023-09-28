from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

# Replace 'your_username', 'your_password', and 'your_database' with your MySQL credentials.
engine = create_engine('mysql://your_username:your_password@localhost:3306/your_database')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example: Add a new state to the database
new_state = State(name='New State')
session.add(new_state)
session.commit()

# Query and print states from the database
states = session.query(State).all()
for state in states:
    print(state.id, state.name)

# Close the session
session.close()
