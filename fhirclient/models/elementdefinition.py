#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ElementDefinition) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .age import Age
from .annotation import Annotation
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .contactpoint import ContactPoint
from .contributor import Contributor
from .count import Count
from .datarequirement import DataRequirement
from .distance import Distance
from .dosage import Dosage
from .duration import Duration
from .element import Element
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier
from .money import Money
from .parameterdefinition import ParameterDefinition
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .relatedartifact import RelatedArtifact
from .sampleddata import SampledData
from .signature import Signature
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class ElementDefinitionType(Element):
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
class ElementDefinitionSlicingDiscriminator(Element):
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

    def elementProperties(self):
        js = super(ElementDefinitionSlicingDiscriminator, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class ElementDefinitionSlicing(Element):
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
class ElementDefinitionMapping(Element):
    """ Map element to another set of definitions.

    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    resource_type: ClassVar[str] = "ElementDefinitionMapping"
    comment: Optional[str] = None
    identity: str = None
    language: Optional[str] = None
    map: str = None

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
class ElementDefinitionExample(Element):
    """ Example value (as defined for type).

    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """
    resource_type: ClassVar[str] = "ElementDefinitionExample"
    label: str = None
    valueAddress: Address = None
    valueAge: Age = None
    valueAnnotation: Annotation = None
    valueAttachment: Attachment = None
    valueBase64Binary: str = None
    valueBoolean: bool = None
    valueCanonical: str = None
    valueCode: str = None
    valueCodeableConcept: CodeableConcept = None
    valueCoding: Coding = None
    valueContactDetail: ContactDetail = None
    valueContactPoint: ContactPoint = None
    valueContributor: Contributor = None
    valueCount: Count = None
    valueDataRequirement: DataRequirement = None
    valueDate: FHIRDate = None
    valueDateTime: FHIRDate = None
    valueDecimal: float = None
    valueDistance: Distance = None
    valueDosage: Dosage = None
    valueDuration: Duration = None
    valueExpression: Expression = None
    valueHumanName: HumanName = None
    valueId: str = None
    valueIdentifier: Identifier = None
    valueInstant: FHIRDate = None
    valueInteger: int = None
    valueMarkdown: str = None
    valueMoney: Money = None
    valueOid: str = None
    valueParameterDefinition: ParameterDefinition = None
    valuePeriod: Period = None
    valuePositiveInt: int = None
    valueQuantity: Quantity = None
    valueRange: Range = None
    valueRatio: Ratio = None
    valueReference: FHIRReference = None
    valueRelatedArtifact: RelatedArtifact = None
    valueSampledData: SampledData = None
    valueSignature: Signature = None
    valueString: str = None
    valueTime: FHIRDate = None
    valueTiming: Timing = None
    valueTriggerDefinition: TriggerDefinition = None
    valueUnsignedInt: int = None
    valueUri: str = None
    valueUrl: str = None
    valueUsageContext: UsageContext = None
    valueUuid: str = None

    def elementProperties(self):
        js = super(ElementDefinitionExample, self).elementProperties()
        js.extend([
            ("label", "label", str, False, None, True),
            ("valueAddress", "valueAddress", Address, False, "value", True),
            ("valueAge", "valueAge", Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", Coding, False, "value", True),
            ("valueContactDetail", "valueContactDetail", ContactDetail, False, "value", True),
            ("valueContactPoint", "valueContactPoint", ContactPoint, False, "value", True),
            ("valueContributor", "valueContributor", Contributor, False, "value", True),
            ("valueCount", "valueCount", Count, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", DataRequirement, False, "value", True),
            ("valueDate", "valueDate", FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueDistance", "valueDistance", Distance, False, "value", True),
            ("valueDosage", "valueDosage", Dosage, False, "value", True),
            ("valueDuration", "valueDuration", Duration, False, "value", True),
            ("valueExpression", "valueExpression", Expression, False, "value", True),
            ("valueHumanName", "valueHumanName", HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueIdentifier", "valueIdentifier", Identifier, False, "value", True),
            ("valueInstant", "valueInstant", FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueMoney", "valueMoney", Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", ParameterDefinition, False, "value", True),
            ("valuePeriod", "valuePeriod", Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", True),
            ("valueRange", "valueRange", Range, False, "value", True),
            ("valueRatio", "valueRatio", Ratio, False, "value", True),
            ("valueReference", "valueReference", FHIRReference, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", RelatedArtifact, False, "value", True),
            ("valueSampledData", "valueSampledData", SampledData, False, "value", True),
            ("valueSignature", "valueSignature", Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", FHIRDate, False, "value", True),
            ("valueTiming", "valueTiming", Timing, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", TriggerDefinition, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("valueUsageContext", "valueUsageContext", UsageContext, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
        ])
        return js


@dataclass
class ElementDefinitionConstraint(Element):
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
class ElementDefinitionBinding(Element):
    """ ValueSet details if this is coded.

    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """
    resource_type: ClassVar[str] = "ElementDefinitionBinding"
    description: Optional[str] = None
    strength: str = None
    valueSet: Optional[str] = None

    def elementProperties(self):
        js = super(ElementDefinitionBinding, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("strength", "strength", str, False, None, True),
            ("valueSet", "valueSet", str, False, None, False),
        ])
        return js


@dataclass
class ElementDefinitionBase(Element):
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

    def elementProperties(self):
        js = super(ElementDefinitionBase, self).elementProperties()
        js.extend([
            ("max", "max", str, False, None, True),
            ("min", "min", int, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


@dataclass
class ElementDefinition(BackboneElement):
    """ Definition of an element in a resource or extension.

    Captures constraints on each element within the resource, profile, or
    extension.
    """
    resource_type: ClassVar[str] = "ElementDefinition"
    alias: Optional[List[str]] = empty_list()
    base: Optional[ElementDefinitionBase] = None
    binding: Optional[ElementDefinitionBinding] = None
    code: Optional[List[Coding]] = empty_list()
    comment: Optional[str] = None
    condition: Optional[List[str]] = empty_list()
    constraint: Optional[List[ElementDefinitionConstraint]] = empty_list()
    contentReference: Optional[str] = None
    defaultValueAddress: Optional[Address] = None
    defaultValueAge: Optional[Age] = None
    defaultValueAnnotation: Optional[Annotation] = None
    defaultValueAttachment: Optional[Attachment] = None
    defaultValueBase64Binary: Optional[str] = None
    defaultValueBoolean: Optional[bool] = None
    defaultValueCanonical: Optional[str] = None
    defaultValueCode: Optional[str] = None
    defaultValueCodeableConcept: Optional[CodeableConcept] = None
    defaultValueCoding: Optional[Coding] = None
    defaultValueContactDetail: Optional[ContactDetail] = None
    defaultValueContactPoint: Optional[ContactPoint] = None
    defaultValueContributor: Optional[Contributor] = None
    defaultValueCount: Optional[Count] = None
    defaultValueDataRequirement: Optional[DataRequirement] = None
    defaultValueDate: Optional[FHIRDate] = None
    defaultValueDateTime: Optional[FHIRDate] = None
    defaultValueDecimal: Optional[float] = None
    defaultValueDistance: Optional[Distance] = None
    defaultValueDosage: Optional[Dosage] = None
    defaultValueDuration: Optional[Duration] = None
    defaultValueExpression: Optional[Expression] = None
    defaultValueHumanName: Optional[HumanName] = None
    defaultValueId: Optional[str] = None
    defaultValueIdentifier: Optional[Identifier] = None
    defaultValueInstant: Optional[FHIRDate] = None
    defaultValueInteger: Optional[int] = None
    defaultValueMarkdown: Optional[str] = None
    defaultValueMoney: Optional[Money] = None
    defaultValueOid: Optional[str] = None
    defaultValueParameterDefinition: Optional[ParameterDefinition] = None
    defaultValuePeriod: Optional[Period] = None
    defaultValuePositiveInt: Optional[int] = None
    defaultValueQuantity: Optional[Quantity] = None
    defaultValueRange: Optional[Range] = None
    defaultValueRatio: Optional[Ratio] = None
    defaultValueReference: Optional[FHIRReference] = None
    defaultValueRelatedArtifact: Optional[RelatedArtifact] = None
    defaultValueSampledData: Optional[SampledData] = None
    defaultValueSignature: Optional[Signature] = None
    defaultValueString: Optional[str] = None
    defaultValueTime: Optional[FHIRDate] = None
    defaultValueTiming: Optional[Timing] = None
    defaultValueTriggerDefinition: Optional[TriggerDefinition] = None
    defaultValueUnsignedInt: Optional[int] = None
    defaultValueUri: Optional[str] = None
    defaultValueUrl: Optional[str] = None
    defaultValueUsageContext: Optional[UsageContext] = None
    defaultValueUuid: Optional[str] = None
    definition: Optional[str] = None
    example: Optional[List[ElementDefinitionExample]] = empty_list()
    fixedAddress: Optional[Address] = None
    fixedAge: Optional[Age] = None
    fixedAnnotation: Optional[Annotation] = None
    fixedAttachment: Optional[Attachment] = None
    fixedBase64Binary: Optional[str] = None
    fixedBoolean: Optional[bool] = None
    fixedCanonical: Optional[str] = None
    fixedCode: Optional[str] = None
    fixedCodeableConcept: Optional[CodeableConcept] = None
    fixedCoding: Optional[Coding] = None
    fixedContactDetail: Optional[ContactDetail] = None
    fixedContactPoint: Optional[ContactPoint] = None
    fixedContributor: Optional[Contributor] = None
    fixedCount: Optional[Count] = None
    fixedDataRequirement: Optional[DataRequirement] = None
    fixedDate: Optional[FHIRDate] = None
    fixedDateTime: Optional[FHIRDate] = None
    fixedDecimal: Optional[float] = None
    fixedDistance: Optional[Distance] = None
    fixedDosage: Optional[Dosage] = None
    fixedDuration: Optional[Duration] = None
    fixedExpression: Optional[Expression] = None
    fixedHumanName: Optional[HumanName] = None
    fixedId: Optional[str] = None
    fixedIdentifier: Optional[Identifier] = None
    fixedInstant: Optional[FHIRDate] = None
    fixedInteger: Optional[int] = None
    fixedMarkdown: Optional[str] = None
    fixedMoney: Optional[Money] = None
    fixedOid: Optional[str] = None
    fixedParameterDefinition: Optional[ParameterDefinition] = None
    fixedPeriod: Optional[Period] = None
    fixedPositiveInt: Optional[int] = None
    fixedQuantity: Optional[Quantity] = None
    fixedRange: Optional[Range] = None
    fixedRatio: Optional[Ratio] = None
    fixedReference: Optional[FHIRReference] = None
    fixedRelatedArtifact: Optional[RelatedArtifact] = None
    fixedSampledData: Optional[SampledData] = None
    fixedSignature: Optional[Signature] = None
    fixedString: Optional[str] = None
    fixedTime: Optional[FHIRDate] = None
    fixedTiming: Optional[Timing] = None
    fixedTriggerDefinition: Optional[TriggerDefinition] = None
    fixedUnsignedInt: Optional[int] = None
    fixedUri: Optional[str] = None
    fixedUrl: Optional[str] = None
    fixedUsageContext: Optional[UsageContext] = None
    fixedUuid: Optional[str] = None
    isModifier: Optional[bool] = None
    isModifierReason: Optional[str] = None
    isSummary: Optional[bool] = None
    label: Optional[str] = None
    mapping: Optional[List[ElementDefinitionMapping]] = empty_list()
    max: Optional[str] = None
    maxLength: Optional[int] = None
    maxValueDate: Optional[FHIRDate] = None
    maxValueDateTime: Optional[FHIRDate] = None
    maxValueDecimal: Optional[float] = None
    maxValueInstant: Optional[FHIRDate] = None
    maxValueInteger: Optional[int] = None
    maxValuePositiveInt: Optional[int] = None
    maxValueQuantity: Optional[Quantity] = None
    maxValueTime: Optional[FHIRDate] = None
    maxValueUnsignedInt: Optional[int] = None
    meaningWhenMissing: Optional[str] = None
    min: Optional[int] = None
    minValueDate: Optional[FHIRDate] = None
    minValueDateTime: Optional[FHIRDate] = None
    minValueDecimal: Optional[float] = None
    minValueInstant: Optional[FHIRDate] = None
    minValueInteger: Optional[int] = None
    minValuePositiveInt: Optional[int] = None
    minValueQuantity: Optional[Quantity] = None
    minValueTime: Optional[FHIRDate] = None
    minValueUnsignedInt: Optional[int] = None
    mustSupport: Optional[bool] = None
    orderMeaning: Optional[str] = None
    path: str = None
    patternAddress: Optional[Address] = None
    patternAge: Optional[Age] = None
    patternAnnotation: Optional[Annotation] = None
    patternAttachment: Optional[Attachment] = None
    patternBase64Binary: Optional[str] = None
    patternBoolean: Optional[bool] = None
    patternCanonical: Optional[str] = None
    patternCode: Optional[str] = None
    patternCodeableConcept: Optional[CodeableConcept] = None
    patternCoding: Optional[Coding] = None
    patternContactDetail: Optional[ContactDetail] = None
    patternContactPoint: Optional[ContactPoint] = None
    patternContributor: Optional[Contributor] = None
    patternCount: Optional[Count] = None
    patternDataRequirement: Optional[DataRequirement] = None
    patternDate: Optional[FHIRDate] = None
    patternDateTime: Optional[FHIRDate] = None
    patternDecimal: Optional[float] = None
    patternDistance: Optional[Distance] = None
    patternDosage: Optional[Dosage] = None
    patternDuration: Optional[Duration] = None
    patternExpression: Optional[Expression] = None
    patternHumanName: Optional[HumanName] = None
    patternId: Optional[str] = None
    patternIdentifier: Optional[Identifier] = None
    patternInstant: Optional[FHIRDate] = None
    patternInteger: Optional[int] = None
    patternMarkdown: Optional[str] = None
    patternMoney: Optional[Money] = None
    patternOid: Optional[str] = None
    patternParameterDefinition: Optional[ParameterDefinition] = None
    patternPeriod: Optional[Period] = None
    patternPositiveInt: Optional[int] = None
    patternQuantity: Optional[Quantity] = None
    patternRange: Optional[Range] = None
    patternRatio: Optional[Ratio] = None
    patternReference: Optional[FHIRReference] = None
    patternRelatedArtifact: Optional[RelatedArtifact] = None
    patternSampledData: Optional[SampledData] = None
    patternSignature: Optional[Signature] = None
    patternString: Optional[str] = None
    patternTime: Optional[FHIRDate] = None
    patternTiming: Optional[Timing] = None
    patternTriggerDefinition: Optional[TriggerDefinition] = None
    patternUnsignedInt: Optional[int] = None
    patternUri: Optional[str] = None
    patternUrl: Optional[str] = None
    patternUsageContext: Optional[UsageContext] = None
    patternUuid: Optional[str] = None
    representation: Optional[List[str]] = empty_list()
    requirements: Optional[str] = None
    short: Optional[str] = None
    sliceIsConstraining: Optional[bool] = None
    sliceName: Optional[str] = None
    slicing: Optional[ElementDefinitionSlicing] = None
    type: Optional[List[ElementDefinitionType]] = empty_list()

    def elementProperties(self):
        js = super(ElementDefinition, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("base", "base", ElementDefinitionBase, False, None, False),
            ("binding", "binding", ElementDefinitionBinding, False, None, False),
            ("code", "code", Coding, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("condition", "condition", str, True, None, False),
            ("constraint", "constraint", ElementDefinitionConstraint, True, None, False),
            ("contentReference", "contentReference", str, False, None, False),
            ("defaultValueAddress", "defaultValueAddress", Address, False, "defaultValue", False),
            ("defaultValueAge", "defaultValueAge", Age, False, "defaultValue", False),
            ("defaultValueAnnotation", "defaultValueAnnotation", Annotation, False, "defaultValue", False),
            ("defaultValueAttachment", "defaultValueAttachment", Attachment, False, "defaultValue", False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("defaultValueCanonical", "defaultValueCanonical", str, False, "defaultValue", False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", CodeableConcept, False, "defaultValue", False),
            ("defaultValueCoding", "defaultValueCoding", Coding, False, "defaultValue", False),
            ("defaultValueContactDetail", "defaultValueContactDetail", ContactDetail, False, "defaultValue", False),
            ("defaultValueContactPoint", "defaultValueContactPoint", ContactPoint, False, "defaultValue", False),
            ("defaultValueContributor", "defaultValueContributor", Contributor, False, "defaultValue", False),
            ("defaultValueCount", "defaultValueCount", Count, False, "defaultValue", False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", DataRequirement, False, "defaultValue", False),
            ("defaultValueDate", "defaultValueDate", FHIRDate, False, "defaultValue", False),
            ("defaultValueDateTime", "defaultValueDateTime", FHIRDate, False, "defaultValue", False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("defaultValueDistance", "defaultValueDistance", Distance, False, "defaultValue", False),
            ("defaultValueDosage", "defaultValueDosage", Dosage, False, "defaultValue", False),
            ("defaultValueDuration", "defaultValueDuration", Duration, False, "defaultValue", False),
            ("defaultValueExpression", "defaultValueExpression", Expression, False, "defaultValue", False),
            ("defaultValueHumanName", "defaultValueHumanName", HumanName, False, "defaultValue", False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("defaultValueIdentifier", "defaultValueIdentifier", Identifier, False, "defaultValue", False),
            ("defaultValueInstant", "defaultValueInstant", FHIRDate, False, "defaultValue", False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("defaultValueMoney", "defaultValueMoney", Money, False, "defaultValue", False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", ParameterDefinition, False, "defaultValue", False),
            ("defaultValuePeriod", "defaultValuePeriod", Period, False, "defaultValue", False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("defaultValueQuantity", "defaultValueQuantity", Quantity, False, "defaultValue", False),
            ("defaultValueRange", "defaultValueRange", Range, False, "defaultValue", False),
            ("defaultValueRatio", "defaultValueRatio", Ratio, False, "defaultValue", False),
            ("defaultValueReference", "defaultValueReference", FHIRReference, False, "defaultValue", False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", RelatedArtifact, False, "defaultValue", False),
            ("defaultValueSampledData", "defaultValueSampledData", SampledData, False, "defaultValue", False),
            ("defaultValueSignature", "defaultValueSignature", Signature, False, "defaultValue", False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("defaultValueTime", "defaultValueTime", FHIRDate, False, "defaultValue", False),
            ("defaultValueTiming", "defaultValueTiming", Timing, False, "defaultValue", False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", TriggerDefinition, False, "defaultValue", False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("defaultValueUrl", "defaultValueUrl", str, False, "defaultValue", False),
            ("defaultValueUsageContext", "defaultValueUsageContext", UsageContext, False, "defaultValue", False),
            ("defaultValueUuid", "defaultValueUuid", str, False, "defaultValue", False),
            ("definition", "definition", str, False, None, False),
            ("example", "example", ElementDefinitionExample, True, None, False),
            ("fixedAddress", "fixedAddress", Address, False, "fixed", False),
            ("fixedAge", "fixedAge", Age, False, "fixed", False),
            ("fixedAnnotation", "fixedAnnotation", Annotation, False, "fixed", False),
            ("fixedAttachment", "fixedAttachment", Attachment, False, "fixed", False),
            ("fixedBase64Binary", "fixedBase64Binary", str, False, "fixed", False),
            ("fixedBoolean", "fixedBoolean", bool, False, "fixed", False),
            ("fixedCanonical", "fixedCanonical", str, False, "fixed", False),
            ("fixedCode", "fixedCode", str, False, "fixed", False),
            ("fixedCodeableConcept", "fixedCodeableConcept", CodeableConcept, False, "fixed", False),
            ("fixedCoding", "fixedCoding", Coding, False, "fixed", False),
            ("fixedContactDetail", "fixedContactDetail", ContactDetail, False, "fixed", False),
            ("fixedContactPoint", "fixedContactPoint", ContactPoint, False, "fixed", False),
            ("fixedContributor", "fixedContributor", Contributor, False, "fixed", False),
            ("fixedCount", "fixedCount", Count, False, "fixed", False),
            ("fixedDataRequirement", "fixedDataRequirement", DataRequirement, False, "fixed", False),
            ("fixedDate", "fixedDate", FHIRDate, False, "fixed", False),
            ("fixedDateTime", "fixedDateTime", FHIRDate, False, "fixed", False),
            ("fixedDecimal", "fixedDecimal", float, False, "fixed", False),
            ("fixedDistance", "fixedDistance", Distance, False, "fixed", False),
            ("fixedDosage", "fixedDosage", Dosage, False, "fixed", False),
            ("fixedDuration", "fixedDuration", Duration, False, "fixed", False),
            ("fixedExpression", "fixedExpression", Expression, False, "fixed", False),
            ("fixedHumanName", "fixedHumanName", HumanName, False, "fixed", False),
            ("fixedId", "fixedId", str, False, "fixed", False),
            ("fixedIdentifier", "fixedIdentifier", Identifier, False, "fixed", False),
            ("fixedInstant", "fixedInstant", FHIRDate, False, "fixed", False),
            ("fixedInteger", "fixedInteger", int, False, "fixed", False),
            ("fixedMarkdown", "fixedMarkdown", str, False, "fixed", False),
            ("fixedMoney", "fixedMoney", Money, False, "fixed", False),
            ("fixedOid", "fixedOid", str, False, "fixed", False),
            ("fixedParameterDefinition", "fixedParameterDefinition", ParameterDefinition, False, "fixed", False),
            ("fixedPeriod", "fixedPeriod", Period, False, "fixed", False),
            ("fixedPositiveInt", "fixedPositiveInt", int, False, "fixed", False),
            ("fixedQuantity", "fixedQuantity", Quantity, False, "fixed", False),
            ("fixedRange", "fixedRange", Range, False, "fixed", False),
            ("fixedRatio", "fixedRatio", Ratio, False, "fixed", False),
            ("fixedReference", "fixedReference", FHIRReference, False, "fixed", False),
            ("fixedRelatedArtifact", "fixedRelatedArtifact", RelatedArtifact, False, "fixed", False),
            ("fixedSampledData", "fixedSampledData", SampledData, False, "fixed", False),
            ("fixedSignature", "fixedSignature", Signature, False, "fixed", False),
            ("fixedString", "fixedString", str, False, "fixed", False),
            ("fixedTime", "fixedTime", FHIRDate, False, "fixed", False),
            ("fixedTiming", "fixedTiming", Timing, False, "fixed", False),
            ("fixedTriggerDefinition", "fixedTriggerDefinition", TriggerDefinition, False, "fixed", False),
            ("fixedUnsignedInt", "fixedUnsignedInt", int, False, "fixed", False),
            ("fixedUri", "fixedUri", str, False, "fixed", False),
            ("fixedUrl", "fixedUrl", str, False, "fixed", False),
            ("fixedUsageContext", "fixedUsageContext", UsageContext, False, "fixed", False),
            ("fixedUuid", "fixedUuid", str, False, "fixed", False),
            ("isModifier", "isModifier", bool, False, None, False),
            ("isModifierReason", "isModifierReason", str, False, None, False),
            ("isSummary", "isSummary", bool, False, None, False),
            ("label", "label", str, False, None, False),
            ("mapping", "mapping", ElementDefinitionMapping, True, None, False),
            ("max", "max", str, False, None, False),
            ("maxLength", "maxLength", int, False, None, False),
            ("maxValueDate", "maxValueDate", FHIRDate, False, "maxValue", False),
            ("maxValueDateTime", "maxValueDateTime", FHIRDate, False, "maxValue", False),
            ("maxValueDecimal", "maxValueDecimal", float, False, "maxValue", False),
            ("maxValueInstant", "maxValueInstant", FHIRDate, False, "maxValue", False),
            ("maxValueInteger", "maxValueInteger", int, False, "maxValue", False),
            ("maxValuePositiveInt", "maxValuePositiveInt", int, False, "maxValue", False),
            ("maxValueQuantity", "maxValueQuantity", Quantity, False, "maxValue", False),
            ("maxValueTime", "maxValueTime", FHIRDate, False, "maxValue", False),
            ("maxValueUnsignedInt", "maxValueUnsignedInt", int, False, "maxValue", False),
            ("meaningWhenMissing", "meaningWhenMissing", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("minValueDate", "minValueDate", FHIRDate, False, "minValue", False),
            ("minValueDateTime", "minValueDateTime", FHIRDate, False, "minValue", False),
            ("minValueDecimal", "minValueDecimal", float, False, "minValue", False),
            ("minValueInstant", "minValueInstant", FHIRDate, False, "minValue", False),
            ("minValueInteger", "minValueInteger", int, False, "minValue", False),
            ("minValuePositiveInt", "minValuePositiveInt", int, False, "minValue", False),
            ("minValueQuantity", "minValueQuantity", Quantity, False, "minValue", False),
            ("minValueTime", "minValueTime", FHIRDate, False, "minValue", False),
            ("minValueUnsignedInt", "minValueUnsignedInt", int, False, "minValue", False),
            ("mustSupport", "mustSupport", bool, False, None, False),
            ("orderMeaning", "orderMeaning", str, False, None, False),
            ("path", "path", str, False, None, True),
            ("patternAddress", "patternAddress", Address, False, "pattern", False),
            ("patternAge", "patternAge", Age, False, "pattern", False),
            ("patternAnnotation", "patternAnnotation", Annotation, False, "pattern", False),
            ("patternAttachment", "patternAttachment", Attachment, False, "pattern", False),
            ("patternBase64Binary", "patternBase64Binary", str, False, "pattern", False),
            ("patternBoolean", "patternBoolean", bool, False, "pattern", False),
            ("patternCanonical", "patternCanonical", str, False, "pattern", False),
            ("patternCode", "patternCode", str, False, "pattern", False),
            ("patternCodeableConcept", "patternCodeableConcept", CodeableConcept, False, "pattern", False),
            ("patternCoding", "patternCoding", Coding, False, "pattern", False),
            ("patternContactDetail", "patternContactDetail", ContactDetail, False, "pattern", False),
            ("patternContactPoint", "patternContactPoint", ContactPoint, False, "pattern", False),
            ("patternContributor", "patternContributor", Contributor, False, "pattern", False),
            ("patternCount", "patternCount", Count, False, "pattern", False),
            ("patternDataRequirement", "patternDataRequirement", DataRequirement, False, "pattern", False),
            ("patternDate", "patternDate", FHIRDate, False, "pattern", False),
            ("patternDateTime", "patternDateTime", FHIRDate, False, "pattern", False),
            ("patternDecimal", "patternDecimal", float, False, "pattern", False),
            ("patternDistance", "patternDistance", Distance, False, "pattern", False),
            ("patternDosage", "patternDosage", Dosage, False, "pattern", False),
            ("patternDuration", "patternDuration", Duration, False, "pattern", False),
            ("patternExpression", "patternExpression", Expression, False, "pattern", False),
            ("patternHumanName", "patternHumanName", HumanName, False, "pattern", False),
            ("patternId", "patternId", str, False, "pattern", False),
            ("patternIdentifier", "patternIdentifier", Identifier, False, "pattern", False),
            ("patternInstant", "patternInstant", FHIRDate, False, "pattern", False),
            ("patternInteger", "patternInteger", int, False, "pattern", False),
            ("patternMarkdown", "patternMarkdown", str, False, "pattern", False),
            ("patternMoney", "patternMoney", Money, False, "pattern", False),
            ("patternOid", "patternOid", str, False, "pattern", False),
            ("patternParameterDefinition", "patternParameterDefinition", ParameterDefinition, False, "pattern", False),
            ("patternPeriod", "patternPeriod", Period, False, "pattern", False),
            ("patternPositiveInt", "patternPositiveInt", int, False, "pattern", False),
            ("patternQuantity", "patternQuantity", Quantity, False, "pattern", False),
            ("patternRange", "patternRange", Range, False, "pattern", False),
            ("patternRatio", "patternRatio", Ratio, False, "pattern", False),
            ("patternReference", "patternReference", FHIRReference, False, "pattern", False),
            ("patternRelatedArtifact", "patternRelatedArtifact", RelatedArtifact, False, "pattern", False),
            ("patternSampledData", "patternSampledData", SampledData, False, "pattern", False),
            ("patternSignature", "patternSignature", Signature, False, "pattern", False),
            ("patternString", "patternString", str, False, "pattern", False),
            ("patternTime", "patternTime", FHIRDate, False, "pattern", False),
            ("patternTiming", "patternTiming", Timing, False, "pattern", False),
            ("patternTriggerDefinition", "patternTriggerDefinition", TriggerDefinition, False, "pattern", False),
            ("patternUnsignedInt", "patternUnsignedInt", int, False, "pattern", False),
            ("patternUri", "patternUri", str, False, "pattern", False),
            ("patternUrl", "patternUrl", str, False, "pattern", False),
            ("patternUsageContext", "patternUsageContext", UsageContext, False, "pattern", False),
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