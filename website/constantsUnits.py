entity_unit_map = {
    'width': {'centimetre', 'cm', 'foot', 'ft', 'inch', 'in', 'metre', 'm', 'millimetre', 'mm', 'yard', 'yd'},
    'depth': {'centimetre', 'cm', 'foot', 'ft', 'inch', 'in', 'metre', 'm', 'millimetre', 'mm', 'yard', 'yd'},
    'height': {'centimetre', 'cm', 'foot', 'ft', 'inch', 'in', 'metre', 'm', 'millimetre', 'mm', 'yard', 'yd'},
    'item_weight': {'gram', 'g', 'kilogram', 'kg', 'microgram', 'µg', 'milligram', 'mg', 'ounce', 'oz', 'pound', 'lb', 'ton', 't'},
    'maximum_weight_recommendation': {'gram', 'g', 'kilogram', 'kg', 'microgram', 'µg', 'milligram', 'mg', 'ounce', 'oz', 'pound', 'lb', 'ton', 't'},
    'voltage': {'kilovolt', 'kV', 'millivolt', 'mV', 'volt', 'V'},
    'wattage': {'kilowatt', 'kW', 'watt', 'W'},
    'item_volume': {'centilitre', 'cL', 'cubic foot', 'ft³', 'cubic inch', 'in³', 'cup', 'c', 'decilitre', 'dL',
                    'fluid ounce', 'fl oz', 'gallon', 'gal', 'imperial gallon', 'litre', 'L', 'microlitre', 'µL', 'millilitre', 'mL', 'pint', 'pt', 'quart', 'qt'}
}

allowed_units = {unit for entity in entity_unit_map for unit in entity_unit_map[entity]}