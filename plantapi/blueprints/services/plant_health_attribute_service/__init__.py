from blueprints.data_provider.plant_health_attribute_data_provider import *
from blueprints.models.plant_health_attributes import *


def getPlantHealthAttributes():
    plantHealthAttributeModels = []
    for plantHealthAttributeDto in getPlantHelathAttributeDtos():
        plantHealthAttributeModels.append(make_plant_health_attribute(plantHealthAttributeDto.id,
                                                                      plantHealthAttributeDto.upper_required_value,
                                                                      plantHealthAttributeDto.lower_required_value,
                                                                      plantHealthAttributeDto.unit_measurement_id,
                                                                      plantHealthAttributeDto.plant_id,
                                                                      plantHealthAttributeDto.health_attribute_id))
    return plantHealthAttributeModels


def postPlantHealthAttribute(upper_required_value, lower_required_value, unit_measurement_id, plant_id,
                             health_attribute_id):
    plantHealthAttributeDto = addPlantHealthAttributeDto(upper_required_value, lower_required_value,
                                                         unit_measurement_id, plant_id, health_attribute_id)
    return plantHealthAttributeDto


def getPlantHealthAttributeById(id):
    plantHealthAttributeDto = getPlantHealthAttributeDtoById(id)
    return make_plant_health_attribute(plantHealthAttributeDto.id, plantHealthAttributeDto.upper_required_value,
                                       plantHealthAttributeDto.lower_required_value,
                                       plantHealthAttributeDto.unit_measurement_id,
                                       plantHealthAttributeDto.plant_id,
                                       plantHealthAttributeDto.health_attribute_id)


def deletePlantHealthAttributeById(id):
    deletePlantHealthAttributeDtoById(id)


def updatePlantHealthAttributeById(plant_health_attribute_id, upper_required_value, lower_required_value,
                                   unit_measurement_id, plant_id, health_attribute_id):

    update_plant_health_attribute = updatePlantHealthAttributeDtoById(plant_health_attribute_id, upper_required_value,
                                                                      lower_required_value, unit_measurement_id,
                                                                      plant_id, health_attribute_id)
    return update_plant_health_attribute
