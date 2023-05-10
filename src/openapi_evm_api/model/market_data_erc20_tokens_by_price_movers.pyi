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


class MarketDataERC20TokensByPriceMovers(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "gainers",
            "losers",
        }
        
        class properties:
        
            @staticmethod
            def gainers() -> typing.Type['MarketDataERC20Token']:
                return MarketDataERC20Token
        
            @staticmethod
            def losers() -> typing.Type['MarketDataERC20Token']:
                return MarketDataERC20Token
            __annotations__ = {
                "gainers": gainers,
                "losers": losers,
            }
    
    gainers: 'MarketDataERC20Token'
    losers: 'MarketDataERC20Token'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainers"]) -> 'MarketDataERC20Token': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["losers"]) -> 'MarketDataERC20Token': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gainers", "losers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainers"]) -> 'MarketDataERC20Token': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["losers"]) -> 'MarketDataERC20Token': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gainers", "losers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        gainers: 'MarketDataERC20Token',
        losers: 'MarketDataERC20Token',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MarketDataERC20TokensByPriceMovers':
        return super().__new__(
            cls,
            *args,
            gainers=gainers,
            losers=losers,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.market_data_erc20_token import MarketDataERC20Token
