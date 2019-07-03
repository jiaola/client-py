#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/List) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier


from . import domainresource

@dataclass
class List(domainresource.DomainResource):
    """ A list is a curated collection of resources.
    """
    resource_type: ClassVar[str] = "List"
    code: Optional[codeableconcept.CodeableConcept] = None
    date: Optional[fhirdate.FHIRDate] = None
    emptyReason: Optional[codeableconcept.CodeableConcept] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    entry: Optional[List[ListEntry]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    mode: str = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    orderedBy: Optional[codeableconcept.CodeableConcept] = None
    source: Optional[fhirreference.FHIRReference] = None
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None
    title: Optional[str] = None

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
#        self.code = None
#        """ What the purpose of this list is.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.date = None
#        """ When the list was prepared.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.emptyReason = None
#        """ Why list is empty.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.encounter = None
#        """ Context in which list created.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.entry = None
#        """ Entries in the list.
#        List of `ListEntry` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Business identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.mode = None
#        """ working | snapshot | changes.
#        Type `str`
#
#. """
#
#
#        self.note = None
#        """ Comments about the list.
#        List of `Annotation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.orderedBy = None
#        """ What order the list has.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.source = None
#        """ Who and/or what defined the list contents (aka Author).
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ current | retired | entered-in-error.
#        Type `str`
#
#. """
#
#
#        self.subject = None
#        """ If all resources have the same subject.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.title = None
#        """ Descriptive name for the list.
#        Type `str`
#
#. """
#

#        super(List, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(List, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("encounter", "encounter", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("entry", "entry", ListEntry, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("mode", "mode", str, {  # #}False, None, {  # #}True),
            ("note", "note", annotation.Annotation, {  # #}True, None, {  # #}False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("source", "source", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("title", "title", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier


from . import backboneelement

@dataclass
class ListEntry(backboneelement.BackboneElement):
    """ Entries in the list.

    Entries in this list.
    """
    resource_type: ClassVar[str] = "ListEntry"
    date: Optional[fhirdate.FHIRDate] = None
    deleted: Optional[bool] = None
    flag: Optional[codeableconcept.CodeableConcept] = None
    item:fhirreference.FHIRReference = None

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
#        self.date = None
#        """ When item added to list.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.deleted = None
#        """ If this item is actually marked as deleted.
#        Type `bool`
#
#. """
#
#
#        self.flag = None
#        """ Status/Workflow information about this item.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.item = None
#        """ Actual entry.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(ListEntry, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ListEntry, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("deleted", "deleted", bool, {  # #}False, None, {  # #}False),
            ("flag", "flag", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("item", "item", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
        ])
        return js