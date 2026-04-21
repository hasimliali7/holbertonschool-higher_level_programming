#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
Prints the new state's id after creation.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Verilənlər bazasına qoşulmaq üçün engine yaradırıq
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    # Session (sessiya) yaradırıq
    Session = sessionmaker(bind=engine)
    session = Session()

    # Yeni State obyekti yaradırıq
    new_state = State(name="Louisiana")
    
    # Obyekti sessiyaya əlavə edirik
    session.add(new_state)
    
    # Dəyişikliyi bazada təsdiqləyirik (COMMIT)
    session.commit()

    # Yeni yaranan ID-ni çap edirik
    print("{}".format(new_state.id))

    # Sessiyanı bağlayırıq
    session.close()
