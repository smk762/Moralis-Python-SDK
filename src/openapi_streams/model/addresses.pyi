# coding: utf-8

"""
    Streams Api

    API that provides access to Moralis Streams  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_streams import schemas  # noqa: F401


class Addresses(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "address",
        }
        
        class properties:
            address = schemas.StrSchema
            __annotations__ = {
                "address": address,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    address: MetaOapg.properties.address
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Addresses':
        return super().__new__(
            cls,
            *_args,
            address=address,
            _configuration=_configuration,
        )
