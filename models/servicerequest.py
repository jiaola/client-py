#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ServiceRequest) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import timing


from . import domainresource

@dataclass
class ServiceRequest(domainresource.DomainResource):
    """ A request for a service to be performed.

    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """
    resource_type: ClassVar[str] = "ServiceRequest"
    asNeededBoolean: Optional[bool] = None
    asNeededCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    authoredOn: Optional[fhirdate.FHIRDate] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    bodySite: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    code: Optional[codeableconcept.CodeableConcept] = None
    doNotPerform: Optional[bool] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    insurance: Optional[List[fhirreference.FHIRReference]] = empty_list()
    intent: str = None
    locationCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    locationReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    occurrencePeriod: Optional[period.Period] = None
    occurrenceTiming: Optional[timing.Timing] = None
    orderDetail: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    patientInstruction: Optional[str] = None
    performer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    performerType: Optional[codeableconcept.CodeableConcept] = None
    priority: Optional[str] = None
    quantityQuantity: Optional[quantity.Quantity] = None
    quantityRange: Optional[range.Range] = None
    quantityRatio: Optional[ratio.Ratio] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    relevantHistory: Optional[List[fhirreference.FHIRReference]] = empty_list()
    replaces: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requester: Optional[fhirreference.FHIRReference] = None
    requisition: Optional[identifier.Identifier] = None
    specimen: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: str = None
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
#        self.asNeededBoolean = None
#        """ Preconditions for service.
#        Type `bool`
#
#. """
#
#
#        self.asNeededCodeableConcept = None
#        """ Preconditions for service.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.authoredOn = None
#        """ Date request signed.
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
#        self.bodySite = None
#        """ Location on Body.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ Classification of service.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.code = None
#        """ What is being requested/ordered.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.doNotPerform = None
#        """ True if service/procedure should not be performed.
#        Type `bool`
#
#. """
#
#
#        self.encounter = None
#        """ Encounter in which the request was created.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Identifiers assigned to this order.
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
#        """ proposal | plan | order +.
#        Type `str`
#
#. """
#
#
#        self.locationCode = None
#        """ Requested location.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.locationReference = None
#        """ Requested location.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.note = None
#        """ Comments.
#        List of `Annotation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.occurrenceDateTime = None
#        """ When service should occur.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.occurrencePeriod = None
#        """ When service should occur.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.occurrenceTiming = None
#        """ When service should occur.
#        Type `Timing`
#
# (represented as `dict` in JSON). """
#
#
#        self.orderDetail = None
#        """ Additional order information.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.patientInstruction = None
#        """ Patient or consumer-oriented instructions.
#        Type `str`
#
#. """
#
#
#        self.performer = None
#        """ Requested performer.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.performerType = None
#        """ Performer role.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.priority = None
#        """ routine | urgent | asap | stat.
#        Type `str`
#
#. """
#
#
#        self.quantityQuantity = None
#        """ Service amount.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.quantityRange = None
#        """ Service amount.
#        Type `Range`
#
# (represented as `dict` in JSON). """
#
#
#        self.quantityRatio = None
#        """ Service amount.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.reasonCode = None
#        """ Explanation/Justification for procedure or service.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reasonReference = None
#        """ Explanation/Justification for service or service.
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
#        self.replaces = None
#        """ What request replaces.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.requester = None
#        """ Who/what is requesting service.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.requisition = None
#        """ Composite Request ID.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.specimen = None
#        """ Procedure Samples.
#        List of `FHIRReference` items
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
#        """ Individual or Entity the service is ordered for.
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

#        super(ServiceRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ServiceRequest, self).elementProperties()
        js.extend([
            ("asNeededBoolean", "asNeededBoolean", bool, {  # #}False, "asNeeded", {  # #}False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "asNeeded", {  # #}False),
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("doNotPerform", "doNotPerform", bool, {  # #}False, None, {  # #}False),
            ("encounter", "encounter", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("instantiatesCanonical", "instantiatesCanonical", str, {  # #}True, None, {  # #}False),
            ("instantiatesUri", "instantiatesUri", str, {  # #}True, None, {  # #}False),
            ("insurance", "insurance", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("intent", "intent", str, {  # #}False, None, {  # #}True),
            ("locationCode", "locationCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("note", "note", annotation.Annotation, {  # #}True, None, {  # #}False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, {  # #}False, "occurrence", {  # #}False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, {  # #}False, "occurrence", {  # #}False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, {  # #}False, "occurrence", {  # #}False),
            ("orderDetail", "orderDetail", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("patientInstruction", "patientInstruction", str, {  # #}False, None, {  # #}False),
            ("performer", "performer", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("priority", "priority", str, {  # #}False, None, {  # #}False),
            ("quantityQuantity", "quantityQuantity", quantity.Quantity, {  # #}False, "quantity", {  # #}False),
            ("quantityRange", "quantityRange", range.Range, {  # #}False, "quantity", {  # #}False),
            ("quantityRatio", "quantityRatio", ratio.Ratio, {  # #}False, "quantity", {  # #}False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("replaces", "replaces", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("requester", "requester", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("requisition", "requisition", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("specimen", "specimen", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
        ])
        return js