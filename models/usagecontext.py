#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/UsageContext) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import element
from . import fhirreference
from . import quantity
from . import range


from . import element

@dataclass
class UsageContext(element.Element):
    """ Describes the context of use for a conformance or knowledge resource.

    Specifies clinical/business/etc. metadata that can be used to retrieve,
    index and/or categorize an artifact. This metadata can either be specific
    to the applicable population (e.g., age category, DRG) or the specific
    context of care (e.g., venue, care setting, provider of care).
    """
    resource_type: ClassVar[str] = "UsageContext"
    code:coding.Coding = None
    valueCodeableConcept:codeableconcept.CodeableConcept = None
    valueQuantity:quantity.Quantity = None
    valueRange:range.Range = None
    valueReference:fhirreference.FHIRReference = None

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
#        """ Type of context being specified.
#        Type `Coding`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueCodeableConcept = None
#        """ Value that defines the context.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueQuantity = None
#        """ Value that defines the context.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueRange = None
#        """ Value that defines the context.
#        Type `Range`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueReference = None
#        """ Value that defines the context.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(UsageContext, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(UsageContext, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, {  # #}False, None, {  # #}True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "value", {  # #}True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, {  # #}False, "value", {  # #}True),
            ("valueRange", "valueRange", range.Range, {  # #}False, "value", {  # #}True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, {  # #}False, "value", {  # #}True),
        ])
        return js