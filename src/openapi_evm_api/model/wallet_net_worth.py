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


class WalletNetWorth(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "native_balance",
            "total_networth_usd",
            "native_balance_decimals",
            "native_balance_usd",
        }
        
        class properties:
            native_balance = schemas.StrSchema
            native_balance_decimals = schemas.IntSchema
            native_balance_usd = schemas.StrSchema
            total_networth_usd = schemas.StrSchema
            __annotations__ = {
                "native_balance": native_balance,
                "native_balance_decimals": native_balance_decimals,
                "native_balance_usd": native_balance_usd,
                "total_networth_usd": total_networth_usd,
            }

    
    native_balance: MetaOapg.properties.native_balance
    total_networth_usd: MetaOapg.properties.total_networth_usd
    native_balance_decimals: MetaOapg.properties.native_balance_decimals
    native_balance_usd: MetaOapg.properties.native_balance_usd
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["native_balance"]) -> MetaOapg.properties.native_balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["native_balance_decimals"]) -> MetaOapg.properties.native_balance_decimals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["native_balance_usd"]) -> MetaOapg.properties.native_balance_usd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_networth_usd"]) -> MetaOapg.properties.total_networth_usd: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["native_balance", "native_balance_decimals", "native_balance_usd", "total_networth_usd", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["native_balance"]) -> MetaOapg.properties.native_balance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["native_balance_decimals"]) -> MetaOapg.properties.native_balance_decimals: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["native_balance_usd"]) -> MetaOapg.properties.native_balance_usd: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_networth_usd"]) -> MetaOapg.properties.total_networth_usd: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["native_balance", "native_balance_decimals", "native_balance_usd", "total_networth_usd", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        native_balance: typing.Union[MetaOapg.properties.native_balance, str, ],
        total_networth_usd: typing.Union[MetaOapg.properties.total_networth_usd, str, ],
        native_balance_decimals: typing.Union[MetaOapg.properties.native_balance_decimals, decimal.Decimal, int, ],
        native_balance_usd: typing.Union[MetaOapg.properties.native_balance_usd, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletNetWorth':
        return super().__new__(
            cls,
            *args,
            native_balance=native_balance,
            total_networth_usd=total_networth_usd,
            native_balance_decimals=native_balance_decimals,
            native_balance_usd=native_balance_usd,
            _configuration=_configuration,
            **kwargs,
        )
