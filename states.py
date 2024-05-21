from aiogram.fsm.state import State, StatesGroup


class Application(StatesGroup):

    name = State()
    age = State()
    method = State()
    comment = State()


class Mailing(StatesGroup):

    draft = State()
