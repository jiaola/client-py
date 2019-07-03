#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import datarequirement
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier


from . import domainresource

@dataclass
class GuidanceResponse(domainresource.DomainResource):
    """ The formal response to a guidance request.

    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """
    resource_type: ClassVar[str] = "GuidanceResponse"
    dataRequirement: Optional[List[datarequirement.DataRequirement]] = empty_list()
    encounter: Optional[fhirreference.FHIRReference] = None
    evaluationMessage: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    moduleCanonical: str = None
    moduleCodeableConcept:codeableconcept.CodeableConcept = None
    moduleUri: str = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    outputParameters: Optional[fhirreference.FHIRReference] = None
    performer: Optional[fhirreference.FHIRReference] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requestIdentifier: Optional[identifier.Identifier] = None
    result: Optional[fhirreference.FHIRReference] = None
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None

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
#        self.dataRequirement = None
#        """ Additional required data.
#        List of `DataRequirement` items
#
# (represented as `dict` in JSON). """
#
#
#        self.encounter = None
#        """ Encounter during which the response was returned.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.evaluationMessage = None
#        """ Messages resulting from the evaluation of the artifact or artifacts.
#        List of `FHIRReference` items
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
#        self.moduleCanonical = None
#        """ What guidance was requested.
#        Type `str`
#
#. """
#
#
#        self.moduleCodeableConcept = None
#        """ What guidance was requested.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.moduleUri = None
#        """ What guidance was requested.
#        Type `str`
#
#. """
#
#
#        self.note = None
#        """ Additional notes about the response.
#        List of `Annotation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.occurrenceDateTime = None
#        """ When the guidance response was processed.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.outputParameters = None
#        """ The output parameters of the evaluation, if any.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.performer = None
#        """ Device returning the guidance.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.reasonCode = None
#        """ Why guidance is needed.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reasonReference = None
#        """ Why guidance is needed.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.requestIdentifier = None
#        """ The identifier of the request associated with this response, if any.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.result = None
#        """ Proposed actions, if any.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ success | data-requested | data-required | in-progress | failure |
        entered-in-error.
#        Type `str`
#
#. """
#
#
#        self.subject = None
#        """ Patient the request was performed for.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(GuidanceResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, {  # #}True, None, {  # #}False),
            ("encounter", "encounter", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("evaluationMessage", "evaluationMessage", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("moduleCanonical", "moduleCanonical", str, {  # #}False, "module", {  # #}True),
            ("moduleCodeableConcept", "moduleCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "module", {  # #}True),
            ("moduleUri", "moduleUri", str, {  # #}False, "module", {  # #}True),
            ("note", "note", annotation.Annotation, {  # #}True, None, {  # #}False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("outputParameters", "outputParameters", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("performer", "performer", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("result", "result", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
        ])
        return js