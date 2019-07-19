#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationKnowledge) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .dosage import Dosage
from .duration import Duration
from .fhirreference import FHIRReference
from .money import Money
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class MedicationKnowledgeRelatedMedicationKnowledge(BackboneElement):
    """ Associated or related medication information.

    Associated or related knowledge about a medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRelatedMedicationKnowledge"
    reference: List[FHIRReference] = empty_list()
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicationKnowledgeRelatedMedicationKnowledge, self).elementProperties()
        js.extend([
            ("reference", "reference", FHIRReference, True, None, True),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeRegulatorySubstitution(BackboneElement):
    """ Specifies if changes are allowed when dispensing a medication from a
    regulatory perspective.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatorySubstitution"
    allowed: bool = None
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySubstitution, self).elementProperties()
        js.extend([
            ("allowed", "allowed", bool, False, None, True),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeRegulatorySchedule(BackboneElement):
    """ Specifies the schedule of a medication in jurisdiction.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatorySchedule"
    schedule: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySchedule, self).elementProperties()
        js.extend([
            ("schedule", "schedule", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeRegulatoryMaxDispense(BackboneElement):
    """ The maximum number of units of the medication that can be dispensed in a
    period.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatoryMaxDispense"
    period: Optional[Duration] = None
    quantity: Quantity = None

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatoryMaxDispense, self).elementProperties()
        js.extend([
            ("period", "period", Duration, False, None, False),
            ("quantity", "quantity", Quantity, False, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeRegulatory(BackboneElement):
    """ Regulatory information about a medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatory"
    maxDispense: Optional[MedicationKnowledgeRegulatoryMaxDispense] = None
    regulatoryAuthority: FHIRReference = None
    schedule: Optional[List[MedicationKnowledgeRegulatorySchedule]] = empty_list()
    substitution: Optional[List[MedicationKnowledgeRegulatorySubstitution]] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatory, self).elementProperties()
        js.extend([
            ("maxDispense", "maxDispense", MedicationKnowledgeRegulatoryMaxDispense, False, None, False),
            ("regulatoryAuthority", "regulatoryAuthority", FHIRReference, False, None, True),
            ("schedule", "schedule", MedicationKnowledgeRegulatorySchedule, True, None, False),
            ("substitution", "substitution", MedicationKnowledgeRegulatorySubstitution, True, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgePackaging(BackboneElement):
    """ Details about packaged medications.

    Information that only applies to packages (not products).
    """
    resource_type: ClassVar[str] = "MedicationKnowledgePackaging"
    quantity: Optional[Quantity] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicationKnowledgePackaging, self).elementProperties()
        js.extend([
            ("quantity", "quantity", Quantity, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeMonograph(BackboneElement):
    """ Associated documentation about the medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMonograph"
    source: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicationKnowledgeMonograph, self).elementProperties()
        js.extend([
            ("source", "source", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeMonitoringProgram(BackboneElement):
    """ Program under which a medication is reviewed.

    The program under which the medication is reviewed.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMonitoringProgram"
    name: Optional[str] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicationKnowledgeMonitoringProgram, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeMedicineClassification(BackboneElement):
    """ Categorization of the medication within a formulary or classification
    system.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMedicineClassification"
    classification: Optional[List[CodeableConcept]] = empty_list()
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicationKnowledgeMedicineClassification, self).elementProperties()
        js.extend([
            ("classification", "classification", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeKinetics(BackboneElement):
    """ The time course of drug absorption, distribution, metabolism and excretion
    of a medication from the body.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeKinetics"
    areaUnderCurve: Optional[List[Quantity]] = empty_list()
    halfLifePeriod: Optional[Duration] = None
    lethalDose50: Optional[List[Quantity]] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledgeKinetics, self).elementProperties()
        js.extend([
            ("areaUnderCurve", "areaUnderCurve", Quantity, True, None, False),
            ("halfLifePeriod", "halfLifePeriod", Duration, False, None, False),
            ("lethalDose50", "lethalDose50", Quantity, True, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeIngredient(BackboneElement):
    """ Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeIngredient"
    isActive: Optional[bool] = None
    itemCodeableConcept: CodeableConcept = None
    itemReference: FHIRReference = None
    strength: Optional[Ratio] = None

    def elementProperties(self):
        js = super(MedicationKnowledgeIngredient, self).elementProperties()
        js.extend([
            ("isActive", "isActive", bool, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", FHIRReference, False, "item", True),
            ("strength", "strength", Ratio, False, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeDrugCharacteristic(BackboneElement):
    """ Specifies descriptive properties of the medicine.

    Specifies descriptive properties of the medicine, such as color, shape,
    imprints, etc.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeDrugCharacteristic"
    type: Optional[CodeableConcept] = None
    valueBase64Binary: Optional[str] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueQuantity: Optional[Quantity] = None
    valueString: Optional[str] = None

    def elementProperties(self):
        js = super(MedicationKnowledgeDrugCharacteristic, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
        ])
        return js


@dataclass
class MedicationKnowledgeCost(BackboneElement):
    """ The pricing of the medication.

    The price of the medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeCost"
    cost: Money = None
    source: Optional[str] = None
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicationKnowledgeCost, self).elementProperties()
        js.extend([
            ("cost", "cost", Money, False, None, True),
            ("source", "source", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics(BackboneElement):
    """ Characteristics of the patient that are relevant to the administration
    guidelines.

    Characteristics of the patient that are relevant to the administration
    guidelines (for example, height, weight, gender, etc.).
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics"
    characteristicCodeableConcept: CodeableConcept = None
    characteristicQuantity: Quantity = None
    value: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, self).elementProperties()
        js.extend([
            ("characteristicCodeableConcept", "characteristicCodeableConcept", CodeableConcept, False, "characteristic", True),
            ("characteristicQuantity", "characteristicQuantity", Quantity, False, "characteristic", True),
            ("value", "value", str, True, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeAdministrationGuidelinesDosage(BackboneElement):
    """ Dosage for the medication for the specific guidelines.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuidelinesDosage"
    dosage: List[Dosage] = empty_list()
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelinesDosage, self).elementProperties()
        js.extend([
            ("dosage", "dosage", Dosage, True, None, True),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeAdministrationGuidelines(BackboneElement):
    """ Guidelines for administration of the medication.

    Guidelines for the administration of the medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuidelines"
    dosage: Optional[List[MedicationKnowledgeAdministrationGuidelinesDosage]] = empty_list()
    indicationCodeableConcept: Optional[CodeableConcept] = None
    indicationReference: Optional[FHIRReference] = None
    patientCharacteristics: Optional[List[MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics]] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelines, self).elementProperties()
        js.extend([
            ("dosage", "dosage", MedicationKnowledgeAdministrationGuidelinesDosage, True, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", CodeableConcept, False, "indication", False),
            ("indicationReference", "indicationReference", FHIRReference, False, "indication", False),
            ("patientCharacteristics", "patientCharacteristics", MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, True, None, False),
        ])
        return js


@dataclass
class MedicationKnowledge(DomainResource):
    """ Definition of Medication Knowledge.

    Information about a medication that is used to support knowledge.
    """
    resource_type: ClassVar[str] = "MedicationKnowledge"
    administrationGuidelines: Optional[List[MedicationKnowledgeAdministrationGuidelines]] = empty_list()
    amount: Optional[Quantity] = None
    associatedMedication: Optional[List[FHIRReference]] = empty_list()
    code: Optional[CodeableConcept] = None
    contraindication: Optional[List[FHIRReference]] = empty_list()
    cost: Optional[List[MedicationKnowledgeCost]] = empty_list()
    doseForm: Optional[CodeableConcept] = None
    drugCharacteristic: Optional[List[MedicationKnowledgeDrugCharacteristic]] = empty_list()
    ingredient: Optional[List[MedicationKnowledgeIngredient]] = empty_list()
    intendedRoute: Optional[List[CodeableConcept]] = empty_list()
    kinetics: Optional[List[MedicationKnowledgeKinetics]] = empty_list()
    manufacturer: Optional[FHIRReference] = None
    medicineClassification: Optional[List[MedicationKnowledgeMedicineClassification]] = empty_list()
    monitoringProgram: Optional[List[MedicationKnowledgeMonitoringProgram]] = empty_list()
    monograph: Optional[List[MedicationKnowledgeMonograph]] = empty_list()
    packaging: Optional[MedicationKnowledgePackaging] = None
    preparationInstruction: Optional[str] = None
    productType: Optional[List[CodeableConcept]] = empty_list()
    regulatory: Optional[List[MedicationKnowledgeRegulatory]] = empty_list()
    relatedMedicationKnowledge: Optional[List[MedicationKnowledgeRelatedMedicationKnowledge]] = empty_list()
    status: Optional[str] = None
    synonym: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledge, self).elementProperties()
        js.extend([
            ("administrationGuidelines", "administrationGuidelines", MedicationKnowledgeAdministrationGuidelines, True, None, False),
            ("amount", "amount", Quantity, False, None, False),
            ("associatedMedication", "associatedMedication", FHIRReference, True, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("contraindication", "contraindication", FHIRReference, True, None, False),
            ("cost", "cost", MedicationKnowledgeCost, True, None, False),
            ("doseForm", "doseForm", CodeableConcept, False, None, False),
            ("drugCharacteristic", "drugCharacteristic", MedicationKnowledgeDrugCharacteristic, True, None, False),
            ("ingredient", "ingredient", MedicationKnowledgeIngredient, True, None, False),
            ("intendedRoute", "intendedRoute", CodeableConcept, True, None, False),
            ("kinetics", "kinetics", MedicationKnowledgeKinetics, True, None, False),
            ("manufacturer", "manufacturer", FHIRReference, False, None, False),
            ("medicineClassification", "medicineClassification", MedicationKnowledgeMedicineClassification, True, None, False),
            ("monitoringProgram", "monitoringProgram", MedicationKnowledgeMonitoringProgram, True, None, False),
            ("monograph", "monograph", MedicationKnowledgeMonograph, True, None, False),
            ("packaging", "packaging", MedicationKnowledgePackaging, False, None, False),
            ("preparationInstruction", "preparationInstruction", str, False, None, False),
            ("productType", "productType", CodeableConcept, True, None, False),
            ("regulatory", "regulatory", MedicationKnowledgeRegulatory, True, None, False),
            ("relatedMedicationKnowledge", "relatedMedicationKnowledge", MedicationKnowledgeRelatedMedicationKnowledge, True, None, False),
            ("status", "status", str, False, None, False),
            ("synonym", "synonym", str, True, None, False),
        ])
        return js