import MySQLdb


#####################################################################
############################ BINARY SEARCH ############################
####################################################################
# NOTE THAT A WORD BEING GREATER THAN ANOTHER MEANS THAT IT IS ALPHABET

def binary_search_name(list, name, start, end):
    # print len(list)
    # print 149/2
    # print "STEP TAKEN"

    if(list[(end + start) / 2] == name):
        return (bool(True), (end + start) / 2)
    elif((start + end) / 2 == end or (start + end) / 2 == start):
        return (bool(False), -1)
    elif(list[(end + start) / 2] < name):
        return binary_search_name(list, name, start, (start + end) / 2)
    else:
        return binary_search_name(list, name, (start + end) / 2, end)


#####################################################################
############################ BIOMARKERS ##############################
#####################################################################

def get_next_available_biomarker_name_pk_key(db):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Biomolecule_Names ORDER BY pk_Biomolecule_Names DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    nextavailable = results[0][0]
    return nextavailable + 1


def get_next_available_biomarker_fk_key(db):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Biomolecule_Names ORDER BY fk_Biomolecules DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results
    nextavailable = results[0][1]
    return nextavailable + 1


def database_has_biomarker(db, name, casesensitive):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Biomolecule_Names ORDER BY Name DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    database_contained_biomarkers = []
    for row in results:
        database_contained_biomarkers.append(row[2])
    if not casesensitive:
        lowercaseList = []
        for item in database_contained_biomarkers:
            lowercaseList.append(item.lower())
        database_contained_biomarkers = lowercaseList
        name = name.lower()
    return binary_search_name(database_contained_biomarkers, name, 0, len(database_contained_biomarkers))


def add_biomarker(db, name):
    nextPk = get_next_available_biomarker_name_pk_key(db)
    nextFk = get_next_available_biomarker_fk_key(db)
    cursor = db.cursor()
    biomarker_existence = database_has_biomarker(db, name, False)
    if not (biomarker_existence[0]):
        cursor.execute("INSERT INTO MARKERVILLE.Biomolecule_Names(pk_Biomolecule_Names, fk_Biomolecules, Name) VALUES (%d, %d, '%s')" % (
            nextPk, nextFk, name))
        return nextPk
    else:
        return biomarker_existence[1]


def get_next_available_biomarker_pk(db):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Biomolecules ORDER BY pk_Biomolecules DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    nextavailable = results[0][0]
    return nextavailable + 1


def add_biomolecule_v2(db, name, medium, type):
    pk_Biomolecules = get_next_available_biomarker_pk(db)
    fk_Biomolecule_Medium = add_medium(db, medium)
    fk_Biomolecule_type = add_type(db, type)
    biomolecule_name = name
    cursor = db.cursor()
    sql = "INSERT INTO MARKERVILLE.Biomolecules(pk_Biomolecules, fk_Biomolecule_Medium, fk_Biomolecule_Type) VALUES (%d, %d, %d)" % (
        pk_Biomolecules, fk_Biomolecule_Medium, fk_Biomolecule_type)
    cursor.execute(sql)
    sql = "INSERT INTO MARKERVILLE.Biomolecules_Names(pk_Biomolecule_Names, fk_Biomolecules, Name) VALUES (%d, %d, '%s')" % (
        get_next_available_biomarker_name_pk_key, pk_Biomolecules, name)
    cursor.execute(sql)


#####################################################################
########################### Medium ###################################
#####################################################################

def get_next_available_medium_pk_key(db):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Biomolecule_Medium ORDER BY pk_Biomolecule_Medium DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    nextavailable = results[0][0]
    return nextavailable + 1


def database_has_medium(db, name, casesensitive):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Biomolecule_Medium ORDER BY Disease DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    all_database_mediums = []
    for row in results:
        all_database_mediums.append(row[1])
    if not casesensitive:
        lowercaseList = []
        for item in all_database_mediums:
            lowercaseList.append(item.lower())
        all_database_mediums = lowercaseList
        name = name.lower()
    return (binary_search_name(all_database_mediums, name, 0, len(all_database_mediums)))


def add_medium(db, name):
    nextPk = get_next_available_medium_pk_key(db)
    cursor = db.cursor()
    medium_existence = database_has_medium(db, name, False)
    if not (medium_existence[0]):
        cursor.execute(
            "INSERT INTO MARKERVILLE.Biomolecule_Names(pk_Biomolecule_Medium, Medium) VALUES (%d, '%s')" % (nextPk, name))
        return nextPk
    else:
        return medium_existence[1]


#####################################################################
############################# Type ###################################
#####################################################################

def get_next_available_type_pk(db):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Biomolecule_Type ORDER BY pk_Biomolecule_Type DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    nextavailable = results[0][0]
    return nextavailable + 1


def database_has_type(db, name, casesensitive):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Biomolecule_Type ORDER BY Disease DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    all_database_types = []
    for row in results:
        all_database_types.append(row[1])
    if not casesensitive:
        lowercaseList = []
        for item in all_database_types:
            lowercaseList.append(item.lower())
        all_database_types = lowercaseList
        name = name.lower()
    return (binary_search_name(all_database_types, name, 0, len(all_database_types)))


def add_type(db, name):
    nextPk = get_next_available_type_pk(db)
    cursor = db.cursor()
    type_existence = database_has_medium(db, name, False)
    if not (type_existence[0]):
        cursor.execute(
            "INSERT INTO MARKERVILLE.Biomolecule_Type(pk_Biomolecule_Type, Type) VALUES (%d, '%s')" % (
                nextPk, name))
        return nextPk
    else:
        return type_existence[1]


#####################################################################
############################ DISEASES ###############################
#####################################################################

def get_next_available_diseases_pk(db):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Diseases ORDER BY pk_Diseases DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    nextavailable = results[0][0]
    return nextavailable + 1


def database_has_disease(db, name, casesensitive):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Diseases ORDER BY Disease DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    all_database_diseases = []
    for row in results:
        all_database_diseases.append(row[1])
    if not casesensitive:
        lowercaseList = []
        for item in all_database_diseases:
            lowercaseList.append(item.lower())
        all_database_diseases = lowercaseList
        name = name.lower()
    return (binary_search_name(all_database_diseases, name, 0, len(all_database_diseases)))


def add_disease(db, name):
    next_disease_pk = get_next_available_diseases_pk(db)
    cursor = db.cursor()
    disease_existence = database_has_disease(db, name, False)
    if not (disease_existence[0]):
        cursor.execute(
            "INSERT INTO MARKERVILLE.Diseases(pk_Diseases, Disease) VALUES (%d, '%s')" % (
                next_disease_pk, name))
        return next_disease_pk
    else:
        return disease_existence[1]


#####################################################################
############################ SOURCES ################################
#####################################################################

def get_next_available_source_pk(db):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Sources ORDER BY pk_Sources DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results
    nextavailable = results[0][0]
    return nextavailable + 1


def database_has_source(db, name, casesensitive):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Sources ORDER BY URL DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    all_database_sources = []
    for row in results:
        all_database_sources.append(row[1])
    if not casesensitive:
        lowercaseList = []
        for item in all_database_sources:
            lowercaseList.append(item.lower())
        all_database_sources = lowercaseList
        name = name.lower()
    return (binary_search_name(all_database_sources, name, 0, len(all_database_sources)))


def add_source(db, url, ID):
    next_source_pk = db.cursor()
    cursor = db.cursor()
    source_existence = database_has_source(db, url, False)
    if not(source_existence[0]):
        cursor.execute("INSERT INTO MARKERVILLE.Diseases(pk_Sources, Google_ID, url) VALUES (%d, '%s', '%s')"
                       % (next_source_pk, ID, url))
        return next_source_pk
    else:
        return source_existence[1]


#####################################################################
############################ LEVELS #################################
#####################################################################

def get_next_available_levels_pk(db):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Levels ORDER BY levels_pk DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results
    nextavailable = results[0][0]
    return nextavailable + 1


def add_levels(db, level, test_set, measurement_type, unit):
    cursor = db.cursor()
    next_available_pk = get_next_available_levels_pk(db)
    sql = "INSERT INTO MARKERVILLE.Levels(levels_pk, levels, test__set, measurement_type, units) VALUES(%d, %d, '%s', '%s', '%s')" % (
        next_available_pk, level, test_set, measurement_type, unit)
    cursor.execute(sql)
    return next_available_pk


#####################################################################
########################## ALT NAMES ################################
#####################################################################

def merge_alternate_names(db, alt_names_db):
    cursor = db.cursor()
    for tuple in alt_names_db:
        if (len(tuple) >= 2):
            count = 0
            sql1 = "SELECT * FROM MARKERVILLE.Biomolecule_Names WHERE Biomolecule_Names="
            sql2 = "WHERE Biomolecule_Names="
            while(count < len(tuple) - 1):
                sql1 += "'" + \
                    tuple[count] + "' OR Biomolecule_Names='" + \
                        tuple[count + 1] + "'"
                sql2 += "'" + \
                    tuple[count] + "' OR Biomolecule_Names='" + \
                        tuple[count + 1] + "'"
                count += 2
            cursor.execute(sql1 + "ORDER BY fk_Biomolecules ASC")
            results = cursor.fetchall()
            best = results[0][1]
            cursor.execute(
                "UPDATE MARKERVILLE.Biomolecule_Names SET fk_Biomolecules=" + best + " " + sql2)

    sql = "UPDATE MARKERVILLE.Biomarker_Names SET"


#####################################################################
########################## RELATIONS ################################
#####################################################################

def get_next_available_relations_pk(db):
    cursor = db.cursor()
    sql = "SELECT * FROM MARKERVILLE.Biomolecules_Sources_Association ORDER BY pk_Biomolecules_Sources_Association DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results
    nextavailable = results[0][0]
    return nextavailable + 1


def add_relation(db, biomarkerID, sourceID, diseaseID, levelID):
    cursor = db.cursor()
    next_available_relation = get_next_available_relations_pk(db)
    sql = "INSERT INTO MARKERVILLE.Levels(pk_Biomolecules_Sources_Association, fk_Biomolecules, fk_Sources, fk_Diseases, level_fk) VALUES(%d, %d, %d, %d, %d)" % (
        next_available_relation, biomarkerID, sourceID, diseaseID, levelID)
    cursor.execute(sql)
    return next_available_relation


#####################################################################
############################ TESTING ################################
#####################################################################
# database = MySQLdb.connect("canaryctr-donald.stanford.edu", "markerville_user", "b1omark3rsRock!", "MARKERVILLE")
# cursor = database.cursor()
# sql = "SELECT * FROM MARKERVILLE.Biomolecule_Names WHERE "
# cursor.execute(sql)
# print cursor.fetchall()
# # add_ease(db = database, name="Ovarian Cancer")
# database.close()


# print (database_has_disease(db = MySQLdb.connect("canaryctr-donald.stanford.edu", "markerville_user", "b1omark3rsRock!", "MARKERVILLE"), name="ovarian cancer", casesensitive=False))

# addBiomarker(name="Hello world")
# getNextAvailableBiomarkerFkKey(db= MySQLdb.connect("canaryctr-donald.stanford.edu", "markerville_user", "b1omark3rsRock!", "MARKERVILLE"))
#    db = MySQLdb.connect("canaryctr-donald.stanford.edu", "markerville_user", "b1omark3rsRock!", "MARKERVILLE")
