from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.service_layer.unit_of_work import SqlalchemyUnitOfWork


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_engine = providers.Singleton(create_async_engine, config.db.url)

    db_session = providers.Factory(
        sessionmaker, bind=db_engine, class_=AsyncSession, expire_on_commit=False
    )

    uow = providers.Factory(SqlalchemyUnitOfWork, session_factory=db_session)
