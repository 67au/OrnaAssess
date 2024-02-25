import math

upgrade_boss = lambda base: math.ceil(base/8) if base>0 else math.ceil(base/-50)
upgrade_notboss = lambda base: math.ceil(base/10) if base>0 else math.ceil(base/-75)
upgrade_delta = lambda base, is_boss: upgrade_boss(base) if is_boss else upgrade_notboss(base)

def getUpgradedStatIter(base: int, quality: float, is_boss: bool):
    delta = upgrade_delta(base, is_boss)
    quality_plus = lambda level: quality+(level-10)/100
    for i in range(1, 14):
        if i == 1:
            yield math.ceil(base*quality)
        elif i<=10:
            yield math.ceil((base + i * delta) * quality)
        else:
            yield math.ceil((base+i*delta)*quality_plus(i))

def getUpgradedStat(base: int, level: int, quality: float, is_boss: bool):
    delta = upgrade_delta(base, is_boss)
    quality_plus = lambda level: quality+(level-10)/100
    if level == 1:
        return math.ceil(base*quality)
    elif level <=10:
        return math.ceil((base + level * delta) * quality)
    else:
        return math.ceil((base+level*delta)*quality_plus(level))

def getItemQuality(base: int, input: int, level: int, is_boss: bool):
    base_stat = getUpgradedStat(base=base, level=level, quality=1, is_boss=is_boss)
    return round((input / base_stat)*100) / 100 + ((level-10) if level>10 else 0) / 100
