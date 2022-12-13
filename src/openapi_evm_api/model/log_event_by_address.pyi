# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1
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

from openapi_evm_api import schemas  # noqa: F401


class LogEventByAddress(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "topic1",
            "topic2",
            "address",
            "topic0",
            "data",
            "topic3",
            "block_timestamp",
            "block_hash",
            "block_number",
            "transaction_index",
            "log_index",
            "transaction_hash",
        }
        
        class properties:
            transaction_hash = schemas.StrSchema
            address = schemas.StrSchema
            block_timestamp = schemas.StrSchema
            block_number = schemas.StrSchema
            block_hash = schemas.StrSchema
            data = schemas.StrSchema
            topic0 = schemas.StrSchema
            topic1 = schemas.StrSchema
            topic2 = schemas.StrSchema
            topic3 = schemas.StrSchema
            transaction_index = schemas.IntSchema
            log_index = schemas.IntSchema
            __annotations__ = {
                "transaction_hash": transaction_hash,
                "address": address,
                "block_timestamp": block_timestamp,
                "block_number": block_number,
                "block_hash": block_hash,
                "data": data,
                "topic0": topic0,
                "topic1": topic1,
                "topic2": topic2,
                "topic3": topic3,
                "transaction_index": transaction_index,
                "log_index": log_index,
            }

    
    topic1: MetaOapg.properties.topic1
    topic2: MetaOapg.properties.topic2
    address: MetaOapg.properties.address
    topic0: MetaOapg.properties.topic0
    data: MetaOapg.properties.data
    topic3: MetaOapg.properties.topic3
    block_timestamp: MetaOapg.properties.block_timestamp
    block_hash: MetaOapg.properties.block_hash
    block_number: MetaOapg.properties.block_number
    transaction_index: MetaOapg.properties.transaction_index
    log_index: MetaOapg.properties.log_index
    transaction_hash: MetaOapg.properties.transaction_hash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic0"]) -> MetaOapg.properties.topic0: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic1"]) -> MetaOapg.properties.topic1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic2"]) -> MetaOapg.properties.topic2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic3"]) -> MetaOapg.properties.topic3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["log_index"]) -> MetaOapg.properties.log_index: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "address", "block_timestamp", "block_number", "block_hash", "data", "topic0", "topic1", "topic2", "topic3", "transaction_index", "log_index", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_hash"]) -> MetaOapg.properties.transaction_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic0"]) -> MetaOapg.properties.topic0: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic1"]) -> MetaOapg.properties.topic1: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic2"]) -> MetaOapg.properties.topic2: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic3"]) -> MetaOapg.properties.topic3: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["log_index"]) -> MetaOapg.properties.log_index: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transaction_hash", "address", "block_timestamp", "block_number", "block_hash", "data", "topic0", "topic1", "topic2", "topic3", "transaction_index", "log_index", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        topic1: typing.Union[MetaOapg.properties.topic1, str, ],
        topic2: typing.Union[MetaOapg.properties.topic2, str, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        topic0: typing.Union[MetaOapg.properties.topic0, str, ],
        data: typing.Union[MetaOapg.properties.data, str, ],
        topic3: typing.Union[MetaOapg.properties.topic3, str, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, str, ],
        block_hash: typing.Union[MetaOapg.properties.block_hash, str, ],
        block_number: typing.Union[MetaOapg.properties.block_number, str, ],
        transaction_index: typing.Union[MetaOapg.properties.transaction_index, decimal.Decimal, int, ],
        log_index: typing.Union[MetaOapg.properties.log_index, decimal.Decimal, int, ],
        transaction_hash: typing.Union[MetaOapg.properties.transaction_hash, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LogEventByAddress':
        return super().__new__(
            cls,
            *_args,
            topic1=topic1,
            topic2=topic2,
            address=address,
            topic0=topic0,
            data=data,
            topic3=topic3,
            block_timestamp=block_timestamp,
            block_hash=block_hash,
            block_number=block_number,
            transaction_index=transaction_index,
            log_index=log_index,
            transaction_hash=transaction_hash,
            _configuration=_configuration,
            **kwargs,
        )
