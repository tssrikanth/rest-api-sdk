# -*- coding: utf-8 -*-

"""
restapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiRestV2DependencyRequest(object):

    """Implementation of the 'Api Rest V2 Dependency Request' model.

    TODO: type model description here.

    Attributes:
        mtype (Type10Enum): Type of the data object
        id (list of string): A JSON array of GUIDs of the objects
        batch_size (int): he maximum number of batches to fetch in a query. If
            this attribute is not defined, the value specified in the cluster
            configuration is used. To get the list of all dependent objects in
            a single query, define the batch size attribute as -1

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "id": 'id',
        "batch_size": 'batchSize'
    }

    def __init__(self,
                 mtype=None,
                 id=None,
                 batch_size=None):
        """Constructor for the ApiRestV2DependencyRequest class"""

        # Initialize members of the class
        self.mtype = mtype
        self.id = id
        self.batch_size = batch_size

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        mtype = dictionary.get('type')
        id = dictionary.get('id')
        batch_size = dictionary.get('batchSize')

        # Return an object of this model
        return cls(mtype,
                   id,
                   batch_size)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
