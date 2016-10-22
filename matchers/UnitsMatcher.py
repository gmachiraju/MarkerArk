from snorkel.snorkel.matchers import *


all_prefixes_units = [['Ym', 'yottameter'], ['Zm', 'zettameter'], ['Em', 'exameter'], ['Pm', 'petameter'], ['Tm', 'terameter'], ['Gm', 'gigameter'], ['Mm', 'megameter'], ['km', 'kilometer'], ['hm', 'hectometer'], ['dam', 'dekameter'], ['dm', 'decimeter'], ['cm', 'centimeter'], ['\\u03bcm', 'micrometer'], ['nm', 'nanometer'], ['pm', 'picometer'], ['fm', 'femtometer'], ['am', 'attometer'], ['zm', 'zeptometer'], ['ym', 'yoctometer'], ['Ym2', 'square yottameter'], ['Zm2', 'square zettameter'], ['Em2', 'square exameter'], ['Pm2', 'square petameter'], ['Tm2', 'square terameter'], ['Gm2', 'square gigameter'], ['Mm2', 'square megameter'], ['km2', 'square kilometer'], ['hm2', 'square hectometer'], ['dam2', 'square dekameter'], ['dm2', 'square decimeter'], ['cm2', 'square centimeter'], ['\\u03bcm2', 'square micrometer'], ['nm2', 'square nanometer'], ['pm2', 'square picometer'], ['fm2', 'square femtometer'], ['am2', 'square attometer'], ['zm2', 'square zeptometer'], ['ym2', 'square yoctometer'], ['Ym2', 'cubic yottameter'], ['Zm2', 'cubic zettameter'], ['Em2', 'cubic exameter'], ['Pm2', 'cubic petameter'], ['Tm2', 'cubic terameter'], ['Gm2', 'cubic gigameter'], ['Mm2', 'cubic megameter'], ['km2', 'cubic kilometer'], ['hm2', 'cubic hectometer'], ['dam2', 'cubic dekameter'], ['dm2', 'cubic decimeter'], ['cm2', 'cubic centimeter'], ['\\u03bcm2', 'cubic micrometer'], ['nm2', 'cubic nanometer'], ['pm2', 'cubic picometer'], ['fm2', 'cubic femtometer'], ['am2', 'cubic attometer'], ['zm2', 'cubic zeptometer'], ['ym2', 'cubic yoctometer'], ['YL', 'yottaliter'], ['ZL', 'zettaliter'], ['EL', 'exaliter'], ['PL', 'petaliter'], ['TL', 'teraliter'], ['GL', 'gigaliter'], ['ML', 'megaliter'], ['kL', 'kiloliter'], ['hL', 'hectoliter'], ['daL', 'dekaliter'], ['dL', 'deciliter'], ['cL', 'centiliter'], ['\\u03bcL', 'microliter'], ['nL', 'nanoliter'], ['pL', 'picoliter'], ['fL', 'femtoliter'], ['aL', 'attoliter'], ['zL', 'zeptoliter'], ['yL', 'yoctoliter'], ['Yg', 'yottagram'], ['Zg', 'zettagram'], ['Eg', 'exagram'], ['Pg', 'petagram'], ['Tg', 'teragram'], ['Gg', 'gigagram'], ['Mg', 'megagram'], ['kg', 'kilogram'], ['hg', 'hectogram'], ['dag', 'dekagram'], ['dg', 'decigram'], ['cg', 'centigram'], ['\\u03bcg', 'microgram'], ['ng', 'nanogram'], ['pg', 'picogram'], ['fg', 'femtogram'], ['ag', 'attogram'], ['zg', 'zeptogram'], ['yg', 'yoctogram']]

def getUnitsMatcher ():
    unitsDatabase = all_prefixes_units

    unit_regex = RegexMatchEach(rgx=r'(?<=\s)[a-zA-Z]{1,2}[1-9]?(?=[\s\,\.])|(?<=\s)[a-zA-Z]{1,2}[1-9]?[\/]{1}[a-zA-Z]{1,2}[1-9]?(?=[\s\.\,])', ignore_case=False,attrib='words')

    return unit_regex



