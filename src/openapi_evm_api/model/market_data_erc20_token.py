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


class MarketDataERC20Token(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class items(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "price_usd",
                    "price_24h_percent_change",
                    "token_logo",
                    "token_name",
                    "rank",
                    "token_decimals",
                    "token_symbol",
                    "contract_address",
                    "price_7d_percent_change",
                    "market_cap_usd",
                }
                
                class properties:
                    rank = schemas.IntSchema
                    token_name = schemas.StrSchema
                    token_symbol = schemas.StrSchema
                    token_logo = schemas.StrSchema
                    token_decimals = schemas.StrSchema
                    contract_address = schemas.StrSchema
                    price_usd = schemas.StrSchema
                    price_24h_percent_change = schemas.StrSchema
                    price_7d_percent_change = schemas.StrSchema
                    market_cap_usd = schemas.StrSchema
                    __annotations__ = {
                        "rank": rank,
                        "token_name": token_name,
                        "token_symbol": token_symbol,
                        "token_logo": token_logo,
                        "token_decimals": token_decimals,
                        "contract_address": contract_address,
                        "price_usd": price_usd,
                        "price_24h_percent_change": price_24h_percent_change,
                        "price_7d_percent_change": price_7d_percent_change,
                        "market_cap_usd": market_cap_usd,
                    }
        
            
            price_usd: MetaOapg.properties.price_usd
            price_24h_percent_change: MetaOapg.properties.price_24h_percent_change
            token_logo: MetaOapg.properties.token_logo
            token_name: MetaOapg.properties.token_name
            rank: MetaOapg.properties.rank
            token_decimals: MetaOapg.properties.token_decimals
            token_symbol: MetaOapg.properties.token_symbol
            contract_address: MetaOapg.properties.contract_address
            price_7d_percent_change: MetaOapg.properties.price_7d_percent_change
            market_cap_usd: MetaOapg.properties.market_cap_usd
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["rank"]) -> MetaOapg.properties.rank: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["token_name"]) -> MetaOapg.properties.token_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["token_decimals"]) -> MetaOapg.properties.token_decimals: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["contract_address"]) -> MetaOapg.properties.contract_address: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["price_usd"]) -> MetaOapg.properties.price_usd: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["price_24h_percent_change"]) -> MetaOapg.properties.price_24h_percent_change: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["price_7d_percent_change"]) -> MetaOapg.properties.price_7d_percent_change: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["market_cap_usd"]) -> MetaOapg.properties.market_cap_usd: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["rank", "token_name", "token_symbol", "token_logo", "token_decimals", "contract_address", "price_usd", "price_24h_percent_change", "price_7d_percent_change", "market_cap_usd", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["rank"]) -> MetaOapg.properties.rank: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["token_name"]) -> MetaOapg.properties.token_name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["token_symbol"]) -> MetaOapg.properties.token_symbol: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["token_logo"]) -> MetaOapg.properties.token_logo: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["token_decimals"]) -> MetaOapg.properties.token_decimals: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["contract_address"]) -> MetaOapg.properties.contract_address: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["price_usd"]) -> MetaOapg.properties.price_usd: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["price_24h_percent_change"]) -> MetaOapg.properties.price_24h_percent_change: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["price_7d_percent_change"]) -> MetaOapg.properties.price_7d_percent_change: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["market_cap_usd"]) -> MetaOapg.properties.market_cap_usd: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["rank", "token_name", "token_symbol", "token_logo", "token_decimals", "contract_address", "price_usd", "price_24h_percent_change", "price_7d_percent_change", "market_cap_usd", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                price_usd: typing.Union[MetaOapg.properties.price_usd, str, ],
                price_24h_percent_change: typing.Union[MetaOapg.properties.price_24h_percent_change, str, ],
                token_logo: typing.Union[MetaOapg.properties.token_logo, str, ],
                token_name: typing.Union[MetaOapg.properties.token_name, str, ],
                rank: typing.Union[MetaOapg.properties.rank, decimal.Decimal, int, ],
                token_decimals: typing.Union[MetaOapg.properties.token_decimals, str, ],
                token_symbol: typing.Union[MetaOapg.properties.token_symbol, str, ],
                contract_address: typing.Union[MetaOapg.properties.contract_address, str, ],
                price_7d_percent_change: typing.Union[MetaOapg.properties.price_7d_percent_change, str, ],
                market_cap_usd: typing.Union[MetaOapg.properties.market_cap_usd, str, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    price_usd=price_usd,
                    price_24h_percent_change=price_24h_percent_change,
                    token_logo=token_logo,
                    token_name=token_name,
                    rank=rank,
                    token_decimals=token_decimals,
                    token_symbol=token_symbol,
                    contract_address=contract_address,
                    price_7d_percent_change=price_7d_percent_change,
                    market_cap_usd=market_cap_usd,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MarketDataERC20Token':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
