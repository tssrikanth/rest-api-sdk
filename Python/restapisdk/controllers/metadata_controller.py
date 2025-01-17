# -*- coding: utf-8 -*-

"""
restapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from restapisdk.api_helper import APIHelper
from restapisdk.configuration import Server
from restapisdk.controllers.base_controller import BaseController
from restapisdk.http.auth.o_auth_2 import OAuth2
from restapisdk.models.metadata_tag_response import MetadataTagResponse
from restapisdk.models.home_liveboard_response import HomeLiveboardResponse
from restapisdk.exceptions.error_response_exception import ErrorResponseException


class MetadataController(BaseController):

    """A Controller to access Endpoints in the restapisdk API."""

    def __init__(self, config, call_back=None):
        super(MetadataController, self).__init__(config, call_back)

    def get_tag(self,
                name=None,
                id=None):
        """Does a GET request to /api/rest/v2/metadata/tag.

        To get details of a specific tag, use this endpoint. At least one of
        id or name of tag is required. When both are given, then id will be
        considered.

        Args:
            name (string, optional): Name of the tag
            id (string, optional): The GUID of the tag

        Returns:
            MetadataTagResponse: Response from the API. Details of the tag
                searched for

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/tag'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'name': name,
            'id': id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': self.config.content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, MetadataTagResponse.from_dictionary)

        return decoded

    def create_tag(self,
                   body):
        """Does a POST request to /api/rest/v2/metadata/tag/create.

        To programmatically create tags, use this endpoint

        Args:
            body (ApiRestV2MetadataTagCreateRequest): TODO: type description
                here.

        Returns:
            MetadataTagResponse: Response from the API. Details of the tag
                created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/tag/create'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, MetadataTagResponse.from_dictionary)

        return decoded

    def update_tag(self,
                   body):
        """Does a PUT request to /api/rest/v2/metadata/tag/update.

        To programmatically update tags, use this endpoint. At least one of id
        or name of tag is required. When both are given, then id will be
        considered.

        Args:
            body (ApiRestV2MetadataTagUpdateRequest): TODO: type description
                here.

        Returns:
            bool: Response from the API. Successfully updated the tag

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/tag/update'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def delete_tag(self,
                   name=None,
                   id=None):
        """Does a DELETE request to /api/rest/v2/metadata/tag/delete.

        To programmatically delete tags, use this endpoint. At least one of id
        or name of tag is required. When both are given, then id will be
        considered.

        Args:
            name (string, optional): Name of the tag
            id (string, optional): The GUID of the tag

        Returns:
            bool: Response from the API. Successfully deleted the tag

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/tag/delete'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'name': name,
            'id': id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': self.config.content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def assign_tag(self,
                   body):
        """Does a POST request to /api/rest/v2/metadata/tag/assign.

        To programmatically assign tags to a metadata object, such as a
        liveboard, search answer, table, worksheet, or view, use this
        endpoint.  At least one of id or name of tag is required. When both
        are given, then id will be considered.

        Args:
            body (ApiRestV2MetadataTagAssignRequest): TODO: type description
                here.

        Returns:
            bool: Response from the API. Successfully assigned the tag to the
                metadata object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/tag/assign'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def unassign_tag(self,
                     body):
        """Does a POST request to /api/rest/v2/metadata/tag/unassign.

        To programmatically unassign tags to a metadata object, such as a
        liveboard, search answer, table, worksheet, or view, use this
        endpoint. At least one of id or name of tag is required. When both are
        given, then id will be considered.

        Args:
            body (ApiRestV2MetadataTagUnassignRequest): TODO: type description
                here.

        Returns:
            bool: Response from the API. Successfully unassigned the tag to
                the metadata object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/tag/unassign'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def assign_favorite(self,
                        body):
        """Does a POST request to /api/rest/v2/metadata/favorite/assign.

        To programmatically assign objects to favorites for a given user
        account, use this endpoint. At least one of user id or username is
        required. When both are given, then id will be considered.

        Args:
            body (ApiRestV2MetadataFavoriteAssignRequest): TODO: type
                description here.

        Returns:
            bool: Response from the API. Successfully assigned the object to
                favorites of the user

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/favorite/assign'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def unassign_favorite(self,
                          body):
        """Does a POST request to /api/rest/v2/metadata/favorite/unassign.

        To programmatically unassign objects to favorites for a given user
        account, use this endpoint. At least one of user id or username is
        required. When both are given, then id will be considered.Screen
        reader support enabled.

        Args:
            body (ApiRestV2MetadataFavoriteUnassignRequest): TODO: type
                description here.

        Returns:
            bool: Response from the API. Successfully unassigned the object
                from favorites of the user

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/favorite/unassign'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def get_homeliveboard(self,
                          user_name=None,
                          user_id=None):
        """Does a GET request to /api/rest/v2/metadata/homeliveboard.

        To get the name and id of liveboard that is set as a home liveboard
        for a user, use this endpoint. At least one of user id or username is
        required. When both are given, then id will be considered.

        Args:
            user_name (string, optional): TODO: type description here.
            user_id (string, optional): The GUID of the user

        Returns:
            HomeLiveboardResponse: Response from the API. The homeliveboard
                assigned to the user

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/homeliveboard'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'userName': user_name,
            'userId': user_id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': self.config.content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, HomeLiveboardResponse.from_dictionary)

        return decoded

    def assign_homeliveboard(self,
                             body):
        """Does a POST request to /api/rest/v2/metadata/homeliveboard/assign.

        To assign a specific liveboard as a home liveboard for a user, use
        this endpoint. At least one of user id or username is required. When
        both are given, then id will be considered.

        Args:
            body (ApiRestV2MetadataHomeliveboardAssignRequest): TODO: type
                description here.

        Returns:
            bool: Response from the API. Successfully assigned the
                homeliveboard to the user

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/homeliveboard/assign'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def unassign_homeliveboard(self,
                               body):
        """Does a POST request to /api/rest/v2/metadata/homeliveboard/unassign.

        To unassign the home liveboard set for a user, use this endpoint. At
        least one of user id or username is required. When both are given,
        then id will be considered.

        Args:
            body (ApiRestV2MetadataHomeliveboardUnassignRequest): TODO: type
                description here.

        Returns:
            bool: Response from the API. Successfully unassigned the
                homeliveboard to the user

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/homeliveboard/unassign'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def get_incomplete_objects(self):
        """Does a GET request to /api/rest/v2/metadata/incomplete.

        To get a list of objects with incomplete metadata, use this endpoint

        Returns:
            object: Response from the API. An object representing map of set
                of incomplete object headers key ed by type

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/incomplete'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': self.config.content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text

        return decoded

    def get_object_header(self,
                          mtype,
                          output_fields=None,
                          offset=None,
                          batch_size=None,
                          sort_by='DEFAULT',
                          sort_order='DEFAULT',
                          name_pattern=None,
                          fetch_id=None,
                          skip_id=None,
                          show_hidden=None,
                          auto_created=None):
        """Does a GET request to /api/rest/v2/metadata/headers.

        To get header details for metadata objects, use this endpoint. You can
        provide as input selective fields to get the data for.

        Args:
            mtype (Type2Enum): Type of the metadata object being searched.
            output_fields (list of string, optional): Array of header field
                names that need to be included in the header response
            offset (string, optional): The batch offset, starting from where
                the records should be included in the response. If no input is
                provided then offset starts from 0.
            batch_size (string, optional): The number of records that should
                be included in the response starting from offset position. If
                no input is provided then first page is included in the
                response.
            sort_by (SortByEnum, optional): Field based on which the response
                needs to be ordered.
            sort_order (SortOrderEnum, optional): Order in which sortBy should
                be applied.
            name_pattern (string, optional): A pattern to match the name of
                the metadata object. This parameter supports matching
                case-insensitive strings. For a wildcard match, use %.
            fetch_id (list of string, optional): A JSON array containing the
                GUIDs of the metadata objects that you want to fetch.
            skip_id (list of string, optional): A JSON array containing the
                GUIDs of the metadata objects that you want to skip.
            show_hidden (bool, optional): When set to true, returns details of
                the hidden objects, such as a column in a worksheet or a
                table.
            auto_created (AutoCreatedEnum, optional): String for UI and
                backend boolean- A flag to indicate whether to list only the
                auto created objects. When no value is provided as input then
                all objects are returned.

        Returns:
            object: Response from the API. Header details based on the search
                criteria and requested output fields

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/headers'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'type': mtype,
            'outputFields': output_fields,
            'offset': offset,
            'batchSize': batch_size,
            'sortBy': sort_by,
            'sortOrder': sort_order,
            'namePattern': name_pattern,
            'fetchId': fetch_id,
            'skipId': skip_id,
            'showHidden': show_hidden,
            'autoCreated': auto_created
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': self.config.content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text

        return decoded

    def get_object_visualization_header(self,
                                        id):
        """Does a GET request to /api/rest/v2/metadata/vizheaders.

        Use this endpoint to get header details of visualization charts for a
        given liveboard or answer. At least one of id or name of liveboard or
        answer is required. When both are given, then id will be considered.

        Args:
            id (string): The GUID of the liveboard or answer

        Returns:
            list of object: Response from the API. Header details of
                vizualization charts in the liveboard/answer object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/vizheaders'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'id': id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': self.config.content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text)

        return decoded

    def get_object_detail(self,
                          mtype,
                          id,
                          show_hidden=None,
                          drop_question_details=None,
                          version=None):
        """Does a GET request to /api/rest/v2/metadata/details.

        Use this endpoint to get full details of metadata objects

        Args:
            mtype (Type3Enum): Type of the metadata object being searched.
                Valid values
            id (list of string): A JSON array of GUIDs of the objects.
            show_hidden (bool, optional): When set to true, returns details of
                the hidden objects, such as a column in a worksheet or a
                table.
            drop_question_details (bool, optional): When set to true, the
                search assist data associated with a worksheet is not included
                in the API response. This attribute is applicable only for
                LOGICAL_TABLE data type.
            version (string, optional): Specify the version to retrieve the
                objects from. By default, the API returns metadata for all
                versions of the object.

        Returns:
            list of object: Response from the API. Full details of metadata
                objects searched for

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/details'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'type': mtype,
            'id': id,
            'showHidden': show_hidden,
            'dropQuestionDetails': drop_question_details,
            'version': version
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': self.config.content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text)

        return decoded

    def export_object_tml(self,
                          body):
        """Does a POST request to /api/rest/v2/metadata/tml/export.

        To export ThoughtSpot objects represented in ThoughtSpot Modeling
        Language (TML), use this endpoint

        Args:
            body (ApiRestV2MetadataTmlExportRequest): TODO: type description
                here.

        Returns:
            object: Response from the API. Successfully exported the requested
                object as TML

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/tml/export'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text

        return decoded

    def import_object_tml(self,
                          body):
        """Does a POST request to /api/rest/v2/metadata/tml/import.

        To import ThoughtSpot objects represented in ThoughtSpot Modeling
        Language (TML), use this endpoint

        Args:
            body (ApiRestV2MetadataTmlImportRequest): TODO: type description
                here.

        Returns:
            object: Response from the API. Successfully imported the objects
                in TML

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/metadata/tml/import'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text

        return decoded
