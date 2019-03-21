# -*- coding: utf-8 -*-

"""The Human Brain Pharmacome knowledge repository."""

import os

from bel_repository import BELMetadata, BELRepository
from bel_repository.utils import serialize_authors

__all__ = [
    'repository',
    'metadata',
    'main',
]

HERE = os.path.dirname(__file__)
VERSION = '0.0.1-dev'

# Author list will be sorted by last name
AUTHORS = [
    'Stephan Gebel',
    'Vanessa Lage-Rupprecht',
]

# All metadata is grouped here
metadata = BELMetadata(
    name='Enzyme Technology Internship 2019',
    version=VERSION,
    authors=serialize_authors(AUTHORS),
    contact='stephan.gebel@scai.fraunhofer.de',
    description="BEL Curation from the Enzyme Technology Internship 2019 at B-IT and Fraunhofer SCAI.",
    license='CC BY 4.0',
)

repository = BELRepository(
    HERE,
    bel_metadata=metadata,
)

main = repository.build_cli()
