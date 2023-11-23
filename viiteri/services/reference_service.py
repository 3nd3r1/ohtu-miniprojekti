""" viiteri/services/reference_service """

from pybtex.database import BibliographyData, Entry
# from viiteri.repositories.article_repository import ReferenceRepository as default_repository


class ReferenceService:
    """ Service for handling references """

    def __init__(self, reference_repository=None):
        self._reference_repository = reference_repository

    def get_all_references(self):
        """ Returns all references """
        return self._reference_repository.get_all_references()

    def create_reference(self, cite_key, fields, cite_type='article'):
        """ Creates a new reference """
        bib_data = BibliographyData({cite_key: Entry(cite_type, fields)})
        return self._reference_repository.add_reference(bib_data.to_string('bibtex'))


reference_service = ReferenceService()