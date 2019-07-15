#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Task) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import age
from . import annotation
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import domainresource
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext

from . import domainresource

@dataclass
class Task(domainresource.DomainResource):
    """ A task to be performed.
    """
    resource_type: ClassVar[str] = "Task"
    authoredOn: Optional[fhirdate.FHIRDate] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    businessStatus: Optional[codeableconcept.CodeableConcept] = None
    code: Optional[codeableconcept.CodeableConcept] = None
    description: Optional[str] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    executionPeriod: Optional[period.Period] = None
    focus: Optional[fhirreference.FHIRReference] = None
    for_fhir: Optional[fhirreference.FHIRReference] = None
    groupIdentifier: Optional[identifier.Identifier] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    input: Optional[List[TaskInput]] = empty_list()
    instantiatesCanonical: Optional[str] = None
    instantiatesUri: Optional[str] = None
    insurance: Optional[List[fhirreference.FHIRReference]] = empty_list()
    intent: str = None
    lastModified: Optional[fhirdate.FHIRDate] = None
    location: Optional[fhirreference.FHIRReference] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    output: Optional[List[TaskOutput]] = empty_list()
    owner: Optional[fhirreference.FHIRReference] = None
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    performerType: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    priority: Optional[str] = None
    reasonCode: Optional[codeableconcept.CodeableConcept] = None
    reasonReference: Optional[fhirreference.FHIRReference] = None
    relevantHistory: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requester: Optional[fhirreference.FHIRReference] = None
    restriction: Optional[TaskRestriction] = None
    status: str = None
    statusReason: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Task, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("businessStatus", "businessStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("executionPeriod", "executionPeriod", period.Period, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, False, None, False),
            ("for_fhir", "for", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("input", "input", TaskInput, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("lastModified", "lastModified", fhirdate.FHIRDate, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("output", "output", TaskOutput, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("restriction", "restriction", TaskRestriction, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class TaskInput(backboneelement.BackboneElement):
    """ Information used to perform task.

    Additional information that may be needed in the execution of the task.
    """
    resource_type: ClassVar[str] = "TaskInput"
    type:codeableconcept.CodeableConcept = None
    valueAddress:address.Address = None
    valueAge:age.Age = None
    valueAnnotation:annotation.Annotation = None
    valueAttachment:attachment.Attachment = None
    valueBase64Binary: str = None
    valueBoolean: bool = None
    valueCanonical: str = None
    valueCode: str = None
    valueCodeableConcept:codeableconcept.CodeableConcept = None
    valueCoding:coding.Coding = None
    valueContactDetail:contactdetail.ContactDetail = None
    valueContactPoint:contactpoint.ContactPoint = None
    valueContributor:contributor.Contributor = None
    valueCount:count.Count = None
    valueDataRequirement:datarequirement.DataRequirement = None
    valueDate:fhirdate.FHIRDate = None
    valueDateTime:fhirdate.FHIRDate = None
    valueDecimal: float = None
    valueDistance:distance.Distance = None
    valueDosage:dosage.Dosage = None
    valueDuration:duration.Duration = None
    valueExpression:expression.Expression = None
    valueHumanName:humanname.HumanName = None
    valueId: str = None
    valueIdentifier:identifier.Identifier = None
    valueInstant:fhirdate.FHIRDate = None
    valueInteger: int = None
    valueMarkdown: str = None
    valueMoney:money.Money = None
    valueOid: str = None
    valueParameterDefinition:parameterdefinition.ParameterDefinition = None
    valuePeriod:period.Period = None
    valuePositiveInt: int = None
    valueQuantity:quantity.Quantity = None
    valueRange:range.Range = None
    valueRatio:ratio.Ratio = None
    valueReference:fhirreference.FHIRReference = None
    valueRelatedArtifact:relatedartifact.RelatedArtifact = None
    valueSampledData:sampleddata.SampledData = None
    valueSignature:signature.Signature = None
    valueString: str = None
    valueTime:fhirdate.FHIRDate = None
    valueTiming:timing.Timing = None
    valueTriggerDefinition:triggerdefinition.TriggerDefinition = None
    valueUnsignedInt: int = None
    valueUri: str = None
    valueUrl: str = None
    valueUsageContext:usagecontext.UsageContext = None
    valueUuid: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TaskInput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
        ])
        return js

@dataclass
class TaskOutput(backboneelement.BackboneElement):
    """ Information produced as part of task.

    Outputs produced by the Task.
    """
    resource_type: ClassVar[str] = "TaskOutput"
    type:codeableconcept.CodeableConcept = None
    valueAddress:address.Address = None
    valueAge:age.Age = None
    valueAnnotation:annotation.Annotation = None
    valueAttachment:attachment.Attachment = None
    valueBase64Binary: str = None
    valueBoolean: bool = None
    valueCanonical: str = None
    valueCode: str = None
    valueCodeableConcept:codeableconcept.CodeableConcept = None
    valueCoding:coding.Coding = None
    valueContactDetail:contactdetail.ContactDetail = None
    valueContactPoint:contactpoint.ContactPoint = None
    valueContributor:contributor.Contributor = None
    valueCount:count.Count = None
    valueDataRequirement:datarequirement.DataRequirement = None
    valueDate:fhirdate.FHIRDate = None
    valueDateTime:fhirdate.FHIRDate = None
    valueDecimal: float = None
    valueDistance:distance.Distance = None
    valueDosage:dosage.Dosage = None
    valueDuration:duration.Duration = None
    valueExpression:expression.Expression = None
    valueHumanName:humanname.HumanName = None
    valueId: str = None
    valueIdentifier:identifier.Identifier = None
    valueInstant:fhirdate.FHIRDate = None
    valueInteger: int = None
    valueMarkdown: str = None
    valueMoney:money.Money = None
    valueOid: str = None
    valueParameterDefinition:parameterdefinition.ParameterDefinition = None
    valuePeriod:period.Period = None
    valuePositiveInt: int = None
    valueQuantity:quantity.Quantity = None
    valueRange:range.Range = None
    valueRatio:ratio.Ratio = None
    valueReference:fhirreference.FHIRReference = None
    valueRelatedArtifact:relatedartifact.RelatedArtifact = None
    valueSampledData:sampleddata.SampledData = None
    valueSignature:signature.Signature = None
    valueString: str = None
    valueTime:fhirdate.FHIRDate = None
    valueTiming:timing.Timing = None
    valueTriggerDefinition:triggerdefinition.TriggerDefinition = None
    valueUnsignedInt: int = None
    valueUri: str = None
    valueUrl: str = None
    valueUsageContext:usagecontext.UsageContext = None
    valueUuid: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TaskOutput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
        ])
        return js

@dataclass
class TaskRestriction(backboneelement.BackboneElement):
    """ Constraints on fulfillment tasks.

    If the Task.focus is a request resource and the task is seeking fulfillment
    (i.e. is asking for the request to be actioned), this element identifies
    any limitations on what parts of the referenced request should be actioned.
    """
    resource_type: ClassVar[str] = "TaskRestriction"
    period: Optional[period.Period] = None
    recipient: Optional[List[fhirreference.FHIRReference]] = empty_list()
    repetitions: Optional[int] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(TaskRestriction, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("repetitions", "repetitions", int, False, None, False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import contributor
except ImportError:
    contributor = sys.modules[__package__ + '.contributor']
try:
    from . import count
except ImportError:
    count = sys.modules[__package__ + '.count']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import distance
except ImportError:
    distance = sys.modules[__package__ + '.distance']
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import parameterdefinition
except ImportError:
    parameterdefinition = sys.modules[__package__ + '.parameterdefinition']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import sampleddata
except ImportError:
    sampleddata = sys.modules[__package__ + '.sampleddata']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
try:
    from . import triggerdefinition
except ImportError:
    triggerdefinition = sys.modules[__package__ + '.triggerdefinition']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']