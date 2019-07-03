#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CatalogEntry) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period


from . import domainresource

@dataclass
class CatalogEntry(domainresource.DomainResource):
    """ An entry in a catalog.

    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """
    resource_type: ClassVar[str] = "CatalogEntry"
    additionalCharacteristic: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    additionalClassification: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    additionalIdentifier: Optional[List[identifier.Identifier]] = empty_list()
    classification: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    lastUpdated: Optional[fhirdate.FHIRDate] = None
    orderable: bool = None
    referencedItem:fhirreference.FHIRReference = None
    relatedEntry: Optional[List[CatalogEntryRelatedEntry]] = empty_list()
    status: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None
    validTo: Optional[fhirdate.FHIRDate] = None
    validityPeriod: Optional[period.Period] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.additionalCharacteristic = None
#        """ Additional characteristics of the catalog entry.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.additionalClassification = None
#        """ Additional classification of the catalog entry.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.additionalIdentifier = None
#        """ Any additional identifier(s) for the catalog item, in the same
        granularity or concept.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.classification = None
#        """ Classification (category or class) of the item entry.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Unique identifier of the catalog item.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.lastUpdated = None
#        """ When was this catalog last updated.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.orderable = None
#        """ Whether the entry represents an orderable item.
#        Type `bool`
#
#. """
#
#
#        self.referencedItem = None
#        """ The item that is being defined.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.relatedEntry = None
#        """ An item that this catalog entry is related to.
#        List of `CatalogEntryRelatedEntry` items
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ draft | active | retired | unknown.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ The type of item - medication, device, service, protocol or other.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.validTo = None
#        """ The date until which this catalog entry is expected to be active.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.validityPeriod = None
#        """ The time period in which this catalog entry is expected to be
        active.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#

#        super(CatalogEntry, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CatalogEntry, self).elementProperties()
        js.extend([
            ("additionalCharacteristic", "additionalCharacteristic", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("additionalClassification", "additionalClassification", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("additionalIdentifier", "additionalIdentifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("classification", "classification", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("lastUpdated", "lastUpdated", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("orderable", "orderable", bool, {  # #}False, None, {  # #}True),
            ("referencedItem", "referencedItem", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("relatedEntry", "relatedEntry", CatalogEntryRelatedEntry, {  # #}True, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("validTo", "validTo", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("validityPeriod", "validityPeriod", period.Period, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period


from . import backboneelement

@dataclass
class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """ An item that this catalog entry is related to.

    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """
    resource_type: ClassVar[str] = "CatalogEntryRelatedEntry"
    item:fhirreference.FHIRReference = None
    relationtype: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.item = None
#        """ The reference to the related item.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.relationtype = None
#        """ triggers | is-replaced-by.
#        Type `str`
#
#. """
#

#        super(CatalogEntryRelatedEntry, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CatalogEntryRelatedEntry, self).elementProperties()
        js.extend([
            ("item", "item", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("relationtype", "relationtype", str, {  # #}False, None, {  # #}True),
        ])
        return js