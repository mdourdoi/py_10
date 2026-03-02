from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: List[Dict]) -> Dict[str, int | float]:
    if len(mages) > 0:
        avg_power = sum(map(lambda x: x['power'], mages))
        avg_power /= len(mages)
        return {'max_power': max(mages, key=lambda x: x['power'])['power'],
                'min_power': min(mages, key=lambda x: x['power'])['power'],
                'avg_power': round(avg_power, 2)}
    else:
        return {'max_power': 0,
                'min_power': 0,
                'avg_power': 0}


def main() -> None:
    artifacts = [{"name": "Crystal Orb", "power": 85, "type": "focus"},
                 {"name": "Fire Staff", "power": 92, "type": "weapon"},
                 {"name": "Ancient Tome", "power": 70, "type": "knowledge"}]
    mages = [{"name": "Aeris", "power": 120, "element": "Air"},
             {"name": "Pyros", "power": 95, "element": "Fire"},
             {"name": "Terra", "power": 110, "element": "Earth"}]
    spells = ["fireball", "heal", "shield"]
    print()
    print('Artifact list:')
    for artifact in artifacts:
        print(f'{artifact["name"]} ({artifact["power"]} power)')
    print()
    print('Mage list:')
    for mage in mages:
        print(f'{mage["name"]} - {mage["power"]} power')
    print()
    print('Spell list:')
    for spell in spells:
        print(spell)
    print()
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) "
          f"comes before "
          f"{sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting power filter (>= 100)...")
    strong_mages = power_filter(mages, 100)
    for mage in strong_mages:
        print(f"{mage['name']} - {mage['power']} power")

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(stats)


if __name__ == "__main__":
    try:
        main()
    except Exception as cur_error:
        print('Error:', cur_error)
