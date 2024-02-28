import math
from typing import Any, Generator


def getDelta(base: int, is_boss: bool) -> int:
    if is_boss:
        return math.ceil(base / 8) if base > 0 else math.ceil(base / -300)
    else:
        return math.ceil(base / 10) if base > 0 else math.ceil(base / -75)


def getUpgradedStatIter(base: int, quality: float, is_boss: bool, key: str = None, is_weapon: bool = False) -> Generator[Any, Any, None]:
    delta = getDelta(base, is_boss)
    def quality_plus(level): 
        return quality+(level-10)/100
    if key == 'crit':
        for level in range(1, 14):
            return base
    elif key == 'dexterity' or (is_weapon and (key == 'hp' or key == 'mana')):
        for level in range(1, 14):
            if level == 1:
                return math.ceil(base)
            else:
                return math.ceil(base + level * delta)
    else:
        for level in range(1, 14):
            if level == 1:
                yield math.ceil(base*quality)
            elif level <= 10:
                yield math.ceil((base + level * delta) * quality)
            else:
                yield math.ceil((base+level*delta)*quality_plus(level))


def getUpgradedStat(base: int, level: int, quality: float, is_boss: bool) -> int:
    delta = getDelta(base, is_boss)
    def quality_plus(level): 
        return quality+(level-10)/100
    if level == 1:
        return math.ceil(base*quality)
    elif level <= 10:
        return math.ceil((base + level * delta) * quality)
    else:
        return math.ceil((base+level*delta)*quality_plus(level))


def getItemQuality(base: int, input: int, level: int, is_boss: bool) -> float:
    delta = level-10 if level > 10 else 0
    base_stat = getUpgradedStat(
        base=base, level=level, quality=1, is_boss=is_boss)
    return round(((input / base_stat) * (1+delta) -delta)*100) / 100
