from zope.interface import Interface
from zope.schema import Iterable

class IEntity(Interface):
    """An entry in a entities directory. Can be a NGO, a students group or whatever
    """

class IEntitiesDirectory(Interface):
    """A directory grouping one or more entities.
    """
