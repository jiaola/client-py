#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceRequest) on 2019-07-03.
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
from . import period
from . import quantity
from . import range
from . import timing


from . import domainresource

@dataclass
class DeviceRequest(domainresource.DomainResource):
    """ Medical device request.

    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    resource_type: ClassVar[str] = "DeviceRequest"
    authoredOn: Optional[fhirdate.FHIRDate] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    codeCodeableConcept:codeableconcept.CodeableConcept = None
    codeReference:fhirreference.FHIRReference = None
    encounter: Optional[fhirreference.FHIRReference] = None
    groupIdentifier: Optional[identifier.Identifier] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    insurance: Optional[List[fhirreference.FHIRReference]] = empty_list()
    intent: str = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    occurrencePeriod: Optional[period.Period] = None
    occurrenceTiming: Optional[timing.Timing] = None
    parameter: Optional[List[DeviceRequestParameter]] = empty_list()
    performer: Optional[fhirreference.FHIRReference] = None
    performerType: Optional[codeableconcept.CodeableConcept] = None
    priorRequest: Optional[List[fhirreference.FHIRReference]] = empty_list()
    priority: Optional[str] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    relevantHistory: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requester: Optional[fhirreference.FHIRReference] = None
    status: Optional[str] = None
    subject:fhirreference.FHIRReference = None
    supportingInfo: Optional[List[fhirreference.FHIRReference]] = empty_list()

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
#        self.authoredOn = None
#        """ When recorded.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.basedOn = None
#        """ What request fulfills.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.codeCodeableConcept = None
#        """ Device requested.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.codeReference = None
#        """ Device requested.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.encounter = None
#        """ Encounter motivating request.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.groupIdentifier = None
#        """ Identifier of composite request.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ External Request identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.instantiatesCanonical = None
#        """ Instantiates FHIR protocol or definition.
#        List of `str` items
#
#. """
#
#
#        self.instantiatesUri = None
#        """ Instantiates external protocol or definition.
#        List of `str` items
#
#. """
#
#
#        self.insurance = None
#        """ Associated insurance coverage.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.intent = None
#        """ proposal | plan | original-order | encoded | reflex-order.
#        Type `str`
#
#. """
#
#
#        self.note = None
#        """ Notes or comments.
#        List of `Annotation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.occurrenceDateTime = None
#        """ Desired time or schedule for use.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.occurrencePeriod = None
#        """ Desired time or schedule for use.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.occurrenceTiming = None
#        """ Desired time or schedule for use.
#        Type `Timing`
#
# (represented as `dict` in JSON). """
#
#
#        self.parameter = None
#        """ Device details.
#        List of `DeviceRequestParameter` items
#
# (represented as `dict` in JSON). """
#
#
#        self.performer = None
#        """ Requested Filler.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.performerType = None
#        """ Filler role.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.priorRequest = None
#        """ What request replaces.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.priority = None
#        """ Indicates how quickly the {{title}} should be addressed with
        respect to other requests.
#        Type `str`
#
#. """
#
#
#        self.reasonCode = None
#        """ Coded Reason for request.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reasonReference = None
#        """ Linked Reason for request.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.relevantHistory = None
#        """ Request provenance.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.requester = None
#        """ Who/what is requesting diagnostics.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ draft | active | suspended | completed | entered-in-error |
        cancelled.
#        Type `str`
#
#. """
#
#
#        self.subject = None
#        """ Focus of request.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.supportingInfo = None
#        """ Additional clinical information.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#

#        super(DeviceRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("codeCodeableConcept", "codeCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "code", {  # #}True),
            ("codeReference", "codeReference", fhirreference.FHIRReference, {  # #}False, "code", {  # #}True),
            ("encounter", "encounter", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("instantiatesCanonical", "instantiatesCanonical", str, {  # #}True, None, {  # #}False),
            ("instantiatesUri", "instantiatesUri", str, {  # #}True, None, {  # #}False),
            ("insurance", "insurance", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("intent", "intent", str, {  # #}False, None, {  # #}True),
            ("note", "note", annotation.Annotation, {  # #}True, None, {  # #}False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, {  # #}False, "occurrence", {  # #}False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, {  # #}False, "occurrence", {  # #}False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, {  # #}False, "occurrence", {  # #}False),
            ("parameter", "parameter", DeviceRequestParameter, {  # #}True, None, {  # #}False),
            ("performer", "performer", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("priorRequest", "priorRequest", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("priority", "priority", str, {  # #}False, None, {  # #}False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("requester", "requester", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}False),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
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
from . import period
from . import quantity
from . import range
from . import timing


from . import backboneelement

@dataclass
class DeviceRequestParameter(backboneelement.BackboneElement):
    """ Device details.

    Specific parameters for the ordered item.  For example, the prism value for
    lenses.
    """
    resource_type: ClassVar[str] = "DeviceRequestParameter"
    code: Optional[codeableconcept.CodeableConcept] = None
    valueBoolean: Optional[bool] = None
    valueCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    valueQuantity: Optional[quantity.Quantity] = None
    valueRange: Optional[range.Range] = None

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
#        """ Device detail.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueBoolean = None
#        """ Value of detail.
#        Type `bool`
#
#. """
#
#
#        self.valueCodeableConcept = None
#        """ Value of detail.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueQuantity = None
#        """ Value of detail.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueRange = None
#        """ Value of detail.
#        Type `Range`
#
# (represented as `dict` in JSON). """
#

#        super(DeviceRequestParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("valueBoolean", "valueBoolean", bool, {  # #}False, "value", {  # #}False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "value", {  # #}False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, {  # #}False, "value", {  # #}False),
            ("valueRange", "valueRange", range.Range, {  # #}False, "value", {  # #}False),
        ])
        return js