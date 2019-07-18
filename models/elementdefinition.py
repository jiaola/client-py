#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ElementDefinition) on 2019-07-18.
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
from . import dosage
from . import duration
from . import element
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

from . import element

@dataclass
class ElementDefinitionType(element.Element):
    """ Data type and Profile for this element.

    The data type or resource that the value of this element is permitted to
    be.
    """
    resource_type: ClassVar[str] = "ElementDefinitionType"
    aggregation: Optional[List[str]] = empty_list()
    code: str = None
    profile: Optional[List[str]] = empty_list()
    targetProfile: Optional[List[str]] = empty_list()
    versioning: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ElementDefinitionType, self).elementProperties()
        js.extend([
            ("aggregation", "aggregation", str, True, None, False),
            ("code", "code", str, False, None, True),
            ("profile", "profile", str, True, None, False),
            ("targetProfile", "targetProfile", str, True, None, False),
            ("versioning", "versioning", str, False, None, False),
        ])
        return js

@dataclass
class ElementDefinitionSlicingDiscriminator(element.Element):
    """ Element values that are used to distinguish the slices.

    Designates which child elements are used to discriminate between the slices
    when processing an instance. If one or more discriminators are provided,
    the value of the child elements in the instance data SHALL completely
    distinguish which slice the element in the resource matches based on the
    allowed values for those elements in each of the slices.
    """
    resource_type: ClassVar[str] = "ElementDefinitionSlicingDiscriminator"
    path: str = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ElementDefinitionSlicingDiscriminator, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js

@dataclass
class ElementDefinitionSlicing(element.Element):
    """ This element is sliced - slices follow.

    Indicates that the element is sliced into a set of alternative definitions
    (i.e. in a structure definition, there are multiple different constraints
    on a single element in the base resource). Slicing can be used in any
    resource that has cardinality ..* on the base resource, or any resource
    with a choice of types. The set of slices is any elements that come after
    this in the element sequence that have the same path, until a shorter path
    occurs (the shorter path terminates the set).
    """
    resource_type: ClassVar[str] = "ElementDefinitionSlicing"
    description: Optional[str] = None
    discriminator: Optional[List[ElementDefinitionSlicingDiscriminator]] = empty_list()
    ordered: Optional[bool] = None
    rules: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ElementDefinitionSlicing, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("discriminator", "discriminator", ElementDefinitionSlicingDiscriminator, True, None, False),
            ("ordered", "ordered", bool, False, None, False),
            ("rules", "rules", str, False, None, True),
        ])
        return js

@dataclass
class ElementDefinitionMapping(element.Element):
    """ Map element to another set of definitions.

    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    resource_type: ClassVar[str] = "ElementDefinitionMapping"
    comment: Optional[str] = None
    identity: str = None
    language: Optional[str] = None
    map: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ElementDefinitionMapping, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("identity", "identity", str, False, None, True),
            ("language", "language", str, False, None, False),
            ("map", "map", str, False, None, True),
        ])
        return js

@dataclass
class ElementDefinitionExample(element.Element):
    """ Example value (as defined for type).

    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """
    resource_type: ClassVar[str] = "ElementDefinitionExample"
    label: str = None
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
        js = super(ElementDefinitionExample, self).elementProperties()
        js.extend([
            ("label", "label", str, False, None, True),
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
class ElementDefinitionConstraint(element.Element):
    """ Condition that must evaluate to true.

    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """
    resource_type: ClassVar[str] = "ElementDefinitionConstraint"
    expression: Optional[str] = None
    human: str = None
    key: str = None
    requirements: Optional[str] = None
    severity: str = None
    source: Optional[str] = None
    xpath: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ElementDefinitionConstraint, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, False),
            ("human", "human", str, False, None, True),
            ("key", "key", str, False, None, True),
            ("requirements", "requirements", str, False, None, False),
            ("severity", "severity", str, False, None, True),
            ("source", "source", str, False, None, False),
            ("xpath", "xpath", str, False, None, False),
        ])
        return js

@dataclass
class ElementDefinitionBinding(element.Element):
    """ ValueSet details if this is coded.

    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """
    resource_type: ClassVar[str] = "ElementDefinitionBinding"
    description: Optional[str] = None
    strength: str = None
    valueSet: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ElementDefinitionBinding, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("strength", "strength", str, False, None, True),
            ("valueSet", "valueSet", str, False, None, False),
        ])
        return js

@dataclass
class ElementDefinitionBase(element.Element):
    """ Base definition information for tools.

    Information about the base definition of the element, provided to make it
    unnecessary for tools to trace the deviation of the element through the
    derived and related profiles. When the element definition is not the
    original definition of an element - i.g. either in a constraint on another
    type, or for elements from a super type in a snap shot - then the
    information in provided in the element definition may be different to the
    base definition. On the original definition of the element, it will be
    same.
    """
    resource_type: ClassVar[str] = "ElementDefinitionBase"
    max: str = None
    min: int = None
    path: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ElementDefinitionBase, self).elementProperties()
        js.extend([
            ("max", "max", str, False, None, True),
            ("min", "min", int, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js

from . import backboneelement

@dataclass
class ElementDefinition(backboneelement.BackboneElement):
    """ Definition of an element in a resource or extension.

    Captures constraints on each element within the resource, profile, or
    extension.
    """
    resource_type: ClassVar[str] = "ElementDefinition"
    alias: Optional[List[str]] = empty_list()
    base: Optional[ElementDefinitionBase] = None
    binding: Optional[ElementDefinitionBinding] = None
    code: Optional[List[coding.Coding]] = empty_list()
    comment: Optional[str] = None
    condition: Optional[List[str]] = empty_list()
    constraint: Optional[List[ElementDefinitionConstraint]] = empty_list()
    contentReference: Optional[str] = None
    defaultValueAddress: Optional[address.Address] = None
    defaultValueAge: Optional[age.Age] = None
    defaultValueAnnotation: Optional[annotation.Annotation] = None
    defaultValueAttachment: Optional[attachment.Attachment] = None
    defaultValueBase64Binary: Optional[str] = None
    defaultValueBoolean: Optional[bool] = None
    defaultValueCanonical: Optional[str] = None
    defaultValueCode: Optional[str] = None
    defaultValueCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    defaultValueCoding: Optional[coding.Coding] = None
    defaultValueContactDetail: Optional[contactdetail.ContactDetail] = None
    defaultValueContactPoint: Optional[contactpoint.ContactPoint] = None
    defaultValueContributor: Optional[contributor.Contributor] = None
    defaultValueCount: Optional[count.Count] = None
    defaultValueDataRequirement: Optional[datarequirement.DataRequirement] = None
    defaultValueDate: Optional[fhirdate.FHIRDate] = None
    defaultValueDateTime: Optional[fhirdate.FHIRDate] = None
    defaultValueDecimal: Optional[float] = None
    defaultValueDistance: Optional[distance.Distance] = None
    defaultValueDosage: Optional[dosage.Dosage] = None
    defaultValueDuration: Optional[duration.Duration] = None
    defaultValueExpression: Optional[expression.Expression] = None
    defaultValueHumanName: Optional[humanname.HumanName] = None
    defaultValueId: Optional[str] = None
    defaultValueIdentifier: Optional[identifier.Identifier] = None
    defaultValueInstant: Optional[fhirdate.FHIRDate] = None
    defaultValueInteger: Optional[int] = None
    defaultValueMarkdown: Optional[str] = None
    defaultValueMoney: Optional[money.Money] = None
    defaultValueOid: Optional[str] = None
    defaultValueParameterDefinition: Optional[parameterdefinition.ParameterDefinition] = None
    defaultValuePeriod: Optional[period.Period] = None
    defaultValuePositiveInt: Optional[int] = None
    defaultValueQuantity: Optional[quantity.Quantity] = None
    defaultValueRange: Optional[range.Range] = None
    defaultValueRatio: Optional[ratio.Ratio] = None
    defaultValueReference: Optional[fhirreference.FHIRReference] = None
    defaultValueRelatedArtifact: Optional[relatedartifact.RelatedArtifact] = None
    defaultValueSampledData: Optional[sampleddata.SampledData] = None
    defaultValueSignature: Optional[signature.Signature] = None
    defaultValueString: Optional[str] = None
    defaultValueTime: Optional[fhirdate.FHIRDate] = None
    defaultValueTiming: Optional[timing.Timing] = None
    defaultValueTriggerDefinition: Optional[triggerdefinition.TriggerDefinition] = None
    defaultValueUnsignedInt: Optional[int] = None
    defaultValueUri: Optional[str] = None
    defaultValueUrl: Optional[str] = None
    defaultValueUsageContext: Optional[usagecontext.UsageContext] = None
    defaultValueUuid: Optional[str] = None
    definition: Optional[str] = None
    example: Optional[List[ElementDefinitionExample]] = empty_list()
    fixedAddress: Optional[address.Address] = None
    fixedAge: Optional[age.Age] = None
    fixedAnnotation: Optional[annotation.Annotation] = None
    fixedAttachment: Optional[attachment.Attachment] = None
    fixedBase64Binary: Optional[str] = None
    fixedBoolean: Optional[bool] = None
    fixedCanonical: Optional[str] = None
    fixedCode: Optional[str] = None
    fixedCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    fixedCoding: Optional[coding.Coding] = None
    fixedContactDetail: Optional[contactdetail.ContactDetail] = None
    fixedContactPoint: Optional[contactpoint.ContactPoint] = None
    fixedContributor: Optional[contributor.Contributor] = None
    fixedCount: Optional[count.Count] = None
    fixedDataRequirement: Optional[datarequirement.DataRequirement] = None
    fixedDate: Optional[fhirdate.FHIRDate] = None
    fixedDateTime: Optional[fhirdate.FHIRDate] = None
    fixedDecimal: Optional[float] = None
    fixedDistance: Optional[distance.Distance] = None
    fixedDosage: Optional[dosage.Dosage] = None
    fixedDuration: Optional[duration.Duration] = None
    fixedExpression: Optional[expression.Expression] = None
    fixedHumanName: Optional[humanname.HumanName] = None
    fixedId: Optional[str] = None
    fixedIdentifier: Optional[identifier.Identifier] = None
    fixedInstant: Optional[fhirdate.FHIRDate] = None
    fixedInteger: Optional[int] = None
    fixedMarkdown: Optional[str] = None
    fixedMoney: Optional[money.Money] = None
    fixedOid: Optional[str] = None
    fixedParameterDefinition: Optional[parameterdefinition.ParameterDefinition] = None
    fixedPeriod: Optional[period.Period] = None
    fixedPositiveInt: Optional[int] = None
    fixedQuantity: Optional[quantity.Quantity] = None
    fixedRange: Optional[range.Range] = None
    fixedRatio: Optional[ratio.Ratio] = None
    fixedReference: Optional[fhirreference.FHIRReference] = None
    fixedRelatedArtifact: Optional[relatedartifact.RelatedArtifact] = None
    fixedSampledData: Optional[sampleddata.SampledData] = None
    fixedSignature: Optional[signature.Signature] = None
    fixedString: Optional[str] = None
    fixedTime: Optional[fhirdate.FHIRDate] = None
    fixedTiming: Optional[timing.Timing] = None
    fixedTriggerDefinition: Optional[triggerdefinition.TriggerDefinition] = None
    fixedUnsignedInt: Optional[int] = None
    fixedUri: Optional[str] = None
    fixedUrl: Optional[str] = None
    fixedUsageContext: Optional[usagecontext.UsageContext] = None
    fixedUuid: Optional[str] = None
    isModifier: Optional[bool] = None
    isModifierReason: Optional[str] = None
    isSummary: Optional[bool] = None
    label: Optional[str] = None
    mapping: Optional[List[ElementDefinitionMapping]] = empty_list()
    max: Optional[str] = None
    maxLength: Optional[int] = None
    maxValueDate: Optional[fhirdate.FHIRDate] = None
    maxValueDateTime: Optional[fhirdate.FHIRDate] = None
    maxValueDecimal: Optional[float] = None
    maxValueInstant: Optional[fhirdate.FHIRDate] = None
    maxValueInteger: Optional[int] = None
    maxValuePositiveInt: Optional[int] = None
    maxValueQuantity: Optional[quantity.Quantity] = None
    maxValueTime: Optional[fhirdate.FHIRDate] = None
    maxValueUnsignedInt: Optional[int] = None
    meaningWhenMissing: Optional[str] = None
    min: Optional[int] = None
    minValueDate: Optional[fhirdate.FHIRDate] = None
    minValueDateTime: Optional[fhirdate.FHIRDate] = None
    minValueDecimal: Optional[float] = None
    minValueInstant: Optional[fhirdate.FHIRDate] = None
    minValueInteger: Optional[int] = None
    minValuePositiveInt: Optional[int] = None
    minValueQuantity: Optional[quantity.Quantity] = None
    minValueTime: Optional[fhirdate.FHIRDate] = None
    minValueUnsignedInt: Optional[int] = None
    mustSupport: Optional[bool] = None
    orderMeaning: Optional[str] = None
    path: str = None
    patternAddress: Optional[address.Address] = None
    patternAge: Optional[age.Age] = None
    patternAnnotation: Optional[annotation.Annotation] = None
    patternAttachment: Optional[attachment.Attachment] = None
    patternBase64Binary: Optional[str] = None
    patternBoolean: Optional[bool] = None
    patternCanonical: Optional[str] = None
    patternCode: Optional[str] = None
    patternCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    patternCoding: Optional[coding.Coding] = None
    patternContactDetail: Optional[contactdetail.ContactDetail] = None
    patternContactPoint: Optional[contactpoint.ContactPoint] = None
    patternContributor: Optional[contributor.Contributor] = None
    patternCount: Optional[count.Count] = None
    patternDataRequirement: Optional[datarequirement.DataRequirement] = None
    patternDate: Optional[fhirdate.FHIRDate] = None
    patternDateTime: Optional[fhirdate.FHIRDate] = None
    patternDecimal: Optional[float] = None
    patternDistance: Optional[distance.Distance] = None
    patternDosage: Optional[dosage.Dosage] = None
    patternDuration: Optional[duration.Duration] = None
    patternExpression: Optional[expression.Expression] = None
    patternHumanName: Optional[humanname.HumanName] = None
    patternId: Optional[str] = None
    patternIdentifier: Optional[identifier.Identifier] = None
    patternInstant: Optional[fhirdate.FHIRDate] = None
    patternInteger: Optional[int] = None
    patternMarkdown: Optional[str] = None
    patternMoney: Optional[money.Money] = None
    patternOid: Optional[str] = None
    patternParameterDefinition: Optional[parameterdefinition.ParameterDefinition] = None
    patternPeriod: Optional[period.Period] = None
    patternPositiveInt: Optional[int] = None
    patternQuantity: Optional[quantity.Quantity] = None
    patternRange: Optional[range.Range] = None
    patternRatio: Optional[ratio.Ratio] = None
    patternReference: Optional[fhirreference.FHIRReference] = None
    patternRelatedArtifact: Optional[relatedartifact.RelatedArtifact] = None
    patternSampledData: Optional[sampleddata.SampledData] = None
    patternSignature: Optional[signature.Signature] = None
    patternString: Optional[str] = None
    patternTime: Optional[fhirdate.FHIRDate] = None
    patternTiming: Optional[timing.Timing] = None
    patternTriggerDefinition: Optional[triggerdefinition.TriggerDefinition] = None
    patternUnsignedInt: Optional[int] = None
    patternUri: Optional[str] = None
    patternUrl: Optional[str] = None
    patternUsageContext: Optional[usagecontext.UsageContext] = None
    patternUuid: Optional[str] = None
    representation: Optional[List[str]] = empty_list()
    requirements: Optional[str] = None
    short: Optional[str] = None
    sliceIsConstraining: Optional[bool] = None
    sliceName: Optional[str] = None
    slicing: Optional[ElementDefinitionSlicing] = None
    type: Optional[List[ElementDefinitionType]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ElementDefinition, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("base", "base", ElementDefinitionBase, False, None, False),
            ("binding", "binding", ElementDefinitionBinding, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("condition", "condition", str, True, None, False),
            ("constraint", "constraint", ElementDefinitionConstraint, True, None, False),
            ("contentReference", "contentReference", str, False, None, False),
            ("defaultValueAddress", "defaultValueAddress", address.Address, False, "defaultValue", False),
            ("defaultValueAge", "defaultValueAge", age.Age, False, "defaultValue", False),
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, False, "defaultValue", False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, False, "defaultValue", False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("defaultValueCanonical", "defaultValueCanonical", str, False, "defaultValue", False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, False, "defaultValue", False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, False, "defaultValue", False),
            ("defaultValueContactDetail", "defaultValueContactDetail", contactdetail.ContactDetail, False, "defaultValue", False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, False, "defaultValue", False),
            ("defaultValueContributor", "defaultValueContributor", contributor.Contributor, False, "defaultValue", False),
            ("defaultValueCount", "defaultValueCount", count.Count, False, "defaultValue", False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", datarequirement.DataRequirement, False, "defaultValue", False),
            ("defaultValueDate", "defaultValueDate", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueDateTime", "defaultValueDateTime", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("defaultValueDistance", "defaultValueDistance", distance.Distance, False, "defaultValue", False),
            ("defaultValueDosage", "defaultValueDosage", dosage.Dosage, False, "defaultValue", False),
            ("defaultValueDuration", "defaultValueDuration", duration.Duration, False, "defaultValue", False),
            ("defaultValueExpression", "defaultValueExpression", expression.Expression, False, "defaultValue", False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, False, "defaultValue", False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, False, "defaultValue", False),
            ("defaultValueInstant", "defaultValueInstant", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("defaultValueMoney", "defaultValueMoney", money.Money, False, "defaultValue", False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", parameterdefinition.ParameterDefinition, False, "defaultValue", False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, False, "defaultValue", False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, False, "defaultValue", False),
            ("defaultValueRange", "defaultValueRange", range.Range, False, "defaultValue", False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, False, "defaultValue", False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, False, "defaultValue", False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", relatedartifact.RelatedArtifact, False, "defaultValue", False),
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, False, "defaultValue", False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, False, "defaultValue", False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("defaultValueTime", "defaultValueTime", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, False, "defaultValue", False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "defaultValue", False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("defaultValueUrl", "defaultValueUrl", str, False, "defaultValue", False),
            ("defaultValueUsageContext", "defaultValueUsageContext", usagecontext.UsageContext, False, "defaultValue", False),
            ("defaultValueUuid", "defaultValueUuid", str, False, "defaultValue", False),
            ("definition", "definition", str, False, None, False),
            ("example", "example", ElementDefinitionExample, True, None, False),
            ("fixedAddress", "fixedAddress", address.Address, False, "fixed", False),
            ("fixedAge", "fixedAge", age.Age, False, "fixed", False),
            ("fixedAnnotation", "fixedAnnotation", annotation.Annotation, False, "fixed", False),
            ("fixedAttachment", "fixedAttachment", attachment.Attachment, False, "fixed", False),
            ("fixedBase64Binary", "fixedBase64Binary", str, False, "fixed", False),
            ("fixedBoolean", "fixedBoolean", bool, False, "fixed", False),
            ("fixedCanonical", "fixedCanonical", str, False, "fixed", False),
            ("fixedCode", "fixedCode", str, False, "fixed", False),
            ("fixedCodeableConcept", "fixedCodeableConcept", codeableconcept.CodeableConcept, False, "fixed", False),
            ("fixedCoding", "fixedCoding", coding.Coding, False, "fixed", False),
            ("fixedContactDetail", "fixedContactDetail", contactdetail.ContactDetail, False, "fixed", False),
            ("fixedContactPoint", "fixedContactPoint", contactpoint.ContactPoint, False, "fixed", False),
            ("fixedContributor", "fixedContributor", contributor.Contributor, False, "fixed", False),
            ("fixedCount", "fixedCount", count.Count, False, "fixed", False),
            ("fixedDataRequirement", "fixedDataRequirement", datarequirement.DataRequirement, False, "fixed", False),
            ("fixedDate", "fixedDate", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedDateTime", "fixedDateTime", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedDecimal", "fixedDecimal", float, False, "fixed", False),
            ("fixedDistance", "fixedDistance", distance.Distance, False, "fixed", False),
            ("fixedDosage", "fixedDosage", dosage.Dosage, False, "fixed", False),
            ("fixedDuration", "fixedDuration", duration.Duration, False, "fixed", False),
            ("fixedExpression", "fixedExpression", expression.Expression, False, "fixed", False),
            ("fixedHumanName", "fixedHumanName", humanname.HumanName, False, "fixed", False),
            ("fixedId", "fixedId", str, False, "fixed", False),
            ("fixedIdentifier", "fixedIdentifier", identifier.Identifier, False, "fixed", False),
            ("fixedInstant", "fixedInstant", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedInteger", "fixedInteger", int, False, "fixed", False),
            ("fixedMarkdown", "fixedMarkdown", str, False, "fixed", False),
            ("fixedMoney", "fixedMoney", money.Money, False, "fixed", False),
            ("fixedOid", "fixedOid", str, False, "fixed", False),
            ("fixedParameterDefinition", "fixedParameterDefinition", parameterdefinition.ParameterDefinition, False, "fixed", False),
            ("fixedPeriod", "fixedPeriod", period.Period, False, "fixed", False),
            ("fixedPositiveInt", "fixedPositiveInt", int, False, "fixed", False),
            ("fixedQuantity", "fixedQuantity", quantity.Quantity, False, "fixed", False),
            ("fixedRange", "fixedRange", range.Range, False, "fixed", False),
            ("fixedRatio", "fixedRatio", ratio.Ratio, False, "fixed", False),
            ("fixedReference", "fixedReference", fhirreference.FHIRReference, False, "fixed", False),
            ("fixedRelatedArtifact", "fixedRelatedArtifact", relatedartifact.RelatedArtifact, False, "fixed", False),
            ("fixedSampledData", "fixedSampledData", sampleddata.SampledData, False, "fixed", False),
            ("fixedSignature", "fixedSignature", signature.Signature, False, "fixed", False),
            ("fixedString", "fixedString", str, False, "fixed", False),
            ("fixedTime", "fixedTime", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedTiming", "fixedTiming", timing.Timing, False, "fixed", False),
            ("fixedTriggerDefinition", "fixedTriggerDefinition", triggerdefinition.TriggerDefinition, False, "fixed", False),
            ("fixedUnsignedInt", "fixedUnsignedInt", int, False, "fixed", False),
            ("fixedUri", "fixedUri", str, False, "fixed", False),
            ("fixedUrl", "fixedUrl", str, False, "fixed", False),
            ("fixedUsageContext", "fixedUsageContext", usagecontext.UsageContext, False, "fixed", False),
            ("fixedUuid", "fixedUuid", str, False, "fixed", False),
            ("isModifier", "isModifier", bool, False, None, False),
            ("isModifierReason", "isModifierReason", str, False, None, False),
            ("isSummary", "isSummary", bool, False, None, False),
            ("label", "label", str, False, None, False),
            ("mapping", "mapping", ElementDefinitionMapping, True, None, False),
            ("max", "max", str, False, None, False),
            ("maxLength", "maxLength", int, False, None, False),
            ("maxValueDate", "maxValueDate", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueDateTime", "maxValueDateTime", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueDecimal", "maxValueDecimal", float, False, "maxValue", False),
            ("maxValueInstant", "maxValueInstant", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueInteger", "maxValueInteger", int, False, "maxValue", False),
            ("maxValuePositiveInt", "maxValuePositiveInt", int, False, "maxValue", False),
            ("maxValueQuantity", "maxValueQuantity", quantity.Quantity, False, "maxValue", False),
            ("maxValueTime", "maxValueTime", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueUnsignedInt", "maxValueUnsignedInt", int, False, "maxValue", False),
            ("meaningWhenMissing", "meaningWhenMissing", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("minValueDate", "minValueDate", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueDateTime", "minValueDateTime", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueDecimal", "minValueDecimal", float, False, "minValue", False),
            ("minValueInstant", "minValueInstant", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueInteger", "minValueInteger", int, False, "minValue", False),
            ("minValuePositiveInt", "minValuePositiveInt", int, False, "minValue", False),
            ("minValueQuantity", "minValueQuantity", quantity.Quantity, False, "minValue", False),
            ("minValueTime", "minValueTime", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueUnsignedInt", "minValueUnsignedInt", int, False, "minValue", False),
            ("mustSupport", "mustSupport", bool, False, None, False),
            ("orderMeaning", "orderMeaning", str, False, None, False),
            ("path", "path", str, False, None, True),
            ("patternAddress", "patternAddress", address.Address, False, "pattern", False),
            ("patternAge", "patternAge", age.Age, False, "pattern", False),
            ("patternAnnotation", "patternAnnotation", annotation.Annotation, False, "pattern", False),
            ("patternAttachment", "patternAttachment", attachment.Attachment, False, "pattern", False),
            ("patternBase64Binary", "patternBase64Binary", str, False, "pattern", False),
            ("patternBoolean", "patternBoolean", bool, False, "pattern", False),
            ("patternCanonical", "patternCanonical", str, False, "pattern", False),
            ("patternCode", "patternCode", str, False, "pattern", False),
            ("patternCodeableConcept", "patternCodeableConcept", codeableconcept.CodeableConcept, False, "pattern", False),
            ("patternCoding", "patternCoding", coding.Coding, False, "pattern", False),
            ("patternContactDetail", "patternContactDetail", contactdetail.ContactDetail, False, "pattern", False),
            ("patternContactPoint", "patternContactPoint", contactpoint.ContactPoint, False, "pattern", False),
            ("patternContributor", "patternContributor", contributor.Contributor, False, "pattern", False),
            ("patternCount", "patternCount", count.Count, False, "pattern", False),
            ("patternDataRequirement", "patternDataRequirement", datarequirement.DataRequirement, False, "pattern", False),
            ("patternDate", "patternDate", fhirdate.FHIRDate, False, "pattern", False),
            ("patternDateTime", "patternDateTime", fhirdate.FHIRDate, False, "pattern", False),
            ("patternDecimal", "patternDecimal", float, False, "pattern", False),
            ("patternDistance", "patternDistance", distance.Distance, False, "pattern", False),
            ("patternDosage", "patternDosage", dosage.Dosage, False, "pattern", False),
            ("patternDuration", "patternDuration", duration.Duration, False, "pattern", False),
            ("patternExpression", "patternExpression", expression.Expression, False, "pattern", False),
            ("patternHumanName", "patternHumanName", humanname.HumanName, False, "pattern", False),
            ("patternId", "patternId", str, False, "pattern", False),
            ("patternIdentifier", "patternIdentifier", identifier.Identifier, False, "pattern", False),
            ("patternInstant", "patternInstant", fhirdate.FHIRDate, False, "pattern", False),
            ("patternInteger", "patternInteger", int, False, "pattern", False),
            ("patternMarkdown", "patternMarkdown", str, False, "pattern", False),
            ("patternMoney", "patternMoney", money.Money, False, "pattern", False),
            ("patternOid", "patternOid", str, False, "pattern", False),
            ("patternParameterDefinition", "patternParameterDefinition", parameterdefinition.ParameterDefinition, False, "pattern", False),
            ("patternPeriod", "patternPeriod", period.Period, False, "pattern", False),
            ("patternPositiveInt", "patternPositiveInt", int, False, "pattern", False),
            ("patternQuantity", "patternQuantity", quantity.Quantity, False, "pattern", False),
            ("patternRange", "patternRange", range.Range, False, "pattern", False),
            ("patternRatio", "patternRatio", ratio.Ratio, False, "pattern", False),
            ("patternReference", "patternReference", fhirreference.FHIRReference, False, "pattern", False),
            ("patternRelatedArtifact", "patternRelatedArtifact", relatedartifact.RelatedArtifact, False, "pattern", False),
            ("patternSampledData", "patternSampledData", sampleddata.SampledData, False, "pattern", False),
            ("patternSignature", "patternSignature", signature.Signature, False, "pattern", False),
            ("patternString", "patternString", str, False, "pattern", False),
            ("patternTime", "patternTime", fhirdate.FHIRDate, False, "pattern", False),
            ("patternTiming", "patternTiming", timing.Timing, False, "pattern", False),
            ("patternTriggerDefinition", "patternTriggerDefinition", triggerdefinition.TriggerDefinition, False, "pattern", False),
            ("patternUnsignedInt", "patternUnsignedInt", int, False, "pattern", False),
            ("patternUri", "patternUri", str, False, "pattern", False),
            ("patternUrl", "patternUrl", str, False, "pattern", False),
            ("patternUsageContext", "patternUsageContext", usagecontext.UsageContext, False, "pattern", False),
            ("patternUuid", "patternUuid", str, False, "pattern", False),
            ("representation", "representation", str, True, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("short", "short", str, False, None, False),
            ("sliceIsConstraining", "sliceIsConstraining", bool, False, None, False),
            ("sliceName", "sliceName", str, False, None, False),
            ("slicing", "slicing", ElementDefinitionSlicing, False, None, False),
            ("type", "type", ElementDefinitionType, True, None, False),
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