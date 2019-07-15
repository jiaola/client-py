#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Bundle) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import fhirdate
from . import identifier
from . import resource
from . import signature

from . import resource

@dataclass
class Bundle(resource.Resource):
    """ Contains a collection of resources.

    A container for a collection of resources.
    """
    resource_type: ClassVar[str] = "Bundle"
    entry: Optional[List[BundleEntry]] = empty_list()
    identifier: Optional[identifier.Identifier] = None
    link: Optional[List[BundleLink]] = empty_list()
    signature: Optional[signature.Signature] = None
    timestamp: Optional[fhirdate.FHIRDate] = None
    total: Optional[int] = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Bundle, self).elementProperties()
        js.extend([
            ("entry", "entry", BundleEntry, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("link", "link", BundleLink, True, None, False),
            ("signature", "signature", signature.Signature, False, None, False),
            ("timestamp", "timestamp", fhirdate.FHIRDate, False, None, False),
            ("total", "total", int, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js

from . import backboneelement

@dataclass
class BundleEntry(backboneelement.BackboneElement):
    """ Entry in the bundle - will have a resource or information.

    An entry in a bundle resource - will either contain a resource or
    information about a resource (transactions and history only).
    """
    resource_type: ClassVar[str] = "BundleEntry"
    fullUrl: Optional[str] = None
    link: Optional[List[BundleLink]] = empty_list()
    request: Optional[BundleEntryRequest] = None
    resource: Optional[resource.Resource] = None
    response: Optional[BundleEntryResponse] = None
    search: Optional[BundleEntrySearch] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BundleEntry, self).elementProperties()
        js.extend([
            ("fullUrl", "fullUrl", str, False, None, False),
            ("link", "link", BundleLink, True, None, False),
            ("request", "request", BundleEntryRequest, False, None, False),
            ("resource", "resource", resource.Resource, False, None, False),
            ("response", "response", BundleEntryResponse, False, None, False),
            ("search", "search", BundleEntrySearch, False, None, False),
        ])
        return js

@dataclass
class BundleEntryRequest(backboneelement.BackboneElement):
    """ Additional execution information (transaction/batch/history).

    Additional information about how this entry should be processed as part of
    a transaction or batch.  For history, it shows how the entry was processed
    to create the version contained in the entry.
    """
    resource_type: ClassVar[str] = "BundleEntryRequest"
    ifMatch: Optional[str] = None
    ifModifiedSince: Optional[fhirdate.FHIRDate] = None
    ifNoneExist: Optional[str] = None
    ifNoneMatch: Optional[str] = None
    method: str = None
    url: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BundleEntryRequest, self).elementProperties()
        js.extend([
            ("ifMatch", "ifMatch", str, False, None, False),
            ("ifModifiedSince", "ifModifiedSince", fhirdate.FHIRDate, False, None, False),
            ("ifNoneExist", "ifNoneExist", str, False, None, False),
            ("ifNoneMatch", "ifNoneMatch", str, False, None, False),
            ("method", "method", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js

@dataclass
class BundleEntryResponse(backboneelement.BackboneElement):
    """ Results of execution (transaction/batch/history).

    Indicates the results of processing the corresponding 'request' entry in
    the batch or transaction being responded to or what the results of an
    operation where when returning history.
    """
    resource_type: ClassVar[str] = "BundleEntryResponse"
    etag: Optional[str] = None
    lastModified: Optional[fhirdate.FHIRDate] = None
    location: Optional[str] = None
    outcome: Optional[resource.Resource] = None
    status: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BundleEntryResponse, self).elementProperties()
        js.extend([
            ("etag", "etag", str, False, None, False),
            ("lastModified", "lastModified", fhirdate.FHIRDate, False, None, False),
            ("location", "location", str, False, None, False),
            ("outcome", "outcome", resource.Resource, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js

@dataclass
class BundleEntrySearch(backboneelement.BackboneElement):
    """ Search related information.

    Information about the search process that lead to the creation of this
    entry.
    """
    resource_type: ClassVar[str] = "BundleEntrySearch"
    mode: Optional[str] = None
    score: Optional[float] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BundleEntrySearch, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, False),
            ("score", "score", float, False, None, False),
        ])
        return js

@dataclass
class BundleLink(backboneelement.BackboneElement):
    """ Links related to this Bundle.

    A series of links that provide context to this bundle.
    """
    resource_type: ClassVar[str] = "BundleLink"
    relation: str = None
    url: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(BundleLink, self).elementProperties()
        js.extend([
            ("relation", "relation", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']