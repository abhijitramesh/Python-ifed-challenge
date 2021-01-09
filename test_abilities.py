from ability import ability

def test_ability_machamp():
    assert(ability("machamp")==['guts', 'no-guard', 'steadfast'])

def test_ability_pikachu():
    assert(ability("pikachu")==['static', 'lightning-rod'])

def test_ability_charizard():
    assert(ability("charizard")==['blaze', 'solar-power'])

def test_ability_evee():
    assert(ability("eevee")==['run-away', 'adaptability', 'anticipation'])