from sqlalchemy import select
from sqlalchemy.orm import Session
from blueprints.data_provider.engine import engine
from blueprints.data_provider.dtos.user_accounts import User_Account
from argon2 import PasswordHasher

session = Session(engine)
ph = PasswordHasher()


def get_user_account_dtos():

    stmt = select(User_Account)
    return session.scalars(stmt)


def encrypt(plain_text_password):
    hashed_password = ph.hash(plain_text_password)
    return hashed_password


def add_user_account_dto(user_name, first_name, last_name, email, password):

    new_user_account = User_Account(
        user_name, first_name, last_name, email, encrypt(password), is_deleted=False
    )

    session.add(new_user_account)
    session.commit()
    return new_user_account


def get_user_account_dto_by_id(user_account_id):

    """stmt = select(User_Account).where(User_Account.id == user_account_id)"""
    """return session.query(User_Account).filter(User_Account.id == user_account_id)"""
    return session.query(User_Account).get(user_account_id)


def delete_user_account_dto_by_id(user_account_id):
    user_account = get_user_account_dto_by_id(user_account_id)
    user_account.is_deleted = True
    session.commit()

    return {"User Account " + user_account.user_name + " deleted"}


def update_user_account_dto_by_id(
    user_account_id,
    new_user_name,
    new_first_name,
    new_last_name,
    new_email,
    new_password,
):
    user_account_to_update = get_user_account_dto_by_id(user_account_id)

    user_account_to_update.user_name = new_user_name
    user_account_to_update.first_name = new_first_name
    user_account_to_update.last_name = new_last_name
    user_account_to_update.email = new_email
    user_account_to_update.password = encrypt(new_password)

    session.commit()

    return user_account_to_update
