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


class Transaction(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "gas_price",
            "receipt_status",
            "receipt_contract_address",
            "receipt_cumulative_gas_used",
            "block_hash",
            "block_number",
            "to_address",
            "transaction_index",
            "nonce",
            "input",
            "receipt_gas_used",
            "block_timestamp",
            "gas",
            "from_address",
            "receipt_root",
            "value",
            "hash",
        }
        
        class properties:
            hash = schemas.StrSchema
            nonce = schemas.StrSchema
            transaction_index = schemas.StrSchema
            from_address = schemas.StrSchema
            to_address = schemas.StrSchema
            value = schemas.StrSchema
            gas = schemas.StrSchema
            gas_price = schemas.StrSchema
            input = schemas.StrSchema
            receipt_cumulative_gas_used = schemas.StrSchema
            receipt_gas_used = schemas.StrSchema
            receipt_contract_address = schemas.StrSchema
            receipt_root = schemas.StrSchema
            receipt_status = schemas.StrSchema
            block_timestamp = schemas.StrSchema
            block_number = schemas.StrSchema
            block_hash = schemas.StrSchema
            __annotations__ = {
                "hash": hash,
                "nonce": nonce,
                "transaction_index": transaction_index,
                "from_address": from_address,
                "to_address": to_address,
                "value": value,
                "gas": gas,
                "gas_price": gas_price,
                "input": input,
                "receipt_cumulative_gas_used": receipt_cumulative_gas_used,
                "receipt_gas_used": receipt_gas_used,
                "receipt_contract_address": receipt_contract_address,
                "receipt_root": receipt_root,
                "receipt_status": receipt_status,
                "block_timestamp": block_timestamp,
                "block_number": block_number,
                "block_hash": block_hash,
            }

    
    gas_price: MetaOapg.properties.gas_price
    receipt_status: MetaOapg.properties.receipt_status
    receipt_contract_address: MetaOapg.properties.receipt_contract_address
    receipt_cumulative_gas_used: MetaOapg.properties.receipt_cumulative_gas_used
    block_hash: MetaOapg.properties.block_hash
    block_number: MetaOapg.properties.block_number
    to_address: MetaOapg.properties.to_address
    transaction_index: MetaOapg.properties.transaction_index
    nonce: MetaOapg.properties.nonce
    input: MetaOapg.properties.input
    receipt_gas_used: MetaOapg.properties.receipt_gas_used
    block_timestamp: MetaOapg.properties.block_timestamp
    gas: MetaOapg.properties.gas
    from_address: MetaOapg.properties.from_address
    receipt_root: MetaOapg.properties.receipt_root
    value: MetaOapg.properties.value
    hash: MetaOapg.properties.hash
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gas"]) -> MetaOapg.properties.gas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gas_price"]) -> MetaOapg.properties.gas_price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input"]) -> MetaOapg.properties.input: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_cumulative_gas_used"]) -> MetaOapg.properties.receipt_cumulative_gas_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_gas_used"]) -> MetaOapg.properties.receipt_gas_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_contract_address"]) -> MetaOapg.properties.receipt_contract_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_root"]) -> MetaOapg.properties.receipt_root: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receipt_status"]) -> MetaOapg.properties.receipt_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hash", "nonce", "transaction_index", "from_address", "to_address", "value", "gas", "gas_price", "input", "receipt_cumulative_gas_used", "receipt_gas_used", "receipt_contract_address", "receipt_root", "receipt_status", "block_timestamp", "block_number", "block_hash", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_index"]) -> MetaOapg.properties.transaction_index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_address"]) -> MetaOapg.properties.from_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_address"]) -> MetaOapg.properties.to_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gas"]) -> MetaOapg.properties.gas: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gas_price"]) -> MetaOapg.properties.gas_price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input"]) -> MetaOapg.properties.input: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_cumulative_gas_used"]) -> MetaOapg.properties.receipt_cumulative_gas_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_gas_used"]) -> MetaOapg.properties.receipt_gas_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_contract_address"]) -> MetaOapg.properties.receipt_contract_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_root"]) -> MetaOapg.properties.receipt_root: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receipt_status"]) -> MetaOapg.properties.receipt_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_timestamp"]) -> MetaOapg.properties.block_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_number"]) -> MetaOapg.properties.block_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_hash"]) -> MetaOapg.properties.block_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hash", "nonce", "transaction_index", "from_address", "to_address", "value", "gas", "gas_price", "input", "receipt_cumulative_gas_used", "receipt_gas_used", "receipt_contract_address", "receipt_root", "receipt_status", "block_timestamp", "block_number", "block_hash", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        gas_price: typing.Union[MetaOapg.properties.gas_price, str, ],
        receipt_status: typing.Union[MetaOapg.properties.receipt_status, str, ],
        receipt_contract_address: typing.Union[MetaOapg.properties.receipt_contract_address, str, ],
        receipt_cumulative_gas_used: typing.Union[MetaOapg.properties.receipt_cumulative_gas_used, str, ],
        block_hash: typing.Union[MetaOapg.properties.block_hash, str, ],
        block_number: typing.Union[MetaOapg.properties.block_number, str, ],
        to_address: typing.Union[MetaOapg.properties.to_address, str, ],
        transaction_index: typing.Union[MetaOapg.properties.transaction_index, str, ],
        nonce: typing.Union[MetaOapg.properties.nonce, str, ],
        input: typing.Union[MetaOapg.properties.input, str, ],
        receipt_gas_used: typing.Union[MetaOapg.properties.receipt_gas_used, str, ],
        block_timestamp: typing.Union[MetaOapg.properties.block_timestamp, str, ],
        gas: typing.Union[MetaOapg.properties.gas, str, ],
        from_address: typing.Union[MetaOapg.properties.from_address, str, ],
        receipt_root: typing.Union[MetaOapg.properties.receipt_root, str, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        hash: typing.Union[MetaOapg.properties.hash, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Transaction':
        return super().__new__(
            cls,
            *_args,
            gas_price=gas_price,
            receipt_status=receipt_status,
            receipt_contract_address=receipt_contract_address,
            receipt_cumulative_gas_used=receipt_cumulative_gas_used,
            block_hash=block_hash,
            block_number=block_number,
            to_address=to_address,
            transaction_index=transaction_index,
            nonce=nonce,
            input=input,
            receipt_gas_used=receipt_gas_used,
            block_timestamp=block_timestamp,
            gas=gas,
            from_address=from_address,
            receipt_root=receipt_root,
            value=value,
            hash=hash,
            _configuration=_configuration,
            **kwargs,
        )
