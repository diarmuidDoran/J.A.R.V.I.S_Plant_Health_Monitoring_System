from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from blueprints.data_provider.engine import Base

plant_user_table = Table(
    "plant_user",
    Base.metadata,
    Column(
        "plant_id",
        Integer,
        ForeignKey(
            "plant.id",
        ),
        primary_key=True,
    ),
    Column(
        "user_id",
        Integer,
        ForeignKey(
            "user_account.id",
        ),
        primary_key=True,
    ),
)


class User_Account(Base):
    __tablename__ = "user_account"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_name = Column("user_name", String(255))
    first_name = Column("first_name", String(255))
    last_name = Column("last_name", String(255))
    email = Column("email", String(255))
    password = Column("password", String(255))
    is_deleted = Column(
        "is_deleted",
        Boolean,
    )

    plants_b = relationship(
        "Plant",
        secondary=plant_user_table,
        back_populates="users",
    )

    def __init__(self, user_name, first_name, last_name, email, password, is_deleted):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_deleted = is_deleted

    def __repr__(self):
        return (
            f"User_Account(id={self.id!r}, user_name={self.user_name!r}, first_name={self.first_name!r},"
            f"last_name={self.last_name!r}, email={self.email!r}, password={self.password!r}, "
            f"is_deleted={self.is_deleted!r})"
        )
